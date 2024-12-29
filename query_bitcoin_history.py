import sqlite3  

def consultar_dados(bitcoin_history, consulta):  
    try:  
        # Conectar ao banco de dados  
        conexao = sqlite3.connect(bitcoin_history)  
        cursor = conexao.cursor()  
        
        # Executar a consulta  
        cursor.execute(consulta)  
        
        # Obter todos os resultados  
        resultados = cursor.fetchall()  
        
        # Exibir os resultados  
        for linha in resultados:  
            print(linha)  

    except sqlite3.Error as e:  
        print(f"Erro ao consultar o banco de dados: {e}")  
    finally:  
        if conexao:  
            conexao.close()  

if __name__ == "__main__":  
    nome_banco = 'bitcoin_history.db' 
    consulta_sql = 'SELECT * FROM bitcoin_prices'  
    
    consultar_dados(nome_banco, consulta_sql)