import os
import json
import requests 
from bs4 import BeautifulSoup

# Change pwd to root directory
os.chdir(os.path.abspath(os.path.join(__file__ ,"../../..")))

TACTICS_BASE_URLS = ["https://attack.mitre.org/tactics/enterprise/", "https://attack.mitre.org/tactics/mobile/", "https://attack.mitre.org/tactics/ics/"]
TECHNIQUES_BASE_URLS = ["https://attack.mitre.org/techniques/enterprise/", "https://attack.mitre.org/techniques/mobile/", "https://attack.mitre.org/techniques/ics/"]
MITIGATIONS_BASE_URLS = ["https://attack.mitre.org/mitigations/enterprise/", "https://attack.mitre.org/mitigations/mobile/", "https://attack.mitre.org/mitigations/ics/"]

def save_data_to_txt(filepath, data: list):
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            for i in data:
                f.write(i + "\n")
        print(f"Data saved in {filepath} successfully!")

    else:
        print("Text file already exists!")


def get_tactic_urls(base_url_list):
    BASE_URL = "https://attack.mitre.org/tactics/"
    tactic_urls = []
    for url in base_url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Get tactic IDS
        for row in soup.find_all("tr")[1:]:
            cols = row.find_all("td")
            tactic_id = cols[0].text.strip()
            tactic_url = BASE_URL + tactic_id + "/"
            tactic_urls.append(tactic_url)
            

    return tactic_urls

def get_tactic_data(tactic_urls):

    data = []

    for url in tactic_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        tactic_name = soup.find("h1")
        tactic_desc = soup.find_all("p")
        tactic_text = ""
        for desc in tactic_desc:
            tactic_text = tactic_text + desc.text.strip()
        
        data.append(tactic_name.text.strip() + ": " + tactic_text)
    
    print("Tactics Data from Mitre Scraped")

    return data
        

def get_techniques_data(URL_list):
    data = []

    for url in URL_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        for row in soup.select("tr", class_="technique"):
            cols = row.find_all("td")
            
            for col in cols[1:]:
                data.append(col.text.strip())

    print("Techniques Data from Mitre Scraped")
    
    return data
                


def get_mitigations_data(URL_list):
    data = []
    for url in URL_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for row in soup.select("tr")[1:]:
            cols = row.find_all("td")
            mitigation_name = cols[1].text.strip()
            mitigation_desc = cols[2].text.strip()
            data.append(mitigation_name + ": " + mitigation_desc)

    print("Mitigations Data from Mitre Scraped")
    
    return data


if __name__ == "__main__":
    print("Scraping of Mitre Initiated")
    tactic_urls = get_tactic_urls(TACTICS_BASE_URLS)
    tactic_data = get_tactic_data(tactic_urls)
    techniques_data = get_techniques_data(TECHNIQUES_BASE_URLS)
    mitigations_data = get_mitigations_data(MITIGATIONS_BASE_URLS)

    filepaths_to_save = {"data/raw/mitre_tactics.txt": tactic_data,
                         "data/raw/mitre_techniques.txt": techniques_data,
                         "data/raw/mitre_mitigations.txt": mitigations_data}

    for filepath, data in filepaths_to_save.items():
        save_data_to_txt(filepath, data)



