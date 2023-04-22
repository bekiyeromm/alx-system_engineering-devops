#!/usr/bin/env bash
# write a puppet to make changes to our configuration file to set up your client
# SSH configuration file so that you can connect to a server without typing a password
exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}
