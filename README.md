# 🧮 Calculadora Científica em Python

Este projeto é uma **calculadora científica** criada em Python, com um **script de automação em shell (`.sh`)** para facilitar a execução no terminal Linux (WSL – Windows Subsystem for Linux).

---

## 📂 Arquivos do projeto

- `calculadora.py`: código principal da calculadora (operações básicas e científicas)
- `calculadora.sh`: script para executar a calculadora
- `comandos.txt`: comandos utilizados para tornar o script executável e rodá-lo

---

## ▶️ Como executar

### Requisitos:
- Ter o **Python 3** instalado
- Estar em um ambiente Linux (ou WSL no Windows)

### Passo a passo:

```bash
# 1. Torne o script executável:
chmod 744 calculadora.sh

# 2. Verifique as permissões (opcional):
ls -l calculadora.sh

# 3. Execute o script:
./calculadora.sh
