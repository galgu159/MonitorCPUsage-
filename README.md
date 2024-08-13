# MonitorCPUsage-
Creating a Service to Monitor CPU Usage and Send Alerts Task

# run MonitorCPUsage.py
python3 MonitorCPUsage.py

# Describe how you would implement this service.
To create a service that monitors CPU usage on an operating system and sends alerts when the CPU usage exceeds 80% I can
build code with 2 functions - monitor on the cpu and send email to the relevant factor.
# Include details on the programming language and libraries you would use.
I will use Python Language. Python is a suitable choice for this task due to its simplicity and extensive library support.
Using that packages -
Psutil - System resource monitoring
Time, sleep - Timely treatment, for checking all the time about cpu
Smtplib - Responsible for sending the emails
Email.mime.text, MIMEText - Creating an Email
Email.mime.multipart, MIMEMultipart - Possession of the Email
# Explain how the service will continuously monitor the CPU usage.
CPU volume goes up and down in seconds. It all depends on what we use and what we run on our computer. 
That's why I used the TIME package and that way I could repeat the tests operation every 10 seconds.
# Describe the method of sending alerts (e.g., email, logging, notification).
Emails - Sending email when the cpu usage exceeds 80%
Logging - The system writes the alert details to a log file or logging system
Notification -  The system sends notifications to mobile devices or desktops using services
I choose email method of sending alerts because it can reach a wide audience for example IT team.
I built a function that builds an email message and sends the relevant party the email with the warning.
# Provide a high-level pseudo-code or a flowchart of your solution.
MonitorCPUsage.py
