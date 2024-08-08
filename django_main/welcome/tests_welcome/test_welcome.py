import pytest
from django.test import Client


class TestWelcome:
    @pytest.fixture
    def setup_client(self):
        self.client = Client()

    def test_homepage_status_code(self, setup_client):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_welcome_in_homepage_content(self, setup_client):
        response = self.client.get("/")
        assert "Welcome!" in response.content.decode()
