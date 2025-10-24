def daily_vote_post(self):
    vote_options = self.generate_mock_data()['vote_options']
    vote_message = "\n".join(vote_options)
    message = f"Ваш выбор завтра:\n{vote_message}\nПроголосуй!"
    self.publish_vk_post(message)
