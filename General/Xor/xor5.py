from PIL.Image import open, fromarray
from numpy import array
img1 = array(open(r"D:\ctfs\crypto\CryptoHack_Solutions\General\Xor\flag.png"))
img2 = array(open(r"D:\ctfs\crypto\CryptoHack_Solutions\General\Xor\lemur.png"))
fromarray(img1^img2).show()

## crypto{X0Rly_n0t!}
