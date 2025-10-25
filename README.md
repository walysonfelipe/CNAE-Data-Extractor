# 🗂️ CNAE Data Extractor (IBGE API → CSV)

Um script Python que consome a **API oficial do IBGE** e gera automaticamente múltiplos arquivos **CSV** contendo a estrutura completa do **CNAE — Classificação Nacional de Atividades Econômicas**, organizada em níveis hierárquicos.

---

## 🚀 Visão Geral

Este script conecta-se à [API pública do IBGE](https://servicodados.ibge.gov.br/api/docs/cnae?versao=2), baixa todas as subclasses de atividades econômicas e gera automaticamente **arquivos CSV limpos e estruturados** para análise, integração em sistemas ou uso em planilhas.

---

## 📦 Estrutura dos Arquivos Gerados

Ao executar o script, serão criados **6 arquivos CSV** no diretório atual:

| Arquivo | Descrição |
|----------|------------|
| `cnae_secoes.csv` | Lista de **Seções** (nível mais alto — ex: Agricultura, Indústria, Comércio) |
| `cnae_divisoes.csv` | Lista de **Divisões** dentro das Seções |
| `cnae_grupos.csv` | Lista de **Grupos** dentro das Divisões |
| `cnae_classes.csv` | Lista de **Classes** dentro dos Grupos |
| `cnae_subclasses.csv` | Lista de **Subclasses** (nível mais detalhado — ex: 0111300 – Cultivo de arroz) |
| `cnae_completo.csv` | Arquivo consolidado com todos os níveis hierárquicos e descrições |

---

## 🧰 Exemplo de Saída (`cnae_completo.csv`)

| secao_id | secao_descricao | divisao_id | divisao_descricao | grupo_id | grupo_descricao | classe_id | classe_descricao | subclasse_id | subclasse_descricao |
|-----------|----------------|-------------|-------------------|-----------|------------------|------------|-------------------|---------------|----------------------|
| A | Agricultura, pecuária, produção florestal, pesca e aquicultura | 01 | Agricultura, pecuária e serviços relacionados | 01 | Produção agrícola | 01113 | Cultivo de cereais | 0111300 | Cultivo de arroz |
| A | Agricultura, pecuária, produção florestal, pesca e aquicultura | 01 | Agricultura, pecuária e serviços relacionados | 01 | Produção agrícola | 01120 | Cultivo de cana-de-açúcar | 0112001 | Cultivo de cana para fabricação de açúcar |

---

## 🧑‍💻 Como Executar

### 1️⃣ Pré-requisitos

- **Python 3.7+**
- Biblioteca `requests`

Instale a dependência:

```bash
pip install requests
```
### 2️⃣ Executar o script

Salve o arquivo como **`main.py`** e execute:

```bash
python3 main.py
```

### 3️⃣ Saída esperada

```bash
🚀 Iniciando importação dos CNAEs do IBGE...
📥 Baixando dados da API do IBGE...
✅ cnae_secoes.csv salvo (21 registros)
✅ cnae_divisoes.csv salvo (87 registros)
✅ cnae_grupos.csv salvo (285 registros)
✅ cnae_classes.csv salvo (672 registros)
✅ cnae_subclasses.csv salvo (1301 registros)
✅ cnae_completo.csv salvo (1301 registros)

🏁 Todos os arquivos CSV foram gerados com sucesso!
```

### 🧩 Estrutura Interna

Cada linha do JSON do IBGE é convertida em registros tabulares, mantendo as chaves hierárquicas:

```text
Seção → Divisão → Grupo → Classe → Subclasse
```

### 🔗 Fonte Oficial

📚 **IBGE – API de CNAE v2**  
[https://servicodados.ibge.gov.br/api/docs/cnae?versao=2](https://servicodados.ibge.gov.br/api/docs/cnae?versao=2)

### ✨ Autor

**Desenvolvido por Walyson**  
💡 Script Python adaptado e otimizado para automação e transparência de dados públicos.
