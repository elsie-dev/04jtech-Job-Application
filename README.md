# 04jtech-project

# LOCAL INFRASTRUCTURE DEVELOPMENT:ANSIBLE AND VAGRANT 

Vagrant is a tool for building and managing virtual machine environment in a single workflow.Lowers development setup time.

Ansible is a configuration management tool used for automating provision,configuration and management of IT processes.

## Setting up Vagrant
Requirements
1. Vagrant software
2. Oracle virtual box
3. Have python installed 
4. Ansible installed correctly
5. GIT bash preferrably



After everything is installed on the terminal,here are the commands to enable ubuntu/binoc64 run inside your vagant machine

Project steps
Create a directory for the application
```
mkdir appsample
cd appsample
vagrant init
```
**_Vagrant init_ creats a vagrantfile wheres _Vagrant box list_ installs the required vagrantbox in the system**

```
vagrant box list ubuntu/bionic64 
```
Vagrantfile should have this next line to enable provision later on ansible when we run _vagrant provision_
```config.vm.provision "ansible" do |ansible|
 ansible.playbook = "playbook.yml"
 end
 ```
 ```Vagrant up```
 


Points to note:

Ansible does indicate compatibility issues when using windows.[https://youtu.be/4sMFybv74Uo]()

Troubleshoot:
Enable the Linux subsytem on the windows platfrom via either the powershell or settings tab.Commands used:
```
Enable-WindowsOptionalFeature-Online -Featurename Microsoft-Windows-Subsystem-Linux 
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get install ansible
ansible --version
```

