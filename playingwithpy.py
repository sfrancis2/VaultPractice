# -*- coding: utf-8 -*-
"""
author: Shyann Francis

application: creating a vault server, sending a secret, retrieving the secret
"""

import subprocess

# p=subprocess.run('export VAULT_ADDR=http://127.0.0.1:8200', 
#                  shell=True, capture_output=True)
# pp=subprocess.run('export VAULT_TOKEN=\'hvs.MKvYZhY4xY8BbrMbrOsO11D3\'', 
#                   shell=True, capture_output=True)
# ppp=subprocess.run('vault status', shell=True, capture_output=True)
# print(pp.stderr.decode("utf-8"), pp.stdout.decode("utf-8"))
p1 = subprocess.run('vault status', shell=True, capture_output=True)
print(p1.stderr.decode("utf-8"), p1.stdout.decode("utf-8"))
p2 = subprocess.run('vault kv put secret/hello foo=world', shell=True, capture_output=True)
print(p2.stderr.decode("utf-8"), p2.stdout.decode("utf-8"))
p3 = subprocess.run('vault kv get secret/hello', shell=True, capture_output=True)
print(p3.stderr.decode("utf-8"), p3.stdout.decode("utf-8"))


print('complete')
