import os
import re
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

API_KEY = os.environ.get('SHORT_IO_API_KEY')
LINK_ID = os.environ.get('SHORT_IO_LINK_ID')
README_PATH = 'README.md'
CSV_PATH = 'assets/telemetry_history.csv'
CHART_PATH = 'assets/telemetry_chart.png'

# 1. Buscar dados da API
headers = {'Authorization': API_KEY, 'accept': '*/*'}
url = f"https://statistics.short.io/statistics/link/{LINK_ID}?period=total&tz=UTC"

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
    clicks = data.get('totalClicks', 0)
    print(f"Sucesso: Total de cliques capturado = {clicks}")
except requests.exceptions.RequestException as e:
    print(f"Erro na API: {e}")
    exit(1)

# 2. Gerenciar Histórico (CSV)
today = datetime.now().strftime('%Y-%m-%d')
new_row = {'date': today, 'clicks': clicks}

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
    # Evita duplicatas se rodar mais de uma vez no mesmo dia
    if today not in df['date'].values:
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
else:
    df = pd.DataFrame([new_row])

df.to_csv(CSV_PATH, index=False)

# 3. Gerar Gráfico (Matplotlib)
df['date'] = pd.to_datetime(df['date'])
plt.style.use('dark_background') # Combina com o tema Nord do PDF
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(df['date'], df['clicks'], marker='o', linestyle='-', color='#28C86F', linewidth=2, markersize=6)
ax.fill_between(df['date'], df['clicks'], color='#28C86F', alpha=0.3)

ax.set_title('Evolução de Adesões (Green Computing Araras)', color='white', fontsize=14, pad=15)
ax.set_xlabel('Data', color='white')
ax.set_ylabel('Cliques Confirmados', color='white')
ax.grid(True, linestyle='--', alpha=0.3)

# Formatação do eixo X
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHART_PATH, dpi=100, facecolor='#161920') # Fundo escuro igual ao PDF
plt.close()

# 4. Atualizar README
try:
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    timestamp = datetime.now().strftime('%d/%m/%Y às %H:%M')
    new_stats_block = f"📊 **Telemetria de Impacto:** {clicks} adesões confirmadas via Short.io (Atualizado em {timestamp})"

    pattern = r'(<!-- TELEMETRY_START -->\n)(.*?)(\n<!-- TELEMETRY_END -->)'
    replacement = r'\1' + new_stats_block + r'\3'

    if '<!-- TELEMETRY_START -->' in content:
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(README_PATH, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("README e Gráfico atualizados com sucesso.")
    else:
        print("Aviso: Marcadores de telemetria não encontrados no README.")
except Exception as e:
    print(f"Erro ao manipular arquivos: {e}")
    exit(1)