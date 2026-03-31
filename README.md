# 🚀 Projeto Decolagem da Missão (Aurora Siger)

## 📋 Explicação do Projeto
Este projeto analisa a telemetria da missão espacial Aurora Siger e executa verificações rigorosas de pré-decolagem usando o notebook `verificacao_decolagem_notebook.ipynb`. 

O algoritmo processa o arquivo `telemetria_missao.csv` e avalia dados vitais de temperatura, pressão dos tanques, níveis de energia e integridade estrutural. Cruzando esses dados com parâmetros de segurança, o sistema automatizado decide se a espaçonave está "PRONTA PARA DECOLAR" ou se a missão deve ser "ABORTADA".

---

## 💻 Prints da Execução

*(Substitua esta linha pela imagem/print da tela do seu código rodando e mostrando a tabela de falhas e aprovados)*
![Print da Execução do Código](INSIRA_O_LINK_DA_IMAGEM_AQUI.png)

---

## ⚙️ Instruções de Execução do Código

Para rodar este projeto e simular a verificação de telemetria na sua máquina, siga os passos abaixo:

### Pré-requisitos
1. Python 3.8+ instalado.
2. Dependências necessárias: `pandas` e `jupyter`.

### Instalação do ambiente (Recomendado: virtualenv)
Abra o seu terminal e execute os comandos abaixo em sequência:

```bash
# Entre na pasta do projeto
cd /projeto_decolagem_da_missao

# Crie o ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual (Se estiver no Windows, use: .venv\Scripts\activate)
source .venv/bin/activate

# Atualize o pip e instale as dependências
pip install --upgrade pip
pip install pandas jupyter
