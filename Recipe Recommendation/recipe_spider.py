import scrapy

class RecipeSpider(scrapy.Spider):
    name = "recipes"
    start_urls = ["https://www.bbcgoodfood.com/search?limit=1000&offset=9000"]
    current_offset = 0
    def parse(self, response):
        for link in response.css('div.card__section.card__content a.link.d-block::attr(href)').getall():
            yield response.follow(link, self.parse_recipe)
        

        for i in range(1000,10000,1000):
            next_url = f"https://www.bbcgoodfood.com/api/search-frontend/search?limit=1000&offset={i}"
            yield scrapy.Request(url=next_url, callback=self.parse)



    def parse_recipe(self, response):
        ingredients = list(response.css("li.pb-xxs.pt-xxs.list-item.list-item--separator::text").getall()) + list(response.css("li.pb-xxs.pt-xxs.list-item.list-item--separator a.link.link--styled::text").getall())
        yield {
            "title": response.css("h1.heading-1::text").get(),
            "link": response.url,
            "ingredients": ingredients
        }
