import scrapy


class OnlineSlangSpider(scrapy.Spider):
    name = "onlineslang"
    start_urls = ["http://onlineslangdictionary.com/browse/a"]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f"onlineslang-{page}.txt"
        with open(filename, "wb") as f:
            list_words = response.selector.xpath(
                '//div[contains(@class, "term")]/h2/a/text()'
            ).getall()
            for word in list_words:
                data = word.encode()
                f.write(data)
                f.write(b"\n")
        self.log(f"Saved file {filename}")
