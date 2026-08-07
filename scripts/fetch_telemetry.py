import os
import re
import requests
from datetime import datetime

API_KEY = os.environ.get('SHORT_IO_API_KEY')
LINK_ID = os.environ.get('SHORT_IO_LINK_ID')  # ex: link_73xm_...
README_PATH = 'README.md'

if not API_KEY or not LINK_ID:
    print("Erro: Variáveis de ambiente SHORT_IO_API_KEY e SHORT_IO_LINK_ID não configuradas.")
    exit(1)

headers = {'Authorization': API_KEY, 'accept': 'application/json'}
url = f"https://statistics.short.io/statistics/link/{LINK_ID}?period=total&tz=UTC"

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
    clicks = data.get('totalClicks', 0)
    print(f"Sucesso: cliques acumulados capturados = {clicks}")
except requests.exceptions.RequestException as e:
    print(f"Erro na Statistics API do Short.io: {e}")
    exit(1)

try:
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    timestamp = datetime.now().strftime('%d/%m/%Y às %H:%M')
    new_stats_block = f"📊 **Telemetria de Impacto:** {clicks} adesões confirmadas via Short.io (Atualizado em {timestamp})"

    pattern = r'(<!-- TELEMETRY_START -->\r?\n)(.*?)(\r?\n<!-- TELEMETRY_END -->)'
    replacement = r'\1' + new_stats_block + r'\3'

    if '<!-- TELEMETRY_START -->' in content and '<!-- TELEMETRY_END -->' in content:
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(README_PATH, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("README.md atualizado com sucesso.")
    else:
        print("Aviso: Marcadores de telemetria não encontrados no README.md.")
except Exception as e:
    print(f"Erro ao manipular o README.md: {e}")
    exit(1)