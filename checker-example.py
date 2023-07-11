#!/usr/bin/env python3

import base64
import fileinput
import json
import requests
import sys
import webbrowser
import zlib


CHECKER_SERVER = 'https://server.alviano.net/utils/lp-cp/checker/db6d8ff3-9f6d-4c6a-9c42-c098de3738a2'
#CHECKER_SERVER = 'http://localhost:8000/utils/lp-cp/checker/db6d8ff3-9f6d-4c6a-9c42-c098de3738a2'

RECIPES = [
    "https://asp-chef.alviano.net/#eJzFWE2XsjgT/UuA2jMuZqEoiBo8inzuBLvlU51BW8Kvn0pAxRS7ec95V08bclNVt+6twPNNl9fwPJWPqvHlvv4+VevZvDSt7O7po86aUZrJxxpl+4glrhk9a6RnbVsSdJ5dEvqxVvNcVHHN6NmHYtQ8BtqHYkg99Uq8XlVcIz37UB0SiyHsk3u4kns4lXkMtIZiyDzG55rSU4fCY6A1VIfCYgj1KpyrJsbv0ds9jt72QqwH00e1skZRWIzl4+KthRb/3ps8WJ+v67y6hwNHihaOtOK9e8gYv33m9MZTFkvEQ5/hXAHP+4/i0wfrhYAHLi2Elzq6feFN9VH34WFdEvDd/r7xFqtfxDP9ofhyh/83PmH1EwHvs/pF/nlPW1138RLGR6x+ET/orZ+y+ucIz3gR8ENev6CVjcrqF+OfWP0if0OucSH+hmvNEPBZX/9HvH4xvtXX//mD5ypwRfYTdq6oy4r0aoCdse05Y97HbUWsPh/Mq76esTN69FURrgWUB+3rG9n3eoydIT359Nk+lXv5iY9hT8PNS18axJiwml46eONeM+mFA73XH7jk7d8WRzuzu8XxXCsB99LtG2cLODbvnzW2OPrmucXVnVn3wgG/VMDJT25bnIR5YfU+lC6umQ++gBN5YXNNwFnvXrY4uTOnW5zd6eELJwn1yZ0ZHTf3tN3RD8M1ffmIZ6F4HPfJJ9eh/FEfj/+6n1qcyAvHVR96aeIL8cQ+ME+iPOvOPfzCiXky337opfFbVy8V1hnHUYybC/FEXXOPf/qI95N09VJhHzWz4YOXBPmPYpyB/Zcg/1Gcp4H9lyD/UcyLgf2XIP9R3AcD+y9B/qO47wb2X4L8R7E+mX7f92uLk3E80Q8E+4EiP9Q4HsG6pkjXNa6PYF0396qAM4T+EdwHzu+Hzpp34UTAWYIfKNJL3dyB3b5zHBXqE/XZ9qWL2yJcwxNBuE9etsh/porqkzAv27LJy+7iRJ1JuA9bpDMTz3kJ932LdNbMxY94Mp7XNsbxvswF3Fbg08Z5cr1+9E/GvNhl47d5Fyf6XcZ9sNF8ae4no8uLjPvuozlo4vmi4Pnio3ltJqi+9huly6eP/GcmiM/2m0XACX43KerfAOMidE+b2O8DrLMI10cRLwPchxPic6MiXoaYlxPKc4PfJ4ZYnxnS5wbrc4Try/D9t+95p2nWmvOT5XGtLvOwMH8D3fk5uCP2nppsiiAOF2YOz7LAbZ49322N9CpFZ4c9o/DsGul2sslvfxhFnhnpJSG1lgazU2Uq9m2j+5VpSRIp7MF6n6ckjW7mbCKZhS+T/Vbx69PISB5JOJjmEdRwcMd3doatVFeISdtnfD2ixtc3XdZHffyAHArfrerAeiS+N32EiyzZnHf06NqlcTYv4SB6/36+Z2vjR1Q42cE14yPLOWFnOQ8W41hoJexNNukE9svXMDG+DMiHx3e1IcsJuEt+PKmEHK6BCs9TW9rMtIzss+F6ryVE395M3a42lhxvZsdkvV+mxPXlII1jU5/LPjVYLo/AW0L8/JfHyM3c95bpQZ2aobLLwwVJgNffaLG7hsqohjr/gHqkcDDp9iSOFtPy2zK+joulzDiIlPj3CPwEUEeksJrj/OAeL+z/j0g6ebBeHd0qZxwa0OtQH1P23sP4aPTzXDNKv6jgTK6zNFSq3yiBO0k/Qq+d++febRkOlnFYHPPPdbsEndBIr4R1vwxg/3dzNqxHF/gGygLrdHHVKlhZWenpw5OhV7FfOOVKjYO1drqurCoKk8nJV8YQz7hsaXRda9XdUKfFtxr7hno5gaYfK+txCs7ZxbUmfxvwHUjUHHDZiZ85u9yMhSkF3uRi06w0dPCLRkrXqvz1HOaBOm1rjWfw+8zzBr8ENC7BE/9ALv5ay2Bf7C9pFSwp+3sqh8XuChymoKNs5bCcJl9ra/r63nPUkt/TrsViPr/3YntVs3fJymc5v74Zte0/fN5r2blnXQIu+Ho02OURnLHeN/MWuDyv9OoaFuVlpZ14LPj33JzD4rb8L5Z5oGZXQ/s/5KmCv89Lxu8gKsb3QB6nELc0tO2N3WXcZ2fnBn2n4LWK6dV38zrwSMfH+Z3F8RSt9hSoCXwBM+Mannd1dx7A3EiZl7zBFDS7u/qKJgUW89r4xy+0Otj7kif/yXyW++AbT3HuoC2Yc7sf+PcOvbwz3zRecsY/VvWabX7q5GR/UszZ9hYUTuFTSTJdArMtGwapfQtSXzb3bC6YMA+WRd9s24EHIv30n3z+/H3QnWugxDCTLwqZsdk14rMa4mUHz4FzLxS+RZOI9V7PU9/b5SyHgM8iJz3of3bj1YGrUV85wWw0kvfv+Kf1HpuZo8CtSjZfu8+BsyHM19ZDwPWZaW35wd3GdWAemjAboxvMzNqHe8GcBfnaZXeMfSMzMgp0LQ/SCfTNrvvvBaeEO0cytE5vvf/RzDx/nrnJywRmNWV1e548Xi/K5OBuGQeprxCJ7KeZmcDd5trKer+VSU3YfVfD/M+CwgedTZRgb2bEbfOD+wz4hxyH7Iw9zE7JmJswP8d3dieFanM/8LvhzHRfJuCh30jtznXtAXN11LmD64M+Hjx//3jy8Wf711//AtMvW1c=%21",
]


