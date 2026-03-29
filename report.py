def generate_report(url, emails, links, phones, ports):
    with open("report.txt", "w") as file:
        file.write("===== MINI RECON REPORT =====\n\n")

        file.write(f"Target URL: {url}\n\n")

        file.write("---- Emails ----\n")
        for email in emails:
            file.write(email + "\n")

        file.write("\n---- Links ----\n")
        for link in links[:10]:
            file.write(link + "\n")

        file.write("\n---- Phone Numbers ----\n")
        for phone in phones:
            file.write(phone + "\n")

        file.write("\n---- Open Ports ----\n")
        for port in ports:
            file.write(port + "\n")

    print("\nReport saved as report.txt")