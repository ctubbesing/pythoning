class XMLAttribute():
  def __init__(self, name, value):
    self.name = name
    self.value = value
  
  def toString(self):
    return self.name + '="' + self.value + '"'

class XMLElement():
  def __init__(self,
               tag,
               attributes,
               children,
               rawContent = '',
               indentSize = 2):
    self.tag = tag
    self.attributes = attributes
    self.children = children
    self.rawContent = rawContent
    self.indentSize = indentSize
  
  def isRaw(self):
    return len(self.rawContent) > 0
  
  def toString(self, baseIndent = 0):
    if (self.isRaw()):
      return self.rawContent
    
    def indent(level = 0):
      return level * self.indentSize * ' '
    
    def buildOpeningTag(isSelfClosing):
      tagStr = ''
      if (len(self.attributes) == 0):
        tagStr += ' />\n' if isSelfClosing else '>\n'
      elif (len(self.attributes) == 1):
        tagStr += ' ' + self.attributes[0].toString() + (' />\n' if isSelfClosing else '>\n')
      else:
        tagStr += '\n'
        for a in self.attributes:
          tagStr += indent(baseIndent + 1) + a.toString() + '\n'
        tagStr += indent(baseIndent) + ('/>\n' if isSelfClosing else '>\n')
      return tagStr
    
    xmlStr = indent(baseIndent) + '<' + self.tag
    closingTag = '</' + self.tag + '>\n'
    if (len(self.children) == 0):
      xmlStr += buildOpeningTag(isSelfClosing = True)
    elif (len(self.attributes) == 1 and len(self.children) == 1 and self.children[0].isRaw()):
      xmlStr += '>' + self.children[0].rawContent + closingTag
    else:
      xmlStr += buildOpeningTag(isSelfClosing = False)
      for c in self.children:
        if (c.isRaw()):
          xmlStr += indent(baseIndent + 1) + c.toString() + '\n'
        else:
          xmlStr += c.toString(baseIndent + 1)
      xmlStr += indent(baseIndent) + closingTag
    
    return xmlStr
