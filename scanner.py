import subprocess

def scan_ports(target):
    print("\n========== NMAP SCAN ==========\n")

    try:
        result = subprocess.run(
            ["nmap", "-sC", "-sV", target],
            capture_output=True,
            text=True
        )

        output = result.stdout

        # Extract useful lines
        lines = output.split("\n")
        open_ports = []

        for line in lines:
            if "open" in line:
                open_ports.append(line)

        print("Open Ports & Services:\n")
        for port in open_ports:
            print(port)

        return open_ports

    except Exception as e:
        print("Error running Nmap:", e)
        return []