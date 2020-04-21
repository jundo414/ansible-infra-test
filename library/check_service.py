#!/usr/bin/python

from ansible.module_utils.basic import *
import dbus

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            is_running=dict(required=False),
            is_enabled=dict(required=False),
        )
    )
    args = module.params

    name = args.get('name')
    is_running = args.get('is_running')
    is_enabled = args.get('is_enabled')

    sysbus = dbus.SystemBus()
    systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
    manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')

    r_running = False
    r_enabled = False
    message = ""

    try:
        enabled = str(manager.GetUnitFileState(name))

        if enabled == "enabled":
            r_enabled = True
    except Exception as e:
        message = "couldn't find the service. (" + name + ")"

    try:
        service = sysbus.get_object('org.freedesktop.systemd1', object_path=manager.GetUnit(name))
        interface = dbus.Interface(service, dbus_interface='org.freedesktop.DBus.Properties')

        status = str(interface.Get('org.freedesktop.systemd1.Unit', 'ActiveState'))
        if status == "active":
            r_running = True
    except Exception as e:
        r_running = False
    
    failed = False
    if is_running is None and r_running == False:
        failed = True
    elif is_enabled is None and r_enabled == False:
        failed = True
    
    module.exit_json(message=message, changed=False, failed=failed)

if __name__ == '__main__':
    main()
