from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Время ожидания между задачами (1-5 секунд)
    wait_time = between(1, 5)

    @task
    def load_homepage(self):
        # Запрос к главной странице
        self.client.get("/")

    @task(3)  # Эта задача выполняется в 3 раза чаще
    def load_about_page(self):
        # Запрос к странице "О нас"
        self.client.get("/about/")

    @task(2)
    def load_contact_page(self):
        # Запрос к странице "Контакты"
        self.client.get("/contact/")