import strawberryfields as sf
from strawberryfields import ops

#create a 2 mode program
prog = sf.Program(2)

#create a free parameter named 'a'
a = prog.params("a")

#define the program
with prog.context as q:
    ops.Dgate(a ** 2) | q[0]
    ops.MeasureX | q[0]
    ops.Sgate(1 - sf.math.sin(q[0].par)) | q[1]
    ops.MeasureFock() | q[1]

#initialize the Fock backend
eng = sf.Engine("fock",backend_options = {"cutoff_dim": 5})

#run the program, with the free parameter 'a' set to 0.9
result = eng.run(prog, args = {"a" : 0.9})

print(result.samples)
