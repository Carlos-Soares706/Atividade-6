# Scraping de Notícias - CNN Brasil

Este projeto realiza o scraping das principais manchetes do site **CNN Brasil**, capturando os títulos das notícias e enviando-as por e-mail para o destinatário configurado.

## Funcionalidades

- **Scraping de Notícias**: Captura as principais manchetes do site da CNN Brasil.
- **Envio de E-mail**: Envia um resumo das manchetes por e-mail para um destinatário configurado.
- **Automatização**: Você pode agendar ou executar o script sempre que desejar receber as notícias mais recentes.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **BeautifulSoup**: Biblioteca para parsing e scraping de HTML.
- **requests**: Biblioteca para fazer requisições HTTP.
- **smtplib**: Biblioteca para envio de e-mails.
- **dotenv**: Para carregar variáveis de ambiente, como credenciais do e-mail.
- **Git**: Controle de versão do projeto.

## Pré-requisitos

Certifique-se de ter as seguintes dependências instaladas:

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`
  - `python-dotenv`

Para instalar as bibliotecas necessárias, execute o seguinte comando:

```bash
pip install requests beautifulsoup4 python-dotenv
