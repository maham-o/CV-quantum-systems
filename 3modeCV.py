import strawberryfields as sf
from strawberryfields import ops

#create a 3-mode quantum program
prog = sf.Program(3)

with prog.context as q:
#prepare squeezed states
    ops.Sgate(0.54) | q[0]
    ops.Sgate(0.54) | q[1]
    ops.Sgate(0.54) | q[2]
#mixing modes using beamsplitters
    ops.BSgate(0.43,0.1) | (q[0], q[2])
    ops.BSgate(0.43,0.1) | (q[1], q[2])
    ops.MeasureFock() | q

#run the program on the Fock backend
eng = sf.Engine("fock", backend_options = {"cutoff_dim":5})

result = eng.run(prog)
print(result.samples)