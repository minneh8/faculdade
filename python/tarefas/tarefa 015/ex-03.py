# Exercício 3 - Cadastro de candidatos MYKROSOFT

import os

ARQUIVO = "CANDIDATOS.TXT"

def carregar_candidatos():
    candidatos = []
    if not os.path.exists(ARQUIVO):
        return candidatos
    with open(ARQUIVO, "r") as f:
        linhas = f.readlines()
    i = 0
    while i < len(linhas):
        if i + 4 < len(linhas):
            candidato = {
                "cpf": linhas[i].strip(),
                "nome": linhas[i + 1].strip(),
                "curso": linhas[i + 2].strip(),
                "status": linhas[i + 3].strip(),
                "datanascimento": linhas[i + 4].strip()
            }
            candidatos.append(candidato)
        i += 5
    return candidatos

def salvar_candidatos(candidatos):
    with open(ARQUIVO, "w") as f:
        for c in candidatos:
            f.write(f"{c['cpf']}\n{c['nome']}\n{c['curso']}\n{c['status']}\n{c['datanascimento']}\n")

def cadastrar(candidatos):
    print("\n--- CADASTRO DE CANDIDATO ---")
    cpf = input("CPF: ").strip()
    for c in candidatos:
        if c["cpf"] == cpf:
            print("CPF já cadastrado!")
            return
    nome = input("Nome: ").strip()
    curso = input("Curso: ").strip()
    print("Status: 1-GRADUADO  2-ALUNO SUPERIOR  3-TÉCNICO")
    op = input("Escolha: ").strip()
    status = {"1": "GRADUADO", "2": "ALUNO SUPERIOR", "3": "TÉCNICO"}.get(op, "TÉCNICO")
    datanascimento = input("Data de Nascimento (DD/MM/AAAA): ").strip()
    candidatos.append({"cpf": cpf, "nome": nome, "curso": curso, "status": status, "datanascimento": datanascimento})
    salvar_candidatos(candidatos)
    print("Candidato cadastrado com sucesso!")

def consultar(candidatos):
    print("\n--- CONSULTA ---")
    print("1 - Por CPF\n2 - Por Nome\n3 - Por Curso\n4 - Por Status")
    op = input("Opção: ").strip()
    if op == "1":
        cpf = input("CPF: ").strip()
        resultado = [c for c in candidatos if c["cpf"] == cpf]
    elif op == "2":
        nome = input("Nome (parte): ").strip().lower()
        resultado = [c for c in candidatos if nome in c["nome"].lower()]
    elif op == "3":
        curso = input("Curso (parte): ").strip().lower()
        resultado = [c for c in candidatos if curso in c["curso"].lower()]
    elif op == "4":
        status = input("Status (GRADUADO/ALUNO SUPERIOR/TÉCNICO): ").strip().upper()
        resultado = [c for c in candidatos if c["status"] == status]
    else:
        print("Opção inválida.")
        return
    if not resultado:
        print("Nenhum candidato encontrado.")
    for c in resultado:
        print(f"\nCPF: {c['cpf']} | Nome: {c['nome']} | Curso: {c['curso']} | Status: {c['status']} | Nasc.: {c['datanascimento']}")

def deletar(candidatos):
    print("\n--- DELETAR CANDIDATO ---")
    cpf = input("CPF do candidato a deletar: ").strip()
    for c in candidatos:
        if c["cpf"] == cpf:
            candidatos.remove(c)
            salvar_candidatos(candidatos)
            print("Candidato removido com sucesso!")
            return
    print("Candidato não encontrado.")

def alterar(candidatos):
    print("\n--- ALTERAR CANDIDATO ---")
    cpf = input("CPF do candidato a alterar: ").strip()
    for c in candidatos:
        if c["cpf"] == cpf:
            print(f"Nome atual: {c['nome']}")
            novo_nome = input("Novo nome (Enter para manter): ").strip()
            if novo_nome:
                c["nome"] = novo_nome
            print(f"Curso atual: {c['curso']}")
            novo_curso = input("Novo curso (Enter para manter): ").strip()
            if novo_curso:
                c["curso"] = novo_curso
            print(f"Status atual: {c['status']}")
            print("1-GRADUADO  2-ALUNO SUPERIOR  3-TÉCNICO (Enter para manter)")
            op = input("Novo status: ").strip()
            if op:
                c["status"] = {"1": "GRADUADO", "2": "ALUNO SUPERIOR", "3": "TÉCNICO"}.get(op, c["status"])
            print(f"Data Nasc. atual: {c['datanascimento']}")
            nova_data = input("Nova data (Enter para manter): ").strip()
            if nova_data:
                c["datanascimento"] = nova_data
            salvar_candidatos(candidatos)
            print("Candidato alterado com sucesso!")
            return
    print("Candidato não encontrado.")

def main():
    candidatos = carregar_candidatos()
    while True:
        print("\n========= MYKROSOFT - CADASTRO =========")
        print("1 - Cadastrar\n2 - Consultar\n3 - Alterar\n4 - Deletar\n0 - Sair")
        op = input("Opção: ").strip()
        if op == "1":
            cadastrar(candidatos)
        elif op == "2":
            consultar(candidatos)
        elif op == "3":
            alterar(candidatos)
        elif op == "4":
            deletar(candidatos)
        elif op == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

main()