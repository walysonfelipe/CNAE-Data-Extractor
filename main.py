#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera múltiplos arquivos CSV contendo os CNAEs (IBGE)
- cnae_secoes.csv
- cnae_divisoes.csv
- cnae_grupos.csv
- cnae_classes.csv
- cnae_subclasses.csv
- cnae_completo.csv
Fonte: https://servicodados.ibge.gov.br/api/docs/cnae?versao=2
"""

import csv
import requests

API_URL = "https://servicodados.ibge.gov.br/api/v2/cnae/subclasses"


def baixar_dados():
    print("📥 Baixando dados da API do IBGE...")
    response = requests.get(API_URL, timeout=60)
    response.raise_for_status()
    return response.json()


def gerar_csv(nome_arquivo, colunas, dados):
    """Salva lista de dicionários em CSV"""
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(dados)
    print(f"✅ {nome_arquivo} salvo ({len(dados)} registros)")


def gerar_tabelas(dados):
    secoes, divisoes, grupos, classes, subclasses, completo = (
        {}, {}, {}, {}, {}, []
    )

    for item in dados:
        secao = item["classe"]["grupo"]["divisao"]["secao"]
        divisao = item["classe"]["grupo"]["divisao"]
        grupo = item["classe"]["grupo"]
        classe = item["classe"]

        # Extrai cada nível, evitando duplicatas (usando dicionários)
        secoes[secao["id"]] = {
            "id": secao["id"],
            "descricao": secao["descricao"],
        }

        divisoes[divisao["id"]] = {
            "id": divisao["id"],
            "descricao": divisao["descricao"],
            "secao_id": secao["id"],
        }

        grupos[grupo["id"]] = {
            "id": grupo["id"],
            "descricao": grupo["descricao"],
            "divisao_id": divisao["id"],
            "secao_id": secao["id"],
        }

        classes[classe["id"]] = {
            "id": classe["id"],
            "descricao": classe["descricao"],
            "grupo_id": grupo["id"],
            "divisao_id": divisao["id"],
            "secao_id": secao["id"],
        }

        subclasses[item["id"]] = {
            "id": item["id"],
            "descricao": item["descricao"],
            "classe_id": classe["id"],
            "grupo_id": grupo["id"],
            "divisao_id": divisao["id"],
            "secao_id": secao["id"],
        }

        completo.append({
            "secao_id": secao["id"],
            "secao_descricao": secao["descricao"],
            "divisao_id": divisao["id"],
            "divisao_descricao": divisao["descricao"],
            "grupo_id": grupo["id"],
            "grupo_descricao": grupo["descricao"],
            "classe_id": classe["id"],
            "classe_descricao": classe["descricao"],
            "subclasse_id": item["id"],
            "subclasse_descricao": item["descricao"],
        })

    # Gera os CSVs individuais
    gerar_csv("cnae_secoes.csv", ["id", "descricao"], secoes.values())
    gerar_csv("cnae_divisoes.csv", ["id", "descricao", "secao_id"], divisoes.values())
    gerar_csv("cnae_grupos.csv", ["id", "descricao", "divisao_id", "secao_id"], grupos.values())
    gerar_csv("cnae_classes.csv", ["id", "descricao", "grupo_id", "divisao_id", "secao_id"], classes.values())
    gerar_csv("cnae_subclasses.csv", ["id", "descricao", "classe_id", "grupo_id", "divisao_id", "secao_id"], subclasses.values())
    gerar_csv("cnae_completo.csv", [
        "secao_id", "secao_descricao",
        "divisao_id", "divisao_descricao",
        "grupo_id", "grupo_descricao",
        "classe_id", "classe_descricao",
        "subclasse_id", "subclasse_descricao"
    ], completo)


def main():
    print("🚀 Iniciando importação dos CNAEs do IBGE...")
    dados = baixar_dados()
    gerar_tabelas(dados)
    print("\n🏁 Todos os arquivos CSV foram gerados com sucesso!")


if __name__ == "__main__":
    main()
