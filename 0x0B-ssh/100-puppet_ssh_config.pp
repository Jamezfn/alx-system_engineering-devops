class ssh_config {
  # Disable password authentication
  file_line { 'disable_password_auth':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^PasswordAuthentication',
  }

  # Set the private key file
  file_line { 'set_private_key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^IdentityFile',
  }
}

# Apply the ssh_config class
include ssh_config
