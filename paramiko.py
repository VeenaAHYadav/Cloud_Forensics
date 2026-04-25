import paramiko

def fetch_ec2_logs(host, user, key_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=host, username=user, key_filename=key_path)

    stdin, stdout, stderr = ssh.exec_command("cat /var/log/syslog")

    logs = stdout.readlines()
    return [l.strip() for l in logs]