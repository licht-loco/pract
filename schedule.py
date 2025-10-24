def schedule_posts(self):
    if self.current_week_day % 7 == 0:  # Воскресенье
        self.weekly_discount_post()
        self.writers_recommendation_post()
    elif self.current_week_day % 7 == 1:  # Понедельник
        self.daily_vote_post()
    elif self.current_week_day % 7 == 6:  # Суббота
        self.free_books_post()
