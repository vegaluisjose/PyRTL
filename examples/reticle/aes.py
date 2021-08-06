import io
import pyrtl
from pyrtl.rtllib.aes import AES
from pyrtl.importexport import output_to_reticle

aes = AES()
plaintext = pyrtl.Input(bitwidth=128, name='aes_plaintext')
key = pyrtl.Input(bitwidth=128, name='aes_key')
aes_ciphertext = pyrtl.Output(bitwidth=128, name='aes_ciphertext')
aes_reset = pyrtl.Input(1, name='aes_reset')
ready = pyrtl.Output(1, name='ready')
ready_out, aes_cipher = aes.encrypt_state_m(plaintext, key, aes_reset)
ready <<= ready_out
aes_ciphertext <<= aes_cipher

pyrtl.optimize()

# Reticle
with open('aes.ir', 'w') as f1, open('aes.json', 'w') as f2:
    output_to_reticle(f1, f2)

# Verilog
with open('main.v', 'w') as f:
   pyrtl.output_to_verilog(f)
