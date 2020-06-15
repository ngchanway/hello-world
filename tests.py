from hello import app
with app.test_client() as c:
    response = c.get('/')
    assertEqual(response.status_code, 200)
    assertEqual(response.data, b'Hello World!')
