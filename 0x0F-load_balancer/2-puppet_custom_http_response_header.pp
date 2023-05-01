# Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine
# name of the custom HTTP header must be X-Served-By
# value of the custom HTTP header must be the hostname of the server Nginx is running on
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  # Install Nginx package
  ensure => installed,
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
