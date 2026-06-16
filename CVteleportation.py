import strawberryfields as sf
from strawberryfields.ops import *
import numpy as np

#Initialize the program with 3 modes 
#Mode 0: Alice's input state to be teleported
#Mode 1: Alice's half of the EPR pair
#Mode 2: Bob's half of the EPR pair
prog = sf.Program(3)

#Define the squeezing parameter 'r' for the EPR pair
#Higher squeezing = higher entanglement fidelity = better teleportation
squeezing_r = 1.5

#Define the unknown coherent state alpha = x + ip to teleport
alpha_target = 0.5 + 0.3j

#Convert alpha to polar coordinates(phase and magnitude)
alpha_mag = np.abs(alpha_target)
alpha_phase = np.angle(alpha_target)

with prog.context as q:
    #State preparation:
    #Pass magnitude and phase separately into Coheret()
    Coherent(alpha_mag, alpha_phase) | q[0]


    #Create the EPR entangled pair between modes 1 and 2
    Squeezed(squeezing_r) | q[1]    #Squeeze mode 1
    Squeezed(-squeezing_r) | q[2]    #Squeeze mode 2 in the opposite direction
    BSgate(sf.hbar * np.pi / 4, 0) | (q[1],q[2])  #50:50 beam splitter to create EPR pair

    #Alice's Protocol (Bell measurement):
    BSgate(sf.hbar * np.pi / 4, 0) | (q[0], q[1])  #Entangle mode 0 and mode 1

    #Alice performs homodyne measurements
    MeasureX | q[0]
    MeasureP | q[1]

    #Bob's Protocol (Displacement):
    #Bob uses Alice's classical measurement results to displace mode 2
    #The scaling factor (sqrt2) accounts for the 50:50 beam splitter geometry
    Xgate(np.sqrt(2) * q[0].par) | q[2]
    Pgate(np.sqrt(2) * q[1].par) | q[2]

#Now run the simlulation using the Fock backend
#We use Fock to easily inspect the resulting state's fidelity
eng = sf.Engine("fock", backend_options = {"cutoff_dim":15})
result =eng.run(prog)

#Extract the reduced density matrix of q[2]
bob_state = result.state.reduced_dm(2)

print("CV Teleportation Complete")
print(f"Target alpha sent by Alice: {alpha_target}")

