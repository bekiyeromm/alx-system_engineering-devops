#Puppet manifest that kills a process named killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
  onlyif  => 'pgrep killmenow',
logoutput => true,
}
