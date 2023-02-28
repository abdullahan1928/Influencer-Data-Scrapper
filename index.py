import calc_time as ct
import requests
from bs4 import BeautifulSoup
import pprint
import json

ct.start_time

url = 'https://www.noxinfluencer.com/youtube-channel-rank/top-100-all-all-youtuber-sorted-by-subs-weekly'

page = requests.get(url)

AreaDict = {}

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('select', attrs={
                    'id': 'area-filter-select'}).findAll('option')

for result in results:
    countryName = str(result.text).strip()
    countryAbbreviation = str(result['value']).lower()
    AreaDict[countryName] = countryAbbreviation

# pretty print the dictionary
# pprint.pprint(AreaDict)

# print(json.dumps(AreaDict, indent=4))


def getYoutubeData(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    tables = soup.findAll('div', attrs={'class': 'table-line clearfix'})
    index = 0
    for table in tables:
        index += 1
        channelLink = table.find('a', attrs={'class': 'link clearfix'})['href']
        channelLinkOnYoutube = channelLink.replace(
            '/youtube', 'https://www.youtube.com')
        channelLinkOnNoxInfluencer = f'https://www.noxinfluencer.com{channelLink}'

        channelName = table.find(
            'span', attrs={'class': 'title pull-left ellipsis'}).text

        try:
            channelCategory = table.find('span', attrs={
                'class': 'rank-cell pull-left rank-category'}).find('a', attrs={'class': 'category'}).text
        except:
            channelCategory = "None"

        channelSubscribers = table.find(
            'span', attrs={'class': 'rank-cell pull-left rank-subs'}).find('span', attrs={'class': 'number'}).text

        channelAverageViews = table.find('span', attrs={
                                         'class': 'rank-cell pull-left rank-avg-view'}).find('span', attrs={'class': 'number'}).text

        print(f'{index} {channelName} {channelCategory} {channelSubscribers} {channelAverageViews} {channelLinkOnYoutube} {channelLinkOnNoxInfluencer}')


for name in AreaDict:
    url = f'https://www.noxinfluencer.com/youtube-channel-rank/top-100-{AreaDict[name]}-all-youtuber-sorted-by-subs-weekly?area='

    getYoutubeData(url)

ct.calc_total_time()
