<h1>0x0F-load_balancer</h1>
<h2> concept</h2>
[load balancer](https://intranet.alxswe.com/concepts/46) <br>
[web stack debuging](https://intranet.alxswe.com/concepts/68)<br>
<h2>Background Context</h2>
You have been given 2 additional servers:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

Resources
Read or watch:
[Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)<br>
[HTTP header](https://www.techopedia.com/definition/27178/http-header)<br>
[Debian/Ubuntu HAProxy packages](Debian/Ubuntu HAProxy packages)<br>
<h1>
Requirements
</h1>
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

<h1>Your servers</h1>

Name	Username	IP	State<br>
128037-web-01	ubuntu	34.229.137.228	running<br>
128037-web-02	ubuntu	100.25.17.98	running<br>
128037-lb-01	ubuntu	100.26.163.179	running<br>

