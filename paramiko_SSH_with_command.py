import paramiko

def execute_remote_command(host, username, password, command):
    """
    Connect to a remote host via SSH and execute a command.
    
    :param host: Remote host IP or domain.
    :param username: SSH username.
    :param password: SSH password.
    :param command: Command to execute on the remote host.
    """
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        
        # Automatically add the host key if not already known
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote host
        print(f"Connecting to {host}...")
        ssh_client.connect(hostname=host, username=username, password=password)
        print("Connection established.")
        
        # Execute the command
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        
        # Print command output
        print("Command output:")
        print(stdout.read().decode())
        
        # Print command error (if any)
        error = stderr.read().decode()
        if error:
            print("Command error:")
            print(error)
        
        # Close the connection
        ssh_client.close()
        print("Connection closed.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Predefined IP address
    remote_host = "192.168.0.244" # Replace with remote ip
    ssh_username = "user"  # Replace with the actual username
    ssh_password = "password" # Replace with the actual password
    remote_command = "python3 test.py"  # Replace with the desired command

    # Execute the command on the predefined remote host
    execute_remote_command(remote_host, ssh_username, ssh_password, remote_command)
