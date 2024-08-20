import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import docker

# Configuração inicial
apis = [
    {"name": "Go", "url": "http://localhost:8081/"},
    {"name": "Python", "url": "http://localhost:8082/"},
    {"name": "Node.js", "url": "http://localhost:8083/"},
    {"name": "PHP (FastRoute)", "url": "http://localhost:8084/"},
    {"name": "Ruby", "url": "http://localhost:8085/"}
]

results = []

# Inicializar Docker client
client = docker.from_env()

# Função para rodar o benchmark
def run_benchmark(api_name, url):
    cmd = f"ab -n 10000 -c 100 {url}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    # Extraindo resultados
    output = result.stdout
    print(f"output for {api_name}: {output}")
    rps = float(output.split("Requests per second:")[1].split("[#/sec]")[0].strip())
    time_per_request = float(output.split("Time per request:")[1].split("[ms]")[0].strip())
    transfer_rate = float(output.split("Transfer rate:")[1].split("[Kbytes/sec]")[0].strip())
    
    return {
        "Language": api_name,
        "Requests per Second": rps,
        "Time per Request (ms)": time_per_request,
        "Transfer Rate (Kbytes/sec)": transfer_rate
    }

# Executar o benchmark para cada API
for api in apis:
    result = run_benchmark(api["name"], api["url"])
    results.append(result)

# Ordenar os resultados por RPS
results = sorted(results, key=lambda x: x["Requests per Second"], reverse=True)

# Criar DataFrame e exibir resultados
df = pd.DataFrame(results)
print(df)

# Reestruturar o DataFrame para gráfico de barras agrupadas
df_melted = pd.melt(df, id_vars='Language', var_name='Metric', value_name='Value')

# Geração do gráfico
plt.figure(figsize=(10, 6))
# metrics = ['Requests per Second', 'Time per Request (ms)', 'Transfer Rate (Kbytes/sec)']
metrics = ['Requests per Second']
colors = ['orange']

for idx, metric in enumerate(metrics):
    subset = df_melted[df_melted['Metric'] == metric]
    plt.barh(subset['Language'] + ' (' + metric + ')', subset['Value'], color=colors[idx], label=metric)

plt.title('Comparação de Desempenho das APIs por Métrica')
plt.xlabel('Valores')
plt.tight_layout()

# Salvar o gráfico como uma imagem
plt.savefig('comparacao_desempenho_apis_por_metrica.png')

# Mostrar o gráfico
plt.show()

# Opcional: Salvar DataFrame como CSV
df.to_csv('api_benchmark_results.csv', index=False)
