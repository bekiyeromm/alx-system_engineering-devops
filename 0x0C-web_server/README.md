<center><h1>0x0C-web_server</h1></center>
<h2>concepts</h2>
[what is child process](https://intranet.alxswe.com/concepts/110)
<p>In this project, some of the tasks will be graded on 2 aspects:

1 Is your web-01 server configured according to requirements<br>
Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)<br>
For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

sylvain@ubuntu cat 88-script_example<br>
#!/usr/bin/env bash<br>
# Configuring a server with specification XYZ<br>
echo hello world > /tmp/test<br>
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default<br>
sylvain@ubuntu<br>
As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

A good Software Engineer is a lazy Software Engineer.<br>
Tips: to test your answer Bash script, feel free to reproduce the checker environment:

start a Ubuntu 16.04 sandbox
run your script on it
see how it behaves
</p>
<h1> Resources</h1>
[how the web works]( )<br>
[Nginx]( )<br>
[how to configure nginx]( )<br>
[root and sub domain]( )<br>
[http request]( )<br>
[http redirection]( )<br>
[Not found HTTP response code]( )<br>
[Logs files on Linux]( )<br>
<p>man or help:<br>
scp<br>
curl<br>
</p>
<h1>Requirements</h1>
Allowed editors: vi, vim, emacs<bR>
All your files will be interpreted on Ubuntu 16.04 LTS<br>
All your files should end with a new line<br>
A README.md file, at the root of the folder of the project, is mandatory<br>
All your Bash script files must be executable<br>
Your Bash script must pass Shellcheck (version 0.3.7) without any error<br>
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash<br>
The second line of all your Bash scripts should be a comment explaining what is the script doing<br>
You can’t use systemctl for restarting a process<br>
<h1>Learning Objectives</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

<h2>General</h2>
What is the main role of a web server
What is a child process
Why web servers usually have a parent process and child processes
What are the main HTTP requests
DNS
What DNS stands for
What is DNS main role
DNS Record Types
A
CNAME
TXT
MX
<h2>Copyright - Plagiarism</h2>
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
</p>

