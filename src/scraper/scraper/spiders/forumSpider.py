from pathlib import Path
import scrapy

class ForumSpider(scrapy.Spider):
    name="forum"
    # linkCount = None
    start_urls = ["https://www.sane.org.uk/how-we-help/sane-community/support-forum/forum/family-friends-and-carers"]

    def parse(self, response):
        postLinks = response.css("div.content-container div.content-element div.topic-name > a::attr(href)").getall()
        
        linkCount = len(postLinks)

        # yield {
        #         "topicCount": linkCount,
        #     }
        

        for url in postLinks:
            yield response.follow(url, callback=self.postParse)

        # Navigate to next page
        next_page = response.css("div.pages-and-menu a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)




    def postParse(self, response):
        # pageTitle = response.css("title::text").get()

        #Context
        mainTitle = response.css("h1.main-title::text").get()

        #Replies
        repliesList = response.css("div.post-element")

        for reply in repliesList:
            paraList = reply.css("div.post-message p::text").getall()
            
            message = " ".join(paraList)
            message = paraList
            yield {
                "title": mainTitle,
                "response": message,
                # "linkCount": linkCount
            }






    