# Python CI - GitHub Actions

Este arquivo de configuração do GitHub Actions descreve um pipeline de integração contínua (CI) para um projeto Python. O objetivo é garantir que o código da branch principal seja testado automaticamente sempre que houver mudanças (push ou pull request). O pipeline realiza o checkout do código, configura o ambiente Python, instala as dependências, executa testes e pode, opcionalmente, verificar o estilo do código com flake8.

## Fluxo do Workflow

### Gatilhos
O workflow é acionado em dois eventos:
- **Push**: Quando houver um push para a branch `main` (ou outra branch especificada).
- **Pull Request**: Quando um pull request for aberto, alterado ou mesclado para a branch `main`.

### Jobs

#### 1. Teste
Este é o único job do workflow, que será executado no sistema operacional Ubuntu mais recente (`ubuntu-latest`).

##### Etapas do Job

- **Checkout do código**: 
  - A ação `actions/checkout@v2` é usada para fazer o checkout do código-fonte, preparando-o para ser utilizado na execução do job.

- **Configuração do Python**:
  - A ação `actions/setup-python@v2` configura o ambiente Python, definindo a versão do Python como `3.10`.

- **Instalação de dependências**:
  - A etapa executa o comando para atualizar o pip e instalar as dependências listadas no arquivo `requirements.txt`.

- **Execução dos testes**:
  - A etapa usa o framework de testes `pytest` (ou qualquer outro framework configurado) para executar os testes. A flag `-v` é usada para exibir resultados mais detalhados.

- **(Opcional) Verificação do estilo de código com flake8**:
  - Esta etapa está comentada, mas, se descomentada, instala e executa o flake8 para verificar a conformidade do código com as melhores práticas de estilo Python.

## Exemplo de Uso

1. Certifique-se de que o arquivo `requirements.txt` esteja presente na raiz do repositório.
2. O workflow será automaticamente acionado sempre que houver um push para a branch principal ou um pull request.
3. Os resultados dos testes e qualquer falha ou erro de linting (caso o flake8 seja ativado) serão exibidos diretamente nos logs do GitHub Actions.

## Personalizações

- **Versão do Python**: A versão do Python pode ser alterada modificando o valor de `python-version` no arquivo.
- **Dependências**: Certifique-se de que todas as dependências do projeto estejam listadas corretamente no arquivo `requirements.txt`.
- **Framework de Testes**: A execução dos testes está configurada para `pytest`, mas pode ser alterada para outro framework de sua escolha (como `unittest` ou `nose`).
- **Linting**: A verificação de estilo de código com `flake8` está opcional, podendo ser ativada ao descomentar a etapa correspondente.

## Benefícios

- **Automação**: Garantir que os testes sejam executados automaticamente a cada modificação no código.
- **Padronização**: Usar flake8 (se ativado) para manter um código limpo e seguir as melhores práticas do Python.
- **Facilidade**: A configuração é simples e pode ser personalizada conforme as necessidades do projeto.