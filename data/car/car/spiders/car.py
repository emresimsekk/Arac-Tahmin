#veri çekmek için scrapy kütüphanesi kullanıldı.
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    #Sayfa Numarası
    page_number=2
    #Verinin çekileceği URL
    start_urls = [
        'https://www.arabam.com/ikinci-el/otomobil?take=50&page=1',
    ]

    def parse(self, response):

        #Verilerin bulunduğu tablonun css özelliği ile kolonlarına erişiyoruz
        all_div_quotes= response.css('tr.listing-list-item')

        #Veriler web sitesinde tabloda bulunduğundan dolayı tr'yi döngüye alıyoruz
        for quote in  all_div_quotes:

            #Css yardımıyla sutunlara erişiğ içerikleri çekip isimlendiriyoruzç
            yield {'model': quote.css('td.listing-modelname>h3>a::text').extract(),
            'yil': quote.css('td.listing-text>div>a::text')[0].extract(),
            'km': quote.css('td.listing-text>div>a::text')[1].extract(),
            'renk':quote.css('td.listing-text>div>a::text')[2].extract(),
            'fiyat': quote.css('td.pl8>div>span>a::text').extract(),
            'il':quote.css('td.listing-text>div>div>a>span::text')[0].extract(),
            }
          
        #Sayfada içerik bittiyle bir sonraki sayfaya geçiyor.
        next_page='https://www.arabam.com/ikinci-el/otomobil?page='+str(QuotesSpider.page_number)
        #50 sayfaya kadar sınır konuldu.
        if QuotesSpider.page_number<=50:
            QuotesSpider.page_number+=1
            yield response.follow(next_page, callback=self.parse)
    
    


    