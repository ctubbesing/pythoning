import sys
from encodingTools import b642Str

def main(base64Str):
  print(b642Str(base64Str))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1])
