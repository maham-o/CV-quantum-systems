import strawberryfields as sf
from strawberryfields import ops

#create a 2 mode program
#In continuous-variable quantum computing, 'modes' are the equivalent of qubits. 
prog = sf.Program(2)

#create a free parameter named 'a'
#Free parameters act as symbolic variables, allowing you to define a circuit template and defer passing the actual numerical values until the simulation is executed. 
a = prog.params("a")

#define the program
with prog.context as q:
    #Apply a Displacement gate with an amplitude to a^2 to mode 0
    #This shifts the state in phase space (adds coherent light)
    ops.Dgate(a ** 2) | q[0]
    #Measure the X-quadrature on mode 0. This collapses the state of mode 0 into a classical real number
    ops.MeasureX | q[0]
    #Apply a squeezing gate to mode 1. q[0].par retrieves the measured classical value from the previous step
    ops.Sgate(1 - sf.math.sin(q[0].par)) | q[1]
    #Perform a Fock back-end measurement. This projects the state into the photon number basis, yielding an integer number of photons. 
    ops.MeasureFock() | q[1]

#Initialize the Fock backend
#The cutoff_dim sets the maximum photon state capacity (0 to 4 photons) that the simulator will track. This is done because the Fock space is infinte-dimensional. 
eng = sf.Engine("fock",backend_options = {"cutoff_dim": 5})

#Run the program, with the free parameter 'a' set to 0.9
result = eng.run(prog, args = {"a" : 0.9})

#Print the measurement results
print(result.samples)
