# **Relatório de Desenvolvimento do Projeto: Simulação de Desenvolvimento usando Ferramentas SCM**

## **1. Introdução**

O projeto "Simulação de Desenvolvimento usando Ferramentas SCM" tem como objetivo aplicar de maneira integrada os conceitos e práticas de Gerência de Configuração de Software (SCM) no desenvolvimento de uma aplicação simples. A proposta visa permitir que a equipe vivencie e utilize ferramentas e processos essenciais de SCM para o controle de versão, gestão de mudanças, automação de builds e integração contínua (CI), além de promover uma colaboração eficaz e organizada por meio de metodologias ágeis, como Scrum ou Kanban.

Para atingir esses objetivos, a equipe desenvolveu uma aplicação de complexidade baixa, resultando num conversor de Unidades, Moedas e leitor de QR Code. Durante o desenvolvimento, foi feita a configuração de um repositório no GitHub, onde estão armazenados o código-fonte, documentação e arquivos de configuração. As práticas de versionamento, incluindo o uso de tags e releases, foram implementadas para garantir a rastreabilidade do projeto.

Adicionalmente, o processo de desenvolvimento foi gerido por meio de GitHub Project Boards, o que facilitou o acompanhamento de tarefas e milestones, proporcionando visibilidade para todos os membros da equipe. Cada integrante assumiu múltiplos papéis, como desenvolvedor, responsável pelo build/CI, gerente de configuração e testador, promovendo uma experiência prática e colaborativa. O uso de Docker para configurar um ambiente replicável e a automação do processo de integração contínua (CI) com ferramentas como GitHub Actions garantiu a consistência e a qualidade do projeto, enquanto o planejamento de releases e testes automatizados assegurou a entrega de uma versão estável e funcional da aplicação.

Este projeto ofereceu uma oportunidade valiosa para explorar profundamente as práticas de SCM em um ambiente real de desenvolvimento de software, abordando não apenas a codificação, mas principalmente os processos essenciais para garantir a qualidade, rastreabilidade e colaboração contínua ao longo do ciclo de vida do software.

## **2. Balanço Geral das Configurações aplicadas**

### **2.1 Especificações e estratégias**

De forma geral, é possível afirmar que as principais estratégias e especificações apresentadas em sala de aula foram utilizadas, seja de forma integral ou parcial, na construção deste projeto. No início, ocorreram alguns deslizes por parte da equipe, como será descrito nas seções e subseções a seguir. Contudo, eles foram corrigidos, com as estratégias abaixo sendo aplicadas e validadas ao longo dos últimos dias por todos os integrantes.

#### **2.1.1 Estratégia de branching utilizada**

