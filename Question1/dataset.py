import os
import requests
from bs4 import BeautifulSoup
import random

# Second Section: Declare important variables
google_image = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

# Third Section: Build the main function
saved_folder = 'images'

test_numbers = random.sample(range(1, 101), 20)

def main():
    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)
    download_images()


# Fourth Section: Build the download function
def download_images():
    data = input('What are you looking for? ')

    print('searching...')

    links = []  

    temp = ["black", "white", "brown", "small", "animated"]

    for i in range(0, 5):

        search_url = google_image + 'q=' + data + " " + temp[i]
        print(search_url)

        response = requests.get(search_url, headers=user_agent)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.findAll('img', {'class': 'DS1iW'})

        count = 1
        for result in results:
            try:
                link = result['src']
                links.append(link)
                count += 1
                if(count > 100):
                    break

            except KeyError:
                continue

    print(f"Downloading {len(links)} images...")

    for i, link in enumerate(links):
        response = requests.get(link)

        if i in test_numbers:
            image_name = saved_folder + '/test/' + data+ '/' + data + str(i+1) + '.jpg'
        else:
            image_name = saved_folder + '/train/' + data + '/' + data + str(i+1) + '.jpg'

        with open(image_name, 'wb') as fh:
            fh.write(response.content)


# Fifth Section: Run your code
if __name__ == "__main__":
    main()