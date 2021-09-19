

# LOCAL INFRASTRUCTURE DEVELOPMENT:
## ANSIBLE AND VAGRANT 

Vagrant is a tool for building and managing virtual machine environment in a single workflow.Lowers development setup time.

Ansible is a configuration management tool used for automating provision,configuration and management of IT processes.

TASKS:


## Setting up Vagrant
Requirements
1. Vagrant software
2. Oracle virtual box
3. Have python installed 
4. Ansible installed correctly
5. GIT bash preferrably

After everything is installed on the terminal,here are the commands to enable ubuntu/binoc64 run inside your vagant machine

## **Project steps**

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
 
## Creating applications to Webserver
Installing flask on the env,creating app.py files then running the file 

```pip install flask``` \
```flask run```\
![CLI output](flaskoutput.png)

To make our webapp dynamic,l added routes to the app.py file indicating the python version,date and type of operating system used.

## Using Ansible for running ngnix and loadbalancing

*****

**Points to note:**

Ansible does indicate compatibility issues when using windows.[https://youtu.be/4sMFybv74Uo]()

## **Troubleshoot** \
Enable the Linux subsytem on the windows platfrom via either the powershell or settings tab.Commands used:

```
Enable-WindowsOptionalFeature-Online -Featurename Microsoft-Windows-Subsystem-Linux 
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get install ansible
ansible --version
```

Webservers and loadbalancers running Nginx
Helps in performance problem,this way we can add new servers (vm's) and increase the capacity of your platform. 
Distributing the load over multiple machines is referred to as "load balancing".

## **Compromises:**
Virtual box with name loadbalancer already exists.
removing load from the vagrant file then doing ```vagrant up``` solved the error.
   
   

