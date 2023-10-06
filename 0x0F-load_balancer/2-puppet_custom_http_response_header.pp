#puppet script that configures a new Ubuntu machine to 

# Install Nginx
package { 'nginx':
    ensure => installed,
}

# Set up default Nginx page
file { '/usr/share/nginx/html/index.nginx-debian.html':
    content => 'Hello World!',
}

# Configure custom 404 page
file { '/usr/share/nginx/html/404.html':
    content => 'Ceci n\'est pas une page',
}

# Configure redirection page
file_line { 'redirect':
    path => '/etc/nginx/sites-available/default',
    line => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGU1wu4/ permanent;',
}

# Configure custom header
file_line { 'custom_header':
    path => '/etc/nginx/sites-available/default',
    line => 'add_header X-Served-By $HOSTNAME;',
}

# Restart Nginx
service { 'nginx':
    ensure => running,
    enable => true,
    require => [
        File['/usr/share/nginx/html/index.nginx-debian.html'],
        File['/usr/share/nginx/html/404.html'],
        File_line['redirect'],
        File_line['custom_header'],
    ],
}
