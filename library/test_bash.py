#!/usr/bin/python

from ansible.module_utils.basic import *
import re

def main():
    module = AnsibleModule(
        argument_spec=dict(
            command=dict(required=True),
            rc=dict(required=False, type='int'),
            value=dict(required=False),
        )
    )
    args = module.params

    command = args.get('command')
    rc = args.get('rc')
    value = args.get('value')
    
    failed = True
    debug = ""
    is_match = None

    #out = subprocess.check_call('ss -ltn state listening sport = ' + port + ' | grep -v " Local Address:Port"', shell=True)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout_list = stdout.decode().strip().split('\n')
    stdout_list2 = [x for x in stdout_list if x]
    count = len(stdout_list2)
    r_rc = process.returncode
    matched = False

    for item in stdout_list2:
        if value is not None:
            pattern = re.compile(r"%s" % value)
            is_match = pattern.match(item)

            if is_match is not None:
                debug = "item=" + item + ", "
                matched = True
                break

    if (rc is not None and rc == r_rc) and (value is not None and matched is not None):
        failed = False
    elif rc is not None and rc == r_rc:
        failed = False
    elif value is not None and matched is not None:
        failed = False

    module.exit_json(rc=r_rc, value=stdout_list2, debug=debug, changed=False, failed=failed)

if __name__ == '__main__':
    main()
