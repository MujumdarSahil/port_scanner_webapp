# port_scanner_webapp

This is a simple web-based port scanner built using Python and Flask. It allows users to scan a target IP address or hostname for open ports within a specified range. The project features a basic GUI that makes it easy to input targets and view scan results.

Features
Scan any target: Input an IP address or hostname and scan for open ports.
Specify port range: Choose the range of ports to scan.
GUI: Simple and user-friendly interface using HTML and CSS.
Threading: Scans are performed using multiple threads to improve speed.

Prerequisites
Before running this project, ensure you have the following installed:

Python 3.7+
pip (Python package manager)

Modules and Methods
Python Modules:
flask: A lightweight WSGI web application framework used to create the web server and handle HTTP requests.
socket: Provides low-level networking interfaces to perform the actual port scanning.
threading: Used to implement threading to speed up the port scanning process.

Key Methods:
scan_port(target, port):

Purpose: Scans a specific port on the target to check if it's open.
Usage: Internally used by the threading function to perform the scan.
Returns: A string indicating if the port is open or an error occurred.
run_port_scan(target, start_port, end_port):

Purpose: Scans a range of ports on the target and returns a list of open ports.
Usage: Called when a user submits the form with target and port range.
Returns: A list of results showing open ports.
@app.route('/', methods=['GET', 'POST']):

Purpose: Handles the root URL route, renders the form, and processes input to start the scan.
Usage: Flask's routing mechanism that binds a URL to a Python function.
Returns: The rendered HTML page with or without results based on the user input.

Tools Used:
Flask: For setting up a simple web server.
HTML/CSS: For building the frontend GUI.
Socket Programming: For performing network operations and port scanning.
Threading: To optimize the scanning process by running multiple port checks concurrently.

This project is licensed under the MIT License. Feel free to modify and distribute as needed.

![Bg](https://github.com/user-attachments/assets/07e0e5fb-b056-4d42-91fc-7403693cf0e5)
