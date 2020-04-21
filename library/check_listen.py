#!/usr/bin/python

from ansible.module_utils.basic import *
import socket


def main():
    module = AnsibleModule(
        argument_spec = dict(
            proto = dict(required=False),
            addr  = dict(required=False),
            port  = dict(required=True),
        )
    )
    args = module.params

    protocol = args.get('proto') or 'tcp'
    address = args.get('addr') or '0.0.0.0'
    port = int(args.get('port'))

    failed = True
    
    if protocol == 'tcp':
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((address, port))
            failed = False
        except:
             message = "[ERROR] TCP: Couldn't open socket. (" + address + ":" + str(port) +")"
        finally:
            if(failed is False and port != sock.getsockname()[1]):
                 message = "TCP: " + address + ":" + str(port) + " was connected successfully."
            sock.close()
    else:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(3)
            sock.connect((address, port))
            failed = False
        except:
             message = "[ERROR] UDP: Couldn't open socket. (" + address + ":" + str(port) +")"
        finally:
            if(failed is False and port != sock.getsockname()[1]):
                 message = "[INFO] UDP: " + address + ":" + str(port) + " was connected successfully."
            sock.close()

    module.exit_json(message= message, failed=failed, changed=False, ignore_errors=True)

if __name__ == '__main__':
    main()
