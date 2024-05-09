import requests
from bs4 import BeautifulSoup
import re
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    return text

def extract_data():
    url = 'https://www.bbc.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', {'data-testid': 'card-text-wrapper'})

    data = []
    for card in cards:
        headline = card.find('h2', {'data-testid': 'card-headline'})
        description = card.find('p', {'data-testid': 'card-description'})
        link_tag = card.parent.find('a', {'data-testid': 'internal-link'})

        title = clean_text(headline.text) if headline else 'No title found'
        description = clean_text(description.text) if description else 'No description available'
        link = url + link_tag['href'] if link_tag and link_tag.get('href') else 'No link available'

        data.append({'title': title, 'description': description, 'link': link})
    return data

def save_data_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data successfully saved to {filename}")

def upload_to_drive(filename):
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds.txt")

    drive = GoogleDrive(gauth)
    file1 = drive.CreateFile({'title': os.path.basename(filename)})
    file1.SetContentFile(filename)
    file1.Upload()
    print('File uploaded to Google Drive')

def main():
    data = extract_data()
    json_filename = 'extracted_data.json'
    save_data_to_json(data, json_filename)
    upload_to_drive(json_filename)
    os.system(f'dvc add {json_filename}')
    os.system('git add .')
    os.system('git commit -m "Update dataset and DVC files"')
    os.system('dvc push')

if __name__ == "__main__":
    main()
