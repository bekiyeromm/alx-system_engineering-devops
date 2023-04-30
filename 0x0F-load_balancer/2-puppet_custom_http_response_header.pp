# Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine
# name of the custom HTTP header must be X-Served-By
# value of the custom HTTP header must be the hostname of the server Nginx is running on
class { 'nginx':
  # Install Nginx package
  ensure => installed,
}

file { '/etc/nginx/conf.d/custom_headers.conf':
  # Adding custom headers configuration
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "add_header X-Served-By $hostname;",
  notify  => Service['nginx'],
}
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/conf.d/custom-http-header.conf'],
}
