from flask import Flask, render_template, request
import socket
import threading

app = Flask(__name__)

def scan_port(target, port):
    """
    Scan a specific port on the target to check if it's open.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        conn = s.connect_ex((target, port))
        if conn == 0:
            return f"Port {port} is OPEN on {target}"
        return None
    except Exception as e:
        return f"Error scanning port {port} on {target}: {str(e)}"
    finally:
        s.close()

def run_port_scan(target, start_port, end_port):
    """
    Run the port scan on a range of ports and return a list of open ports.
    """
    open_ports = []
    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=lambda p: open_ports.append(scan_port(target, p)) if scan_port(target, p) else None, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Ensure all threads have completed

    return [result for result in open_ports if result]

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    target = None
    start_port = None
    end_port = None

    if request.method == 'POST':
        target = request.form.get('target')
        start_port = int(request.form.get('start_port'))
        end_port = int(request.form.get('end_port'))

        results = run_port_scan(target, start_port, end_port)

    return render_template('index.html', results=results, target=target, start_port=start_port, end_port=end_port)

if __name__ == '__main__':
    app.run(debug=True)
