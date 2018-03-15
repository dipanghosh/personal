import pysitemap


if __name__ == '__main__':
    url = 'http://thedesignerd.in/travels.html'  # url from to crawl
    logfile = 'errlog.log'  # path to logfile
    oformat = 'txt'  # output format
    crawl = pysitemap.Crawler(url=url, logfile=logfile, oformat=oformat)
    crawl.crawl()