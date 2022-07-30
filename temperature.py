from selectorlib import Extractor
import requests

class Temperature:

    base_url = "https://www.timeanddate.com/weather/"
    yaml_path = "temperature.yaml"

    def __init__(self, country, city):
        self.city = city.replace(" ", "-")
        self.country = country.replace(" ", "-")
        
    def _build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yaml_path)
        r = requests.get(url)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        scraped_content = self._scrape()
        return float(scraped_content["temp"].replace("°C", "").strip())

        