import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    # Gemini 1.5 Pro es el estándar de oro actual para razonamiento
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-pro-latest")
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LEAN_SRC_DIR = os.path.join(BASE_DIR, "EuclideanBench")
    LOGS_DIR = os.path.join(BASE_DIR, "experiments", "logs")

    @staticmethod
    def validate():
        if not Config.GOOGLE_API_KEY:
            raise ValueError("❌ Error: GOOGLE_API_KEY no encontrada en .env")