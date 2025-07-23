# Projeto To-Do List com Django

<img src="https://static.djangoproject.com/img/logos/django-logo-positive.svg" width="150" alt="Django"> 

## 📖 Sobre o Projeto

# Ainda em desenvolvimento..

## ✨ Funcionalidades

-   **Adicionar Tarefas:** Crie novas tarefas com títulos e descrições.
-   **Visualizar Tarefas:** Veja uma lista de todas as suas tarefas pendentes e concluídas.
-   **Marcar como Concluída:** Altere o status de uma tarefa para "concluída".
-   **Editar Tarefas:** Modifique os detalhes de uma tarefa existente.
-   **Excluir Tarefas:** Remova tarefas que não são mais necessárias.

## 🚀 Tecnologias Utilizadas

-   **Backend:**
    -   ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    -   ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
-   **Frontend:**
    - ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
    - ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

-   **Banco de Dados:**
    -   ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

-   Python 3.8 ou superior
-   pip (gerenciador de pacotes do Python)

## 🏁 Começando

Siga estas instruções para obter uma cópia do projeto em funcionamento em sua máquina local para desenvolvimento e teste.

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/caioeduardo4100/to-do-list.git
    cd to-do-list-django
    ```

2.  **Crie e ative um ambiente virtual:**

    * No macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * No Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instale as dependências a partir do arquivo `requirements.txt`:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário para acessar o painel de administração do Django:**

    ```bash
    python manage.py createsuperuser
    ```
    *Siga as instruções no terminal para definir nome de usuário, email e senha.*

6.  **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

Agora você pode acessar a aplicação em seu navegador no endereço `http://127.0.0.1:8000`. 
O painel de administração estará disponível em `http://127.0.0.1:8000/admin`.
