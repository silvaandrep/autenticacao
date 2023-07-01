import streamlit as st

def autenticar_usuario(username, password):    
    # Verifique se o nome de usuário e a senha correspondem a um usuário válido
    # Retorne True se a autenticação for bem-sucedida, ou False caso contrário

    # Exemplo simples: autenticação sempre bem-sucedida para o usuário "admin" com a senha "senha123"
    if username == "admin" and password == "senha123":
        return True
    else:
        return False

def exibir_pagina_inicial():
    # Aqui você pode exibir a página inicial do seu aplicativo
    st.write("Página de autenticação!")

# Código da aplicação #=======================================================

def exibir_pagina_restrita():
    # Aqui você pode exibir a página restrita acessível somente após a autenticação

    st.sidebar.header('MENU DE AÇÕES DA B3')
    
    st.title('Gráfico de Velas com Linha')
    
# Fim do código da aplicação #=====================================
def main():
    # Inicializa o estado de autenticação como False (não autenticado)
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    # Se estiver autenticado, exibe a página restrita
    if st.session_state.autenticado:
        exibir_pagina_restrita()
    else:
        # Se não estiver autenticado, exibe a página de login
        username = st.text_input("Nome de Usuário")
        password = st.text_input("Senha", type="password")

        if st.button("Login"):
            # Verifica a autenticação do usuário
            if autenticar_usuario(username, password):
                st.session_state.autenticado = True
            else:
                st.error("Falha na autenticação. Tente novamente.")

    # Exibe a página inicial se não estiver autenticado
    if not st.session_state.autenticado:
        exibir_pagina_inicial()

if __name__ == "__main__":
    main()
