import os
import shutil
from glob import glob
import tempfile

global bufferLines

def getRecursiveFiles(path, filefilter):
  return [y for x in os.walk(path) for y in glob(os.path.join(x[0], filefilter))]

def charoussel(p,t,n,nextchar):
 p = t
 t = n
 n = nextchar
 return p,t,n

def CheckToolTipOnThisLine(line, filename, linenr):
    if len(line)<8: return False, line
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
        #print('%s|%i|%s' % (filename, linenr, line[tooltip_cursor+1:endpos]))
    return changed, line    

def mycopy(namein, nameout): #std move/copy only gave zero byte files
  fin=open(namein, 'r')
  fout=open(nameout, 'w')
  lines=fin.readlines()
  for oneline in lines:
    fout.write(oneline)
  fin.close
  fout.close

def procesALfile(filename):
  linenr = 0
  bufferLines=[]
  alFile = open(filename, 'r')
  alLines = alFile.readlines()
  # tf = tempfile.NamedTemporaryFile(mode='w', encoding='utf8')

  allchanged = False
  newchanged = False
  for oneline in alLines:
    linenr += 1
    newchanged, newline = CheckToolTipOnThisLine(oneline, filename, linenr)
    allchanged = allchanged or newchanged
    bufferLines.append(newline)
    
  alFile.close
  #tf.flush
  #os.fsync(tf.fileno())
  #tf.close
  if allchanged:
    #mycopy(tf.name, os.path.expanduser('~') + '/done-al.txt')
    #shutil.move(tf.name, '/media/edo/Linux Home/Downloads/ISF-AL/App/iSFB/pageext/die.PageExt.al')
    #print(tf.name)
    alFile = open(filename,'w')
    #alFile = open('/media/edo/Linux Home/Downloads/ISF-AL/App/iSFB/pageext/die.PageExt.al', 'w')
    for oneline in bufferLines:
      #print(oneline)
      alFile.write(oneline)
    alFile.close  
    bufferLines=[]


files = getRecursiveFiles('/media/edo/Linux Home/Downloads/iSF-AL/App/iSFB/','*.al')
for filename in files:
  procesALfile(filename)
  #print(filename)
#procesALfile('/media/edo/Linux Home/Downloads/ISF-AL/App/iSFB/pageext/deze.PageExt.al')