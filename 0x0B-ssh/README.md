<center><h1>0x0B. SSH</h1></center>
<p>Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 20.04 LTS environment.
</p>
<h1>Resources</h1>
[What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)<br>
[What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA)<br>
[SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)<br>
[SSH Config File](https://www.ssh.com/academy/ssh/config)<br>
[Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)<br>
[How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)<br>
[SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc)<br>
[Understanding the SSH Encryption and Connection Process](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)<br>
[Secure Shell Wiki](https://en.wikipedia.org/wiki/Secure_Shell)<br>
[IETF RFC 4251 (Description of the SSH Protocol)](https://www.ietf.org/rfc/rfc4251.txt)<br>
[Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)<br>
[Request for Comments](https://en.wikipedia.org/wiki/Request_for_Comments)<br>
<h3>man or help </h3>]
<ul>
<li>ssh</li>
<li>ssh-keygen</li>
<li>env</li>
</ul>
<h1>Learning Objectives</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, without the help of Google:</p>
What is a server<br>
Where servers usually live<br>
What is SSH<br>
How to create an SSH RSA key pair<br>
How to connect to a remote host using an SSH RSA key pair<br>
The advantage of using #!/usr/bin/env bash instead of /bin/bash<br>
<h2> Requirements</h2>
Allowed editors: vi, vim, emacs<br>
All your files will be interpreted on Ubuntu 20.04 LTS<br>
All your files should end with a new line<br>
A README.md file, at the root of the folder of the project, is mandatory<br>
All your Bash script files must be executable<br>
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash<br>
The second line of all your Bash scripts should be a comment explaining what is the script doing<br>
