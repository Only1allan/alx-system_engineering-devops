file { '/etc/ssh/ssh_config':
    ensure => present,
    mode   => '0600',
    owner  => 'dev254',
    group  => 'dev254',
    content => "    
        Host remote-server
            Hostname 100.25.134.21
            User ubuntu
            IdentityFile /home/.ssh/school
            PasswordAuthentication no
    ",
}
