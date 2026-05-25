# ⚙️ TheLook Financial Engine

Motor de processamento e limpeza de dados financeiros focado em garantir a integridade dos dados antes da ingestão no Data Warehouse.

## 🚀 Tecnologias Utilizadas
- **Python 3.9** (Lógica principal)
- **Pytest** (Testes Unitários e Edge Cases)
- **Docker** (Conteinerização e Infraestrutura Efêmera)

## 🧠 Funcionalidades Atuais (Fase 1)
A classe `TheLookCleaner` possui o método de limpeza e formatação de preços:
- Converte strings com padrão BR (vírgula) para padrão US (ponto).
- Garante o retorno matemático como `float`.
- Força o arredondamento em 2 casas decimais.
- Trava e alerta (lança `ValueError`) ao receber dados corrompidos ou em formato de texto não numérico.

## 🛠️ Como rodar o projeto localmente

**Opção 1: Usando Python Virtual Environment**
```bash
source venv/bin/activate
python -m pytest