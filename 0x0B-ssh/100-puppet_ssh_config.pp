# script that changes the config file with puppet
include stdlib

file_line { 'SSH key':
    path               => '/etc/ssh/ssh_config',
    line               => '  IdentityFile ~/.ssh/school',
    match              => '^#*\s*IdentityFile ~/ssh/id_rsa$',
    replace            => true,
    append_on_no_match => true
}

file_line { 'No Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^#*\s*PasswordAuthentication yes|no$',
  replace            => true,
  append_on_no_match => true
}