import os
from glob import glob
import tempfile

def getRecursiveFiles(path, filefilter):
  return [y for x in os.walk(path) for y in glob(os.path.join(x[0], filefilter))]

def charoussel(p,t,n,nextchar):
 p = t
 t = n
 n = nextchar
 return p,t,n

def CheckToolTip(line, filename, linenr):
    if len(line)<8: return False
    changed = False
    orgline=line
    tooltip_cursor = line.lower().find('tooltip')
    if tooltip_cursor>0:
      while line[tooltip_cursor] != '\'':
        tooltip_cursor+=1
      endpos = tooltip_cursor+1
      prevchar=line[tooltip_cursor-1]
      prevchar='\\'
      thischar=line[tooltip_cursor]
      nextchar=line[tooltip_cursor+1]
      while ((thischar != '\'') or ((thischar == '\'') and (     (prevchar=='\'') or (nextchar=='\'') or (prevchar=='\\')     )   )):
        endpos += 1
        prevchar,thischar,nextchar=charoussel(prevchar,thischar,nextchar,line[endpos])

      if (prevchar != '.') :
        changed = True
        line = line[:endpos-1]+'.'+line[endpos-1:]
        print('%s|%i|%s' % (filename, linenr, line[tooltip_cursor+1:endpos]))
    return changed    


def procesALfile(filename):
  linenr = 0
  alFile = open(filename, 'r')
  alLines = alFile.readlines()
  # tf = tempfile.NamedTemporaryFile(mode='w', encoding='utf8')

  changed = False
  for oneline in alLines:
    tf = open(os.path.expanduser('~') + '/todo-al.txt','w')
    linenr += 1
    changed = changed or CheckToolTip(oneline, filename, linenr)
    tf.write(oneline)
  if changed:
    tf.close
    os.copy_file_range(tf.name, '/media/edo/Linux Home/Downloads/ISF-AL/App/iSFB/pageext/LocationCardISFB2.PageExt.al',1)
    print(tf.name)

# files = getRecursiveFiles('/media/edo/Linux Home/Downloads/ISF-AL/App/iSFB','*.al')
# for filename in files:
#   procesALfile(filename)
procesALfile('/media/edo/Linux Home/Downloads/ISF-AL/App/iSFB/pageext/LocationCardISFB.PageExt.al')