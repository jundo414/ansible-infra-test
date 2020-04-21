#!/usr/bin/python

from ansible.module_utils.basic import *
import configparser

def main():
    module = AnsibleModule(
        argument_spec=dict(
            file=dict(required=True),
            section=dict(required=True),
            key=dict(required=True),
            value=dict(required=True),
        )
    )
    args = module.params

    file = args.get('file')
    section = args.get('section')
    key = args.get('key')
    value = args.get('value')

    failed = True
    message = ""
    cfg_val = ""

    config = configparser.ConfigParser()
    config.read(file)

    try:
        cfg_val = config[section][key]
    except KeyError as e:
        message = "[ERROR] Couldn't find any key in " + file + " (key=" + key + ")"
    except Exceptions as e:
        message = "[ERROR] You've got unexpected error during getting key."
    
    if cfg_val == value:
        failed = False

    module.exit_json(value=cfg_val, message=message, changed=False, failed=failed)

if __name__ == '__main__':
    main()
