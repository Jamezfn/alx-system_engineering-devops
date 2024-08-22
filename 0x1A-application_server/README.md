0. Set up development with Python
mandatory
Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
Install the net-tools package on your server: sudo apt install -y net-tools
Git clone your AirBnB_clone_v2 on your web-01 server.
Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
Your Flask application object must be named app (This will allow us to run and check your code).
Example:

Window 1:
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
Window 2:
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

1. Set up production with Gunicorn

To set up your production environment with Gunicorn on web-01, follow these steps:

1. Install Gunicorn and Dependencies:
First, ensure you have Gunicorn and any other dependencies installed:

bash
Copy code
sudo apt update
sudo apt install -y python3-pip
pip3 install gunicorn
pip3 install flask  # If Flask is not already installed
2. Configure Your Flask Application:
Make sure your Flask application is set up correctly in web_flask/0-hello_route.py:

python
Copy code
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
3. Run Gunicorn:
Run Gunicorn to serve your Flask application on port 5000:

bash
Copy code
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
4. Verify Gunicorn is Running:
Check if Gunicorn is running and listening on port 5000:

bash
Copy code
sudo netstat -tuln | grep 5000
You should see Gunicorn listed as listening on port 5000. The output should look something like this:

ruby
Copy code
tcp6       0      0 :::5000                 :::*                    LISTEN
5. Test the Application:
From a different terminal or from another machine (if applicable), use curl to test if the application is accessible:

bash
Copy code
curl http://127.0.0.1:5000/airbnb-onepage/
You should receive the response:

Copy code
Hello HBNB!
6. Check for Port Conflicts:
Ensure that no other service is using port 6000:

bash
Copy code
sudo netstat -tuln | grep 6000
If port 6000 is in use, you need to stop the service using that port or configure Gunicorn to use a different port temporarily.

Summary:
Install Gunicorn and dependencies.
Ensure your Flask app is correctly set up.
Start Gunicorn with the appropriate command.
Verify Gunicorn is listening on port 5000.
Test the application with curl.
Ensure port 6000 is free for the checker.



Summary of Commands
Install python3-venv:

bash
Copy code
sudo apt update
sudo apt install python3.8-venv
Create and activate the virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install necessary packages:

bash
Copy code
pip install flask click gunicorn
Run the application with Gunicorn:

bash
Copy code
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
This setup ensures that your environment is isolated and should resolve the issues with package conflicts.
