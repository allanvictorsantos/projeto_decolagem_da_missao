#!/usr/bin/env python3
import pandas as pd

# Carregar dados
dados = pd.read_csv('telemetria_missao.csv')

capacidade_total_kwh = 1000  # capacidade total da bateria da nave
consumo_decolagem_kwh = 350  # consumo estimado para a decolagem
perda_percentual = 0.05  # perda percentual de energia durante a decolagem

# Criar função de verificação para cada registro
def verificar_registro(row):
    criterios_nomes = [
        'Temp Int (°C)',
        'Temp Ext (°C)',
        'Integridade Estrutural',
        'Energia (%)',
        'Energia para Decolagem (KWh)',
        'Pressão (PSI)',
        'Módulos Críticos'
    ]
    criterios = [
        row['temperatura_interna_celsius'] >= 15 and row['temperatura_interna_celsius'] <= 28,
        row['temperatura_externa_celsius'] >= -50 and row['temperatura_externa_celsius'] <= 60,
        row['integridade_estrutural'] == True,
        row['nivel_energia_percentual'] >= 60 and row['nivel_energia_percentual'] <= 100,
        row['energia_disponivel_kwh'] >= consumo_decolagem_kwh,
        row['pressao_tanques_psi'] >= 80 and row['pressao_tanques_psi'] <= 150,
        row['status_modulos_criticos'] == True
    ]
    
    falhas = [nome for nome, criterio in zip(criterios_nomes, criterios) if not criterio]
    
    decisao = "PRONTO PARA DECOLAR" if all(criterios) else "DECOLAGEM ABORTADA"
    falhas_str = ', '.join(falhas) if falhas else 'Nenhum'
    
    return {'decisao': decisao, 'falhas': falhas_str}

# Calcular energia antes de verificar cada registro
dados['energia_atual_kwh'] = (dados['nivel_energia_percentual'] / 100) * capacidade_total_kwh
dados['energia_disponivel_kwh'] = dados['energia_atual_kwh'] * (1 - perda_percentual)
dados['perda_energetica_kwh'] = dados['energia_atual_kwh'] * perda_percentual

# Criar coluna de decisão
dados['resultado'] = dados.apply(verificar_registro, axis=1)
dados['decisao'] = dados['resultado'].apply(lambda x: x['decisao'])
dados['falhas'] = dados['resultado'].apply(lambda x: x['falhas'])

# Contar aprovados
aprovados = sum(dados['decisao'] == "PRONTO PARA DECOLAR")
total = len(dados)

# Cabeçalho
print("\n" + "="*200)
print(" "*75 + "SISTEMA DE VERIFICAÇÃO DE DECOLAGEM DA MISSÃO")
print("="*200)

# Estatísticas resumidas
print(f"\nResumo:")
print(f"  Total de registros analisados: {total}")
print(f"  ✓ Pronto para decolar: {aprovados} ({100*aprovados/total:.1f}%)")
print(f"  ✗ Decolagem abortada: {total-aprovados} ({100*(total-aprovados)/total:.1f}%)")

# Exibir tabela completa
print(f"\n{'-'*200}")
print("Detalhamento de todos os registros:")
print(f"{'-'*200}\n")

# Formatar dados para exibição
tabela = dados[[
    'temperatura_interna_celsius', 
    'temperatura_externa_celsius', 
    'integridade_estrutural', 
    'nivel_energia_percentual', 
    'energia_atual_kwh', 
    'energia_disponivel_kwh', 
    'perda_energetica_kwh',
    'pressao_tanques_psi', 
    'status_modulos_criticos', 
    'decisao', 
    'falhas'
    ]].copy()

tabela.columns = [
        'Temp Int (°C)', 
        'Temp Ext (°C)', 
        'Integridade Estrutural', 
        'Energia (%)', 
        'Energia Atual (KWh)', 
        'Energia Disponível (KWh)', 
        'Perda Energética (KWh)', 
        'Pressão (PSI)', 
        'Módulos Críticos', 
        'Decisão', 
        'Falhas'
    ]

# Usar pandas display com formatting
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

print(tabela.to_string())

print(f"\n{'='*200}\n")
