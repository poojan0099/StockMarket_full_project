To run the project on Aws Ec2 Ubuntu instance 
- create the instance
- clone this repository using "git clone StockMarket_full_project".
- change the working directory to the project's directory uing cd command.
- install pip using "sudo apt install python3-pip".
- to install all the libraries in the requiremnet.txt file, run "pip3 install -r requirements.txt".
- execute runner.sh file by first giving all permission using "chmod -r +777 runner.sh" and then run "./runner.sh". This kills all the processes running at port 80
and creates a log.txt file which stores the log of the project in background.
- finally, run the project using "python3 app.py"
- copy the public ipv4 address provided and paste it in new tab.
-project will be successfully hosted and on the cloud.
