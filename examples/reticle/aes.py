import io
import pyrtl
from pyrtl.rtllib.aes import AES
from pyrtl.importexport import output_to_reticle

aes = AES()
plaintext = pyrtl.Input(bitwidth=128, name='aes_plaintext')
key = pyrtl.Input(bitwidth=128, name='aes_key')
aes_ciphertext = pyrtl.Output(bitwidth=128, name='aes_ciphertext')
reset = pyrtl.Input(1, name='reset')
ready = pyrtl.Output(1, name='ready')
ready_out, aes_cipher = aes.encrypt_state_m(plaintext, key, reset)
ready <<= ready_out
aes_ciphertext <<= aes_cipher

pyrtl.optimize()

with io.StringIO() as vfile:
    output_to_reticle(vfile, vfile)
    print(vfile.getvalue())

#print("\n\n\n\n")
#with io.StringIO() as vfile:
#    pyrtl.output_to_verilog(vfile)
#    print(vfile.getvalue())
