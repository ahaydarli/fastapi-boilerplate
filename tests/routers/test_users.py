class TestPing:
    def test__ping(self, client):
        response = client.get("/v1/users")
        assert response.status_code == 200
