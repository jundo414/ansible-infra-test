#!/usr/bin/python

from ansible.module_utils.basic import *
import os
import stat
import grp
import pwd

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=False),
            user  = dict(required=False),
            group  = dict(required=False),
            mode  = dict(required=False),
        )
    )
    args = module.params

    path = args.get('path')
    user = args.get('user')
    group = args.get('group')
    mode = args.get('mode')

    failed = True

    status = os.stat(path)
    stat_mode = status.st_mode

    #st_exists = stat.st_exists
    s_isdir = stat.S_ISDIR(stat_mode)
    s_mode = str(oct(stat.S_IMODE(stat_mode)))[-4:]

    s_user = pwd.getpwuid(status.st_uid)[0]
    s_group = grp.getgrgid(status.st_gid)[0]

    message = "(isdir=" + str(s_isdir) + ", user=" + s_user + ", group=" + s_group + ", mode=" + s_mode + ")"

    if s_isdir is False and user == s_user and group == s_group and mode == s_mode:
        failed = False
    
    module.exit_json(message=message, failed=failed, changed=False, ignore_errors=True)

if __name__ == '__main__':
    main()
