from pathlib import Path
import scrapy
from urllib.parse import urlparse

class PsychForumSpider(scrapy.Spider):
    name="psychForum"
    # linkCount = None
    start_urls = ["https://www.psychforums.com/"]

    # link_withfragment = []

    def parse(self, response):
        postLinks = response.css("div.post div.postbody h3 > a::attr(href)").getall()
        
        linkCount = len(postLinks)
        
        #follow each of the links 
        for url in postLinks:
            parsed_url = urlparse(url)
            fragment = parsed_url.fragment

            yield response.follow(url, callback=self.postParse, meta={'fragment': fragment})

        # # Navigate to next page
        # next_page = response.css("div.pages-and-menu a::attr(href)").get()

        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

    def postParse(self, response):
        
        fragment = response.meta.get('fragment')

        #Title
        mainTitle = response.css("h1 > a::text").get()

        #Post
        # yield {
        #     "title": mainTitle,
        #     "fragment": fragment
        # }

        postContext = response.css(f"div#{fragment} div.postbody div.content::text").getall()

        yield {
            "title": mainTitle,
            "post": postContext
        }

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

