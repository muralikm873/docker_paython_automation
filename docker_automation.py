import docker
import paramiko

def create_container(client, image_name):
    container = client.containers.run(image_name, detach=True, name="my_container")
    print("Container created:", container.short_id)
    return container

def get_container_details(container):
    details = container.attrs
    ip = details['NetworkSettings']['Networks']['bridge']['IPAddress']
    gateway = details['NetworkSettings']['Networks']['bridge']['Gateway']
    print(f"IP: {ip}, Gateway: {gateway}")
    return ip, gateway

def ssh_to_container(ip, password='root'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username='root', password=password)
    stdin, stdout, stderr = ssh.exec_command('free -m')
    print(stdout.read().decode())
    ssh.close()

def main():
    client = docker.from_env()
    container = create_container(client, "ubuntu")
    
    ip, gateway = get_container_details(container)
    ssh_to_container(ip)

if __name__ == "__main__":
    main()
