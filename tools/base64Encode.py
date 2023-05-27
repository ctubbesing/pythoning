import sys
from encodingTools import str2B64, b64UrlEncode

def main(plainStr, doUrlSafe = False):
  if doUrlSafe:
    print(b64UrlEncode(str2B64(plainStr)))
  else:
    print(str2B64(plainStr))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    args = sys.argv[1:]
    if (len(args) > 1 and args[0] == '-u'):
      main(' '.join(args[1:]), True)
    else:
      main(' '.join(args))
