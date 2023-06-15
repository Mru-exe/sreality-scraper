import psycopg2
from scrapy.exceptions import DropItem

class PostgresPipeline:
    def __init__(self, db_params):
        self.db_params = db_params

    @classmethod
    def from_crawler(cls, crawler):
        db_params = {
            'host': crawler.settings.get('DB_HOST'),
            'port': crawler.settings.get('DB_PORT'),
            'database': crawler.settings.get('DB_NAME'),
            'user': crawler.settings.get('DB_USER'),
            'password': crawler.settings.get('DB_PASSWORD'),
        }
        return cls(db_params)

    def open_spider(self, spider):
        self.connection = psycopg2.connect(**self.db_params)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS scraped_data (
            id SERIAL PRIMARY KEY,
            title TEXT,
            image TEXT
        )
        '''
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def process_item(self, item, spider):
        self.insert_item(item)
        raise DropItem()  # Drop the item after inserting to avoid further processing

    def insert_item(self, item):
        insert_query = '''
        INSERT INTO scraped_data (title, image)
        VALUES (%s, %s)
        '''
        self.cursor.execute(insert_query, (item['title'], item['image']))
        self.connection.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
