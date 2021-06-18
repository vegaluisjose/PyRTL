import io
import pyrtl
from pyrtl.reticle import add

a = pyrtl.Input(8, 'a')
b = pyrtl.Input(8, 'b')
y = pyrtl.Output(8, 'y')
m = add(a, b)
y <<= m

pyrtl.optimize()

print("--- PyRTL Representation ---")
print(pyrtl.working_block())
print()

print("--- Verilog for the Counter ---")
with io.StringIO() as vfile:
    pyrtl.output_to_verilog(vfile)
    print(vfile.getvalue())


print("--- Simulation Results ---")
sim_trace = pyrtl.SimulationTrace([a, b, y])
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(15):
    sim.step({'a':cycle, 'b':cycle})

sim_trace.print_vcd()
