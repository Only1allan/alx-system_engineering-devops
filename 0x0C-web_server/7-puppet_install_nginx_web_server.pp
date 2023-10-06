# FILEPATH: /home/dev254/Desktop/my_projects/ALX/alx-system_engineering-devops/0x0C-web_server/7-puppet_install_nginx_web_server.pp

# Update and upgrade packages
exec { 'update and upgrade packages':
    command => '/usr/bin/apt-get update -y && /usr/bin/apt-get upgrade -y',
}

# Install nginx
package { 'nginx':
    ensure => installed,
}

# Set up default nginx page
file { '/usr/share/nginx/html/index.nginx-debian.html':
    content => 'Hello World!',
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
}

file { '/etc/nginx/sites-enabled/default':
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
}

# Add redirection page
file { '/etc/nginx/sites-available/default':
    content => template('nginx/default.erb'),
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
}

# Configure custom 404 page
file { '/usr/share/nginx/html/404.html':
    content => 'Ceci n\'est pas une page',
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
}

file { '/etc/nginx/sites-available/default':
    content => template('nginx/default.erb'),
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
}

# Restart nginx service
service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => [
        File['/usr/share/nginx/html/index.nginx-debian.html'],
        File['/etc/nginx/sites-available/default'],
        File['/usr/share/nginx/html/404.html'],
    ],
}
