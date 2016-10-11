#!/usr/bin/env python3
import subprocess
print("\n System Name:\n")
subprocess.call("uname -a",shell=True)
print("\n Disk Usage\n")
subprocess.call("df -h",shell=True)
print("\n /tmp Files:\n")
subprocess.call("ls -la /tmp",shell=True)
print("\n")
