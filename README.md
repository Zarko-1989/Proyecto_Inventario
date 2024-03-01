README para la API de Productos con FastAPI
Descripción
Esta es una API RESTful basada en FastAPI para gestionar productos. Proporciona puntos finales para recuperar, crear, actualizar y eliminar productos. La API incluye características como autenticación utilizando JSON Web Tokens (JWT) y validación de parámetros de entrada.

Configuración
Instale los paquetes necesarios utilizando el siguiente comando:

pip install fastapi
Asegúrese de que las dependencias necesarias estén instaladas:

pip install uvicorn
Ejecute la aplicación FastAPI con el siguiente comando:

uvicorn main:app --reload
Reemplace main con el nombre del archivo que contiene su aplicación FastAPI.

La API estará accesible en http://127.0.0.1:8000.

Puntos finales
1. Obtener Todos los Productos
Endpoint: /product
Método: GET
Descripción: Recupera una lista de todos los productos.
Autenticación: Requiere un token JWT válido.
2. Obtener Producto por ID
Endpoint: /product/{id}
Método: GET
Descripción: Recupera un producto por su ID.
Parámetros:
id (Path): ID del producto (entero).
Códigos de Estado:
200 OK: Recuperación exitosa.
404 Not Found: Producto no encontrado.
3. Obtener Productos por Categoría
Endpoint: /product/
Método: GET
Descripción: Recupera una lista de productos basados en la categoría especificada.
Parámetros:
category (Query): Categoría del producto (cadena, longitud 3-15).
Códigos de Estado:
200 OK: Recuperación exitosa.
404 Not Found: No se encontraron productos para la categoría especificada.
4. Crear Producto
Endpoint: /product
Método: POST
Descripción: Crea un nuevo producto.
Cuerpo de la Solicitud:
product (JSON): Detalles del producto.
Códigos de Estado:
201 Created: Producto creado con éxito.
5. Actualizar Producto por ID
Endpoint: /product/{id}
Método: PUT
Descripción: Actualiza un producto existente por su ID.
Parámetros:
id (Path): ID del producto (entero).
Cuerpo de la Solicitud:
product (JSON): Detalles actualizados del producto.
Códigos de Estado:
200 OK: Producto actualizado con éxito.
404 Not Found: Producto no encontrado.
6. Eliminar Producto por ID
Endpoint: /product/{id}
Método: DELETE
Descripción: Elimina un producto por su ID.
Parámetros:
id (Path): ID del producto (entero).
Autenticación: Requiere un token JWT válido.
Códigos de Estado:
200 OK: Producto eliminado con éxito.
404 Not Found: Producto no encontrado.
Autenticación
Algunos puntos finales requieren autenticación utilizando JSON Web Tokens (JWT). Asegúrese de incluir un token JWT válido en el encabezado de la solicitud.