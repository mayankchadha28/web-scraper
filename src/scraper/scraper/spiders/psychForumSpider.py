from pathlib import Path
import scrapy
from urllib.parse import urlparse

class PsychForumSpider(scrapy.Spider):
    name="psychForum"
    # linkCount = None
    start_urls = ["https://www.psychforums.com/"]

    index=0
    # link_withfragment = []

    def parse(self, response):
        postLinks = response.css("div.post div.postbody h3 > a::attr(href)").getall()
        
        linkCount = len(postLinks)
        
        #follow each of the links 
        for url in postLinks:
            parsed_url = urlparse(url)
            fragment = parsed_url.fragment

            yield response.follow(url, callback=self.postParse, meta={'fragment': fragment})

        # Navigate to next page
        
        next_page = response.css("div.pagination > span > a::attr(href)")[self.index + 1].get()

        if next_page is not None:
            self.index += 1
            yield response.follow(next_page, callback=self.parse)

        


        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        # yield {
        #     "link-count": linkCount
        # }

    def postParse(self, response):
        
        fragment = response.meta.get('fragment')

        #Title
        mainTitle = response.css("h1 > a::text").get()

        postContext = response.css(f"div#{fragment} div.postbody div.content::text").getall()

        replies = response.css("div.post::attr(id)").getall()
        if fragment in replies:
            replies.remove(fragment)

        for reply in replies:
            element = response.css(f"div#{reply} div.postbody div.content::text").getall()
            
            yield {
                "title": mainTitle,
                "post": postContext,
                "reply": element
            }