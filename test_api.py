import requests # type: ignore

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1ra Prueba: Obtener un usuario y verificar su estructura
def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data
    assert data["id"] == 1

# 2️da Prueba: Obtener un post y validar contenido
def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert data["id"] == 1

# 3ra Prueba: Crear un nuevo post y verificar respuesta
def test_create_post():
    payload = {"title": "Nuevo post", "body": "Contenido del post", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

# 4️ta Prueba: Verificar la lista de comentarios de un post
def test_get_post_comments():
    response = requests.get(f"{BASE_URL}/posts/1/comments")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "postId" in data[0]
    assert "email" in data[0]
    assert data[0]["postId"] == 1
