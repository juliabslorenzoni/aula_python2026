import pandas as pd
import numpy as np
#ETAPA 1 - CONHECENDO A BASE:
arquivo = pd.read_excel(r"C:\Users\julia\OneDrive\Desktop\JULIA\LINGUAGENS DE PROGRAMAÇÃO\4ae91468-53a4-4b37-bda3-bc9c10b5c019.xlsx")

print("2. Primeiras 5 observações:")
print(arquivo.head(5))

linhas, colunas = arquivo.shape
print(f"3.1 Total de empresas: {linhas}\n3.2 Total de variáveis: {colunas}")

print("4. Lista de colunas")
print(arquivo.columns)

print("5 e 6. Tipo  de dados e valores ausentes")
print(arquivo.info())

print("Análise: Devemos verificar os valores ausentes (apagar linha ou algo assim) e verificar se o dado está correto (int, float, str)")

#ETAPA 2 - PRIMEIRO DIAGNÓSTICO DAS EMPRESAS
print("7. Estatística descritiva")
print(arquivo.describe())

receita_media = arquivo["Receita"].mean()
print(f"8. Receita média: {receita_media:,.2f}")

lucro_medio = arquivo["Lucro_Liquido"].mean()
print(f"9. Lucro médio: {lucro_medio:,.2f}")

empresa_maior_receita = arquivo.loc[arquivo["Receita"].idxmax()]
print(f"10. Empresa com maior receita: {empresa_maior_receita["Empresa"]}")

empresa_maior_lucro = arquivo.loc[arquivo["Lucro_Liquido"].idxmax()]
print(f"10. Empresa com maior lucro: {empresa_maior_lucro["Empresa"]}")

empresa_mais_funcs = arquivo.loc[arquivo["Funcionarios"].idxmax()]
print(f"10. Empresa com mais funcionários: {empresa_mais_funcs["Empresa"]}")

lucro_positivo = (arquivo["Lucro_Liquido"]> 0).sum()
print(f"11. Empresas com lucro positivo: {lucro_positivo}")

prejuizo = (arquivo["Lucro_Liquido"]< 0).sum()
print(f"12. Empresa com lucro negativo: {prejuizo}")

print("ANÁLISE: Não. A receita apresenta apenas a entrada bruta de dinheiro.")

#ETAPA 3 — INVESTIGANDO GRUPOS DE EMPRESAS
receita_media = arquivo["Receita"].mean()

empresas_receita_alta = arquivo[arquivo['Receita'] > receita_media]
print("15. Empresas com receita superior à média")
print(empresas_receita_alta[['Empresa', 'Receita']])
print(f"Total: {len(empresas_receita_alta)} empresas\n")

empresas_lucro_positivo = arquivo[arquivo['Lucro_Liquido'] > 0]
print("16. Empresas com lucro líquido positivo")
print(empresas_lucro_positivo[['Empresa', 'Lucro_Liquido']])
print(f"Total: {len(empresas_lucro_positivo)} empresas\n")

empresas_destaque = arquivo[(arquivo['Receita'] > receita_media) & (arquivo['Lucro_Liquido'] > 0)]
print("17. Empresas com receita > média E lucro positivo")
print(empresas_destaque[['Empresa', 'Receita', 'Lucro_Liquido']])
print(f"Total: {len(empresas_destaque)} empresas\n")

estado_escolhido = 'SP'
empresas_estado = arquivo[arquivo['Estado'] == estado_escolhido]
print(f"18. Empresas do estado {estado_escolhido}")
print(empresas_estado[['Empresa', 'Estado']])
print(f"Total: {len(empresas_estado)} empresas\n")

setor_escolhido = 'Tecnologia'
empresas_setor = arquivo[arquivo['Setor'] == setor_escolhido]
print(f"19. Empresas do setor {setor_escolhido}")
print(empresas_setor[['Empresa', 'Setor', 'Receita']])
print(f"Total: {len(empresas_setor)} empresas\n")

