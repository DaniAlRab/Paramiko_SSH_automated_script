# Remote SSH Command Execution Script

## Project Overview
This project provides a **Python script** that connects to a remote host via **SSH** using `paramiko` and executes a command. It is useful for automating remote tasks such as running scripts, executing system commands, or managing servers remotely.

---

## Key Features
- **SSH Connection:**
  - Establishes a secure SSH connection to a remote server.
  - Uses the `paramiko` library to handle SSH authentication.

- **Remote Command Execution:**
  - Executes a specified command on the remote host.
  - Captures and prints both **standard output** and **error output**.

- **Error Handling:**
  - Handles connection failures and command execution errors gracefully.

---

## Requirements
- **Python 3**
- **Dependencies:**
  - `paramiko`

Install dependencies using:
```bash
pip install paramiko
```

---

## Script Usage
### **1. Define Connection Parameters**
Modify the following variables inside the script:
```python
remote_host = "192.168.0.244"  # Replace with the actual remote IP
ssh_username = "user"          # Replace with the actual username
ssh_password = "password"      # Replace with the actual password
remote_command = "python3 test.py"  # Replace with the desired command
```

### **2. Run the Script**
Execute the script using:
```bash
python3 remote_ssh.py
```

---

## Workflow
1. **SSH Connection:**
   - Connects to the remote host using the provided credentials.
   - Adds the host key automatically if not previously stored.

2. **Command Execution:**
   - Executes the command on the remote server.
   - Captures and prints both **output** and **error messages**.

3. **Error Handling & Connection Closing:**
   - Detects and reports errors if the command execution fails.
   - Ensures the SSH connection is properly closed after execution.

---

## Example Output
```bash
Connecting to 192.168.0.244...
Connection established.
Executing command: python3 test.py
Command output:
Hello, World!
Command error:
(No errors detected)
Connection closed.
```

---

## Notes
- Ensure that SSH access is enabled on the remote machine.
- If using **SSH key authentication**, modify the `connect` function to include a private key instead of a password.
- For enhanced security, avoid storing passwords in plain text. Consider using **environment variables** or **SSH keys**.

---
