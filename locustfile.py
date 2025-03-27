from locust import HttpUser, task, between


class MyApiUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://reqres.in/api"

    @task
    def get_users(self):
        self.client.get("/users?page=2")

    @task
    def post_user(self):
        self.client.post("/users", json={"name": "John", "job": "developer"})
