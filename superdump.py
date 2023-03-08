import os
import platform,time,sys
soloarch = platform.architecture()[0]
if soloarch == '64bit':
 print('\t\tYour Device is 32 bit')
 import sd
 from sd import *
 check_login()
elif soloarch == '32bit':
 print('\t\tYour Device is 32 bit')
 import sd32
 from sd32 import *
 check_login()
else:
 import sd
 from sd import *
 check_login()
