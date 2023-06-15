BOT_NAME = 'myscraper'

SPIDER_MODULES = ['myscraper.spiders']
NEWSPIDER_MODULE = 'myscraper.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'myscraper.pipelines.PostgresPipeline': 300,
}

# PostgreSQL Database Configuration
DB_HOST = 'database'
DB_PORT = '5432'
DB_NAME = 'database'
DB_USER = 'user'
DB_PASSWORD = 'password'
