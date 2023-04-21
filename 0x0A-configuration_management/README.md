<center><h1>0x0A-configuration_management</h1></center>
<br>
<h2>Background Context</h2>
<p>When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent nil to the filter method.

There were 2 pieces of bad news:

When MCollective receives nil as an argument for its filter method, it takes this to mean ‘all servers’
The action I sent was to terminate the selected servers
I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.
</p>
<h2>Resources</h2>
[Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)<br>
[Puppet resource type: file ](https://www.puppet.com/docs/puppet/5.5/types/file.html)<br>
[Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)<br>
[Puppet lint](http://puppet-lint.com/)<br>
[Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)<br>
<h2>Requirements</h2>
<ul>
<li>All your files will be interpreted on Ubuntu 20.04 LTS </li>
<li>All your files should end with a new line </li>
<li>A README.md file at the root of the folder of the project is mandatory </li>
<li>Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors </li>
<li>Your Puppet manifests must run without error </li>
<li>Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about </li>
<li>Your Puppet manifests files must end with the extension .pp </li>
</ul>
<p>
Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

Install puppet
<br>
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades<br>
$ apt-get install -y ruby-augeas<br>
$ apt-get install -y ruby-shadow<br>
$ apt-get install -y puppet<br>
You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.
<br>
[Puppet 5 Docs](https://www.puppet.com/docs/puppet/5.5/puppet_index.html)<br>
<p>Install puppet-lint</p>
$ gem install puppet-lint

