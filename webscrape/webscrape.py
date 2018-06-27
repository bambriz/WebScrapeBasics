from bs4 import BeautifulSoup as bSoup
import aiohttp
import asyncio
import string

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        url = input()
        html = await fetch(session, url)
        soup = bSoup(html, 'html.parser')
        print(soup.title.get_text())
        print(soup.title.name)
        print(soup.p)
        words = soup.get_text()

        delimits = string.punctuation

        words = words.strip(delimits).lower()
        wordsList = words.split()
        wordsList = [x.strip(delimits) for x in wordsList]
        notCount = ["a", "the", "and", "but", "or", "of", " "]
        for i in wordsList:
            if i in notCount:
                wordsList.remove(i)

        wordCount = {}
        for word in wordsList:
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
        filestring = ""
        for key, item in wordCount.items():
            filestring += key + " " + str(item) + "\n"

        with open('wordcount.txt', 'w') as fp:
            fp.write(filestring)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())



