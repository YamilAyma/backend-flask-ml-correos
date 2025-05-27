# Servicio de modelo de Machine Learning para la clasificación de correos
---


# Acerca del modelo 🤖
**config.json**: Este archivo contiene la configuración del modelo, incluyendo la arquitectura, el número de capas, el tamaño de los embeddings, etc. Es esencial para que la librería transformers pueda cargar el modelo correctamente.

**model.safetensors**: Este archivo contiene los pesos del modelo, es decir, los valores numéricos que el modelo ha aprendido durante el entrenamiento. La extensión .safetensors indica que los pesos están guardados en un formato seguro y eficiente.

**tokenizer_config.json**: Este archivo contiene información sobre cómo se tokeniza el texto de entrada, incluyendo el vocabulario, los tokens especiales y otros parámetros de configuración.

**tokenizer.json**: Contiene toda la configuración necesaria para tokenizar el texto.

**vocab.txt**: Este archivo contiene el vocabulario del tokenizador, es decir, la lista de todas las palabras y subpalabras que el tokenizador reconoce. Si estás usando un tokenizador más avanzado, es posible que tengas otros archivos de vocabulario en lugar de vocab.txt.

**special_tokens_map.json**: Este archivo define los tokens especiales que utiliza el tokenizador, como el token de inicio de secuencia ([CLS]), el token de fin de secuencia ([SEP]), el token de relleno ([PAD]) y el token de desconocido ([UNK]).