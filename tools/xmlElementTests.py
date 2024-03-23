from xmlElement import XMLElement, XMLAttribute

def runLayoutTests():
  print('0 - 0')
  e00 = XMLElement('tag')
  print(e00.toString())

  print('1 - 0')
  a1 = XMLAttribute('att1', 'val1')
  e10 = XMLElement('tag',
                   attributes = [ a1 ])
  print(e10.toString())

  print('2+ - 0')
  a2 = XMLAttribute('att2', 'val2')
  e20 = XMLElement('tag',
                   attributes = [ a1, a2 ])
  print(e20.toString())

  print('0 - 1 raw (special case)')
  eRaw = XMLElement('', rawContent = 'raw content')
  e01raw = XMLElement('tag',
                      children = [ eRaw ])
  print(e01raw.toString())

  print('1 - 1 raw')
  e11raw = XMLElement('tag',
                      attributes = [ a1 ],
                      children = [ eRaw ])
  print(e11raw.toString())

  print('2+ - 1 raw')
  e21raw = XMLElement('tag',
                      attributes = [ a1, a2 ],
                      children = [ eRaw ])
  print(e21raw.toString())

  print('0 - 1')
  e1 = XMLElement('tag1', children = [ eRaw ])
  e01 = XMLElement('tag',
                   children = [ e1 ])
  print(e01.toString())

  print('1 - 1')
  e11 = XMLElement('tag',
                   attributes = [ a1 ],
                   children = [ e1 ])
  print(e11.toString())

  print('2+ - 1')
  e21 = XMLElement('tag',
                   attributes = [ a1, a2 ],
                   children = [ e1 ])
  print(e21.toString())

  print('0 - 2+')
  e2 = XMLElement('tag2', children = [ eRaw ])
  e02 = XMLElement('tag',
                   children = [ e1, e2 ])
  print(e02.toString())

  print('1 - 2+')
  e12 = XMLElement('tag',
                   attributes = [ a1 ],
                   children = [ e1, e2 ])
  print(e12.toString())

  print('2+ - 2+')
  e22 = XMLElement('tag',
                   attributes = [ a1, a2 ],
                   children = [ e1, e2 ])
  print(e22.toString())

def runIndentTests():
  eRaw = XMLElement('', rawContent = 'raw content')
  a1 = XMLAttribute('att1', 'val1')
  a2 = XMLAttribute('att2', 'val2')
  e1 = XMLElement('tag1', children = [ eRaw ])
  e2 = XMLElement('tag2', children = [ eRaw ])
  e3 = XMLElement('tag3',
                  attributes = [ a1 ],
                  children = [ e1, e2 ])
  e4 = XMLElement('tag4',
                  attributes = [ a1, a2 ],
                  children = [ e3, e1, e2 ])
  
  print(e4.toString())
  print()
  print(e4.toString(indentSize = 4))
  print()
  print(e4.toString(baseIndent = 4))
  print()
  print(e4.toString(baseIndent = 4, indentSize = 4))

def main():
  print('=== Attribute & Child Layout')
  runLayoutTests()
  print('============================\n')

  print('===  Indentation  ==========')
  runIndentTests()
  print('============================\n')

main()
