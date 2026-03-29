from fetcher import fetch_website
from extractor import extract_emails, extract_links, extract_phone_numbers
from scanner import scan_ports
from report import generate_report

def main():
    url = "http://localhost:3000"
    target = "localhost"

    response = fetch_website(url)

    if response:
        content = response.text

        emails = extract_emails(content)
        links = extract_links(content)
        phones = extract_phone_numbers(content)

        print("\n========== OSINT RESULTS ==========\n")
        print("Emails Found:", emails)
        print("\nLinks Found (First 10):", links[:10])
        print("\nPhone Numbers Found:", phones)

        ports = scan_ports(target)

        generate_report(url, emails, links, phones, ports)

if __name__ == "__main__":
    main()