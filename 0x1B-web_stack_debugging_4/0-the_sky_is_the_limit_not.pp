# setting a limit to the number of requests to my server
exec { '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
