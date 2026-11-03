import pandas as pd

#DESAFIO 1
arquivo = pd.ExcelFile(r"C:\Users\julia\Downloads\1bf41aa8-c68e-4c30-857f-8123b5962bba.xlsx")

alunos = pd.read_excel(arquivo,"alunos")
disciplinas = pd.read_excel(arquivo,"disciplinas")
matriculas_sem1 = pd.read_excel(arquivo,"matriculas_sem1")
matriculas_sem2 = pd.read_excel(arquivo,"matriculas_sem2")

df = pd.merge(alunos, matriculas_sem1, on="matricula", how="left")
df2 = pd.merge(alunos, matriculas_sem2, on="matricula", how="left")
df_final = pd.concat([df,df2],axis=0)
df_final2 = pd.merge(df_final,disciplinas, how="inner")

#print(df_final)
#print(df.groupby("matricula").count())
#print(df_final2)

#DESAFIO 2
cidades = pd.read_excel(arquivo,"cidades")
df3 = pd.merge(alunos, cidades, on="cidade", how="inner")
#print(df3)
aluno_por_cidade = df3["cidade"].value_counts()
#print(aluno_por_cidade)
cidade_com_mais_alunos = (aluno_por_cidade.idxmax())
#print(cidade_com_mais_alunos)

#DESAFIO 3
df_final3 = pd.concat([matriculas_sem1,matriculas_sem2],axis=0)
print(df_final3)
disciplina_mais_matricula = df_final3["cod_disc"].value_counts()
print(disciplina_mais_matricula)
df_comparacao = matriculas_sem1["cod_disc"].value_counts(), matriculas_sem2["cod_disc"].value_counts()
print(df_comparacao)
df_qtdmatricula1 = pd.merge(matriculas_sem1, matriculas_sem2, on="matricula", how="inner")
print(df_qtdmatricula1)
print("ANÁLISE: Os dados revela que todos os alunos foram matriculados em pelo menos duas disciplinas, também vemos que as disciplinas que tiveram mais matrículas no primeiro semestra, tiveram menos matrículas no segundo semestre. Percebe-se que a maioria dos alunos passaram nas matérias.")