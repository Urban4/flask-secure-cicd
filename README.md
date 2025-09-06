# Flask Secure CI/CD App

## Overview
This is a simple Flask application built to demonstrate secure CI/CD practices.

### Endpoints
- `/healthz` - Health check, returns a 200 OK if the app is running.
- `/hello/<name>` - Returns a greeting for the given name.

## Running Locally
Make sure you have Python 3.11 installed.

```bash
# Navigate to the project directory
cd flask-secure-cicd

# Install dependencies
pip install -r requirements.txt

If you come across any issue you can use a virtual environment

# Create a virtual environment
python3 -m venv venv                                   
                                                                                                                                            
source venv/bin/activate

#Install the requirements
pip install -r requirements.txt

# Run the application
python app/main.py

