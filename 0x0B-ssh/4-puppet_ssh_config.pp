# Conect to server using ssh:
# SSH client configuration is configured to use the private key ~/.ssh/holberton
# The SSH client configuration is configured to refuse to authenticate using a password

exec { 'change_ssh_config':
command  => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" > /etc/ssh/ssh_config',
provider => 'shell'
    }
