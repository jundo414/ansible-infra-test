# About ansible-test
This is ansible library for testing infrastructure.
If you use this library, you can test infrastructures with ansible after build it with ansible.
If you want to use this, just set library directory on playbook top directory.

# How to run
```
$ ansible-playbook -i inventory site.yml -vv
```

# Result
<details>
<summary>show logs</summary>

```
2020-04-21 13:41:14,743 p=77871 u=jundo414 n=ansible | ansible-playbook 2.9.6
  config file = /Users/jundo414/work/ansible-test/ansible.cfg
  configured module search path = ['/Users/jundo414/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/Cellar/ansible/2.9.6_1/libexec/lib/python3.8/site-packages/ansible
  executable location = /usr/local/bin/ansible-playbook
  python version = 3.8.2 (default, Mar 11 2020, 00:29:50) [Clang 11.0.0 (clang-1100.0.33.17)]
2020-04-21 13:41:14,743 p=77871 u=jundo414 n=ansible | Using /Users/jundo414/work/ansible-test/ansible.cfg as config file
2020-04-21 13:41:15,152 p=77871 u=jundo414 n=ansible | statically imported: /Users/jundo414/work/ansible-test/roles/test/tasks/check_listen.yml
2020-04-21 13:41:15,210 p=77871 u=jundo414 n=ansible | statically imported: /Users/jundo414/work/ansible-test/roles/test/tasks/check_dir.yml
2020-04-21 13:41:15,212 p=77871 u=jundo414 n=ansible | statically imported: /Users/jundo414/work/ansible-test/roles/test/tasks/check_file.yml
2020-04-21 13:41:15,217 p=77871 u=jundo414 n=ansible | statically imported: /Users/jundo414/work/ansible-test/roles/test/tasks/check_package.yml
2020-04-21 13:41:15,220 p=77871 u=jundo414 n=ansible | statically imported: /Users/jundo414/work/ansible-test/roles/test/tasks/check_service.yml
2020-04-21 13:41:15,223 p=77871 u=jundo414 n=ansible | statically imported: /Users/jundo414/work/ansible-test/roles/test/tasks/inspect_file.yml
2020-04-21 13:41:15,225 p=77871 u=jundo414 n=ansible | statically imported: /Users/jundo414/work/ansible-test/roles/test/tasks/inspect_ini.yml
2020-04-21 13:41:15,229 p=77871 u=jundo414 n=ansible | statically imported: /Users/jundo414/work/ansible-test/roles/test/tasks/test_bash.yml
2020-04-21 13:41:15,233 p=77871 u=jundo414 n=ansible | statically imported: /Users/jundo414/work/ansible-test/roles/test/tasks/test_api.yml
2020-04-21 13:41:15,303 p=77871 u=jundo414 n=ansible | PLAYBOOK: site.yml **********************************************************************************************************************************************************************
2020-04-21 13:41:15,303 p=77871 u=jundo414 n=ansible | 1 plays in site.yml
2020-04-21 13:41:15,305 p=77871 u=jundo414 n=ansible | PLAY [server] ***************************************************************************************************************************************************************************
2020-04-21 13:41:15,327 p=77871 u=jundo414 n=ansible | META: ran handlers
2020-04-21 13:41:15,334 p=77871 u=jundo414 n=ansible | TASK [test : check the listen ports..] **************************************************************************************************************************************************
2020-04-21 13:41:15,334 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/check_listen.yml:2
2020-04-21 13:41:16,780 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'proto': 'tcp', 'addr': '10.16.56.101', 'port': '22'}) => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python"}, "ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"addr": "10.16.56.101", "port": "22", "proto": "tcp"}, "message": "TCP: 10.16.56.101:22 was connected successfully."}
2020-04-21 13:41:17,337 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'proto': 'tcp', 'addr': '10.16.56.101', 'port': '80'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"addr": "10.16.56.101", "port": "80", "proto": "tcp"}, "message": "TCP: 10.16.56.101:80 was connected successfully."}
2020-04-21 13:41:17,341 p=77871 u=jundo414 n=ansible | TASK [test : check the listen ports..] **************************************************************************************************************************************************
2020-04-21 13:41:17,341 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/check_listen.yml:12
2020-04-21 13:41:18,015 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'addr': '10.16.56.101', 'port': '3000'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"addr": "10.16.56.101", "port": "3000"}, "message": "TCP: 10.16.56.101:3000 was connected successfully."}
2020-04-21 13:41:18,495 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'addr': '10.16.56.101', 'port': '111'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"addr": "10.16.56.101", "port": "111"}, "message": "TCP: 10.16.56.101:111 was connected successfully."}
2020-04-21 13:41:18,500 p=77871 u=jundo414 n=ansible | TASK [test : check the listen ports..] **************************************************************************************************************************************************
2020-04-21 13:41:18,500 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/check_listen.yml:21
2020-04-21 13:41:19,185 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'port': '111'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"port": "111"}, "message": "TCP: 0.0.0.0:111 was connected successfully."}
2020-04-21 13:41:19,189 p=77871 u=jundo414 n=ansible | TASK [test : check the listen ports..] **************************************************************************************************************************************************
2020-04-21 13:41:19,190 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/check_listen.yml:28
2020-04-21 13:41:19,867 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'proto': 'udp', 'port': '67'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"port": "67", "proto": "udp"}, "message": "[INFO] UDP: 0.0.0.0:67 was connected successfully."}
2020-04-21 13:41:20,395 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'proto': 'tcp', 'port': '111'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"port": "111", "proto": "tcp"}, "message": "TCP: 0.0.0.0:111 was connected successfully."}
2020-04-21 13:41:20,400 p=77871 u=jundo414 n=ansible | TASK [test : check directory..] *********************************************************************************************************************************************************
2020-04-21 13:41:20,400 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/check_dir.yml:2
2020-04-21 13:41:21,209 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'path': '/var/tmp', 'user': 'root', 'group': 'root', 'mode': '1777'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"group": "root", "mode": "1777", "path": "/var/tmp", "user": "root"}, "message": "(isdir=True, user=root, group=root, mode=1777)"}
2020-04-21 13:41:21,784 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'path': '/root', 'user': 'root', 'group': 'root', 'mode': '0550'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"group": "root", "mode": "0550", "path": "/root", "user": "root"}, "message": "(isdir=True, user=root, group=root, mode=0550)"}
2020-04-21 13:41:22,282 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'path': '/home/stack', 'user': 'stack', 'group': 'stack', 'mode': '0700'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"group": "stack", "mode": "0700", "path": "/home/stack", "user": "stack"}, "message": "(isdir=True, user=stack, group=stack, mode=0700)"}
2020-04-21 13:41:22,287 p=77871 u=jundo414 n=ansible | TASK [test : check directory..] *********************************************************************************************************************************************************
2020-04-21 13:41:22,287 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/check_file.yml:2
2020-04-21 13:41:23,162 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'path': '/etc/passwd', 'user': 'root', 'group': 'root', 'mode': '0644'}) => {"ansible_loop_var": "item", "changed": false, "ignore_errors": true, "item": {"group": "root", "mode": "0644", "path": "/etc/passwd", "user": "root"}, "message": "(isdir=False, user=root, group=root, mode=0644)"}
2020-04-21 13:41:23,167 p=77871 u=jundo414 n=ansible | TASK [test : check the rpm packages..] **************************************************************************************************************************************************
2020-04-21 13:41:23,167 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/check_package.yml:2
2020-04-21 13:41:24,486 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'name': 'httpd', 'is_installed': True, 'version': '2.4', 'flag': '>='}) => {"ansible_loop_var": "item", "changed": false, "chk_installed": true, "chk_version": true, "item": {"flag": ">=", "is_installed": true, "name": "httpd", "version": "2.4"}}
2020-04-21 13:41:25,367 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'name': 'gzip', 'is_installed': True, 'version': '1.2', 'flag': '>'}) => {"ansible_loop_var": "item", "changed": false, "chk_installed": true, "chk_version": true, "item": {"flag": ">", "is_installed": true, "name": "gzip", "version": "1.2"}}
2020-04-21 13:41:26,226 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'name': 'python', 'is_installed': True, 'version': '2.7.5', 'flag': '=='}) => {"ansible_loop_var": "item", "changed": false, "chk_installed": true, "chk_version": true, "item": {"flag": "==", "is_installed": true, "name": "python", "version": "2.7.5"}}
2020-04-21 13:41:26,231 p=77871 u=jundo414 n=ansible | TASK [test : check the rpm packages..] **************************************************************************************************************************************************
2020-04-21 13:41:26,231 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/check_package.yml:14
2020-04-21 13:41:27,309 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'name': 'bind', 'is_installed': False}) => {"ansible_loop_var": "item", "changed": false, "chk_installed": false, "chk_version": false, "item": {"is_installed": false, "name": "bind"}}
2020-04-21 13:41:28,156 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'name': 'bind-utils', 'is_installed': False}) => {"ansible_loop_var": "item", "changed": false, "chk_installed": false, "chk_version": false, "item": {"is_installed": false, "name": "bind-utils"}}
2020-04-21 13:41:28,161 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:28,161 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/check_service.yml:2
2020-04-21 13:41:29,062 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'name': 'httpd.service', 'is_running': True, 'is_enabled': None, True: None}) => {"ansible_loop_var": "item", "changed": false, "item": {"name": "httpd.service", "is_running": true, "is_enabled": null, "true": null}, "message": "", "warnings": ["The value True (type bool) in a string field was converted to u'True' (type string). If this does not look like what you expect, quote the entire value to ensure it does not change."]}
2020-04-21 13:41:29,538 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'name': 'cpupower.service', 'is_running': False, 'is_enabled': None, False: None}) => {"ansible_loop_var": "item", "changed": false, "item": {"name": "cpupower.service", "is_running": false, "is_enabled": null, "false": null}, "message": "", "warnings": ["The value False (type bool) in a string field was converted to u'False' (type string). If this does not look like what you expect, quote the entire value to ensure it does not change."]}
2020-04-21 13:41:29,539 p=77871 u=jundo414 n=ansible | [WARNING]: The value True (type bool) in a string field was converted to u'True' (type string). If this does not look like what you expect, quote the entire value to ensure it does not
change.

2020-04-21 13:41:29,539 p=77871 u=jundo414 n=ansible | [WARNING]: The value False (type bool) in a string field was converted to u'False' (type string). If this does not look like what you expect, quote the entire value to ensure it does
not change.

2020-04-21 13:41:29,544 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:29,544 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/inspect_file.yml:2
2020-04-21 13:41:30,185 p=77871 u=jundo414 n=ansible | ok: [master01] => {"changed": false, "item_ng": "", "item_ok": ["TYPE=Ethernet\n", "BOOTPROTO=static\n", "DEFROUTE=yes\n", "NAME=enp0s3\n", "DEVICE=enp0s3\n", "ONBOOT=yes\n", "IPADDR=172.16.12.1\n", "NETMASK=255.255.255.0\n"]}
2020-04-21 13:41:30,189 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:30,190 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/inspect_ini.yml:2
2020-04-21 13:41:31,002 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'file': '/etc/nova/nova.conf', 'section': 'DEFAULT', 'key': 'verbose', 'value': 'True'}) => {"ansible_loop_var": "item", "changed": false, "item": {"file": "/etc/nova/nova.conf", "key": "verbose", "section": "DEFAULT", "value": "True"}, "message": "", "value": "True", "warnings": ["The value True (type bool) in a string field was converted to u'True' (type string). If this does not look like what you expect, quote the entire value to ensure it does not change."]}
2020-04-21 13:41:31,483 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'file': '/etc/nova/nova.conf', 'section': 'DEFAULT', 'key': 'vncserver_listen', 'value': '192.168.206.130'}) => {"ansible_loop_var": "item", "changed": false, "item": {"file": "/etc/nova/nova.conf", "key": "vncserver_listen", "section": "DEFAULT", "value": "192.168.206.130"}, "message": "", "value": "192.168.206.130"}
2020-04-21 13:41:32,105 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'file': '/etc/nova/nova.conf', 'section': 'glance', 'key': 'api_servers', 'value': '192.168.206.130:9292'}) => {"ansible_loop_var": "item", "changed": false, "item": {"file": "/etc/nova/nova.conf", "key": "api_servers", "section": "glance", "value": "192.168.206.130:9292"}, "message": "", "value": "192.168.206.130:9292"}
2020-04-21 13:41:32,574 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'file': '/etc/nova/nova.conf', 'section': 'libvirt', 'key': 'virt_type', 'value': 'qemu'}) => {"ansible_loop_var": "item", "changed": false, "item": {"file": "/etc/nova/nova.conf", "key": "virt_type", "section": "libvirt", "value": "qemu"}, "message": "", "value": "qemu"}
2020-04-21 13:41:32,579 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:32,580 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/test_bash.yml:2
2020-04-21 13:41:33,428 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'command': 'date | wc -l', 'rc': 0, 'value': '1'}) => {"ansible_loop_var": "item", "changed": false, "debug": "item=1, ", "item": {"command": "date | wc -l", "rc": 0, "value": "1"}, "rc": 0, "value": ["1"]}
2020-04-21 13:41:33,432 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:33,432 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/test_bash.yml:11
2020-04-21 13:41:34,118 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'command': '/usr/bin/calc_sum 1 4', 'value': '5'}) => {"ansible_loop_var": "item", "changed": false, "debug": "item=5, ", "item": {"command": "/usr/bin/calc_sum 1 4", "value": "5"}, "rc": 0, "value": ["5"]}
2020-04-21 13:41:34,122 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:34,122 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/test_bash.yml:19
2020-04-21 13:41:34,806 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'command': 'hostname -s', 'rc': 0}) => {"ansible_loop_var": "item", "changed": false, "debug": "", "item": {"command": "hostname -s", "rc": 0}, "rc": 0, "value": ["master01"]}
2020-04-21 13:41:34,810 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:34,810 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/test_bash.yml:27
2020-04-21 13:41:35,511 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'command': 'cinder list', 'value': "r'*cinder-volume*cotoller@cdot-nfs*enabled*up*'"}) => {"ansible_loop_var": "item", "changed": false, "debug": "", "item": {"command": "cinder list", "value": "r'*cinder-volume*cotoller@cdot-nfs*enabled*up*'"}, "rc": 0, "value": ["+------------------+------------------------+------+---------+-------+------------------------+-----------------+", "|      Binary      |           Host         | Zone |  Status | State |         Updated_at     | Disabled Reason |", "+------------------+------------------------+------+---------+-------+------------------------+-----------------+", "| cinder-scheduler |         cotoller       | nova | enabled |   up  | 2020-04-20T03:13:12.00 |       None      |", "|  cinder-volume   |   cotoller@cdot-iscsi  | nova | enabled |   up  | 2020-04-20T03:13:10.00 |       None      |", "|  cinder-volume   |    cotoller@cdot-nfs   | nova | enabled |   up  | 2020-04-20T03:13:11.00 |       None      |", "|  cinder-volume   | cotoller@eseries-iscsi | nova | enabled |   up  | 2020-04-20T03:13:06.00 |       None      |", "+------------------+------------------------+------+---------+-------+------------------------+-----------------+"]}
2020-04-21 13:41:35,514 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:35,514 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/test_bash.yml:35
2020-04-21 13:41:36,237 p=77871 u=jundo414 n=ansible | ok: [master01] => (item={'command': 'cinder list', 'value': "r'\\|\\s+cinder-volume\\s+\\|\\s+\\cotoller@cdot-nfs\\s+\\|\\s+nova\\s+\\|\\s+enabled\\s+\\|\\s+up\\s+\\|\\s+.*\\s+\\|\\s+.*\\s+\\|'"}) => {"ansible_loop_var": "item", "changed": false, "debug": "", "item": {"command": "cinder list", "value": "r'\\|\\s+cinder-volume\\s+\\|\\s+\\cotoller@cdot-nfs\\s+\\|\\s+nova\\s+\\|\\s+enabled\\s+\\|\\s+up\\s+\\|\\s+.*\\s+\\|\\s+.*\\s+\\|'"}, "rc": 0, "value": ["+------------------+------------------------+------+---------+-------+------------------------+-----------------+", "|      Binary      |           Host         | Zone |  Status | State |         Updated_at     | Disabled Reason |", "+------------------+------------------------+------+---------+-------+------------------------+-----------------+", "| cinder-scheduler |         cotoller       | nova | enabled |   up  | 2020-04-20T03:13:12.00 |       None      |", "|  cinder-volume   |   cotoller@cdot-iscsi  | nova | enabled |   up  | 2020-04-20T03:13:10.00 |       None      |", "|  cinder-volume   |    cotoller@cdot-nfs   | nova | enabled |   up  | 2020-04-20T03:13:11.00 |       None      |", "|  cinder-volume   | cotoller@eseries-iscsi | nova | enabled |   up  | 2020-04-20T03:13:06.00 |       None      |", "+------------------+------------------------+------+---------+-------+------------------------+-----------------+"]}
2020-04-21 13:41:36,241 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:36,241 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/test_api.yml:2
2020-04-21 13:41:41,411 p=77871 u=jundo414 n=ansible | [WARNING]: Module did not set no_log for password

2020-04-21 13:41:41,411 p=77871 u=jundo414 n=ansible | ok: [master01] => {"changed": false, "power_state": "Off"}
2020-04-21 13:41:41,416 p=77871 u=jundo414 n=ansible | TASK [test : test] **********************************************************************************************************************************************************************
2020-04-21 13:41:41,416 p=77871 u=jundo414 n=ansible | task path: /Users/jundo414/work/ansible-test/roles/test/tasks/test_api.yml:10
2020-04-21 13:41:46,211 p=77871 u=jundo414 n=ansible | ok: [master01] => {"changed": false, "power_state": "Off"}
2020-04-21 13:41:46,213 p=77871 u=jundo414 n=ansible | META: ran handlers
2020-04-21 13:41:46,213 p=77871 u=jundo414 n=ansible | META: ran handlers
2020-04-21 13:41:46,214 p=77871 u=jundo414 n=ansible | PLAY RECAP ******************************************************************************************************************************************************************************
2020-04-21 13:41:46,214 p=77871 u=jundo414 n=ansible | master01                   : ok=18   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
</details>
