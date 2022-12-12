import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.26', username='tapha', key_filename="C:\\Users\\Pot2Fleur\\.ssh\\id_rsa")

sftp = ssh.open_sftp()
# Upload
filepath = "/home/tapha"
localpath = "C:\\Users\\Pot2Fleur\\Desktop\\courspython.txt"
sftp.put(localpath,filepath)

stdin, stdout, stderr = ssh.exec_command('uptime')
print(stdout.readlines())
ssh.close()