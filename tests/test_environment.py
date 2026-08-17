"""Verify the toolchain before any algorithm is written.

Three things must work for this project to be possible at all: simulating small
circuits, constructing large ones without executing them, and converting logical
resources into physical ones. One test each.
"""

import warnings

import pytest


def test_qiskit_can_simulate_a_small_circuit():
    """Stage 1 needs a working state-vector simulator."""
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator

    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    counts = AerSimulator().run(qc, shots=1000).result().get_counts()
    assert set(counts) <= {"00", "11"}
    assert sum(counts.values()) == 1000


def test_a_circuit_too_large_to_run_can_still_be_built_and_counted():
    """Stage 2's central premise.

    Building a circuit costs memory in the number of gates, not in 2^qubits, so a
    circuit far beyond simulation range can still be constructed and measured.
    """
    from qiskit import QuantumCircuit

    qc = QuantumCircuit(2000)
    for i in range(0, 1998, 2):
        qc.ccx(i, i + 1, i + 2)

    assert qc.num_qubits == 2000
    assert qc.count_ops()["ccx"] == 999
    assert qc.depth() > 0


@pytest.mark.slow
def test_resource_estimator_shows_t_factories_dominating():
    """Stage 3's tool, and the fact that motivates the whole project.

    A single Toffoli gate already costs thousands of physical qubits, and the large
    majority of them are magic-state factories rather than the algorithm itself.
    """
    warnings.filterwarnings("ignore")
    qsharp = pytest.importorskip("qsharp")

    qsharp.eval(
        """
        operation Demo() : Unit {
            use q = Qubit[3];
            within { H(q[0]); H(q[1]); } apply { CCNOT(q[0], q[1], q[2]); }
            ResetAll(q);
        }
        """
    )
    counts = qsharp.estimate("Demo()")["physicalCounts"]
    breakdown = counts["breakdown"]

    algorithm = breakdown["physicalQubitsForAlgorithm"]
    factories = breakdown["physicalQubitsForTfactories"]

    assert breakdown["algorithmicLogicalQubits"] < 50
    assert counts["physicalQubits"] > 1000
    assert factories > algorithm, "magic state distillation should dominate"
