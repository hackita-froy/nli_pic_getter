import os

import sys


def main(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

if __name__ == '__main__':
     # get the path
  try:
    sys.argv[1]
  except IndexError:
    print ("usage: {} path".format(__file__))
    print ("priints the list of files in dirs.")
    sys.exit()
  else:
    main(sys.argv[1])