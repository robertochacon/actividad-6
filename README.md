# 📝 Actividad #6 - Pruebas Unitarias con Pytest y API REST

## Roberto Chacon A. - 20-0918

Este proyecto contiene pruebas unitarias utilizando `pytest` para validar los endpoints de la API pública `JSONPlaceholder` (`https://jsonplaceholder.typicode.com`). Se prueban operaciones como obtener usuarios, publicaciones, comentarios y creación de posts.

## 📌 Requisitos Previos
Antes de ejecutar las pruebas, asegúrate de tener instalado:
- Python 3.x
- `pytest` y `requests`

Para instalar las dependencias necesarias, ejecuta:
```bash
pip install pytest requests
```

---

## 📂 Estructura del Proyecto
```bash
📦 pytest_api_tests
 ┣ 📜 test_api.py    # Archivo con las pruebas unitarias
 ┣ 📜 README.md      # Documentación del proyecto
```

---

## 📌 Descripción de las Pruebas

| 🏷️ Prueba                 | 🔎 Descripción |
|---------------------------|------------------------------|
| `test_get_user()`         | Obtiene un usuario y valida la estructura de la respuesta |
| `test_get_post()`         | Recupera un post y verifica los campos recibidos |
| `test_create_post()`      | Crea un nuevo post y valida que los datos coincidan |
| `test_get_post_comments()` | Obtiene los comentarios de un post y revisa su estructura |

---

## 🚀 Ejecución de Pruebas

Ejecuta las pruebas con el siguiente comando:
```bash
pytest test_api.py -v
```

El parámetro `-v` (`--verbose`) muestra detalles de cada prueba ejecutada.

---

## 📌 Ejemplo de Salida
Si todas las pruebas pasan, verás un resultado similar a:
```bash
============================= test session starts =============================
collected 4 items

test_api.py::test_get_user PASSED ✅
test_api.py::test_get_post PASSED ✅
test_api.py::test_create_post PASSED ✅
test_api.py::test_get_post_comments PASSED ✅

=========================== 4 passed in 2.10s ============================
```

---

## 🔄 Personalización
Si deseas probar otro endpoint, modifica `BASE_URL` en `test_api.py`:
```python
BASE_URL = "https://jsonplaceholder.typicode.com"
```
Y ajusta los endpoints en cada prueba según sea necesario.

Y esto es todo, gracias por ver esta testing!.
