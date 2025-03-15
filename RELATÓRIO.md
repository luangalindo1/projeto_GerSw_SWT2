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

Este foi, possivelmente, o aspecto da gerência de configurações que mais deixou o Grupo 3 confuso e indeciso. De forma geral, sabia-se que a release final seria o próprio arquivo em Python, como relatado anteriormente. Por conta disso, não foram criadas muitas tags e releases para ao longo do desenvolvimento do projeto, sendo um ponto trabalhado já "nos finalmentes". As tags foram escritas de acordo com a possibilidade de execução do arquivo principal, variando de `unusable` até `first_release`.

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

### **3.2 Lições Aprendidas - Victor Augusto**

Inicialmente, o maior ponto que deveria destacar é a minha inexperiência com ferramentas de gerência, em especial o Git e o Github, onde os comandos eram sempre um grande desafio, tinha sempre que ficar lembrando comandos específicos, quando não faziam parte do "padrão" (git init, git clone, git status, git commit, git push), embora saiba que esses comandos básicos já cobrem boa parte dos comandos mais usados, me faltava um pouco mais de desenvoltura para isso, pois para o correto desenvolvimento do trabalho, eram necessários outros comandos mais robustos, e esse trabalho foi uma boa oportunidade para poder conhecer mais sobre eles, poder testar na prática e por fim me sentir confiante no uso destes comandos.

Outro ponto relevante, que mereça estar aqui relatado, foi a parte do gerenciamento de tarefas dentro do Github Projects, mas com a questão que tem diversos tópicos ligados aos conteúdos do Github, como tags, menções aos PRs, issues etc, isso é muito interessante, e diferente, mas que ajudam muito nas tarefas e no desenvolvimento do projeto, ainda mais para equipes maiores e com diversas atividades, commits, features e issues para resolver, e dentro do Projects, é concentrado tudo isso dentro do repositório, sem a necessidade de ter que fazer esse gerenciamento de atividades em outros sistemas, como Trello ou Jira, isso é um ponto muito positivo para equipes em grandes projetos, facilitando esse "trackeamento" de tarefas e minimização de erros por ter que sempre estar registrando em outras plataformas.

Um dos aprendizados mais significativos para mim foi a utilização do GitHub Actions para automação de testes e integração contínua (CI). No início, configurar o GitHub Actions foi um desafio, especialmente porque nunca havia trabalhado com pipelines de CI antes. Aprendi a criar um workflow básico para executar testes automatizados a cada push ou pull request, garantindo que o código fosse validado antes de ser mesclado na branch principal. Essa automação não só acelerou o processo de desenvolvimento, mas também aumentou a confiança na qualidade do código, já que erros eram detectados rapidamente. 

Um erro que cometi e que serviu como uma grande lição: deixei a API Key do conversor de moedas exposta no código-fonte. Isso foi um problema grave, pois comprometia a segurança do projeto. Após perceber o erro, pesquisei sobre como proteger informações sensíveis e utilizei o GitHub Secrets, o que foi uma boa solução, pois estava tudo dentro do Github e o Actions precisava disso para fazer a parte de testes. Aprendi a armazenar a API Key como um segredo no repositório e a acessá-la no código por meio de variáveis de ambiente. Essa solução não apenas resolveu o problema de segurança, mas também me mostrou o poder do GitHub em oferecer ferramentas robustas para gerenciar informações sensíveis de forma segura.

Além disso, a experiência com testes automatizados foi fundamental para entender a importância de garantir a qualidade do código. Utilizando o framework Pytest, pude criar testes unitários para as funcionalidades que desenvolvi, como a conversão de moedas, onde precisava testar alguns aspectos das suas funções. A integração desses testes com o GitHub Actions permitiu que eles fossem executados automaticamente a cada alteração no código, garantindo que novas implementações não quebrassem funcionalidades existentes. Essa prática foi essencial para manter a estabilidade do projeto, onde faz pensar que para uma equipe composta por 3 integrantes, já é de grande ajuda, quando se aumenta para grandes equipes, é realmente de grande ajuda o Actions para automatizar essa parte.

Como lição aprendida maior, não somente pelo projeto, mas a matéria como um todo: pude  entender como o GitHub é uma plataforma completa para desenvolvimento colaborativo. Desde o versionamento de código com Git até a automação de processos com GitHub Actions, todas as ferramentas estão integradas e são fáceis de usar quando bem compreendidas. Aprendi que, com um pouco de estudo e prática, é possível dominar essas ferramentas e utilizá-las para melhorar a eficiência e a qualidade do trabalho em equipe.

