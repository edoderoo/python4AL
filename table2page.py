import os
import shutil
from glob import glob
import tempfile

def getRecursiveFiles(path, filefilter):
  return [y for x in os.walk(path) for y in glob(os.path.join(x[0], filefilter))]

def OneTable2Page(tablefilename):
  path,filename = os.path.split(tablefilename)
  pagefilename = filename.lower().replace('.table.al','.page.al')
  pagepath=os.path.join(path,pagefilename)
  tablefile=open(tablefilename,'r')
  tablelines=tablefile.readlines()
  for tableline in tablelines:
    print(tableline)
    
  # pagefile=open(pagefilename,'w')

  tablefile.close()
  # close(pagefile)



if False:
  files = getRecursiveFiles('/media/edo/Linux Home/Downloads/iSF-AL/App/iSFB/','*.?able.al')
  for filename in files:
    OneTable2Page(filename)
else:
  OneTable2Page('/media/edo/Linux Home/Downloads/iSF-AL/App/iSFB/obsolete/PrepackDefinitionISFB.Table.al')