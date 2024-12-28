import docker
import psutil
import subprocess

# Function to check Docker connectivity
def check_docker_connection():
    try:
        client = docker.from_env()
        client.ping()  # Test connection
        print("Docker daemon is accessible.")
        return True
    except Exception as e:
        print(f"Error connecting to Docker daemon: {str(e)}")
        return False

# Function to create a Docker container
def create_docker_container(image_name):
    client = docker.from_env()
    try:
        container = client.containers.run(image_name, detach=True)
        print(f"Container {container.id} created successfully.")
        return container
    except Exception as e:
        print(f"Error creating container: {str(e)}")
        return None

# Function to delete a Docker container
def delete_docker_container(container_id):
    client = docker.from_env()
    try:
        container = client.containers.get(container_id)
        container.stop()
        container.remove()
        print(f"Container {container_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting container: {str(e)}")

# Function to get system information (IP, Gateway, Memory)
def get_system_info():
    ip = subprocess.getoutput("hostname -I").strip()
    gateway = subprocess.getoutput("ip route | grep default | awk '{print $3}'").strip()
    memory = psutil.virtual_memory()
    return {
        'IP': ip,
        'Gateway': gateway,
        'Total Memory (GB)': memory.total / (1024**3),
        'Used Memory (GB)': memory.used / (1024**3),
        'Free Memory (GB)': memory.free / (1024**3),
        'Available Memory (GB)': memory.available / (1024**3)
    }

# Function to take corrective action if free memory is low
def reduce_memory_if_needed(free_memory, threshold=1):
    if free_memory < threshold:
        print(f"Free memory is low ({free_memory} GB). Taking corrective action.")
        client = docker.from_env()
        containers = client.containers.list()
        for container in containers:
            print(f"Stopping container {container.id} to free up memory.")
            container.stop()

# Main function
def main():
    # Check Docker connectivity
    if not check_docker_connection():
        print("Exiting script due to Docker connection issues.")
        return

    # Example: Create a container
    container = create_docker_container("nginx")

    # Get system info
    sys_info = get_system_info()
    print("System Information:")
    for key, value in sys_info.items():
        print(f"{key}: {value}")

    # Take corrective action if needed
    reduce_memory_if_needed(sys_info['Free Memory (GB)'])

    # Example: Delete a container
    if container:
        delete_docker_container(container.id)

if __name__ == "__main__":
    main()
