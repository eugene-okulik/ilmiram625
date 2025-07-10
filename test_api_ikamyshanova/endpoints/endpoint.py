import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None

    @allure.step('Name, id and data is correct')
    def check_data(self, data, name=None):
        assert 'id' in self.json
        assert self.json['id']
        if name:
            assert self.json['name'] == name
        assert self.json['data'] == data

    @allure.step('Check status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, f'Status code is "{self.response.status_code}", not 200!'