def compress_object_for_url(obj: object, *, suffix: str = '%21'):
    json_dump = json.dumps(obj, separators=(',', ':')).encode()
    json_dump = base64.b64encode(json_dump)
    return base64.b64encode(zlib.compress(json_dump)).decode() + suffix



args = [arg for arg in sys.argv if arg != "--no-browser"]
no_browser = bool([arg for arg in sys.argv if arg == "--no-browser"])

if len(args) != 3:
    sys.exit("ERROR: missing problem-ID and instance-ID in command parameters")

try:
    problem = int(sys.argv[1])
    instance = int(sys.argv[2])
except ValueError:
    sys.exit("ERROR: problem-ID and instance-ID must be integers")

if problem < 0 or problem > 0:
    sys.exit("ERROR: invalid problem-ID")
if instance < 1 or instance > 5:
    sys.exit("ERROR: invalid instance-ID")

solution = ''.join(fileinput.input("-"))

url = f'{CHECKER_SERVER}/{problem}/{instance}/'

res = requests.post(url, data={"value": solution})
j = res.json()
if 'message' in j:
    print('\n'.join(j['message'].split('\n')[1:]))
    if not no_browser:
        webbrowser.open(
            RECIPES[problem].replace("/#", "/open#" + compress_object_for_url({"input": j['message']}, suffix="") + ";", 1)
        )
else:
    print('WRONG RESPONSE RECEIVED!')
    print(res)
    print(j)
