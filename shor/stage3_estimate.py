"""Stage 3 — extrapolate to RSA-2048, then check the answer.

Goal
----
Turn stage 2's logical resource counts into *physical* ones for n = 512, 1024, 2048,
and explain the result.  This is the point of the repository.

The approach is deliberately hybrid
-----------------------------------
    1. OUR model      write the logical -> physical conversion by hand
    2. the estimator  feed the same assumptions to Microsoft's QDK estimator
    3. the gap        explain why the two differ

Step 3 is the deliverable.  A number with no reference point is worthless; a number
that comes out at 2.4x the established tool, together with a stated reason why this
model is more naive, is a result.  Only step 1 teaches anything, and only step 2 can
catch a systematic error in step 1.

What the hand-written model has to account for
----------------------------------------------
- **code distance d** -- how much redundancy each logical qubit needs, driven by the
  physical error rate and the total number of operations the computation must survive
- **logical cycles** -- a surface code proceeds in rounds of syndrome measurement;
  runtime is (cycles x cycle time), not gate count
- **magic state distillation** -- T and Toffoli gates are not applied directly.
  Factories produce magic states, and those factories dominate the qubit budget
  (93% in the measured example in stage 2)
- **error budget** -- the whole computation must succeed with some target
  probability, which sets the tolerated error per logical operation

Assumptions must be explicit and identical on both sides, or the comparison in step 3
is meaningless.  Physical error rate, gate time, cycle time, code choice, target
success probability: all named, all justified.

Open question, to settle here and not before
--------------------------------------------
The `qsharp` package is deprecated in favour of `qdk`, and `qsharp.estimate()` is
itself deprecated in favour of `qdk.qre` (QRE v3).  Which API to depend on is a
stage 3 decision; `qdk` is pinned in pyproject.toml so both paths are available.

The trap
--------
The estimator encodes *Microsoft's* assumptions: a qubit technology, gate times, a
noise model, defaults chosen for their roadmap.  A figure produced by calling
`estimate()` without understanding those defaults is a figure that cannot be
defended.  Hence step 1 first, tool second.

Context worth reporting
-----------------------
Published estimates for RSA-2048 have fallen by orders of magnitude since 2012 with
*no hardware improvement* -- purely from better algorithms and better codes.  The
threat timeline therefore moves from both ends, which matters more for migration
planning than any single figure.  Check the primary sources rather than quoting
secondhand numbers.

And the reason any of this matters: encrypted traffic can be captured today and
decrypted later.  The deadline for leaving RSA is not the arrival of the machine, it
is that date minus the required secrecy lifetime of the data.

References to check against
---------------------------
A. Fowler et al., *Surface codes: towards practical large-scale quantum
computation*, 2012.
C. Gidney, M. Ekera, *How to factor 2048 bit RSA integers in 8 hours using 20
million noisy qubits*, Quantum 5, 2021.
C. Gidney, *How to factor 2048 bit RSA integers with less than a million noisy
qubits*, 2025.
"""

from __future__ import annotations

__all__: list[str] = []


if __name__ == "__main__":
    raise SystemExit("stage 3 (estimate) is not implemented yet — see the module docstring")
