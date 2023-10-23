# Space-Galery

O Space Gallery é um projeto desenvolvido em Django que permite aos usuários visualizar e compartilhar fotos relacionadas ao espaço. Os principais recursos incluem o cadastro de novos usuários, login, a capacidade de adicionar novas fotos e descrições, além de funcionalidades de gerenciamento de fotos por pefil de administradores.

![image](https://github.com/Lucas-Benediht/Space-Galery/assets/110697669/4b42f001-052d-4f25-8cc9-621808faca41)


## Pré requisitos
Antes de iniciar o projeto, certifique-se de ter o seguinte instalado em seu ambiente:

- Python ( v3.12.0)
- Django ( v4.2.6)
- Banco de dados SQL (por padrão, o projeto utiliza SQLite)


## Instalação

1.Clonar o repositório
```https://github.com/Lucas-Benediht/Space-Galery.git```
```cd space-gallery```

2.Criar uma maquina virtual
```python -m venv venv```

2.1Ative a maquina virtual
```source venv/bin/activate```

3.Instale as dependências:
```pip install -r requirements.txt```

4.Execute as migrações do banco de dados:
```python manage.py migrate```

5.Crie um superusuário (administrador) para gerenciar o site:
```python manage.py createsuperuser```

6.Inicie o servidor :
```python manage.py runserver```

Acesse o site em http://localhost:8000/ e faça login com as credenciais do superusuário.

## Uso 
- Faça login com suas credenciais para acessar as funcionalidades do site.
- Os usuários com perfil de administrador podem aprovar novas fotos enviadas por outros usuários.
- Você pode adicionar novas fotos e descrições no painel de administração ou por meio da interface do usuário.
- Use a funcionalidade de CRUD para editar fotos existentes

# Contato

Lucas Benediht - lucas_benediht@hotmail.com

Link do projeto: https://github.com/Lucas-Benediht/Space-Galery
