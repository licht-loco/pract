def free_books_post(self):
    books = self.generate_mock_data()['free_books']
    books_message = '\n'.join(books[:10])  # Только первые 10 книг (ограничение VK/TG)
    message = f"Список бесплатных книг на этой неделе:\n{books_message}"
    self.publish_vk_post(message)
