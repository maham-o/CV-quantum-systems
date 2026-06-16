Continuous-Variable (CV) Quantum Teleportation in Strawberry Fields

This repository contains a Python implementation of the Continuous-Variable (CV) Quantum Teleportation protocol using Xanadu's StrawberryFields library.

The script simulates the teleportation of an unknown coherent state ∣α⟩ from Alice to Bob using a shared, highly entangled Einstein-Podolsky-Rosen (EPR) state.


Protocol Overview

Quantum teleportation allows the transfer of a quantum state using a shared entangled state and classical communication. In the continuous-variable regime (position and momentum quadratures rather than discrete qubits), the protocol follows these core steps:

    State Preparation: Alice prepares a target coherent state ∣α⟩ on Mode 0.

    EPR Pair Generation: A highly entangled EPR pair is created across Mode 1 (Alice) and Mode 2 (Bob) using squeezed vacuum states and a 50:50 beam splitter.

    Bell Measurement: Alice performs a joint Bell measurement on her target state (Mode 0) and her half of the EPR pair (Mode 1) by sending them through a second beam splitter and measuring the X and P quadratures.

    Classical Feedforward & Displacement: Alice sends her measurement results to Bob over a classical channel. Bob applies conditional displacement gates (X and P) scaled by 2​ to reconstruct the exact target state on Mode 2.
