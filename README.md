# Quantum-shor-rsa-2048

## Objective

Shor's algorithm breaks RSA "in principle". This repository puts a number on **in
principle**.

The goal is not to factor a large integer — that is impossible on a simulator and will
stay impossible on hardware for years. The goal is to answer a quantitative question:

> **How many qubits, how many gates, and how much time would it actually take to factor a
> 2048-bit RSA modulus?**

The interesting result is not the algorithm. It is the gap between two numbers:

```text
   logical qubits needed    ~ a few thousand     ← almost within reach
   physical qubits needed   ~ orders of magnitude more
```

That ratio is the entire cost of quantum error correction, and it is what separates a
headline from a threat model. Quantifying it is the point of this project.

## Approach: start small, then scale

The method is deliberately incremental. Each stage answers a question the previous stage
cannot.

### Stage 1 — Run Shor for real, on tiny moduli

`N = 15`, `21`, `35` (4 to 6 bits). Small enough to simulate end to end and verify the
factors come out right.

This stage proves the mechanism is understood, nothing more. It also forces an honest
question that most Shor tutorials dodge: is the modular exponentiation a **general
construction**, or a gate sequence hard-coded for one specific `N`? The second is not
Shor, it is an animation of Shor. This repository will state which one it implements.

### Stage 2 — Build circuits too large to run, and count them

`n = 8`, `16`, `32`, `64` bits. Beyond roughly 20 qubits the state vector no longer fits
in memory, so these circuits cannot be executed.

They can still be **constructed and measured**: qubit count, circuit depth, number of
Toffoli and T gates. A circuit you cannot run is still a circuit you can count — and that
is the bridge from a toy demo to a real estimate.

### Stage 3 — Extrapolate to RSA-2048, then check the answer

Fit the scaling law from stage 2, extend it to `n = 512`, `1024`, `2048`, and convert
logical resources into physical ones: surface-code distance, physical error rate, cycle
time, magic-state distillation.

Then the step that matters most — **compare against the published estimates** and explain
the difference. A number without a reference point is worthless; a number that is 3× the
literature value, with a stated reason why the model here is more naive, is a result.

| stage | modulus size | what is possible |
| ----- | ------------ | ---------------------------------------------- |
| 1     | 4–6 bits     | simulate and verify                            |
| 2     | 8–64 bits    | construct and count, cannot execute            |
| 3     | 512–2048 bits| extrapolate and compare with published results |

## Why it matters

Encrypted data can be **captured today and decrypted later**. The deadline for migrating
away from RSA is therefore not the day a quantum computer arrives — it is that day minus
however long the data must stay secret. For medical records or state secrets, that
subtraction lands in the past.

Published estimates for RSA-2048 have also fallen by orders of magnitude since 2012
without any hardware improving, purely from better algorithms and better error-correcting
codes. The threat timeline moves from both ends, and that is a large part of what this
repository is meant to show.

## Status

Nothing implemented yet. Stage 1 first.

## References to check against

- P. Shor, _Algorithms for quantum computation: discrete logarithms and factoring_, 1994.
- S. Beauregard, _Circuit for Shor's algorithm using 2n+3 qubits_, 2003.
- A. Fowler _et al._, _Surface codes: towards practical large-scale quantum computation_,
  2012.
- C. Gidney, M. Ekerå, _How to factor 2048 bit RSA integers in 8 hours using 20 million
  noisy qubits_, Quantum 5, 2021.
- C. Gidney, _How to factor 2048 bit RSA integers with less than a million noisy qubits_,
  2025.
