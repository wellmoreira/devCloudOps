# devCloudOps
 trabalho de devCloudOps



to run :

-create table dynamoDB
-create SQS aws 
-change the SQS and lambda url 
-rename the name of queue and table dynamoDB
-run the following commands >>  python3 -m venv ~/venv 
								source ~/venv/bin/activate
								sls deploy --verbose
								python3 putEventsPizzaria.py