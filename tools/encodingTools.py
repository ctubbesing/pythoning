import math
import secrets

def get_bit(val, n):
  return ((val >> n) & 1) == 1

def rrot_bits(val, n, totalBits = 32):
  return ((val >> n) | (val << (totalBits - n))) & ((2 ** totalBits) - 1)

def lrot_bits(val, n, totalBits = 32):
  return ((val << n) & ((2 ** totalBits) - 1) | (val >> (totalBits - n)))

def bin2Dec(binVal):
  if binVal[:2] == '0b':
    binVal = binVal[2:]
  l = len(binVal)
  dec = 0
  for n in range(l):
    if binVal[l - n - 1] == '1':
      dec += 2 ** n
  return dec

def dec2Bin(decVal, doPrefix = True, numBits = 8):
  bits = '0b' if doPrefix else ''
  for n in range(numBits):
    bits += ('1' if get_bit(decVal, numBits - n - 1) else '0')
  return bits

def bin2Hex(binVal, doPrefix = True):
  if binVal[:2] == '0b':
    binVal = binVal[2:]
  l = len(binVal)
  paddingLen = (4 - (l % 4)) % 4
  binVal = (paddingLen * '0') + binVal
  l = len(binVal)
  result = '0x' if doPrefix else ''
  for i in range(math.floor(l / 4)):
    bits = binVal[(i * 4):((i * 4) + 4)]
    n = bin2Dec(bits)
    if (n < 10):
      result += str(n)
    else:
      result += chr(n - 10 + ord('a'))
  return result

def hex2Bin(hexVal, doPrefix = True):
  if hexVal[:2] == '0x':
    hexVal = hexVal[2:]
  hexVal = hexVal.lower()
  l = len(hexVal)
  bits = '0b' if doPrefix else ''
  for i in range(l):
    n = 0
    try:
      n = int(hexVal[i])
    except ValueError:
      n = 10 + ord(hexVal[i]) - ord('a')
    bits += dec2Bin(n, False, 4)
  return bits

def dec2Hex(decVal, doPrefix = True, numBits = 32):
  binVal = dec2Bin(decVal, False, numBits)
  return bin2Hex(binVal, doPrefix)

def hex2Dec(hexVal):
  binVal = hex2Bin(hexVal, False)
  return bin2Dec(binVal)

def str2Bin(strVal, doPrefix = True):
  result = '0b' if doPrefix else ''
  for i in range(len(strVal)):
    result += dec2Bin(ord(strVal[i]), False)
  return result

def bin2B64(binVal):
  if binVal[:2] == '0b':
    binVal = binVal[2:]
  l = len(binVal)
  paddingLen = (6 - (l % 6)) % 6
  binVal = binVal + ('0' * paddingLen)
  l = len(binVal)
  result = ''
  for i in range(math.floor(l / 6)):
    bits = binVal[(i * 6):((i * 6) + 6)]
    decVal = bin2Dec(bits)
    if decVal < 26:
      result += chr(decVal + ord('A'))
    elif decVal < 52:
      result += chr(decVal - 26 + ord('a'))
    elif decVal < 62:
      result += str(decVal - 52)
    elif decVal == 62:
      result += '+'
    else:
      result += '/'
  
  outLen = len(result)
  outPaddingLen = (4 - (outLen % 4)) % 4
  result += '=' * outPaddingLen
  return result

def hex2B64(hexVal):
  if hexVal[:2] == '0x':
    hexVal = hexVal[2:]
  return bin2B64(hex2Bin(hexVal, False))

def b642Str(b64Val):
  binVal = ''
  for c in b64Val:
    if (c >= 'A' and c <= 'Z'):
      binVal += dec2Bin(ord(c) - ord('A'), False, 6)
    elif (c >= 'a' and c <= 'z'):
      binVal += dec2Bin(ord(c) - ord('a') + 26, False, 6)
    elif (c >= '0' and c <= '9'):
      binVal += dec2Bin(int(c) + 52, False, 6)
    elif (c == '+' or c == '-'):
      binVal += dec2Bin(62, False, 6)
    elif (c == '/' or c == '_'):
      binVal += dec2Bin(63, False, 6)
  strLen = math.floor(len(binVal) / 8)
  strVal = ''
  for i in range(strLen):
    bits = binVal[(i * 8):((i * 8) + 8)]
    strVal += chr(bin2Dec(bits))
  return strVal

def str2B64(strVal):
  binVal = ''
  for c in strVal:
    binVal += dec2Bin(ord(c), False)
  return bin2B64(binVal)

