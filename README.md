# Selenium WebDriver

- Projeto para aprender teste automatizados com Selenium WebDriver e pytest aplicando boas práticas como Page Object Model (POM) e AAA (Arrange, Action, Assert), além de integração com CI do GitHub Actions.
- Utilizando o site: https://www.saucedemo.com/ para realização dos testes (Login e adicionar itens no carrinho)

## Objetivos

- Explorar testes automatizados com Selenium WebDriver + pytest
- Utilizar padrões e boas práticas como POM e AAA
- Integrar testes com GitHub Actions para CI

## Estrutura

- `pages`: Camada de abstração das páginas (Page Object Model), contendo elementos e ações reutilizáveis
- `pytest.ini`: Configuração central do Pytest (opções padrão, organização e execução dos testes)
- `requirements.txt`: Gerenciamento de dependências do projeto
- `.github/workflows/`: Configuração do CI

## Requisitos

- Phyton
- Selenium
- pytest

## Como executar

```bash
pip install selenium
python -m pip install pytest
py -m pytest
```

## Integração CI

Os testes são executados automaticamente via GitHub Actions a cada push.
