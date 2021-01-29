#!/usr/bin/python
# coding: utf8
import re,sys,commands
command = "/usr/local/nagios/libexec/check_log -F /var/log/apache2/access.log -O oldlog -q 'GET /nagios/images/thermok.png HTTP/1.1' -w 9"
result = commands.getstatusoutput(command)
result0 = bool(re.search("match=0;;;0", result[1]))
result1 = bool(re.search("match=1;;;0", result[1]))
result2 = bool(re.search("match=2;;;0", result[1]))
result3 = bool(re.search("match=3;;;0", result[1]))
result4 = bool(re.search("match=4;;;0", result[1]))
result5 = bool(re.search("match=5;;;0", result[1]))
result6 = bool(re.search("match=6;;;0", result[1]))
result7 = bool(re.search("match=7;;;0", result[1]))
result8 = bool(re.search("match=8;;;0", result[1]))
result9 = bool(re.search("match=9;;;0", result[1]))
if result0 or result1 or result2 or result3:
    print("OK:")
    print("moins de 4 commentaires") 
    print("ces 4 dernières heures.")
    sys.exit(0)
elif result4 or result5 or result6 or result7 or result8 or result9:
    print("WARNING")
    print("entre 4 et 9 commentaires")
    print("ces 4 dernières heures.")
    sys.exit(1)
else:
    print("CRITICAL")
    print("plus de 10 commentaires")
    print("ces 4 dernières heures.")
    sys.exit(2)

