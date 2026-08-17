"""Shor's algorithm, and what it would actually cost against RSA-2048.

The repository is organised as three stages, one module each.  Each stage answers a
question the previous one cannot, and each is limited by a different wall.

    stage1_simulate   N = 15, 21, 35        wall: simulator memory (~2^n amplitudes)
    stage2_count      n = 8 .. 64 bits      wall: none -- we count, we do not run
    stage3_estimate   n = 512 .. 2048 bits  wall: none -- we extrapolate and compare

The interesting result lives in stage 3: the ratio between logical and physical
qubits, which is the entire cost of quantum error correction.

Nothing is implemented yet.
"""

__all__: list[str] = []
