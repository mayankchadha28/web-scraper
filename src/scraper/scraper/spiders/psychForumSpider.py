from pathlib import Path
import scrapy
from urllib.parse import urlparse

class PsychForumSpider(scrapy.Spider):
    name="psychForum"
    # linkCount = None
    start_urls = ["https://www.psychforums.com/"]

    def parse(self, response):
        postLinks = response.css("div.post div.postbody h3 > a::attr(href)").getall()
        
        linkCount = len(postLinks)
        
        #follow each of the links 
        for url in postLinks:
            yield response.follow(url, callback=self.postParse)

        # # Navigate to next page
        # next_page = response.css("div.pages-and-menu a::attr(href)").get()

        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)




    def postParse(self, response):
        # pageTitle = response.css("title::text").get()
        parsed_url = urlparse(response.url)
        fragment = parsed_url.fragment

        #Title
        mainTitle = response.css("h1 > a::text").get()

        #Post
        yield {
            "title": mainTitle,
            "fragment": response.url
        }
        # postContext = response.css(f"div #{fragment} div.postbody div.content::text").getall()

        # yield {
        #     "title": mainTitle,
        #     "post": postContext
        # }

        #Replies
        # repliesList = response.css("div.post-element")

        # for reply in repliesList:
        #     paraList = reply.css("div.post-message p::text").getall()
            
        #     message = " ".join(paraList)
        #     message = paraList
        #     yield {
        #         "title": mainTitle,
        #         "response": message,
        #         # "linkCount": linkCount
        #     }

