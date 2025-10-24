def writers_recommendation_post(self):
    recommendations = self.generate_mock_data()['writers_recommendations']
    recommendation_message = '\n'.join(recommendations)
    message = f"Писатели рекомендуют:\n{recommendation_message}"
    self.publish_vk_post(message)