if not empresas_setor.empty:
    maior_rec_setor = empresas_setor.loc[empresas_setor['Receita'].idxmax()]
    print(f"20. Maior receita do setor {setor_escolhido}")
    print(f"Empresa: {maior_rec_setor['Empresa']} | Receita: {maior_rec_setor['Receita']:,.2f}")

print("ANÁLISE: O filtro 17 é o mais interessante pois isola empresas de alto porte (receita acima da média) que são comprovadamente eficientes e saudáveis (lucrativas), eliminando gigantes com prejuízo ou microempresas sem escala.")

#ETAPA 4 — CRIANDO NOVOS INDICADORES
arquivo['Margem_Liquida'] = arquivo['Lucro_Liquido'] / arquivo['Receita']

arquivo['Receita_por_Funcionario'] = arquivo['Receita'] / arquivo['Funcionarios']

condicoes_situacao = [
    arquivo['Lucro_Liquido'] > 0,
    arquivo['Lucro_Liquido'] < 0,
    arquivo['Lucro_Liquido'] == 0
]
valores_situacao = ['Lucro', 'Prejuízo', 'Equilíbrio']
arquivo['Situacao'] = np.select(condicoes_situacao, valores_situacao, default='Equilíbrio')

arquivo['Receita_Acima_Media'] = (arquivo['Receita'] > receita_media).astype(int)

maiores_margens = arquivo.nlargest(5, 'Margem_Liquida')
print("25. Top 5 Empresas por Margem Líquida")
print(maiores_margens[['Empresa', 'Margem_Liquida', 'Receita', 'Lucro_Liquido']])

maiores_rec_func = arquivo.nlargest(5, 'Receita_por_Funcionario')
print("\n26. Top 5 Empresas por Receita por Funcionário")
print(maiores_rec_func[['Empresa', 'Receita_por_Funcionario', 'Receita', 'Funcionarios']])

print("Análise: Não necessariamente, pois faturamento alto mede apenas a escala do negócio, enquanto a margem líquida mede a eficiência operacional em transformar cada real vendido em lucro real.")

#ETAPA 5 — O DESAFIO DA DIRETORIA
print("27 e 28: Selecionamos Margem Líquida acima da média (para garantir eficiência operacional), Receita por Funcionário acima da média (para avaliar a alta produtividade da equipe) e Situação igual a Lucro (para eliminar qualquer empresa deficitária da análise).")

media_margem = arquivo['Margem_Liquida'].mean()
media_rec_func = arquivo['Receita_por_Funcionario'].mean()

condicao_tripla = (
    (arquivo['Margem_Liquida'] > media_margem) &
    (arquivo['Receita_por_Funcionario'] > media_rec_func) &
    (arquivo['Situacao'] == 'Lucro')
)

arquivo['Selecionada'] = condicao_tripla.astype(int)

total_selecionadas = arquivo['Selecionada'].sum()
print(f"30. Total de empresas selecionadas: {total_selecionadas}\n")

colunas_exibicao = ['Empresa', 'Setor', 'Estado', 'Receita', 'Lucro_Liquido', 'Margem_Liquida', 'Selecionada']

empresas_filtradas = arquivo[arquivo['Selecionada'] == 1].copy()
tabela_final = empresas_filtradas[colunas_exibicao].sort_values(by='Margem_Liquida', ascending=False)

print("32 e 33. Tabela Final das Empresas Selecionadas (Ordenadas por Margem Líquida)")
print(tabela_final.to_string(index=False))

#ETAPA 6 — ENTREGA PARA O CLIENTE
df_selecionadas = arquivo[arquivo['Selecionada'] == 1].copy()

df_selecionadas.to_excel('empresas_selecionadas.xlsx', index=False)
print("Arquivo 'empresas_selecionadas.xlsx' gerado com sucesso!")

print("Conclusão Executiva: A análise comprovou que alta receita não garante saúde financeira, levando à seleção de um grupo de elite baseado em três critérios: Margem Líquida acima da média, Receita por Funcionário superior à média e Lucro Líquido positivo. As empresas selecionadas destacam-se pela excelente produtividade e eficiência operacional, com prioridade máxima de consultoria para as líderes em Margem Líquida por apresentarem a maior capacidade de conversão de vendas em retorno real.")
