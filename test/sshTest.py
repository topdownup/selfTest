# coding=utf-8
#!/usr/bin/python
import datetime
import os, sys, time
import commands


# 这个函数是校验IP合法性的。
def check_ip(ipaddr):
    import sys
    addr = ipaddr.strip().split('.')
    # print addr
    if len(addr) != 4:
        print "check ip address failed!"
        sys.exit()
    for i in range(4):
        try:
            addr[i] = int(addr[i])
        except:
            sys.exit()
        if addr[i] <= 255 and addr[i] >= 0:
            pass
        else:
            print "check ip address failed!"
            sys.exit()
        i += 1
    else:
        print "check ip address success!"


node_dict = {}
host_all = []
host_ip_all = {}


# 这个函数获取输入的节点信息,并校验输入的IP是否合法。
def get_nodes():
    while True:
        node = raw_input("""Input node's info. Usage: hosta/192.168.0.101. Press Enter is complete.
Please input Node info:  """)
        if len(node) == 0:
            return 2
        node_result = node.strip().split('/')
        host_ip_all[node_result[0]] = [node_result[1], '']
        # print node_result
        if len(node_result[0]) == 0:
            print "Hostname is failed!"
            sys.exit()
        check_ip(node_result[1])
        # node_dict[node_result[0]]=[node_result[1]]
        host_all.append(node_result[0])
        # print node_dict
        local_ip_status, local_ip_result = commands.getstatusoutput(
            """ifconfig |grep 'inet addr'|awk -F '[: ]+' '{print $4}' """)
        local_ip = local_ip_result.split('\n')
        # print host_all
        if len(host_all) == 1:
            if node_result[1] in local_ip:
                pass
            else:
                print "The first IP must be native IP."
                sys.exit()


# 这个函数生成ssh密钥文件,简单的3条shell命令
def create_sshkey_file():
    os.system("rm -rf ~/.ssh/")
    os.system("/usr/bin/ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''    ")
    os.system("cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys")


# 这个函数配置/etc/hosts文件
def add_etc_hosts():
    for i in host_ip_all.keys():
        # print host_ip_all.keys()
        # 判断/etc/hosts是否存在
        if os.path.exists('/etc/hosts'):
            pass
        else:
            os.system("touch /etc/hosts")
        # 删除掉原有主机名项，并添加新的对应关系
        os.system("sed -i '/%s/d' /etc/hosts" % i)
        # print i,host_ip_all[i][0]
        os.system(''' echo '%s %s\r' >>/etc/hosts ''' % (host_ip_all[i][0], i))
        # with open('/etc/hosts','ab') as f :
        #       f.write('%s  %s\r'%(host_ip_all[i][0],i))


# 拷贝ssh密钥文件
def scp_sshkey():
    # 把/root/.ssh文件放在/tmp下，并开使其生效。
    os.system("sed -i /tmp/d /etc/exports")
    os.system("echo '/tmp *(rw)' >>/etc/exports")
    os.system("exportfs -r")
    os.system("cp -a /root/.ssh /tmp")
    os.system("chmod 777 /tmp")
    os.system("/etc/init.d/iptables stop")
    os.system("chmod 777 /tmp/.ssh/id_rsa")
    os.system("chmod 777 /tmp/.ssh")
    print 'Scp ssh key file too another node...'
    print host_all[1:]
    localhost = host_all[0]
    local_ip = host_ip_all[localhost][0]
    # 输入一次密码，登陆上去后执行了N条命令，挂载nfs，拷贝.ssh，修改权限，卸载等等。
    for i in host_all[1:]:
        os.system(
            '''/usr/bin/ssh %s "/bin/umount -lf /mnt >/dev/null 2 &>1;/bin/mount %s:/tmp /mnt ;rm -rf /root/.ssh;mkdir /root/.ssh;sleep 3; /bin/cp -a /mnt/.ssh/* /root/.ssh/ ;echo 'copy ssh file successful';/bin/chmod 600 /root/.ssh/id_rsa;/bin/chmod 700 /root/.ssh;/bin/umount -lf /mnt "''' % (
            i, local_ip))
    print "Done"


# 测试ssh互信是否成功
def test_sshkey(host):
    for host_n in host_all:
        try:
            # to gain public key
            # 使用StrictHostKeyChecking跳过公钥接收提示。并远程执行命令，连上了自然会输出成功信息。
            os.system(
                ''' ssh  -o  "StrictHostKeyChecking no" %s "echo -e local %s RsaKey remote %s  is successful" ''' % (
                host_n, host_all[0], host_n))
        except:
            print "\033[31mlocal %s RsaKey remote %s is fail.\033[0m" % (host_all[0], host_n)

    # 全部测试完成后，把known_hosts文件拷贝到所有主机。一台服务器获取了所有公钥，那拷贝到远端自然是所有节点都有对方公钥了。
    for host_m in host_all[1:]:
        # copy ~/.ssh/known_hosts file to another host...
        os.system("""/usr/bin/scp ~/.ssh/known_hosts %s:~/.ssh/known_hosts""" % host_m)
        # copy hosts file to another host...
        os.system("""/usr/bin/scp /etc/hosts %s:/etc/hosts """ % host_m)  # 函数执行部分

get_nodes()
a = raw_input("Are you sure you want  to set ssh mutual trust? (yes/no) ").strip()
# 提示一下，做不做互信要让用户选择。
if a == "yes":
    create_sshkey_file()
    add_etc_hosts()
    scp_sshkey()
    test_sshkey('192.168.2.73')
elif a == "no":
    # 输入no就代表互信已做好了。接下来执行别的代码。
    pass
else:
    print 'Byebye,Please input yes or no.'
    sys.exit()
