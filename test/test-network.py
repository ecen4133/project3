#import base64
#import re
import sys
#import hmac
#import hashlib
#import itertools
import os
import os.path
import subprocess
#import zipfile
import sys
#import signal
import time
import urllib.request


path = "./"
network_grades = []



try:
  # Launch python file
  #p = os.spawnl(os.P_NOWAIT, '/usr/bin/python', 'python', python_file)
  subprocess.run(['python3', 'attack.py'])
    
  time.sleep(1)
  # Make webrequest
  response = urllib.request.urlopen('http://freeaeskey.xyz/')
  #response = urllib.urlretrieve('http://freeaeskey.xyz/')
  
  resp = response.read()

  if '4d6167696320576f7264733a2053717565616d697368204f7373696672616765' in resp:
    print('Key injected!')
    print(resp)
    #os.kill(p, signal.SIGKILL)
    network_grades.append((10,''))
  else:
    print('failed to inject key')
    #os.kill(p, signal.SIGKILL)
    network_grades.append(0,("Failed to inject key."))

  #results = subprocess.check_output(['python', python_file], env=self.new_env)
except Exception as e:
  print("Failure - python exception.")
  network_grades.append((0,"Code failure."))

#else:
#  network_grades.append((0,"No file submitted."))
#  sys.exit(-1)
  
print(network_grades)
sys.exit(0)