### **3.3 Lições Aprendidas - Paulo César**

Diversos dos pontos que eu poderia elencar como lições aprendidas já foram abordados ao longo de outras seções, especialmente na **Seção 3.1**, escrita pelo Luan. Por isso, considero mais apropriado focar em aspectos mais amplos e gerais, que demonstram uma evolução significativa para mim e dos quais extraí aprendizados ao longo da realização deste projeto.

O principal ponto que quero abordar diz respeito à própria definidação das atividades de gerência, onde aprendi que suas configurações e tarefas devem ser estabelecidas antes mesmo do início efetivo do projeto. O maior exemplo disso, para mim, foi a necessidade de, após certo tempo, **adequar as *issues* e estruturar melhor o uso do GitHub Projects**. Como eu já estava mais acostumado com Jira e Trello, no início acabei esquecendo de elencar issues e dar mais atenção aos nomes colocados em commits e branches. Isso foi corrigido no meio do projeto, mas admito que isso acabou impactando no fluxo do trabalho realizado por mim e pelos demais membros. Além disso, a conformidade com Flake8 foi um ponto debatido, mas acabou sendo retirada ao longo do desenvolvimento, visto que não estávamos seguindo seus *guidelines*. Definir esses pontos antecipadamente teria evitado ajustes no meio do caminho.

Contudo, esse aspecto, que considero minha maior falha, também representa o ponto de maior evolução ao longo do projeto. Apesar das dificuldades e confusões iniciais na aplicação de certos conceitos, o GitHub proporcionou flexibilidade suficiente para corrigir problemas, permitindo que categorizações fossem ajustadas posteriormente. Assim, as issues que haviam sido negligenciadas no início foram criadas retroativamente, os nomes das branches foram corrigidos e as milestones foram devidamente adicionadas. Após essas correções, o fluxo do projeto tornou-se mais organizado e eficiente, com todo o time alinhado às boas práticas de gerência.

Por fim, também reconheço que este projeto teve suas limitações, principalmente devido às restrições de tempo e às outras obrigações da Residência Tecnológica. No que diz respeito à minha parte, algumas melhorias que poderiam ter sido implementadas incluem a adição de novas funções para personalizar QR Codes, como alterar cores, adicionar imagens de fundo e permitir a escolha do caminho de salvamento, já que, atualmente, os arquivos são salvos apenas no diretório local onde o `conversor.py` está. Além disso, uma interface gráfica mais robusta teria sido vantajosa, não apenas para melhorar a estética do projeto, mas também para viabilizar testes de integração entre a UI e as funções previamente validadas nos testes unitários.

## 4. Desafios Enfrentados

Durante o desenvolvimento do projeto, a equipe enfrentou diversos desafios que, embora tenham sido superados, serviram de reflexão e demandou um certo foco a mais, além da organização do projeto. Foram elencados os principais desafios identificados, são eles:

### 4.1 Inexperiência com Ferramentas de SCM
No início do projeto, a equipe demonstrou dificuldades em utilizar corretamente as ferramentas de SCM, como Git, GitHub Projects e GitHub Actions. Isso resultou em práticas inadequadas, como a falta de issues no início do projeto e a criação de branches com **nomes arbitrários**. A equipe realizou pesquisas e consultas para entender melhor as práticas recomendadas, como o uso de Git Flow, a criação de issues antecipadas e a configuração de pipelines de CI com GitHub Actions. A correção dessas práticas foi feita ao longo do projeto, resultando em um fluxo de trabalho mais organizado.

### 4.2 Dificuldades com Integração Contínua (CI)
Configurar o GitHub Actions para executar testes automatizados foi desafiador, especialmente para membros que nunca haviam trabalhado com CI antes. Erros frequentes nos pipelines atrasaram o desenvolvimento inicial, além de problemas com as keys sendo mostradas publicamente nos arquivos.
A solução para esse desafio foi a equipe dedicar tempo para estudar a documentação do GitHub Actions e realizar testes iterativos até que o pipeline funcionasse corretamente. A automação dos testes trouxe benefícios significativos, como a detecção precoce de erros, assim como a automação para esses testes a todo novo PR feito na branch main do repositório.

### 4.3 Versionamento e Releases
Houve dificuldades em definir critérios claros para o versionamento do projeto, resultando em poucas tags e releases. Após discussões, a equipe estabeleceu critérios para criar tags e releases, como a conclusão de funcionalidades principais e a correção de bugs críticos. Isso permitiu um controle mais eficiente das versões do projeto.

