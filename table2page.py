import os
import shutil
from glob import glob
import tempfile

def getRecursiveFiles(path, filefilter):
  return [y for x in os.walk(path) for y in glob(os.path.join(x[0], filefilter))]

def OneTable2Page(tablefile):
  #pagefile = open('', 'w')
  path,filename = os.path.split(tablefile)
  print(path)
  print(filename)



# files = getRecursiveFiles('/media/edo/Linux Home/Downloads/iSF-AL/App/iSFB/','*.Table.al')
# for filename in files:
#   OneTable2Page(filename)

OneTable2Page('/media/edo/Linux Home/Downloads/iSF-AL/App/iSFB/obsolete/PrepackDefinitionISFB.Table.al')