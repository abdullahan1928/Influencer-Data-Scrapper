import calc_time as ct
import requests
from bs4 import BeautifulSoup
import pprint
import json
import excel_logic as ex
import cloudscraper

ct.start_time

url = 'https://www.noxinfluencer.com/youtube-channel-rank/top-100-all-all-youtuber-sorted-by-subs-weekly'

page = requests.get(url)

AreaDict = {}

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('select', attrs={
                    'id': 'area-filter-select'}).findAll('option')

for result in results:
    countryName = str(result.text).strip()
    countryAbbreviation = str(result['value']).lower()
    AreaDict[countryName] = countryAbbreviation


def getIndividualChannelData(noxInfluencerUrl):
    page = requests.get(noxInfluencerUrl)
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        twitterAccount = soup.find('a', attrs={'title': 'Twitter'})['href']
    except:
        twitterAccount = "None"

    try:
        instagramAccount = soup.find('a', attrs={'title': 'Instagram'})['href']
    except:
        instagramAccount = "None"

    try:
        facebookPage = soup.find('a', attrs={'title': 'Facebook'})['href']
    except:
        facebookPage = "None"

    return twitterAccount, instagramAccount, facebookPage


totalIndex = 1


def getTopYoutubeChannelsBySubscribers(url):
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

        twitterAccount, instagramAccount, facebookPage = getIndividualChannelData(
            channelLinkOnNoxInfluencer)

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
        singleEntry = {
            'index': index,
            'channelName': channelName,
            'channelCategory': channelCategory,
            'channelSubscribers': channelSubscribers,
            'channelAverageViews': channelAverageViews,
            'channelLinkOnYoutube': channelLinkOnYoutube,
            'twitterAccount': twitterAccount,
            'instagramAccount': instagramAccount,
            'facebookPage': facebookPage
        }

        print(json.dumps(singleEntry, indent=4))

        global totalIndex

        i = 1
        for key in singleEntry:
            ex.ws.cell(row=totalIndex + 1, column=i,
                       value=singleEntry[key])
            i += 1

        totalIndex += 1

        if index == 80:
            ex.wb.save('youtube_channels.xlsx')


for name in AreaDict:
    url = f'https://www.noxinfluencer.com/youtube-channel-rank/top-100-{AreaDict[name]}-all-youtuber-sorted-by-subs-weekly?area='

    getTopYoutubeChannelsBySubscribers(url)

ct.calc_total_time()
