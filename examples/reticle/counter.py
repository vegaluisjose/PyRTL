import pyrtl
from pyrtl.importexport import output_to_reticle

en = pyrtl.Input(bitwidth=1, name='en')
y = pyrtl.Output(bitwidth=4, name="y")

cnt = pyrtl.Register(4, 'cnt')
val = pyrtl.WireVector(4, 'val')
cnt.next <<= val

with pyrtl.conditional_assignment:
   with en == 1:
      val |= cnt + 1
   with pyrtl.otherwise:
      val |= cnt

y <<= cnt

pyrtl.optimize()

# Reticle
with open('aes.ir', 'w') as f1, open('aes.json', 'w') as f2:
   output_to_reticle(f1, f2)

# Verilog
# with open('main.v', 'w') as f:
#    pyrtl.output_to_verilog(f)
