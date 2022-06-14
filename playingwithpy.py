# -*- coding: utf-8 -*-
"""
author: Shyann Francis

application: creating a vault server, sending a secret, retireving the secret
"""

import subprocess

p1 = subprocess.run('vault server -dev', shell=True, capture_output=True)
p2 = subprocess.run('vault kv put secret/hello foo=world', shell=True, capture_output=True)
p3 = subprocess.run('vault kv get secret/hello', shell=True, capture_output=True)
print(p1.stdout, p2.stdout, p3.stdout)
print('complete')
