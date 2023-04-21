# Puppet manifest that kills a process named "killmenow" using the "pkill" command
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/bin', '/usr/local/bin'],
  onlyif  => 'pgrep killmenow',
}
