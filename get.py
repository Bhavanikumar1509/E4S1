import requests
link='https://github.com/Bhavanikumar1509/Phishin-url/raw/main/phishing_site_urls.zip'
r = requests.get(link, allow_redirects=True)
open('phishing_site_urls.zip', 'wb').write(r.content)
