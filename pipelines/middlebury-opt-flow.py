
from subprocess import call
import sys
from os import listdir
from os.path import isfile, join

# Run alternative pipelines on the middlebury-opt-flow dataset

if len(sys.argv) < 2:
  print('Usage: python middlebury-opt-flow <version number>')
  quit()

version = int(sys.argv[1])

image_dirs = ['Dimetrodon','Grove2','Grove3','Hydrangea','RubberWhale','Urban2','Urban3','Venus']

datasetpath = '/datasets/middlebury-opt-flow/'
inputpath   = datasetpath + 'v0/'
outputpath  = datasetpath + 'v' +str(version)+'/'

call(['mkdir',outputpath])

call('make --directory ./common/ version='+str(version),shell=True)

for image_dir in image_dirs:
  in_img0  = inputpath  +image_dir+ '/frame10.png'
  print in_img0
  out_img0 = outputpath +image_dir+ '/frame10.png'
  call('./common/pipeline_V'+str(version)+'.o '
         +in_img0 + ' ' + outputpath, shell=True)
  call("mv "+outputpath+'output.png '+out_img0,shell=True);

  #img1 = inputpath +image_dir+ '/frame11.png'
  #call(' ./common/pipeline-V'+str(version) 

  print in_img0

