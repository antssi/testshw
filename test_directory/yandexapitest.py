import yandexapi as yapi

class TestYandexApi:

    def test_create_new_folder(self):
        assert yapi.folder_create('New_Test') == (201, True)

    def test_exists_create_folder(self):
        assert yapi.folder_create('New_Test') == f'already exist'