# CPU & RAM Monitor

A simple script to monitor CPU and RAM usage on Linux systems and log the data to a file.  
Includes a **systemd service** to run the monitor automatically in the background.


## Features

- Monitors CPU and RAM usage in real-time
- Logs usage every 10 seconds to a file
- Can run as a **systemd service**
- Automatically restarts if the script crashes

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/annachemicz/cpu_ram_monitoring.git
cd cpu_ram_monitoring
chmod +x monitor.sh
sudo cp cpu_ram.service /etc/systemd/system/

## **Usage**
Manual Execution
./monitor.sh

Running as a Systemd Service
# Reload systemd after adding the service
sudo systemctl daemon-reload

# Enable service to start at boot
sudo systemctl enable cpu_ram.service

# Start the service
sudo systemctl start cpu_ram.service

# Check service status
sudo systemctl status cpu_ram.service

## **Logs**

The script writes logs to:

usage.log


Sample output:

2026-01-08 18:20:12 CPU: 12.3% RAM: 45.6%
2026-01-08 18:20:22 CPU: 15.1% RAM: 46.2%

## **Requirements**

Linux (Ubuntu, Debian, or similar)

## **Bash**

Systemd (if running as a service)

## **License**

Open-source project – free to use and modify.
