from locust import task, HttpUser
import random


class Object(HttpUser):
    bodies = [{
        "data": {
            "color": "purple",
            "size": "small"
        },
        "name": "New object-1"
    }, {
        "data": {
            "color": "white",
            "size": "big"
        },
        "name": "New object-2"
    }, {
        "data": {
            "color": "pink",
            "size": "medium"
        },
        "name": "New object-3"
    }]
    id = None

    def on_start(self):
        response = self.client.post('/object', json=self.bodies[random.choice(range(2))])
        self.id = response.json()['id']

    @task(1)
    def get_objects(self):
        self.client.get('/object')

    @task(4)
    def get_object_by_id(self):
        self.client.get(f'/object/{self.id}')

    @task
    def put_object_by_id(self):
        self.client.put(f'/object/{self.id}',
                        json={
                            "data": {
                                "color": "purple-UPD",
                                "size": "small-UPD"
                            },
                            "name": "New object"
                        })

    @task
    def patch_object_by_id(self):
        self.client.patch(f'/object/{self.id}',
                          json={
                              "data": {
                                  "color": "purple-UPD-2",
                                  "size": "small-UPD-2"
                              }
                          })

    def on_stop(self):
        self.client.delete(f'/object/{self.id}')
