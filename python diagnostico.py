
import pandas as pd


def carregar_dados(caminho_do_arquivo):
    try:
        if caminho_do_arquivo.endswith('.csv'):
            df = pd.read_csv(caminho_do_arquivo)
        elif caminho_do_arquivo.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(caminho_do_arquivo)
        else:
            print("Erro: formato não suportado. Use CSV ou Excel.")
            return None

        print(f"Arquivo carregado com sucesso: {caminho_do_arquivo}")
        return df

    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho_do_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")
        return None


def contar_linhas_colunas(df):
    linhas, colunas = df.shape
    nomes_colunas = ", ".join(df.columns)
    return (
        "[DIMENSÃO DA BASE]\n"
        f"Linhas: {linhas}\n"
        f"Colunas: {colunas}\n"
        f"Nomes das colunas: {nomes_colunas}\n"
    )


def analisar_nulos(df):
    relatorio = "[CÉLULAS VAZIAS POR COLUNA]\n"
    total_nulos = 0

    for coluna in df.columns:
        contagem = df[coluna].isnull().sum()
        percentual = round((contagem / len(df)) * 100, 2)
        total_nulos += contagem
        relatorio += f"- {coluna}: {contagem} ({percentual}%)\n"

    relatorio += f"Total de células vazias na base: {total_nulos}\n"
    return relatorio


def analisar_duplicatas(df):
    total_duplicatas = df.duplicated().sum()
    return f"[DUPLICATAS]\nTotal de linhas duplicadas: {total_duplicatas}\n"


def encontrar_colunas_compostas(df):
    candidatas = []

    for coluna in df.columns:
        amostra = df[coluna].head(50).astype(str)
        if amostra.str.contains(r"/|-", regex=True).any():
            candidatas.append(coluna)

    return (
        "[COLUNAS POTENCIALMENTE COMPOSTAS]\n"
        f"Quantidade: {len(candidatas)}\n"
        f"Colunas: {', '.join(candidatas) if candidatas else 'Nenhuma'}\n"
    )


def encontrar_inconsistencias_texto(df):
    relatorio = "[INCONSISTÊNCIAS DE TEXTO POTENCIAIS]\n"
    encontrou = False

    for coluna in df.select_dtypes(include=['object']).columns:
        valores_unicos = df[coluna].nunique()
        if valores_unicos > 50:
            encontrou = True
            relatorio += f"- {coluna}: {valores_unicos} valores únicos\n"

            exemplos = df[coluna].value_counts().head(10)
            relatorio += "  Exemplos mais frequentes:\n"
            for valor, qtd in exemplos.items():
                relatorio += f"    • {valor} ({qtd})\n"

    if not encontrou:
        relatorio += "Nenhuma inconsistência relevante detectada\n"

    return relatorio


def analisar_tipos_de_dados(df):
    relatorio = "[TIPOS DE DADOS]\n"
    for coluna, tipo in df.dtypes.items():
        relatorio += f"- {coluna}: {tipo}\n"
    return relatorio


def gerar_relatorio(df):
    relatorio = ""

    relatorio += contar_linhas_colunas(df)

    relatorio += analisar_nulos(df)

    relatorio += analisar_duplicatas(df)

    relatorio += encontrar_colunas_compostas(df)

    relatorio += encontrar_inconsistencias_texto(df)

    relatorio += analisar_tipos_de_dados(df)
    return relatorio


def main():
    caminho = input("Digite o caminho do arquivo do cliente: ")
    df = carregar_dados(caminho)

    if df is not None:
        relatorio = gerar_relatorio(df)

        print("\n==============================")
        print("RELATÓRIO DE DIAGNÓSTICO")
        print("==============================")
        print(relatorio)

        with open("relatorio_diagnostico.txt", "w", encoding="utf-8") as f:
            f.write(relatorio)

        print("Relatório salvo como 'relatorio_diagnostico.txt'")


if __name__ == "__main__":
    main()
