# -*- coding:utf-8 -*-
from scrapy.loader import ItemLoader, Identity

__author__ = 'xuan'

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
# from amazonspider.items import AmazonItem
from amazon.items import AmazonItem



import sys
from scrapy.crawler import  CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner




reload(sys)
sys.setdefaultencoding('utf8')

class AmazomSpider_reviews(CrawlSpider):
    name = 'amazonspider_reviews' #这个是scrapy crawl 的项目名字

    custom_settings = {
          "ITEM_PIPELINES":{'amazon.pipelines.AmazonPipelineByMongo_Reviews':500}
    }

    allowed_domains = ["www.amazon.com"]
    # print(sys.argv[1])
    #
    good_name = sys.argv[1].split('/')[0]
    print('goodname', good_name)
    good_num = sys.argv[1].split('/')[1]
    print('good_num', good_num)

    start_urls = ["https://www.amazon.co.uk/%s/product-reviews/%s/ref=cm_cr_arp_d_show_all?ie=UTF8&reviewerType=all_reviews&pageNumber=1"%(good_name, good_num)]


    '''这里的第一个正则要注意最后面不能加&pageNumber='''
    '''这里用rules出问题'''
    rules = [
     #    # Rule(LinkExtractor(allow=r'/(\w+.*)/product-reviews/(\w+.*)/ref=cm_cr_dp_d_acr_sr\?ie=UTF8&reviewerType=avp_only_reviews',)),
     #    # Rule(LinkExtractor(allow=r'/(\w+.*)/product-reviews/(\w+.*)/ref=cm_cr_arp_d_show_all\?ie=UTF8&reviewerType=all_reviews',)),
        Rule(LinkExtractor(allow=r'/(\w+.*)/product-reviews/(\w+.*)/ref=cm_cr_arp_d_paging_btm_(\d+.*)\ie=UTF8&reviewerType=all_reviews',),callback='parse_item',follow=True),
	    Rule(LinkExtractor(allow=r'/(\w+.*)/product-reviews/(\w+.*)/ref=cm_cr_arp_d_paging_btm_(\d+.*)\ie=UTF8pageNumber=(\d+.*)&reviewerType=all_reviews',),callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=r'/(\w+.*)/product-reviews/(\w+.*)/ref=cm_cr_getr_d_paging_btm_(\d+.*)\ie=UTF8pageNumber=(\d+.*)&reviewerType=all_reviews&pageSize=10',),callback='parse_item',follow=True),
	#     # Rule(LinkExtractor(allow=r'https://www.amazon.com/(\w+.*)/dp/(\w+.*)//ref=cm_cr_arp_d_product_top\?ie=UTF8',),callback='parse_item1',follow=True),
	]


    def parse(self,response):
        #爬取reviews
        review_list = response.xpath("//div[@data-hook='review']")
        for info in review_list:
            item = AmazonItem()

            rating = info.xpath("div[@class='a-section celwidget']/div[@class='a-row']/a[@class='a-link-normal']/i[contains(@data-hook,'review-star-rating')]/span[@class='a-icon-alt']/text()").extract()
            title = info.xpath("div[@class='a-section celwidget']/div[@class='a-row']/a[@data-hook='review-title']/text()").extract()
            author = info.xpath("div[@class='a-section celwidget']/div[@class='a-row']/span[@data-hook='review-author']/a[@data-hook='review-author']/text()").extract()
            date = info.xpath("div[@class='a-section celwidget']/div[@class='a-row']/span[@data-hook='review-date']/text()").extract()
            body = info.xpath("normalize-space(div[@class='a-section celwidget']/div[@class='a-row review-data']/span[@data-hook='review-body']/text())").extract()

            item['rating'] = rating
            item['title'] = title
            item['author'] = author
            item['date'] = date
            item['body'] = body

            yield  item


            nextLink = response.xpath('//li[@class="a-last"]/a/@href').extract()
            print ('pages %s' % nextLink)


            #有下一页的链接继续,没有下一页的连接时停止
            if nextLink:
                nextLink = nextLink[0]
                #print nextLink
                yield Request('https://www.amazon.com' + nextLink,callback=self.parse)


class AmazomSpider_description(CrawlSpider):
    name = 'amazonspider_description'

    custom_settings = {
          "ITEM_PIPELINES":{'amazon.pipelines.AmazonPipelineByMongo_Description':500}
    }

    allowed_domains = ["www.amazon.com"]
    #print(sys.argv[1])
    start_urls = [sys.argv[1]]

    def parse(self,response):

        #爬取
        productname = response.xpath("normalize-space(//h1[@id='title']/span[@id='productTitle']/text())").extract()
        description = response.xpath("//div[@id='featurebullets_feature_div']/div[@id='feature-bullets']/ul[@class='a-unordered-list a-vertical a-spacing-none']/li/span[@class='a-list-item']/text()").extract()

        item = AmazonItem()

        item['productname'] = productname
        item['description'] = description

        yield  item


