# 📬 Backend Flask ML Correos
> Backend Flask ML Correos es un servicio backend desarrollado con Flask que proporciona funcionalidades de predicción utilizando un modelo de Machine Learning. Este backend está diseñado para integrarse con un frontend, pero también puede operar de manera independiente.



# 🚀 Características
- Predicción de Correos: Clasifica correos electrónicos utilizando un modelo de Machine Learning.
- Integración con Transformers: Utiliza modelos preentrenados de la biblioteca transformers.
- CORS habilitado: Permite solicitudes desde diferentes dominios, facilitando la integración con frontends.

# 🛠️ Tecnologías Utilizadas
- Flask: Microframework web para Python.
- Transformers: Biblioteca de modelos de Machine Learning de Hugging Face.
- Flask-CORS: Extensión para habilitar CORS en Flask.


# 📁 Estructura del Proyecto
```
backend-flask-ml-correos/
├── model/
│  ├── config.json
│  ├── model.safetensors
│  └── tokenizer_config.json
├── main.py
├── requirements.txt
├── gunicorn.conf.py
├── build.sh
├── start.sh
└── README.md
```



# ⚙️ Configuración y Ejecución en Entorno Local
1. Clonar el Repositorio
```
git clone https://github.com/YamilAyma/backend-flask-ml-correos.git
cd backend-flask-ml-correos
```

2. Crear y Activar un **Entorno Virtual**
```
python -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate
```


3. Instalar Dependencias
```
pip install -r requirements.txt
```

4. Ejecutar la Aplicación
```
python main.py
```

La aplicación estará disponible en http://127.0.0.1:5000/.


# 📬 Endpoints Disponibles
POST /predict: Recibe datos de entrada JSON con ùnicamente un valor a enviar ("email") y devuelve la predicción del modelo.


# 📝 Notas Adicionales
Asegúrate de que los archivos del modelo (config.json, model.safetensors, tokenizer_config.json) estén correctamente ubicados en la carpeta model/.

**Este backend está configurado para su despliegue en Render, pero las instrucciones proporcionadas aquí están adaptadas para su ejecución en un entorno local.**

Para pruebas y desarrollo, se recomienda utilizar el entorno local antes de proceder al despliegue en producción.


---
# Acerca del modelo 🤖
** ⚙ config.json**: Este archivo contiene la configuración del modelo, incluyendo la arquitectura, el número de capas, el tamaño de los embeddings, etc. Es esencial para que la librería transformers pueda cargar el modelo correctamente.

**🔢 model.safetensors**: Este archivo contiene los pesos del modelo, es decir, los valores numéricos que el modelo ha aprendido durante el entrenamiento. La extensión .safetensors indica que los pesos están guardados en un formato seguro y eficiente.

**⚙▶🔢 tokenizer_config.json**: Este archivo contiene información sobre cómo se tokeniza el texto de entrada, incluyendo el vocabulario, los tokens especiales y otros parámetros de configuración.

**📗 tokenizer.json**: Contiene toda la configuración necesaria para tokenizar el texto.

**📚 vocab.txt**: Este archivo contiene el vocabulario del tokenizador, es decir, la lista de todas las palabras y subpalabras que el tokenizador reconoce. Si estás usando un tokenizador más avanzado, es posible que tengas otros archivos de vocabulario en lugar de vocab.txt.

**ℹ special_tokens_map.json**: Este archivo define los tokens especiales que utiliza el tokenizador, como el token de inicio de secuencia ([CLS]), el token de fin de secuencia ([SEP]), el token de relleno ([PAD]) y el token de desconocido ([UNK]).
