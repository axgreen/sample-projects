# -*- coding: utf-8 -*-

BOT_NAME = 'splash_crawlera_example'
SPIDER_MODULES = ['splash_crawlera_example.spiders']
NEWSPIDER_MODULE = 'splash_crawlera_example.spiders'

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

CRAWLERA_APIKEY = '85dccf322a2e4a6b9c7b6f6e99b0f758'  # Your crawlera API key

# Splash settings
SPLASH_URL = 'https://a3wrgp4j-splash.scrapinghub.com/'     # Splash instance URL from Scrapy Cloud
SPLASH_APIKEY = '100cfdae551a41cda4617883289d0efb'  # Your API key for the Splash instance hosted on Scrapy Cloud
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
