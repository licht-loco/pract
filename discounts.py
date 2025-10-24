  def weekly_discount_post(self):
      discounts = self.generate_mock_data()['discounts']
      discount_message = '\n'.join(discounts)
      message = f"Сегодняшняя подборка скидок:\n{discount_message}"
      self.publish_vk_post(message)
