# Configurações do Ambiente Python

Este documento contém comandos e informações úteis para configuração do ambiente Python, incluindo pytest, ambiente virtual, extensões recomendadas, uso do GitHub e manipulação de pastas e arquivos no terminal do VSCode.

---

## 1. Pytest

Pytest é uma ferramenta para execução de testes em Python.

- Instalar pytest:
```bash
pip install pytest
```

- Executar todos os testes no diretório atual:
```bash
pytest
```

- Executar um arquivo de teste específico:
```bash
pytest nome_do_arquivo_test.py
```

- Executar testes com saída detalhada:
```bash
pytest -v
```

---

## 2. Ambiente Virtual (env)

Para isolar dependências do projeto, utilize ambientes virtuais.

- Criar um ambiente virtual:
```bash
python -m venv nome_do_ambiente
```

- Ativar o ambiente virtual:

  - No Windows (PowerShell):
  ```powershell
  .\nome_do_ambiente\Scripts\Activate.ps1
  ```

  - No Windows (cmd):
  ```cmd
  .\nome_do_ambiente\Scripts\activate.bat
  ```

  - No macOS/Linux:
  ```bash
  source nome_do_ambiente/bin/activate
  ```

- Desativar o ambiente virtual:
```bash
deactivate
```

- Instalar pacotes dentro do ambiente virtual:
```bash
pip install nome_do_pacote
```

- Gerar arquivo de dependências:
```bash
pip freeze > requirements.txt
```

- Instalar dependências a partir do arquivo:
```bash
pip install -r requirements.txt
```

---

## 3. Extensões Necessárias para VSCode

Recomenda-se instalar as seguintes extensões para trabalhar com Python e testes:

- **Python** (Microsoft): suporte a linting, debugging, execução de testes, etc.
- **Pylance**: análise avançada de código Python.
- **Python Test Explorer**: integração com frameworks de teste como pytest.
- **GitLens**: melhorias para uso do Git no VSCode.
- **Visual Studio IntelliCode**: sugestões inteligentes de código.

---

## 4. GitHub

Comandos básicos para uso do Git e GitHub no terminal:

- Inicializar repositório Git:
```bash
git init
```

- Clonar repositório:
```bash
git clone url_do_repositorio
```

- Verificar status dos arquivos:
```bash
git status
```

- Adicionar arquivos para commit:
```bash
git add nome_do_arquivo
```
ou para adicionar todos:
```bash
git add .
```

- Fazer commit:
```bash
git commit -m "Mensagem do commit"
```

- Enviar alterações para o repositório remoto:
```bash
git push origin nome_da_branch
```

- Atualizar repositório local:
```bash
git pull
```

---

## 5. Manipulação de Pastas e Arquivos no Terminal do VSCode

Comandos básicos para navegação e manipulação de arquivos e pastas:

- Listar arquivos e pastas:
```bash
ls
```

- Listar arquivos com detalhes:
```bash
ls -la
```

- Mudar de diretório:
```bash
cd nome_da_pasta
```

- Voltar para o diretório anterior:
```bash
cd ..
```

- Criar uma nova pasta:
```bash
mkdir nome_da_pasta
```

- Criar um novo arquivo vazio:
```bash
touch nome_do_arquivo
```

- Copiar arquivo:
```bash
cp arquivo_origem arquivo_destino
```

- Mover ou renomear arquivo:
```bash
mv arquivo_origem arquivo_destino
```

- Apagar arquivo:
```bash
rm nome_do_arquivo
```

- Apagar pasta e seu conteúdo:
```bash
rm -r nome_da_pasta
```

---

Este arquivo pode ser atualizado conforme novas necessidades surgirem.
