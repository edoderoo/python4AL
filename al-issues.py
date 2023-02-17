import os
from glob import glob
import tempfile

def getRecursiveFiles(path, filefilter):
  return [y for x in os.walk(path) for y in glob(os.path.join(x[0], filefilter))]

def CheckToolTip(line, filename, linenr):
    changed = False
    tooltip_cursor = line.lower().find('tooltip')
    if tooltip_cursor>0:
      while line[tooltip_cursor] != '\'':
        tooltip_cursor+=1
      endpos = tooltip_cursor+1
      while (line[endpos] != '\'') and (line[endpos-1]!='\\') and (line[endpos+1] != '\''): 
        endpos += 1
      if (line[endpos-1] != '.') :
        changed = True
        line = line[:endpos]+'.'+line[endpos:]
        print('%s|%i|%s' % (filename, linenr, line[tooltip_cursor+1:endpos]))
    return changed    


def procesALfile(filename):
  linenr = 0
  alFile = open(filename, 'r')
  alLines = alFile.readlines()
  # tf = tempfile.NamedTemporaryFile(mode='w', encoding='utf8')
  tf = open(os.path.expanduser('~') + '/edo.txt','w')

  changed = False
  for oneline in alLines:
    linenr += 1
    changed = changed or CheckToolTip(oneline, filename, linenr)
    tf.write(oneline)
  print(tf.name)
  # os.rename(tf.name, '/tmp/edo.txt')
  tf.close

# files = getRecursiveFiles('/media/edo/Linux Home/Downloads/ISF-AL/App/iSFB','*.al')
# for filename in files:
#   procesALfile(filename)
procesALfile('/media/edo/Linux Home/Downloads/ISF-AL/App/iSFB/pageext/LocationCardISFB.PageExt.al')