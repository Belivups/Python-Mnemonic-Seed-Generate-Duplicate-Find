from mnemonic import Mnemonic
from binascii import hexlify
mnemo = Mnemonic("english")

i = 1
while i < 1000000:
    words = mnemo.generate(strength=128)
    entropy = mnemo.to_entropy(words)
    seed = mnemo.to_seed(words, passphrase="")
    pubkey = Mnemonic.to_hd_master_key(seed)

    print(words)
    # print(hexlify(entropy))
    with open('Wallet GenX3.txt', 'a') as f:
        print(words, file=f)
    i += 1
