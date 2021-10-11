import base64
import re
import sys
import hmac
import hashlib
import itertools
import json
import os
import os.path
import subprocess
import zipfile
import sys
import signal
import time
import urllib2


def grade_network(file):
  path = "./"
  network_grades = []
  
  p1 = os.path.normpath(os.path.join(path, file))
  print('Grading "%s"' % p1)
  
  if os.path.exists(p1):
  
    try:
      # Launch python file
      p = os.spawnl(os.P_NOWAIT, '/usr/bin/python', 'python', python_file)
      time.sleep(1)
      # Make webrequest
      response = urllib2.urlopen('http://freeaeskey.xyz/')
      resp = response.read()

      if '4d6167696320576f7264733a2053717565616d697368204f7373696672616765' in resp:
        printc(colors.GREEN, 'Key injected!')
        print(resp)
        os.kill(p, signal.SIGKILL)
        network_grades.append((10,''))
      else:
        printc(colors.RED, 'failed to inject key')
        os.kill(p, signal.SIGKILL)
        network_grades.append(0,("Failed to inject key."))

      #results = subprocess.check_output(['python', python_file], env=self.new_env)
    except KeyboardInterrupt:
      print 'Hit Ctrl-C, stopping'
      sys.exit(1)
    except Exception as e:
      printc(colors.RED, 'hmm: %s' % e)
      network_grades.append((0,"Code failure."))
  else:
    network_grades.append((0,"No file submitted."))
  
  print(network_grades)
  sys.exit(0)
  
  
if __name__ == '__main__':
  grade_network(sys.argv[1])
