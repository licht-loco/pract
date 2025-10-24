import requests
from datetime import datetime, timedelta
class Database:
    def __init__(self):
        self.published_books = []
        def add_published_book(self, book_id):
        current_date = datetime.now().strftime('%Y-%m-%d')
        self.published_books.append((book_id, current_date))
    def is_recently_published(self, book_id):
        threshold_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
        for published_book in reversed(self.published_books): 
            if published_book[0] == book_id and published_book[1] >= threshold_date:
                return True
        return False
def publish_daily_bestseller(group_id, access_token, top_30_books):
    db = Database()
    today = datetime.now().strftime('%Y-%m-%d')
    for book in top_30_books:
        book_id = book['id']
        title = book['title']
        if not db.is_recently_published(book_id):
            message = f'Книга № {top_30_books.index(book)+1}: "{title}"'
            response = requests.post(
                'https://api.vk.com/method/wall.post',
                params={
                    'owner_id': '-' + group_id,
                    'message': message,
                    'access_token': access_token,
                    'v': '5.131'
                }
            )
            print(f'{today} Опубликована книга: {title}')
            db.add_published_book(book_id)
            break 
        else:
            continue 
