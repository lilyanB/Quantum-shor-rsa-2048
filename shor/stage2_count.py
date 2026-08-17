"""Stage 2 — build circuits too large to run, and count them.

Goal
----
Construct Shor circuits for n = 8, 16, 32, 64-bit moduli and measure their size.
None of these can be executed: beyond roughly 20 qubits the state vector no longer
fits in memory.

The idea that makes this stage work
-----------------------------------
**A circuit you cannot run is still a circuit you can count.**

Building a QuantumCircuit object costs memory proportional to the number of *gates*,
not to 2^qubits.  So the circuit for a 64-bit modulus can be constructed, inspected
and measured on a laptop, even though executing it would require more memory than
exists.  This is the bridge from a toy demonstration to a real estimate.

Planned contents
----------------
- circuit construction for arbitrary n, reusing stage 1's arithmetic
- resource counting: qubit count, circuit depth, gate counts by type
- decomposition into a fixed gate set, because raw `count_ops()` on a
  high-level circuit counts abstractions, not real operations
- a scaling table and fit: resource vs n

Why the gate set matters more than the gate count
-------------------------------------------------
In a surface code the cost of a gate is wildly non-uniform:

    Clifford gates (H, CNOT, X, Z, S)   nearly free
    T and Toffoli gates                 ruinous -- each needs magic state
                                        distillation, i.e. entire factories
                                        of physical qubits

So the number that predicts the physical cost is not the total gate count but the
**T-count** (or Toffoli count).  Counting anything else is counting the wrong thing.

Measured evidence for that claim, from the estimator, on a circuit with a *single*
Toffoli gate:

    logical qubits (algorithm)              12
    physical qubits for the algorithm    1 176
    physical qubits for T factories     15 680     <- 93% of the total
    total                               16 856

Shor on 2048 bits contains billions of Toffoli gates.  That is the whole story.

Deliverable
-----------
A scaling law for T-count and logical qubits as a function of n, extracted from real
constructed circuits rather than copied from a paper.  Stage 3 consumes it.
"""

from __future__ import annotations

__all__: list[str] = []


if __name__ == "__main__":
    raise SystemExit("stage 2 (count) is not implemented yet — see the module docstring")
