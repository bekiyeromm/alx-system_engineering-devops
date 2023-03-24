#Using Puppet, create a file named school in /tmp
file { '/tmp/school':
ensure  => file,
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
