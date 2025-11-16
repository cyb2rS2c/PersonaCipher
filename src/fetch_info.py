import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_infobox(username=None):
    url = f"https://en.wikipedia.org/wiki/{username}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print(f"Sorry, no Wikipedia page found for {username}.")
        else:
            print(f"HTTP error occurred: {err}")
        return False 

    soup = BeautifulSoup(response.text, 'html.parser')

    infobox = soup.find('table', {'class': 'infobox'})

    if not infobox:
        print("No infobox found on Wikipedia.")
        return False

    labels = []
    values = []

    for row in infobox.find_all('tr'):
        th = row.find('th')
        td = row.find('td')

        if th and td:
            label = th.get_text(strip=True)
            value = td.get_text(strip=True)

            if label and value:
                if any(keyword in label.lower() for keyword in ['website', 'medal record', 'signature']):
                    continue
                value = ''.join(BeautifulSoup(value, 'html.parser').findAll(text=True)).strip()
                labels.append(label)
                values.append(value)
    print(f"{'Label':<30} {'Value'}")
    print('-' * 50)

    for label, value in zip(labels, values):
        print(f"{label:<30} {value}")

    return True

def main():
    person_detected = input("Enter the name of the detected person, country, content, etc: ")
    fetch_wikipedia_infobox(person_detected)

if __name__ == "__main__":
    main()
