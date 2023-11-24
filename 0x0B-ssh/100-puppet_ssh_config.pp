# script that changes the config file with puppet

# remove password authentication
augeas{'remove passwd auth':
    context => '/etc/ssh/ssh_config',
    changes => 'set PasswordAuthentication no'
}

# ensures the right private authentication key is provided
augeas{'my identity file':
    context => '/etc/ssh/ssh_config',
    changes => 'set IdentityFile ~/.ssh/school'
}