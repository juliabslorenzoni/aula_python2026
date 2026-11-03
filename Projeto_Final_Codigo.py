import sys
import os
import subprocess

# --- EXECUTADOR AUTOMÁTICO (Permite rodar pelo botão Play do PyCharm) ---
if __name__ == "__main__" and not os.environ.get("STREAMLIT_RUNNING"):
    os.environ["STREAMLIT_RUNNING"] = "true"
    subprocess.run([sys.executable, "-m", "streamlit", "run", __file__])
    sys.exit()

import json
import pandas as pd
import streamlit as st
from datetime import datetime

# Configuração da página Web
st.set_page_config(page_title="Minha Agenda Web", page_icon="📅", layout="wide")

ARQUIVO_AGENDA = 'agenda_banco.json'


# --- FUNÇÃO DE COMPATIBILIDADE PARA O RERUN ---
def reiniciar_app():
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()


# --- FUNÇÕES DE DADOS ---
def carregar_agenda():
    if os.path.exists(ARQUIVO_AGENDA):
        with open(ARQUIVO_AGENDA, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def salvar_agenda(agenda):
    with open(ARQUIVO_AGENDA, 'w', encoding='utf-8') as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)


# Carrega os dados na sessão do Streamlit
if 'tarefas' not in st.session_state:
    st.session_state['tarefas'] = carregar_agenda()

tarefas = st.session_state['tarefas']


# --- FUNÇÃO DE ALERTAS ---
def exibir_alertas():
    hoje = datetime.now().date()
    tem_alerta = False
    for t in tarefas:
        if not t['concluida']:
            data_limite = datetime.strptime(t['data_entrega'], "%Y-%m-%d").date()
            dias_restantes = (data_limite - hoje).days

            if dias_restantes < 0:
                st.error(f"🚨 ATRASADA: '{t['titulo']}' ({t['disciplina']}) venceu há {abs(dias_restantes)} dia(s)!")
                tem_alerta = True
            elif 0 <= dias_restantes <= 3:
                st.warning(f"⚠️ PRÓXIMA: '{t['titulo']}' ({t['disciplina']}) vence em {dias_restantes} dia(s)!")
                tem_alerta = True

    if not tem_alerta and tarefas:
        st.success("Tudo em dia! Nenhuma tarefa atrasada ou para os próximos 3 dias.")


# --- MENU LATERAL ---
st.sidebar.title("Navegação")
menu = st.sidebar.radio("Escolha uma opção:",
                        ["🏠 Dashboard e Alertas",
                         "➕ Adicionar Tarefa",
                         "📋 Lista e Filtros",
                         "⚙️ Gerenciar Tarefas"]
                        )

# --- PÁGINA 1: DASHBOARD ---
if menu == "🏠 Dashboard e Alertas":
    st.title("Visão Geral")
    st.markdown("Acompanhe os prazos e pendências.")
    exibir_alertas()

    col1, col2 = st.columns(2)
    pendentes = len([t for t in tarefas if not t['concluida']])
    concluidas = len(tarefas) - pendentes
    col1.metric("Tarefas Pendentes", pendentes)
    col2.metric("Tarefas Concluídas", concluidas)

# --- PÁGINA 2: ADICIONAR TAREFA ---
elif menu == "➕ Adicionar Tarefa":
    st.title("Cadastrar Nova Tarefa")

    with st.form("form_nova_tarefa"):
        titulo = st.text_input("Título da Tarefa")
        disciplina = st.text_input("Tipo / Disciplina (ex: Cálculo, Python, Trabalho)")
        data_entrega = st.date_input("Data de Entrega")

        submit = st.form_submit_button("Salvar Tarefa")

        if submit:
            if titulo and disciplina:
                nova_tarefa = {
                    "titulo": titulo,
                    "disciplina": disciplina,
                    "data_entrega": data_entrega.strftime("%Y-%m-%d"),
                    "concluida": False
                }
                tarefas.append(nova_tarefa)
                salvar_agenda(tarefas)
                st.success(f"Tarefa '{titulo}' cadastrada com sucesso!")
            else:
                st.error("Por favor, preencha o título e a disciplina.")

# --- PÁGINY 3: LISTA E FILTROS ---
elif menu == "📋 Lista e Filtros":
    st.title("Quadro de Tarefas")

    if not tarefas:
        st.info("Nenhuma tarefa cadastrada ainda.")
    else:
        df = pd.DataFrame(tarefas)

        col1, col2 = st.columns(2)
        filtro_status = col1.selectbox("Status", ["Todas", "Pendentes", "Concluídas"])

        lista_disciplinas = ["Todas"] + df['disciplina'].unique().tolist()
        filtro_disciplina = col2.selectbox("Filtrar por Disciplina", lista_disciplinas)

        if filtro_status == "Pendentes":
            df = df[df['concluida'] == False]
        elif filtro_status == "Concluídas":
            df = df[df['concluida'] == True]

        if filtro_disciplina != "Todas":
            df = df[df['disciplina'] == filtro_disciplina]

        if not df.empty:
            df['Status'] = df['concluida'].apply(lambda x: "✅ Concluída" if x else "⏳ Pendente")
            df_visual = df[['titulo', 'disciplina', 'data_entrega', 'Status']]
            df_visual.columns = ["Título", "Disciplina", "Data de Entrega", "Status"]

            st.dataframe(df_visual)
        else:
            st.warning("Nenhuma tarefa encontrada com os filtros atuais.")

# --- PÁGINA 4: GERENCIAR (Editar/Excluir/Concluir) ---
elif menu == "⚙️ Gerenciar Tarefas":
    st.title("Gerenciar e Editar")

    if not tarefas:
        st.info("Nenhuma tarefa cadastrada.")
    else:
        opcoes_tarefas = [f"{i} - {t['titulo']} ({t['data_entrega']})" for i, t in enumerate(tarefas)]
        escolha = st.selectbox("Selecione a tarefa que deseja modificar:", opcoes_tarefas)

        idx = int(escolha.split(" - ")[0])
        tarefa_alvo = tarefas[idx]

        st.markdown("---")

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if not tarefa_alvo['concluida']:
                if st.button("✅ Marcar como Concluída"):
                    tarefas[idx]['concluida'] = True
                    salvar_agenda(tarefas)
                    reiniciar_app()
            else:
                if st.button("⏳ Reverter para Pendente"):
                    tarefas[idx]['concluida'] = False
                    salvar_agenda(tarefas)
                    reiniciar_app()

        with col_btn2:
            if st.button("🗑️ Excluir Tarefa"):
                tarefas.pop(idx)
                salvar_agenda(tarefas)
                reiniciar_app()

        st.markdown("### Editar Informações")
        with st.form("form_edicao"):
            novo_titulo = st.text_input("Título", value=tarefa_alvo['titulo'])
            nova_disc = st.text_input("Disciplina", value=tarefa_alvo['disciplina'])

            data_atual = datetime.strptime(tarefa_alvo['data_entrega'], "%Y-%m-%d").date()
            nova_data = st.date_input("Data de Entrega", value=data_atual)

            if st.form_submit_button("Salvar Edição"):
                tarefas[idx]['titulo'] = novo_titulo
                tarefas[idx]['disciplina'] = nova_disc
                tarefas[idx]['data_entrega'] = nova_data.strftime("%Y-%m-%d")
                salvar_agenda(tarefas)
                st.success("Tarefa editada com sucesso!")
                reiniciar_app()