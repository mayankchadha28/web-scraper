from pathlib import Path
import scrapy

class ForumSpider(scrapy.Spider):
    name="forum"

    start_urls = ["https://www.sane.org.uk/how-we-help/sane-community/support-forum/topic/forum-feedback-suggestions"]

    # def start_requests(self):
    #     urls = [
    #         "https://www.sane.org.uk/how-we-help/sane-community/support-forum/topic/forum-feedback-suggestions"
    #     ]

    #     for url in urls:
    #         yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        pageTitle = response.css("title::text").get()

        #Context
        mainTitle = response.css("h1.main-title::text").get()

        #Replies
        repliesList = response.css("div.post-element")

        for reply in repliesList:
            paraList = reply.css("div.post-message p::text").getall()
            # para = 
            message = " ".join(paraList)
            message = paraList
            yield {
                "title": mainTitle,
                "response": message
            }






    