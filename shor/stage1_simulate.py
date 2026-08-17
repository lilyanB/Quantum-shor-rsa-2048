"""Stage 1 — run Shor for real, on tiny moduli.

Goal
----
Factor N = 15, 21, 35 end to end on a simulator and verify the factors are correct.
This stage proves the mechanism is understood; it claims nothing else.

What Shor actually is
---------------------
Factoring is reduced to *order finding*, and only that part is quantum:

    1. classical  pick a random a < N, check gcd(a, N) == 1
    2. QUANTUM    find r, the period of x -> a^x mod N
    3. classical  recover r from the measurement via continued fractions
    4. classical  gcd(a^(r/2) +- 1, N) gives a factor, if r is even and the
                  result is non-trivial -- otherwise pick a new a and retry

Steps 1, 3 and 4 are ordinary number theory and run on a laptop.  Step 2 is the
only reason a quantum computer is involved: it is the periodicity of modular
exponentiation, extracted by the inverse QFT.

Planned contents
----------------
- modular arithmetic circuits: controlled addition, multiplication, exponentiation
- the order-finding circuit: modular exponentiation + inverse QFT + measurement
- the classical wrapper: continued fractions, gcd, retry loop
- a `factor(N)` entry point returning the factors and the number of attempts

The pitfall to name explicitly
------------------------------
Most Shor tutorials do not implement modular exponentiation at all.  They hard-code
a gate sequence for one specific N (almost always 15), often found by hand or by
searching.  That is not Shor; it is an animation of Shor, and it teaches nothing
about cost -- which makes stage 2 impossible.

This module must state, in its docstring and in its tests, whether the arithmetic is
a **general construction** parameterised by N, or **compiled for a fixed N**.  The
honest answer is the useful one either way.

The wall
--------
Shor is not Clifford -- unlike BB84, there is no stabilizer shortcut, so simulation
means state vectors and ~2^n memory.  N = 35 already needs around 20 qubits.  Running
out of memory here is expected, and is exactly what motivates stage 2.

Reference
---------
S. Beauregard, *Circuit for Shor's algorithm using 2n+3 qubits*, 2003.
"""

from __future__ import annotations

__all__: list[str] = []


if __name__ == "__main__":
    raise SystemExit("stage 1 (simulate) is not implemented yet — see the module docstring")
