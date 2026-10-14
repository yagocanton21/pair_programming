import sqlite3

DATABASE_NAME = "estoque.db"

def get_connection():
    """Retorna uma nova conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome: row["nome"]
    return conn

def init_db():
    """Cria as tabelas no banco de dados SQLite nativo caso não existam."""
    conn = get_connection()
    cursor = conn.cursor()

    # Habilita suporte a chaves estrangeiras no SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade REAL NOT NULL,
            preco_unitario REAL NOT NULL,
            id_categoria INTEGER,
            FOREIGN KEY (id_categoria) REFERENCES categorias (id)
        );

        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_produto INTEGER,
            tipo TEXT NOT NULL,
            quantidade REAL NOT NULL,
            data DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_produto) REFERENCES produtos (id)
        );
    """)

    conn.commit()
    conn.close()
    print("Banco de dados SQLite inicializado com sucesso!")


if __name__ == "__main__":
    init_db()