### 4.4 Testes Automatizados
A implementação de testes automatizados foi um processo lento, especialmente devido à falta de experiência com o framework Pytest. A equipe realizou pesquisas e testes iterativos para garantir que todas as funcionalidades fossem cobertas por testes unitários. A automação dos testes via CI garantiu que erros fossem detectados rapidamente, e feitos de forma automática, em conjunto do **Github Actions**

## **5. Melhorias e Ajustes**

Baseado nos desafios enfrentados e nas lições aprendidas, foram identificados vários pontos de melhorias que podem ser implementados em futuros projetos, onde haja o uso de ferramentas de **Gerencias de Configuração**, os pontos são os seguintes:

### 5.1  Definição Antecipada de Práticas de SCM
- Estabelecer desde o início as práticas de SCM, como estratégias de branching, convenções de commit e políticas de versionamento. 
**Benefício:** Evitará a necessidade de correções no meio do projeto e garantirá um fluxo de trabalho mais organizado.

### 5.2 Uso de Ferramentas de Comunicação Integradas
- Utilizar ferramentas de comunicação integradas ao GitHub, como discussões ou projetos, em vez de depender de aplicativos externos como WhatsApp. 
**Benefício**: Melhorará a rastreabilidade das decisões e tarefas, além de centralizar todas as informações no GitHub.

### 5.3 Expansão dos Testes Automatizados
- Implementar testes de integração e testes de UI para garantir uma cobertura mais abrangente.
**Benefício**: Aumentará a confiabilidade do software e reduzirá a probabilidade de erros em produção.

### 5.4 Documentação Detalhada
- Criar uma documentação mais detalhada, incluindo tutoriais para configuração do ambiente, execução de testes e deploy.
**Benefício**: Facilitará a colaboração de novos membros e a manutenção do projeto.

## **6. Conclusão**

### 6.1 Resultados Obtidos

É possível afirmar que todos o software *"conversor"*, proposto na última aula da disciplina de gerência, foi, de fato, construído. Além disso, é possível notar, por tudo o que foi exposto acima, que o Grupo 3 enfrentou dificuldades no início, mas acredita ter conseguido superá-las e aplicar de maneira clara todos os conhecimentos adquiridos nas aulas. Elencando alguns dos principais resultados em bullets, temos:

- Um programa em Python, utilizando Tkinter para gerar uma UI Básica, capaz de converter unidades físicas básicas, tipos de moedas a partir da `exchangerate-api` e um conversor/leitor de QR Code.
- Mais de 10 branches criadas, com mais de 60 commits no total;
- Mais de 15 Pull Requests discutidas, revisadas e fechadas (aprovadas ou não);
- Mais de 10 Issues criadas, discutidas, relacionadas ao Github Projects e Milestones e cumpridas;
- Um Kanban Board (No Github Projects) que orientou a construção do software;
- Mais de 5 Releases (apesar da maioria não ser plenamente utilizável);
- 1 README.md e 1 RELATORIO.md em produção.
  
### 6.2 Contribuições da Equipe

De acordo com as diretrizes do projeto, *"Cada integrante deve assumir ao menos duas funções durante o projeto (importante alternar ao longo do desenvolvimento)"*. Pode-se afirmar categoricamente que esse requisito foi plenamente cumprido, visto que:  

- Todos os integrantes atuaram como **desenvolvedores**, implementando funcionalidades relacionadas a um tipo específico de conversão.  
- Todos os integrantes atuaram como **testadores**, garantindo uma cobertura mínima de testes para as funcionalidades que cada um criou.  
- Todos os integrantes desempenharam o papel de **Gerentes de Configuração**, participando da criação, correção e revisão de nomenclaturas, branches, issues, milestones e demais aspectos do gerenciamento.  
- Luan criou o arquivo `.github/workflows/main_CI.yml`, assumindo a função de **Responsável por Build/CI**, com seu trabalho sendo revisado por Paulo e Victor.

### 6.3 Considerações finais
O projeto foi uma boa oportunidade para a equipe aplicar os conceitos de SCM em um ambiente real de desenvolvimento. Apesar dos desafios enfrentados, a equipe demonstrou capacidade de aprendizado e adaptação, resultando em um projeto bem-sucedido. As lições aprendidas serão fundamentais para projetos futuros, especialmente no que diz respeito à organização, automação e colaboração em equipe.