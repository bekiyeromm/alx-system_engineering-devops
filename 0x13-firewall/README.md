0x13. Firewall

<h2>Concepts</h2><br>
[<h3>Web stack debugging</h3>] (https://intranet.alxswe.com/concepts/68)<br>
<h1>Resources</h1> <br>
[<h3>What is a firewall</h3>] (https://en.wikipedia.org/wiki/Firewall_%28computing%29)<br>
<h1>More Info</h1>
<br><br>
<p>As explained in the web stack debugging guide concept page, telnet is a very good tool to check if sockets are open with telnet IP PORT. For example, if you want to check if port 22 is open on web-02:</p><br>
<p>sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...<br>
Connected to web-02.holberton.online.<br>
Escape character is '^]'.<br>
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8<br>

Protocol mismatch.<br>
Connection closed by foreign host.<br>
sylvain@ubuntu$<br>
</p>
<br>
<p>We can see for this example that the connection is successful: Connected to web-02.holberton.online.

Now let’s try connecting to port 2222:
</p>
<br>
<p>sylvain@ubuntu$ telnet web-02.holberton.online 2222<br>
Trying 54.89.38.100...<br>
^C
sylvain@ubuntu$<br>
</p>
<br>
<p>
We can see that the connection never succeeds, so after some time I just use ctrl+c to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on web-01, please perform the test from outside of the school network, like from your web-02 server. If you SSH into your web-02 server, the traffic will be originating from web-02 and not from the school’s network, bypassing the firewall.
</p>
<br><br>
<h1>Warning!</h1>
<p><strong>Containers on demand cannot be used for this project (Docker container limitation)

Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.
</strong>
</p>
