from crawl4ai import WebCrawler
crawler = WebCrawler () 
crawler.warmup ( ) 
result = crawler.run (url="https://digikala.com" )
print(result.markdown)
