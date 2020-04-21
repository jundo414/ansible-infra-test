#!/usr/bin/python

from ansible.module_utils.basic import *
import re

def main():
    module = AnsibleModule(
        argument_spec=dict(
            file=dict(required=True),
            validations=dict(required=True, type='list'),
        )
    )
    args = module.params

    file = args.get('file')
    validations = args.get('validations')

    item_ng = ""
    item_ok = list()

    for item in validations:
        matched = False
        line_ok = ""
        f = open(file, 'r')
        line = f.readline()
        while line:
            pattern = re.compile(r"%s" % item)
            is_match = pattern.match(line)

            if is_match is not None:
                matched = True
                line_ok = line
                break

            line = f.readline()

        f.close()

        if matched:
            failed = False
            item_ok.append(line_ok)
        else:
            failed = True
            item_ng = item
            break

    module.exit_json(item_ok=item_ok, item_ng=item_ng, changed=False, failed=failed)

if __name__ == '__main__':
    main()
