#!/usr/bin/python

from ansible.module_utils.basic import *
import rpm

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            is_installed=dict(required=True, type='bool'),
            version=dict(required=False),
            flag=dict(required=False),
        )
    )
    args = module.params

    name = args.get('name')
    is_installed = args.get('is_installed')
    version = args.get('version')
    flag = args.get('flag')
    chk_installed = False
    chk_version = False

    failed = True

    ts = rpm.TransactionSet()
    mi = ts.dbMatch()
    for h in mi:
        if h['name'] == name:
            chk_installed = True
            
            if flag == '>=' and h['version'] >= version:
                chk_version = True
            if flag == '>' and h['version'] > version:
                chk_version = True
            if flag == '<=' and h['version'] <= version:
                chk_version = True
            if flag == '<' and h['version'] < version:
                chk_version = True
            if flag == '==' and h['version'] == version:
                chk_version = True

    if is_installed is True and chk_installed is True and chk_version:
        failed = False
    if is_installed is False and chk_installed is False:
        failed = False
    
    module.exit_json(chk_installed=chk_installed, chk_version=chk_version, changed=False, failed=failed)

if __name__ == '__main__':
    main()
