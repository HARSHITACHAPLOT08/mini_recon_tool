import requests

def fetch_website(url):
    try:
        proxies = {
            "http": "http://127.0.0.1:8080",
            "https": "http://127.0.0.1:8080"
        }

        response = requests.get(url, proxies=proxies)

        print("Status Code:", response.status_code)
        print("\nHeaders:\n", response.headers)
        print("\nFirst 500 Characters of HTML:\n")
        return response

    except Exception as e:
        print("Error:", e)
        return None