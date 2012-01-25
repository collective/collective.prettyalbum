#!/usr/bin/env python

import sys
import glob, os
from PIL import Image

sys.argv
if len(sys.argv) < 3:
    print "Usage: convert [filter] [size]"
    sys.exit(0)

filter = sys.argv[1]
size = int(sys.argv[2]), int(sys.argv[2])

for infile in glob.glob(filter):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    out = file + ".%s.jpg" % sys.argv[2]
    print "Write: %s" % out
    im.save(out, "jpeg")

