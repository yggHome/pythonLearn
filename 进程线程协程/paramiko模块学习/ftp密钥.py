# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import paramiko

private_key = paramiko.RSAKey.from_private_key_file("id_rsa")

# 建立与目标主机之间的连接通道
transport = paramiko.Transport(('192.168.17.133', 22))
transport.connect(username="root", pkey=private_key)

# 将已建立好的连接交给paramiko.SFTPClient.from_transport对象
sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 将当前目录下的test上传至/tmp/test
sftp.put("test", "/tmp/test")

# 将/tmp/test下载至当前目录的local
sftp.get("/tmp/test", "local")

transport.close()