import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.26', username='tapha', key_filename="C:\\Users\\Pot2Fleur\\.ssh\\id_rsa")
stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.readlines())
ssh.close()