- Inicialmente, foram utilizados nomes arbitrários relacionados às funcionalidades construídas para nossa aplicação;
- Em seguida, corrigimos essa ineficiência, utilizando a estratégia de [Git Flow](https://www.alura.com.br/artigos/git-flow-o-que-e-como-quando-utilizar)
  - A partir dessa estratégia, foram adotadas convenções de nomenclatura para cada nova branch e commit criados.

#### **Procedimentos de build e CI/CD**

- Quanto à construção de builds, devido ao fato de o projeto ser em Python e às restrições de tempo, o arquivo executável final é o próprio **"conversor.py"**, que contém uma UI básica na qual o usuário pode acessar as três categorias de conversões propostas para este projeto: conversões de unidades físicas, de moedas e de QR Code.
- Quanto à CI/CD, foi utilizado o GitHub Actions em paralelo à escrita das funções principais da nosso projeto, relacionada à primeira milestone "Desenvolvimento do código de conversão das 3 categorias";
- O GitHub actions descrito foi feito ao longo do projeto todo com base no mesmo arquivo "main_CI.yml". Este arquivo contém as configurações de checkout, configuração, instalação de dependências e execução dos testes;
- Explicações mais detalhadas do CI podem ser encontradas no arquivo ".github/workflows/README_CI.md".

#### **Estrutura e política de testes**

- A estrutura dos arquivos de teste seguiu as recomendações do framework [Pytest] (https://docs.pytest.org/en/stable/) utilizado, estando colocado em uma pasta própria, "./tests";
- Cada desenvolvedor realizou os testes referentes aos arquivos com as funções que ele próprio desenvolveu, a saber: **"currency_converter.py"**, **"qrcode_converter.py"** e **"und_fisicas.py"**;
- Os testes abrangem todas as funções colocadas nesses arquivos, que são chamadas por meio dos botões da interface gráfica.

#### **Forma de versionamento adotada (tags, releases)**

Este foi, possivelmente, o aspecto da gerência de configurações que mais deixou o Grupo 3 confuso e indeciso. De forma geral, sabia-se que a release final seria o próprio arquivo em Python, como relatado anteriormente. Por conta disso, não foram criadas muitas tags e releases para o projeto. A primeira tag estava relacionada à primeira versão incompleta, mas já pronta para testes. A segunda será referente à release final, com os principais bugs corrigidos e a UI integrada às funções criadas e lançadas na primeira release.

### **2.2 Gerenciamento de Issues**

O gerenciamento de issues foi outro ponto em que o Grupo 3 apresentou certa confusão no início, mas que foi corrigido e melhorou significativamente com o passar dos dias.  

- Inicialmente, por estarmos em contato constante e acostumados com ferramentas externas como o Trello, acabamos esquecendo de criar as issues referentes às tarefas iniciais.  
- **Em seguida**, ao percebermos essa falha, criamos issues retroativas com o objetivo de documentar corretamente as branches e commits relacionados às tarefas especificadas.  
- A partir desse momento, todas as issues passaram a ser criadas antecipadamente, prevendo melhorias e implementações, relatando problemas encontrados e sendo vinculadas ao **GitHub Projects** e às **Milestones**.  


## **3. Lições Aprendidas**

### **3.1 Lições Aprendidas - Luan**

Durante o desenvolvimento do projeto de conversão de unidades físicas, foi possível aplicar diversos conceitos fundamentais de Gerência de Configuração de Software (SCM) e de controle de versão utilizando o Git. Analisando o enunciado do projeto, senti que posso melhorar bastante, mas sob o ponto de vista de ter desenvolvido um projeto assim pela primeira vez, me senti bastante satisfeito com o resultado. A seguir, apresento mais detalhadamente algumas das lições aprendidas.

#### **3.1.1. Uso do Git e SCM para Colaboração Eficiente**

O uso de Git e GitHub foi essencial para a colaboração e organização do projeto, apesar de termos usado o WhatsApp também. Ainda assim, desde a criação do repositório até a execução de deploys e integração contínua, as ferramentas de SCM permitiram que a equipe trabalhasse de forma coordenada, mesmo de forma completamente remota. Enquanto escrevo esse relatório, parei para refletir sobre o quanto foi prático trabalhar com Paulo e Victor sem nunca tê-los conhecido pessoalmente (por enquanto), depois de termos tido esse curso com o professor Leopoldo também sem nunca tê-lo conhecido pessoalmente também.

- **Versionamento e Controle de Alterações**: Utilizamos Git para gerenciar as alterações no código, o que nos permitiu rastrear mudanças e revertê-las caso necessário. A prática de commits frequentes e bem descritos foi fundamental para manter o histórico de alterações claro e compreensível.
  
- **Branching com Git Flow**: Adotar uma estratégia de branching como o **Git Flow** foi crucial para o desenvolvimento organizado do código. Criamos uma branch principal (`main`) para a versão estável do código, enquanto utilizamos branches de desenvolvimento (`feature/xxx`) para implementar novas funcionalidades. O fluxo de trabalho envolvia trabalhar em uma branch separada para cada tarefa ou bugfix, o que evitou que mudanças não testadas fossem incorporadas ao código principal sem a devida revisão. Conforme pode ser visto no histórico do GitHub, no começo do projeto nossa coordenação não foi muito eficiente nesse quesito, mas rapidamente aprendemos e evoluímos para fazer um projeto com um gerenciamento mais eficiente.

- **Pull Requests e Revisões de Código**: A criação de **Pull Requests (PRs)** foi uma das práticas mais importantes para garantir que todas as mudanças fossem revisadas antes de serem integradas ao código principal. Cada PR era revisado por pelo menos um membro da equipe, o que ajudava a detectar erros mais rapidamente, discutia melhorias e aumentava a qualidade do código.


#### **3.1.2. Controle de Mudanças e Rastreamento com Issues e Milestones**

A rastreabilidade das mudanças no projeto foi uma prática chave para garantir que todas as funcionalidades e melhorias fossem devidamente documentadas e acompanhadas.

- **Uso de Issues**: A criação de **issues** foi uma maneira eficiente de registrar e acompanhar as tarefas a serem feitas, bem como identificar problemas no código ou melhorias a serem implementadas. A equipe utilizou issues para definir claramente as responsabilidades de cada membro e garantir que as funcionalidades fossem desenvolvidas de acordo com as prioridades estabelecidas.

- **Associação de Issues com Milestones**: Associar as issues a **milestones** (marcos do projeto) aparentou ser uma alternativa bastante interessante para acompanhar o progresso do projeto e garantir que os objetivos do sprint fossem cumpridos. Apesar de não ter usado muito esse recurso neste projeto, pretendo aplicá-lo melhor em projetos futuros.

- **Uso de Labels**: As **labels** nas issues, como `bug`, `enhancement`, e `documentation`, ajudaram a categorizar as tarefas de maneira eficiente e mais agradável de se ler. Isso facilitou a priorização e organização das atividades ao longo do desenvolvimento, além de dar visibilidade ao progresso do projeto para toda a equipe.


#### **3.1.3. Integração Contínua (CI) e Automação de Processos**

A integração contínua foi outro conceito importante aplicado no projeto. A configuração de pipelines de CI no GitHub Actions permitiu que os testes fossem executados automaticamente sempre que uma mudança era enviada para o repositório.

- **GitHub Actions e Automação de Testes**: A configuração de um **pipeline de CI** utilizando GitHub Actions foi uma das principais práticas aprendidas. O processo de CI foi configurado para rodar os testes automatizados sempre que um commit era realizado na branch `main` ou quando um PR era aberto. Isso garantiu que, sempre que novas alterações eram feitas no código, a integridade do sistema era verificada automaticamente. Acho importante destacar que foi a **primeira vez que fiz** um pipeline desses.

  - A execução de testes automatizados, como os realizados com o framework **pytest**, evitou que erros passassem despercebidos. Além disso, a **automação do processo de build** com o CI reduziu significativamente o tempo necessário para validar as alterações, permitindo um ciclo de desenvolvimento mais rápido e seguro. Pessoalmente eu achei bastante satisfatório ver o teste rodando sem erros quando as PR's eram aceitas (isso obviamente só aconteceu depois de um tempinho quebrando cabeça e tentando fazer funcionar).

- **Verificação de Estilo de Código**: Embora opcional, a verificação de estilo de código com **flake8** foi uma prática interessante que consideramos implementar para garantir que o código estivesse sempre formatado de acordo com as boas práticas. Mesmo que isso não tenha sido ativado na pipeline de CI, a ideia foi bem recebida pela equipe como uma futura melhoria para evitar problemas de legibilidade no código. 


#### **3.1.4. Versionamento de Código e Tags**

Durante o desenvolvimento, infelizmente pecamos um pouco sobre a correta utilização de **tags** no Git e como ela pode facilitar a organização e o rastreamento de versões.

- **Uso de Tags**: O uso de **tags** para marcar versões estáveis do código é algo que poderíamos ter feito melhor. Creio que por imaturidade nossa, falhamos em como mensurar aonde cada versão que era considerada pronta para o uso deveria marcada com uma tag, o que poderia ter nos permitido um controle mais eficiente de quando as alterações foram feitas e a data de lançamento de uma nova versão do software. Isso também poderia ter sido útil caso precisássemos reverter para uma versão anterior do código, por exemplo, se algum erro grave fosse encontrado.


#### **3.1.5. Lições de Colaboração em Equipe e Comunicação**

A colaboração foi facilitada não apenas pelo uso de Git e GitHub, mas também pela constante comunicação entre os membros da equipe via WhatsApp.

- **Revisões Colaborativas de Código**: O processo de revisão de código foi uma excelente oportunidade para compartilhar conhecimentos entre os membros da equipe. Cada um trouxe uma perspectiva diferente sobre como resolver problemas e como otimizar o código. Isso não apenas melhorou a qualidade do código, mas também ampliou o entendimento de todos sobre o funcionamento do sistema.

- **Comunicação e Transparência**: Manter uma comunicação aberta e transparente sobre as tarefas, problemas e decisões tomadas foi crucial para o sucesso do projeto. Utilizamos o **GitHub Project Boards** para planejar e acompanhar as atividades, o que nos ajudou a ter uma visão clara das prioridades e das etapas a serem cumpridas.


#### **3.1.6. Conclusão**

Ao longo do desenvolvimento do projeto, os principais aprendizados giraram em torno das práticas de **Gerência de Configuração de Software (SCM)** e **controle de versão** utilizando o Git. A adoção de práticas de Git Flow, automação com CI, rastreabilidade de mudanças através de issues e milestones, e a utilização de tags para versionamento permitiram que o projeto fosse desenvolvido de forma organizada, eficiente e colaborativa.

Esses conceitos e ferramentas não só melhoraram a qualidade do código, mas também promoveram uma colaboração mais eficaz e transparente entre os membros da equipe. As lições aprendidas nesse processo serão essenciais para projetos futuros, especialmente na construção de sistemas mais complexos, onde o controle de versão e a colaboração em equipe são fundamentais.

### **3.2 Lições Aprendidas - Victor**



### **3.3 Lições Aprendidas - Paulo César**


### 4. Desafios Enfrentados

- Em construção

### 5. Melhorias e Ajustes

- Em construção

## **6. Conclusão**

### 6.1 Resultados Obtidos

É possível afirmar que todos o software *"conversor"*, proposto na última aula da disciplina de gerência, foi, de fato, construído. Além disso, é possível notar, por tudo o que foi exposto acima, que o Grupo 3 enfrentou dificuldades no início, mas acredita ter conseguido superá-las e aplicar de maneira clara todos os conhecimentos adquiridos nas aulas. Elencando alguns dos principais resultados em bullets, temos:

- Um programa em Python, utilizando Tkinter para gerar uma UI Básica, capaz de converter unidades físicas básicas, tipos de moedas a partir da `exchangerate-api` e um conversor/leitor de QR Code.
- Mais de 10 branches criadas, com mais de 60 commits no total;
- Mais de 15 Pull Requests discutidas, revisadas e fechadas (aprovadas ou não);
- Mais de 10 Issues criadas, discutidas, relacionadas ao Github Projects e Milestones e cumpridas;
- Um Kanban Board (No Github Projects) que orientou a construção do software;
- 2 Releases;
- 1 README.md e 1 RELATORIO.md em produção.
  
### 6.2 Contribuições da Equipe

De acordo com as diretrizes do projeto, *"Cada integrante deve assumir ao menos duas funções durante o projeto (importante alternar ao longo do desenvolvimento)"*. Pode-se afirmar categoricamente que esse requisito foi plenamente cumprido, visto que:  

- Todos os integrantes atuaram como **desenvolvedores**, implementando funcionalidades relacionadas a um tipo específico de conversão.  
- Todos os integrantes atuaram como **testadores**, garantindo uma cobertura mínima de testes para as funcionalidades que cada um criou.  
- Todos os integrantes desempenharam o papel de **Gerentes de Configuração**, participando da criação, correção e revisão de nomenclaturas, branches, issues, milestones e demais aspectos do gerenciamento.  
- Luan criou o arquivo `.github/workflows/main_CI.yml`, assumindo a função de **Responsável por Build/CI**, com seu trabalho sendo revisado por Paulo e Victor.