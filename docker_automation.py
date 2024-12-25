import docker
import psutil
import subprocess

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
    # Get IP address and Gateway using subprocess to call system commands
    ip = subprocess.getoutput("hostname -I").strip()  # Get the local IP address
    gateway = subprocess.getoutput("ip route | grep default | awk '{print $3}'").strip()  # Get the default gateway

    # Get memory details using psutil
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 * 1024 * 1024)  # Convert bytes to GB
    available_memory = memory.available / (1024 * 1024 * 1024)  # Convert bytes to GB
    used_memory = memory.used / (1024 * 1024 * 1024)  # Convert bytes to GB
    free_memory = memory.free / (1024 * 1024 * 1024)  # Convert bytes to GB

    return {
        'IP': ip,
        'Gateway': gateway,
        'Total Memory (GB)': total_memory,
        'Used Memory (GB)': used_memory,
        'Free Memory (GB)': free_memory,
        'Available Memory (GB)': available_memory
    }

# Function to take corrective action if free memory is low
def reduce_memory_if_needed(free_memory, threshold=1):
    if free_memory < threshold:
        print(f"Free memory is low ({free_memory} GB). Taking corrective action.")
        # List all running containers and stop unused ones
        client = docker.from_env()
        containers = client.containers.list()

        for container in containers:
            print(f"Stopping container {container.id} to free up memory.")
            container.stop()

# Main function to orchestrate everything
def main():
    # Example: Create a container
    container = create_docker_container("nginx")  # Replace "nginx" with any image you prefer

    # Get system info
    sys_info = get_system_info()
    print("System Information:")
    for key, value in sys_info.items():
        print(f"{key}: {value}")

    # If free memory is low, take corrective action
    reduce_memory_if_needed(sys_info['Free Memory (GB)'])

    # Example: Delete a container
    if container:
        delete_docker_container(container.id)

if __name__ == "__main__":
    main()
