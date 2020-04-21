#!/usr/bin/python

from ansible.module_utils.basic import *
import requests
import json

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
            username=dict(required=True),
            password=dict(required=True),
            item=dict(required=False)
        )
    )
    args = module.params

    url = args.get('url')
    username = args.get('username')
    password = args.get('password')
    item = args.get('item')

    response = requests.get(url, verify=False, auth=(username, password))
    data = response.json()
    power_state = data[item]
    #print("\n- WARNING, Current server power state is: %s\n" % data[u'PowerState'])
    #
    #print("- Supported values for server power control are:\n")
    #for i in data[u'Actions'][u'#ComputerSystem.Reset'][u'ResetType@Redfish.AllowableValues']:
    #    print(i)

    module.exit_json(power_state=power_state, changed=False, failed=False)

if __name__ == '__main__':
    main()
