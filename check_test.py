#!/usr/bin/python
# coding: utf8

import re,sys,commands

command = /usr/local/nagios/libexec/check_log

result = commands.getstatusoutput(command)

print(result)
