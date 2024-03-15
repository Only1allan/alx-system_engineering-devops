#nginx traffic handler
exec { 'handle more traffic':
  command => '/bin/sed -i "s/25/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
