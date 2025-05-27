from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import logging

app = Flask(__name__)
CORS(app)

# Clases
clases = {
    0: "Legitima",
    1: "Fraude"
}

# Logging de monitoreo
logging.basicConfig(level=logging.ERROR,  
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 1. Cargar el modelo y el tokenizador
MODEL_PATH = "./model" 
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH) #Especifica que debe leer safetensors
    model.eval()  # Poner el modelo en modo de evaluación
    print("¡Modelo cargado exitosamente!")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

# Seleccionar el dispositivo (CPU o GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


# 2. Definir la función de predicción
def predict(text):
    # Tokenizar el texto
    inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)

    # Realizar la predicción (desactivar el cálculo del gradiente)
    with torch.no_grad():
        outputs = model(**inputs)

    # Obtener las probabilidades
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)

    # Obtener la clase predicha (0 para legítimo, 1 para fraude)
    predicted_class = torch.argmax(probabilities, dim=-1).item()

    return predicted_class, probabilities.tolist()[0]


@app.route("/")
def home():
    return jsonify({"mensaje": "Holaa"})

# 3. Definir la ruta de la API
@app.route('/predict', methods=['POST'])
def predict_email():
    try:
        # Obtener el texto del correo electrónico de la solicitud
        logger.info("Recibida solicitud de predicción")
        data = request.get_json(force=True)
        email_text = data['email']

        # Realizar la predicción
        predicted_class, probabilities = predict(email_text)

        # Crear la respuesta
        result = {
            'etiqueta_clase': clases.get(predicted_class, "desconocido"),
            'probabilidades': probabilities,
            'es_fraud': bool(predicted_class),  # Añadir una bandera booleana
            "porcentaje_clase": f"{probabilities[predicted_class]*100:.2f}" 
        }
        logger.info(f"Predicción exitosa: {result}")
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500