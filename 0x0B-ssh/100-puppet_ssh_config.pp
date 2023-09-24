#make changes to config file with puppet
file { '/etc/ssh/ssh_config':
    ensure => present,
    mode   => '0600',
    owner  => 'dev254',
    group  => 'dev254',
    content => "    
        Host remote-server
            Hostname 100.25.134.21
            User ubuntu
            IdentityFile ~/.ssh/school
            PasswordAuthentication no
    ",
}
