# **Simulação de Desenvolvimento usando Ferramentas SCM**

## **Objetivo**
Aplicar de forma **integrada** os conceitos, práticas e ferramentas de **Gerência de Configuração de Software (SCM)** no desenvolvimento de uma aplicação simples escolhida pelo grupo. O foco está na **correta utilização das práticas de SCM**, incluindo:
- Versionamento de código e identificação de releases
- Controle de mudanças e rastreabilidade (issues, pull requests, revisões)
- Automação de builds e integração contínua (CI)
- Planejamento de sprints (ou Kanban) com GitHub Project Boards
- Colaboração efetiva em equipe

A complexidade do projeto não precisa ser alta, mas deve permitir que **todos os membros** pratiquem as tarefas de SCM.

## **Deadline**
- **16.03.2025, 23h59**

## **Diretrizes do Projeto**

### **1. Configuração e Planejamento**
1. **Criar um Repositório no GitHub**  
   - Pode ser público ou privado (_desde que todos os membros **e o instrutor** tenham acesso_).  
   - Esse repositório deve conter **todo o código-fonte**, **scripts de build**, **documentação** e **arquivos de configuração**.

2. **Definir o Escopo da Aplicação**  
   - Deve ser **moderadamente simples**, mas com potencial para demonstrar práticas de SCM.  
   - Possíveis exemplos:  
     - Gerenciador de tarefas  
     - Sistema de controle de estoque  
     - Gerador de relatórios financeiros  
     - Dashboard de métricas para um sistema
   - **Descreva no `README.md`** as funcionalidades principais e a proposta do projeto.

3. **Papéis e Responsabilidades**  
   - Cada integrante deve assumir **ao menos duas funções** durante o projeto (importante alternar ao longo do desenvolvimento):  
     - **Desenvolvedor**: implementa funcionalidades  
     - **Responsável por Build/CI**: configura e mantém _pipelines_ de integração e build  
     - **Gerente de Configuração**: monitora mudanças e zela pela rastreabilidade (ex.: tags, versões)  
     - **Testador**: cuida da estratégia de testes, garantindo cobertura e qualidade

4. **Ambiente de Desenvolvimento**  
   - Utilizar **Docker** para criar um ambiente replicável para todos os membros.  
   - Incluir um **`Dockerfile`** (e, se preciso, um `docker-compose.yml`) definindo dependências e instruções de build.  
   - Documentar no `README.md` como iniciar e configurar o ambiente local.

5. **Planejamento com GitHub Project Boards**  
   - Adotar **Scrum** ou **Kanban** para organizar tarefas.  
   - Criar **issues** para cada tarefa a ser realizada (ex.: “Configurar ambiente”, “Criar endpoints da API”, “Implementar testes”), bem como potenciais problemas reportados.  
   - **Relacionar issues** com milestones ou sprints, se aplicável.

### **2. Desenvolvimento e Colaboração**
1. **Gerenciamento de Código-Fonte**  
   - Utilizar **[Git Flow](https://www.alura.com.br/artigos/git-flow-o-que-e-como-quando-utilizar)** ou estratégia similar de _branching_ (ex.: `main`, `develop`, `feature/...`, `hotfix/...`).  
   - Toda nova funcionalidade deve ser implementada em **branches específicas**; abrir Pull Requests (PRs) para revisão.  
   - Ao menos **uma revisão de código** deve ser feita, obrigatoriamente, antes de mesclar PRs na _branch_ principal.  
   - Adotar alguma **convenção de commit** (ex.: `feat: ...`, `fix: ...`, `docs: ...`) e versionar com **tags** (`v1.0.0`, `v1.1.0`, etc.) na medida que o projeto for evoluindo.

2. **Automação de Build e Integração Contínua (CI)**  
   - Configurar um pipeline (ex.: **GitHub Actions**) para:  
     - Verificar a sintaxe do código (`linting`)
     - Compilar/construir a aplicação  
     - Rodar testes automatizados
     - Gerar imagem Docker, se for o caso  
   - Criar ao menos um workflow básico (`.github/workflows/ci.yml`) incluindo testes e build.  
   - **Documentar** como o CI foi configurado e quais passos ocorrem automaticamente.

3. **Gerenciamento de Mudanças e Rastreabilidade**  
   - Criar **issues** para cada nova funcionalidade, bug ou melhoria.  
   - Atribuir **labels** adequadas (`enhancement`, `bug`, `documentation`, etc.).  
   - Fazer referência cruzada em commits/PRs utilizando keywords como `closes #12` ou `fixes #34`.

### **3. Teste e Lançamento**
1. **Testes Automatizados**  
   - Implementar testes unitários e, se possível, testes de integração.  
   - Os testes devem rodar automaticamente via pipeline de CI a cada push ou PR.  
   - Definir **critérios de aceitação** para funcionalidades chave.

2. **Planejamento de Release**  
   - Utilizar o recurso de **Releases** no GitHub para criar versões estáveis e disponibilizar pacotes (ou imagens Docker).  
   - Criar um `CHANGELOG.md` para documentar mudanças de versão para versão.  
   - Cada release deve ter um **rótulo/versão imutável** (`v1.0.0`, `v1.1.0` etc.).

3. **Implantação**  
   - Descrever, no `README.md` ou em um documento separado, **como fazer o deploy** da aplicação (ex.: subir _container_ Docker no Docker Hub, deploy em um servidor de testes).  
   - Se possível, criar um **ambiente de staging** para validar os releases antes de enviá-los ao ambiente final.

### **4. Revisão e Documentação**
1. **Documentação de SCM**  
   - Criar um arquivo `relatorio.md` descrevendo:  
     - Estratégia de branching utilizada 
     - Procedimentos de build e CI/CD  
     - Estrutura e política de testes  
     - Forma de versionamento adotada (tags, releases)  
   - Explorar **como gerenciou issues** (ciclo de vida de um bug/feature).

2. **Reflexão e Lições Aprendidas**  
   - Incluir uma seção **“Lições Aprendidas”** no `relatorio.md`, apontando desafios, melhorias e como o time lidou com problemas de SCM.  
   - Cada membro deve adicionar **reflexões** sobre o uso das ferramentas e práticas de SCM durante o projeto.
      - Lembre-se, o arquivo também é versionado, então sugiro que o mesmo receba contribuições de todos os membros da equipe, cada um dando a sua contribuição/_insight_. 

## **Entregáveis**
1. **Repositório GitHub** contendo:
   - Código-fonte e documentação
   - Histórico de commits, PRs e issues
   - Pipelines de build/CI configurados
   - Dockerfile (e `docker-compose.yml` se necessário)
2. **Documento relatorio.md**:  
   - Explicações sobre branching, CI/CD, testes e versionamento
   - Registro de **lições aprendidas**  
3. **Histórico de trabalho**: Project Board com tarefas concluídas, issues e milestones.

## **Papel do Instrutor**
- **Orientar** em relação a ferramentas e processos de SCM.  
- **Auxiliar** na definição de práticas de branching, automação e testes.  
- **Avaliar** os artefatos entregues com base no que foi solicitado.

## **Observações Gerais**
- **Escolha de Tecnologias:** Livre, desde que sejam adotadas as práticas SCM de forma consistente.  
- **Tamanho do Grupo:** De **3 a 4 pessoas**, para garantir participação ativa de todos.  
- **Foco no SCM:** O projeto deve evidenciar **processos e práticas de configuração**, não apenas o desenvolvimento de código.