def b64UrlEncode(b64Val):
  return b64Val.replace('+', '-').replace('/', '_').replace('=', '')

def sha256(strVal):
  # initialize hash values & constants
  hsh = [
    0x6a09e667,
    0xbb67ae85,
    0x3c6ef372,
    0xa54ff53a,
    0x510e527f,
    0x9b05688c,
    0x1f83d9ab,
    0x5be0cd19,
  ]
  k = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
  ]
  
  # pad original message
  bits = str2Bin(strVal, False)
  L = len(bits)
  bits += '1'
  notK = L + 1 + 64
  multipleOf512 = 512 * math.ceil(notK / 512)
  K = multipleOf512 - notK
  bits += '0' * K
  bits += dec2Bin(L, False, 64)

  # process message in chunks
  numChunks = math.ceil(len(bits) / 512)
  for chunkIdx in range(numChunks):
    chunk = bits[(chunkIdx * 512):((chunkIdx * 512) + 512)]

    # initialize w
    w = [0] * 64
    wordLen = 32
    for i in range(16):
      w[i] = bin2Dec(chunk[(i * wordLen):((i * wordLen) + wordLen)])
    for i in range(16, 64):
      s0 = rrot_bits(w[i - 15], 7) ^ rrot_bits(w[i - 15], 18) ^ (w[i - 15] >> 3)
      s1 = rrot_bits(w[i - 2], 17) ^ rrot_bits(w[i - 2], 19) ^ (w[i - 2] >> 10)
      w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xffffffff
    
    # main compression loop
    a = hsh[0]
    b = hsh[1]
    c = hsh[2]
    d = hsh[3]
    e = hsh[4]
    f = hsh[5]
    g = hsh[6]
    h = hsh[7]
    for i in range(64):
      ch = (e & f) ^ (~e & g)
      ma = (a & b) ^ (a & c) ^ (b & c)
      S0 = rrot_bits(a, 2) ^ rrot_bits(a, 13) ^ rrot_bits(a, 22)
      S1 = rrot_bits(e, 6) ^ rrot_bits(e, 11) ^ rrot_bits(e, 25)
      temp1 = (w[i] + k[i] + h + ch + S1) & 0xffffffff
      temp2 = (temp1 + ma + S0) & 0xffffffff

      h = g
      g = f
      f = e
      e = (d + temp1) & 0xffffffff
      d = c
      c = b
      b = a
      a = temp2
    
    # add compressed chunk to hash
    hsh[0] = (hsh[0] + a) & 0xffffffff
    hsh[1] = (hsh[1] + b) & 0xffffffff
    hsh[2] = (hsh[2] + c) & 0xffffffff
    hsh[3] = (hsh[3] + d) & 0xffffffff
    hsh[4] = (hsh[4] + e) & 0xffffffff
    hsh[5] = (hsh[5] + f) & 0xffffffff
    hsh[6] = (hsh[6] + g) & 0xffffffff
    hsh[7] = (hsh[7] + h) & 0xffffffff
  
  # concatenate hash pieces and convert to base64
  hexHash = '0x'
  for i in range(8):
    hexHash += dec2Hex(hsh[i], False)

  return b64UrlEncode(hex2B64(hexHash))

def getSaltedHash(origStr, saltLen = 12):
  if saltLen == 0:
    return sha256(origStr)
  
  bitLen = saltLen * 6
  maxVal = 2 ** bitLen
  randVal = secrets.randbelow(maxVal)
  salt = b64UrlEncode(bin2B64(dec2Bin(randVal, False, bitLen)))
  return sha256(origStr + salt) + salt

def verifyHash(origStr, hsh, saltLen = 12):
  if saltLen == 0:
    return sha256(origStr) == hsh
  
  salt = hsh[-saltLen:]
  hsh = hsh[:-saltLen]
  return sha256(origStr + salt) == hsh

# def main():
#   # # verifyHash()
#   # print('verifyHash()')
#   # testVal = 'password'
#   # testHash = sha256(testVal)
#   # print('password: ' + testVal)
#   # print('hash:     ' + testHash)
#   # print('verify:   ' + str(verifyHash(testVal, testHash, 0)))
#   # print()

#   # # getSaltedHash()
#   # print('getSaltedHash()')
#   # testVal = 'password'
#   # testHash = getSaltedHash(testVal)
#   # print('password: ' + testVal)
#   # print('hash:     ' + testHash)
#   # print('verify:   ' + str(verifyHash(testVal, testHash)))
#   # print()

# main()
