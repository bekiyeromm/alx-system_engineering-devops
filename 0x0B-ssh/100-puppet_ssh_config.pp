#!/usr/bin/env bash
# write a puppet to make changes to our configuration file to set up your client
# SSH configuration file so that you can connect to a server without typing a password
file { '/home/beki/.ssh/config':
  owner   => 'beki',
  group   => 'beki',
  mode    => '0600',
  content => "Host my-server\n\
	    HostName 52.91.178.133\n\
	    User beki\n\
	    IdentityFile ~/.ssh/school\n\
	    PasswordAuthentication no\n",
}
