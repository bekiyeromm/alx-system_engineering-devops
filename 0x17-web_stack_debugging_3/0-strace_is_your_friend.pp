# Using strace, find out why Apache is returning a 500 error. Once you find
# the issue,fix it and then automate it using Puppet

exec { 'internal-server':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/usr/bin/:/bin/'
}
