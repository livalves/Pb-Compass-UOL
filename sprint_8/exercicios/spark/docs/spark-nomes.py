from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, rand, col

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# 1 - Lendo arquivo, carregando dataframe e listando linhas
df_nomes = spark.read.csv("nomes_aleatorios.txt", encoding="UTF-8")
df_nomes.show(5)

# 2 - Verificando squema, renomeando coluna e listando 10 linhas
df_nomes.printSchema()
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()
df_nomes.show(10)

# 3 - Adicionando coluna Escolaridade e atribuindo valores
df_nomes = df_nomes.withColumn("Escolaridade", 
                               when((rand() < 0.33), "Fundamental")
                               .when((rand() <= 0.67), "Medio")
                               .otherwise("Superior"))

# 4 - Adicionando coluna Pais e atribuindo valores
paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador", "Guiana",
          "Guiana Francesa", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]
df_nomes = df_nomes.withColumn("Pais", 
                               when(rand() < 1/13, paises[0])
                               .when(rand() < 2/13, paises[1])
                               .when(rand() < 3/13, paises[2])
                               .when(rand() < 4/13, paises[3])
                               .when(rand() < 5/13, paises[4])
                               .when(rand() < 6/13, paises[5])
                               .when(rand() < 7/13, paises[6])
                               .when(rand() < 8/13, paises[7])
                               .when(rand() < 9/13, paises[8])
                               .when(rand() < 10/13, paises[9])
                               .when(rand() < 11/13, paises[10])
                               .when(rand() < 12/13, paises[11])
                               .otherwise(paises[12]))

# 5 - Adicionando coluna AnoNascimento e atribuindo valores
df_nomes = df_nomes.withColumn("AnoNascimento", 
                               (rand() * (2010 - 1945) + 1945).cast("int"))

# 6 - Selecionando pessoas que nasceram neste século e armazenando em outro dataframe
df_select = df_nomes.select("*").where(col("AnoNascimento") >= 2000)
df_select.show(10)

# 7 - Usando SparkSQL para resolução do processo n° 6 
df_nomes.createOrReplaceTempView("pessoas")
df_sql_select = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")
df_sql_select.show(10)

# 8 - Contando o número de pessoas da geração Millennials
df_millennials = df_nomes.select("*").where((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()
print(f"Quantidade de Millennials: {df_millennials}")

# 9 - Usando SparkSQL para resolução do processo n° 8
df_sql_millennials = spark.sql("SELECT count(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")
df_sql_millennials.show()

# 10 - Obtendo a quantidade de pessoas de cada país na geração Baby Boomers e ordenando pelo País e quantidade
consulta_sql_paises = """
SELECT
    Pais,
    CASE
        WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
        WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'G. X'
        WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
        ELSE 'G. Z'
    END AS Geracao,
    COUNT(*) AS Quantidade
FROM
    pessoas
GROUP BY
    Pais, Geracao
ORDER BY 
    Pais, Geracao
"""
df_sql_paises = spark.sql(consulta_sql_paises)
df_sql_paises.show()

