from urllib.request import urlopen
from urllib.request import Request
import os
import re
import string
import math

url = "http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest"
filename_tmp = "delegated-apnic-latest"
chnroute_new = "chnroute.new"
chnroute_old = "chnroute.old"

req = Request(url)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

result = urlopen(req)

file = result.read()

with open(filename_tmp, "wb") as f:
    f.write(file)

ip_file = open(filename_tmp)
pattern = re.compile(r"apnic\|CN\|ipv4\|((?:(?:25[0-5]|2[0-4]\d|(?:1\d{2}|[1-9]?\d))\.){3}(?:25[0-5]|2[0-4]\d|(?:1\d{2}|[1-9]?\d)))\|\d+")

with open(chnroute_new, "w") as chn_file:
    for line in ip_file:
        matched = re.match(pattern, line)
        if None != matched:
            splitinfo = matched.group(0).split("|")
            chn_file.write('%s/%d\n' % (splitinfo[3],(32 - math.log(int(splitinfo[4]), 2))))

ip_file.close()



