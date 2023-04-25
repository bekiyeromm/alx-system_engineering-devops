# Puppet manifest that installs and configures an Nginx server with a 301 redirect
package { 'nginx':
  ensure => installed,
}
file { '/etc/nginx/sites-available/default':
  content => "
    server {
      listen 80;
      root /var/www/html;

      location / {
	return 200 "Hello world!";
      }
      location /redirect_me {
	return 301 https://twitter.com/BereketTena1;
      }
    }
  ",
  notify  =>Service['nginx'],
}
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target =>'/etc/nginx/sites-available/default',
  notify =>service['nginx'],
}
service { 'nginx':
  ensure =>running,
  enable =>true,
}
