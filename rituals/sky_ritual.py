import random
from datetime import datetime

def perform_ritual():
    spirits = ["Ülgen", "Erlik", "Karakurt", "Umay", "Ay Dede"]
    selected = random.choice(spirits)
    return {
        "timestamp": datetime.now().isoformat(),
        "invoked_spirit": selected,
        "symbolic_weather": random.choice(["Güneş", "Fırtına", "Sis", "Kırağı"]),
        "meaning": f"{selected} ruhu çağrıldı, göksel bağlantı kuruldu."
    }
