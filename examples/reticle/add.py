import io
import pyrtl
from pyrtl.importexport import output_to_reticle

a = pyrtl.Input(8, "a")
b = pyrtl.Input(8, "b")
y = pyrtl.Output(8, "y")
m = pyrtl.add(a, b)
y <<= m

pyrtl.optimize()

print("--- PyRTL Representation ---")
print(pyrtl.working_block())
print()

print("--- Verilog ---")
with io.StringIO() as vfile:
    pyrtl.output_to_verilog(vfile)
    print(vfile.getvalue())

print("--- Reticle ---")
with io.StringIO() as vfile:
    output_to_reticle(vfile)
    print(vfile.getvalue())

