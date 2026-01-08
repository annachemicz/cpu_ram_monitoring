# CPU & RAM Monitor

A simple script to monitor CPU and RAM usage on Linux systems and log the data to a file.  
Includes a **systemd service** to run the monitor automatically in the background.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Systemd Service](#systemd-service)
- [Logs](#logs)
- [Requirements](#requirements)
- [License](#license)

---

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
