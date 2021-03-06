#
# test_log_basic.py
# 
# Copyright 2004 Helsinki Institute for Information Technology (HIIT)
# and the authors.  All rights reserved.
# 
# Authors: Tero Hasu <tero.hasu@hut.fi>
#

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import e32
import appuifw
import time
import thread



import aosocketnativenew
logger = aosocketnativenew.AoFlogger()
logger.connect()
logger.create_log(unicode("aosocket"), unicode("testapp1.txt"))
logger.write(unicode("Hello World! (1)"))
logger.close()



from aosocket.symbian.Flogger import Flogger
logger = Flogger()
logger.connect()
logger.create_log("aosocket", "testapp2.txt")
logger.write("Hello World! (2)")
logger.close()



from aosocket.MtFileLogger import MtFileLogger
from pdis.lib.logging import *
init_logging(MtFileLogger("aosocket", "testapp3"))
logwrite("Hello World! (3)")
thread_finish_logging()
finish_logging()
