<Center><h1>0x0F. Load balancer</h1></center>
<h2> concepts</h2>
[load balancer](https://intranet.alxswe.com/concepts/46) <br>
[web stack debugging](https://intranet.alxswe.com/concepts/68) <br>
<h2>Background Context</h2>
You have been given 2 additional servers:<br>

gc-[STUDENT_ID]-web-02-XXXXXXXXXX<br>
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX<br>
<p>Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

</p>
<h1>Resources</h1>
[Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)<br>
[http header](https://www.techopedia.com/definition/27178/http-header)<br>
[Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)<br>
[How do I assign a static hostname to an Amazon EC2 instance running Ubuntu Linux?](https://repost.aws/knowledge-center/linux-static-hostname)<br>
[Change the hostname of your Amazon Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html)<br>

<h1>Requirements</h1>
Allowed editors: vi, vim, emacs <br>
All your files will be interpreted on Ubuntu 16.04 LTS <br>
All your files should end with a new line <br>
A README.md file, at the root of the folder of the project, is mandatory <br>
All your Bash script files must be executable<br>
Your Bash script must pass Shellcheck (version 0.3.7) without any error<br>
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash<br>
The second line of all your Bash scripts should be a comment explaining what is the script doing<br>

<h1>your servers</h1>
<table>
<tr>
<th>Name</th>
<th>username</th>
<th>ip</th>
<th>status</th>
</tr>
<tr>
<td>128037-web-01</td>
<td>ubuntu</td>
<td>52.91.178.133</td>
<td>running</td>
</tr>
<tr>
 37 <td>128037-web-02</td>
 38 <td>ubuntu</td>
 39 <td>54.160.69.6</td>
 40 <td>running</td>
 41 </tr>
 <tr>
 37 <td>128037-lb-01</td>
 38 <td>ubuntu</td>
 39 <td>54.90.12.103</td>
 40 <td>running</td>
 41 </tr>
 </table>
