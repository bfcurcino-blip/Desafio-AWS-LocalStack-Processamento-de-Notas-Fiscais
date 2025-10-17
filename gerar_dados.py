
import json
import random
from datetime import datetime, timedelta
from random import choice

def random_date():
    today = datetime.today()
    days_ago = random.randint(1, 30)
    random_date = today - timedelta(days=days_ago)
    return random_date.strftime("%Y-%m-%d")

# Clientes fictícios
clientes = ["João Silva", "Maria Oliveira", "Carlos Santos", "Ana Costa", "Pedro Lima"]

# Gerar registros
registros = []
for i in range(10):
    registro = {
        "id": f"NF-{i+1}",
        "cliente": choice(clientes),
        "valor": round(random.uniform(100.0, 5000.0), 2),
        "data_emissao": random_date()
    }
    registros.append(registro)

# Salvar no arquivo JSON
with open("notas_fiscais_2025.json", "w", encoding="utf-8") as f:
    json.dump(registros, f, indent=4, ensure_ascii=False)

print("✅ Arquivo 'notas_fiscais_2025.json' gerado com sucesso!")