class AmazomSpider_qa(CrawlSpider):
    name = 'amazonspider_qa'

    custom_settings = {
          "ITEM_PIPELINES":{'amazon.pipelines.AmazonPipelineByMongo_Qa':500}
    }


    allowed_domains = ["www.amazon.com"]
    print(sys.argv[1])
    #start_urls = [ sys.argv[1] ]

    good_num = sys.argv[1].split('/')[1]
    #print(good_num)

    start_urls = ["https://www.amazon.com/ask/questions/asin/%s/1/ref=ask_ql_psf_ql_hza?isAnswered=true"%good_num]
    #print(start_urls)


    #QA  #注意这里的问号要用转义符
    '''Rule allow中不能加上https://www.amazonspider.com 要对应标签中来链接'''
    rules = [
        Rule(LinkExtractor(allow=r'/ask/questions/asin/(\w+.*)/(\d+.*)/ref=ask_ql_psf_ql_hza',)),
        Rule(LinkExtractor(allow=r'/forum/(\w+.*)/(\w+.*)/(\d+.*)/ref=cm_cd_al_psf_al_pg(\d+.*)\?_encoding=UTF8&asin=(\w+.*)',)), #注意这里的问号要用转义符)
        Rule(LinkExtractor(allow=r'/forum/-/(\w+.*)/ref=ask_ql_ql_al_hza\?asin=(\w+.*)',),callback='parse_item',follow = True),
    ]


    def parse_item(self,response):

        print('------------------parse_item-----------------------')

        item = AmazonItem()

        #qa_list  = response.xpath("//div[starts-with(@id,'question-')]")

        #for info in qa_list:

        question = response.xpath("normalize-space(//div[@class='cdQuestionText']/text())").extract_first()
        answer = response.xpath("normalize-space(//div[@class='cdMessageInfo']/span[contains(@id,'cdPostContentBox_')]/text())").extract()

        #question = info.xpath("normalize-space(div[@class='a-fixed-left-grid-inner']/div[@class='a-fixed-left-grid-col a-col-right']/a[@class='a-link-normal']/text())").extract()
        #answer = response.xpath("normalize-space(//div[@class='cdMessageInfo']/span[contains(@id,'cdPostContentBox_')]/text())").extract()

        #question_url = info.xpath("normalize-space(div[@class='a-fixed-left-grid-inner']/div[@class='a-fixed-left-grid-col a-col-right']/a[@class='a-link-normal']/@href)").extract_first()
        #print(question_url)


        item['question'] = question
        item['answer'] = answer

        yield item


            #yield Request('https://www.amazon.com' + question_url,callback=self.parse_item2())

            # nextLink = response.xpath('//li[@class="a-last"]/a/@href').extract()
            # print ('pages %s' % nextLink)
            #
            #
            # #没有下一页的连接时停止
            # if nextLink:
            #     nextLink = nextLink[0]
            #     print nextLink
            #     yield Request('https://www.amazon.com' + nextLink,callback=self.parse)


    # def parse_item2(self,response):
    #
    #     print('------------------parse_item2-----------------------')
    #
    #     item = AmazonItem()
    #
    #     #question = response.xpath("normalize-space(//div[@class='cdQuestionText']/text())").extract_first()
    #     answer = response.xpath("normalize-space(//div[@class='cdMessageInfo']/span[contains(@id,'cdPostContentBox_')]/text())").extract()
    #
    #     #item['question'] = question
    #     item['answer'] = answer
    #
    #     yield item   #yield Request('https://www.amazon.com' + question_url,callback=self.parse_item2())

            # nextLink = response.xpath('//li[@class="a-last"]/a/@href').extract()
            # print ('pages %s' % nextLink)
            #
            #
            # #没有下一页的连接时停止
            # if nextLink:
            #     nextLink = nextLink[0]
            #     print nextLink
            #     yield Request('https://www.amazon.com' + nextLink,callback=self.parse)


    # def parse_item2(self,response):
    #
    #     print('------------------parse_item2-----------------------')
    #
    #     item = AmazonItem()
    #
    #     #question = response.xpath("normalize-space(//div[@class='cdQuestionText']/text())").extract_first()
    #     answer = response.xpath("normalize-space(//div[@class='cdMessageInfo']/span[contains(@id,'cdPostContentBox_')]/text())").extract()
    #
    #     #item['question'] = question
    #     item['answer'] = answer
    #
    #     yield item


if __name__ == '__main__':
    if len(sys.argv) == 2:
        settings = get_project_settings()
        process = CrawlerProcess(settings=settings)

        #process.crawl(AmazomSpider_description)

        process.crawl(AmazomSpider_reviews)
	print(process.crawl(AmazomSpider_reviews))

        #process.crawl(AmazomSpider_qa)

        process.start()
    else:
        print "[-] For example[python -m amazon.spiders.amazonspider 'url']"
