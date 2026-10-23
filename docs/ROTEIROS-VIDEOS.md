# Gênio Oculto · Roteiros dos vídeos tutoriais (um por seção)

Sete vídeos curtos, um para cada seção do construtor. Cada vídeo abre com a importância da seção e depois mostra o preenchimento na tela do aplicativo, com o personagem Gê narrando e apontando. Estilo: motion 2D (desenho animado chapado) sobre as telas reais do app.

A versão visual, com as telas e o desenho do personagem, está em `docs/storyboard.html`. As telas de referência estão em `docs/telas/`.

## Como ligar cada vídeo no app
Suba no YouTube (pode ser não listado) e cole o ID no `CONFIG.VIDEOS` do `index.html`, na chave da seção:

| Seção | Chave | Fundo do vídeo | Duração estimada |
|---|---|---|---|
| 1. Você | `voce` | Escuro | ~72s |
| 2. Seu aluno | `aluno` | Claro (areia) | ~57s |
| 3. Seu método | `metodo` | Escuro | ~66s |
| 4. Seu formato | `formato` | Claro (areia) | ~66s |
| 5. Seu potencial | `potencial` | Escuro | ~50s |
| 6. Lançamento | `lancamento` | Claro (areia) | ~53s |
| 7. Envio | `envio` | Escuro | ~69s |

## Direção geral
- **Formato:** 16:9, 1920×1080 (é o formato do player do app). Opcional: versão 9:16 reaproveitando as cenas para Reels e remarketing.
- **Voz:** feminina, calorosa e clara, a "professora que todo mundo queria ter tido". Ritmo de ~150 palavras por minuto. É a voz do Gê.
- **Personagem Gê:** gênio da lâmpada em verde FEX, com capelo de formatura, cauda de fumaça em espiral no lugar das pernas, contorno preto e cores chapadas. Inteligente e acolhedor, nunca infantil. Poses: acenando, apontando, explicando, pensando, surpreso, comemorando.
- **Telas:** use as capturas de `docs/telas/` dentro de um notebook flutuante desenhado (ou em tela cheia com zoom). Mão-cursor 2D branca com contorno preto. Texto digitado aparece letra a letra.
- **Fundo:** igual à fase no app. Seções 1, 3, 5 e 7 em verde-escuro com textura leve; seções 2, 4 e 6 em areia claro (#F4F2EC).
- **Transição assinatura:** a barra verde do meio do "E" do logo FEX atravessa a tela e revela a cena seguinte.
- **Tipografia:** Montserrat. Palavras-chave em Bold gigante (VOCÊ, SEU ALUNO…), frases de apoio em Light.
- **Legendas:** sempre queimadas (muita gente assiste sem som), Montserrat Bold branca em pílula preta 80% opaca, na parte de baixo.
- **Som:** trilha leve e otimista bem baixa sob a voz; pops em cards, digitação suave, whoosh nas transições, "ding" quando algo se completa.
- **Cores:** verde #32CD32, verde brilho #00D84F, preto #040805, areia #E8E4D9 / #F4F2EC.
- **Regras de texto:** sempre "Faculdade FEX Educação®"; nunca "reconhecido pelo MEC" ou "chancela"; use "validade acadêmica". Valores do simulador são projeção, não garantia.

## Seção 1 · Você  (chave `voce`, ~72s, fundo escuro)

**Objetivo:** Mostrar que o curso nasce da experiência da pessoa e ensinar as 4 primeiras respostas: nome, área, anos de prática e as perguntas que ela mais ouve.

### Narração completa

> Oi! Eu sou o Gê, e vou te acompanhar na criação do seu curso. Esta primeira seção é sobre a parte mais importante dele: você. O seu curso nasce da sua experiência, e isso ninguém consegue copiar.
>
> Primeiro, escreva o seu nome e sobrenome. É ele que assina o curso como especialista responsável.
>
> Depois, a sua área. Pode ser ampla ou bem específica, e quanto mais específica, mais fácil de vender. Se ela estiver nos botões, é só clicar.
>
> Agora, arraste a barra até os seus anos de experiência. Repare no número que aparece: são milhares de horas de prática. Uma pós-graduação inteira tem trezentas e sessenta.
>
> E aqui mora o seu gênio oculto: o que as pessoas sempre te perguntam? Escreva uma por linha, do jeito que você ouve no dia a dia. Cada pergunta dessas é uma aula esperando para ser gravada.
>
> Pronto! Clique em Continuar e vamos conhecer o seu aluno.

### Cenas

| # | Tempo | Cena | Narração | Visual | Gê | Texto na tela | Som | Tela |
|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Vinheta | (sem fala) | Fundo verde-escuro com textura. A barra verde do logo FEX atravessa a tela da esquerda para a direita e, por onde passa, revela o selo "Seção 1 de 7" e a palavra VOCÊ em Montserrat Bold gigante. | Gê surge de uma espiral de fumaça verde no canto direito e acena. | Seção 1 de 7 · VOCÊ | Whoosh curto + nota de abertura. | quadro desenhado |
| 2 | 0:03–0:19 | Por que importa | Oi! Eu sou o Gê, e vou te acompanhar na criação do seu curso. Esta primeira seção é sobre a parte mais importante dele: você. O seu curso nasce da sua experiência, e isso ninguém consegue copiar. | Gê no centro. Quando a narração diz "você", ele aponta para a câmera e a palavra VOCÊ pulsa atrás dele. Três ícones orbitam o Gê: maleta (área), relógio (anos), balão de fala (perguntas). | Apontando para a câmera, depois mão no peito em "isso ninguém consegue copiar". | Seu curso nasce da sua experiência | Pop leve em cada ícone. | quadro desenhado |
| 3 | 0:19–0:27 | Nome | Primeiro, escreva o seu nome e sobrenome. É ele que assina o curso como especialista responsável. | Tela do app dentro de um notebook flutuando. Zoom no campo Nome. A mão-cursor clica e o texto "Carla Exemplo" aparece letra a letra. Corte rápido para o painel "Seu curso, ao vivo": o nome surge num chip. | Gê pequeno no canto segurando um crachá em branco que ganha o nome. | Seu nome assina o curso | Digitação suave. | `telas/01-voce-1-nome.jpg` |
| 4 | 0:27–0:38 | Área | Depois, a sua área. Pode ser ampla ou bem específica, e quanto mais específica, mais fácil de vender. Se ela estiver nos botões, é só clicar. | Zoom no campo de área, digitação de "Sua área". Os botões de atalho embaixo acendem em cascata, um por um. No painel ao lado, o título do curso aparece sozinho. | Gê com uma lupa sobre os botões. | Quanto mais específica, mais fácil de vender | Ticks em cascata nos botões. | `telas/01-voce-2-area.jpg` |
| 5 | 0:38–0:51 | Anos de experiência | Agora, arraste a barra até os seus anos de experiência. Repare no número que aparece: são milhares de horas de prática. Uma pós-graduação inteira tem trezentas e sessenta. | A mão arrasta o controle. O contador de horas sobe rápido. Ao lado, uma pilha de relógios cresce até ficar maior que um único bloco escrito "360h". | Gê de queixo caído (pose surpreso). | Milhares de horas × 360h | Contador subindo + "ding". | `telas/01-voce-3-anos.jpg` |
| 6 | 0:51–1:07 | Perguntas | E aqui mora o seu gênio oculto: o que as pessoas sempre te perguntam? Escreva uma por linha, do jeito que você ouve no dia a dia. Cada pergunta dessas é uma aula esperando para ser gravada. | Balões de fala saem de vários celulares desenhados e caem dentro do campo, virando linhas de texto. Em seguida cada linha se transforma num mini-card com um ícone de play escrito "Aula". | Gê pensando, depois sorriso quando os cards viram aulas. | Cada pergunta é uma aula | Pops dos balões. | `telas/01-voce-4-perguntas.jpg` |
| 7 | 1:07–1:12 | Encerramento | Pronto! Clique em Continuar e vamos conhecer o seu aluno. | O botão Continuar pulsa em verde. A barra verde do logo passa e revela o card "Próxima seção: Seu aluno". | Gê aponta para o botão e acena. | Próxima seção: Seu aluno | Whoosh de saída. | quadro desenhado |

## Seção 2 · Seu aluno  (chave `aluno`, ~57s, fundo claro)

**Objetivo:** Fazer a pessoa escolher um aluno ideal concreto e escrever uma promessa que dá para enxergar acontecendo.

### Narração completa

> Um curso que fala com todo mundo não vende para ninguém. Nesta seção você decide para quem é o seu curso e o que essa pessoa vai conseguir fazer no final.
>
> Primeiro, descreva o seu aluno ideal em uma frase. Lembre: para fazer uma pós-graduação, a pessoa precisa ter uma graduação concluída. Se travar, clique em Sugerir com IA ou escolha uma das opções.
>
> Agora, a promessa. Termine a frase: depois do meu curso, o meu aluno vai conseguir... Pense na segunda-feira de manhã dele. O que muda no trabalho ou na vida?
>
> Evite promessas vagas, como crescer na carreira. Prefira algo que dá para ver acontecendo.
>
> Promessa escrita? Continue, porque agora o seu curso vai ganhar forma.

### Cenas

| # | Tempo | Cena | Narração | Visual | Gê | Texto na tela | Som | Tela |
|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Vinheta | (sem fala) | Mesma vinheta, agora em fundo areia claro (como a fase no app). Revela "Seção 2 de 7 · SEU ALUNO". | Gê entra flutuando pela esquerda. | Seção 2 de 7 · SEU ALUNO | Whoosh. | quadro desenhado |
| 2 | 0:03–0:17 | Por que importa | Um curso que fala com todo mundo não vende para ninguém. Nesta seção você decide para quem é o seu curso e o que essa pessoa vai conseguir fazer no final. | Uma multidão de silhuetas cinza. Um holofote verde varre a multidão e para em uma única pessoa, que ganha cor. | Gê segurando o holofote. | Para quem é o seu curso? | Clique de holofote. | quadro desenhado |
| 3 | 0:17–0:31 | Aluno ideal | Primeiro, descreva o seu aluno ideal em uma frase. Lembre: para fazer uma pós-graduação, a pessoa precisa ter uma graduação concluída. Se travar, clique em Sugerir com IA ou escolha uma das opções. | Tela do app em fundo claro. A mão clica em "Sugerir com IA": faíscas verdes saem do botão e o texto se escreve sozinho no campo. | Gê segura um diploma com a etiqueta "graduação concluída". | Pós exige graduação concluída | Brilho mágico curto no clique da IA. | `telas/02-aluno-1-persona.jpg` |
| 4 | 0:31–0:44 | Promessa | Agora, a promessa. Termine a frase: depois do meu curso, o meu aluno vai conseguir... Pense na segunda-feira de manhã dele. O que muda no trabalho ou na vida? | Uma folhinha de calendário vira e mostra SEGUNDA. A frase "Ele vai conseguir…" aparece grande, depois a tela do app com a promessa sendo escrita. A frase voa até a capa do curso no painel. | Gê pensando, com um balão mostrando o calendário. | O que muda na segunda-feira? | Virada de página. | `telas/02-aluno-2-promessa.jpg` |
| 5 | 0:44–0:51 | Dica | Evite promessas vagas, como crescer na carreira. Prefira algo que dá para ver acontecendo. | Card cinza "crescer na carreira" ganha um X e se desfaz em pó. Card verde "aplicar o método com segurança e ter resultado nos primeiros casos" entra com um check. | Gê faz "não" com o dedo e depois joinha. | Vago ✕ · Concreto ✓ | Erro suave + acerto. | quadro desenhado |
| 6 | 0:51–0:56 | Encerramento | Promessa escrita? Continue, porque agora o seu curso vai ganhar forma. | Botão Continuar pulsa. Barra verde revela "Próxima seção: Seu método". | Gê acena. | Próxima seção: Seu método | Whoosh. | quadro desenhado |

## Seção 3 · Seu método  (chave `metodo`, ~66s, fundo escuro)

**Objetivo:** Mostrar a mágica principal: tema vira disciplina, disciplina vira quatro aulas. Ensinar temas, ferramentas, referências e a pergunta "você já ensina?".

### Narração completa

> É nesta seção que o seu curso ganha forma. Cada tema vira uma disciplina, e cada disciplina ganha quatro aulas, no padrão pedagógico da Faculdade FEX Educação®.
>
> Escreva um grande tema que você ensinaria e aperte Enter. Olha só: ele aparece na hora no painel, como disciplina. De três a cinco temas é o ideal.
>
> A disciplina de fundamentos, a de ferramentas e o projeto final, a gente já cria para você.
>
> Depois, as ferramentas que você usa no trabalho: fichas, checklists, roteiros, o seu passo a passo. É isso que deixa o seu curso diferente de qualquer outro.
>
> Se tiver autores ou livros que você segue, escreva. Se não lembrar agora, pode pular. Por último, conte se você já ensina hoje.
>
> Olha o seu curso tomando forma ali do lado. Clique em Continuar para escolher o formato.

### Cenas

| # | Tempo | Cena | Narração | Visual | Gê | Texto na tela | Som | Tela |
|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Vinheta | (sem fala) | Vinheta em fundo escuro: "Seção 3 de 7 · SEU MÉTODO". | Gê gira e para de frente. | Seção 3 de 7 · SEU MÉTODO | Whoosh. | quadro desenhado |
| 2 | 0:03–0:15 | Por que importa | É nesta seção que o seu curso ganha forma. Cada tema vira uma disciplina, e cada disciplina ganha quatro aulas, no padrão pedagógico da Faculdade FEX Educação®. | Diagrama animado: um bloco "Tema" encaixa e vira um bloco maior "Disciplina", que se divide em quatro blocos "Aula" que se alinham embaixo, como peças de montar. | Gê empilha os blocos com as mãos. | Tema → Disciplina → 4 aulas | Cliques de encaixe. | quadro desenhado |
| 3 | 0:15–0:27 | Temas | Escreva um grande tema que você ensinaria e aperte Enter. Olha só: ele aparece na hora no painel, como disciplina. De três a cinco temas é o ideal. | Digitação de "Tema 01" + Enter. Uma seta curva desenhada liga o campo ao painel e o card da disciplina voa até lá. Repete rápido com Tema 02 e Tema 03 (acelerado 2x). | Gê acompanha o card voando com os olhos. | Enter ↵ = nova disciplina | Whoosh pequeno a cada card. | `telas/03-metodo-1-temas.jpg` |
| 4 | 0:27–0:35 | O que vem pronto | A disciplina de fundamentos, a de ferramentas e o projeto final, a gente já cria para você. | No painel, três cards ganham uma estrelinha e o selo "automático". | Gê com uma varinha de condão (estrelas verdes). | 3 disciplinas automáticas | Brilho. | quadro desenhado |
| 5 | 0:35–0:47 | Ferramentas | Depois, as ferramentas que você usa no trabalho: fichas, checklists, roteiros, o seu passo a passo. É isso que deixa o seu curso diferente de qualquer outro. | Uma caixa de ferramentas desenhada abre e os itens saltam para a lista do app. Clique em "Sugerir com IA" mostra três sugestões entrando. | Gê segura a caixa de ferramentas. | O seu jeito de fazer | Metais leves (tim tim). | `telas/03-metodo-2-ferramentas.jpg` |
| 6 | 0:47–0:58 | Referências e "você já ensina?" | Se tiver autores ou livros que você segue, escreva. Se não lembrar agora, pode pular. Por último, conte se você já ensina hoje. | Tela das referências com o link "Pular esta" circulado à mão em verde. Corte para a tela de opções: a mão escolhe "Curso online". | Gê folheando um livro. | Pode pular se não lembrar | Página virando. | `telas/03-metodo-3-referencias.jpg` |
| 7 | 0:58–1:05 | Encerramento | Olha o seu curso tomando forma ali do lado. Clique em Continuar para escolher o formato. | Câmera passeia pelo painel com todas as disciplinas. Barra verde revela "Próxima seção: Seu formato". | Gê aplaude. | Próxima seção: Seu formato | Whoosh. | `telas/03-metodo-4-ensina.jpg` |

## Seção 4 · Seu formato  (chave `formato`, ~66s, fundo claro)

**Objetivo:** Explicar a recomendação de formato, o padrão 30/30/40 (grava-se muito menos do que se imagina) e a lógica de vender a parcela.

### Narração completa

> Agora você decide o formato do curso e quanto o seu aluno vai investir. Fica tranquilo: a ferramenta já sugere o melhor caminho para você.
>
> MBA combina com gestão e negócios. O formato com mediação ao vivo combina com áreas mais práticas. Se quiser, é só trocar.
>
> E repare nesta barra. Numa pós de trezentas e sessenta horas, só trinta por cento é hora-aula. São cento e oito horas para gravar, não trezentas e sessenta.
>
> Confira o nome do curso. Dá para editar ou pedir uma sugestão à IA.
>
> Por último, o investimento do aluno. Em pós-graduação, a gente vende a parcela, não o valor total, porque o aluno compara com a mensalidade de uma faculdade. Escolha o valor que faz sentido para o seu público.
>
> Formato escolhido. Agora vem a parte que mais surpreende: o seu potencial.

### Cenas

| # | Tempo | Cena | Narração | Visual | Gê | Texto na tela | Som | Tela |
|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Vinheta | (sem fala) | Vinheta em fundo claro: "Seção 4 de 7 · SEU FORMATO". | Gê entra. | Seção 4 de 7 · SEU FORMATO | Whoosh. | quadro desenhado |
| 2 | 0:03–0:14 | Por que importa | Agora você decide o formato do curso e quanto o seu aluno vai investir. Fica tranquilo: a ferramenta já sugere o melhor caminho para você. | Quatro cards (Pós 6 meses, Pós 12 meses, MBA 6 meses, MBA 12 meses) giram como cartas e um deles se destaca com o selo "Recomendado para você". | Gê embaralhando as cartas. | A sugestão já vem pronta | Cartas embaralhando. | quadro desenhado |
| 3 | 0:14–0:24 | Formato recomendado | MBA combina com gestão e negócios. O formato com mediação ao vivo combina com áreas mais práticas. Se quiser, é só trocar. | Tela do app em fundo claro. O selo "Recomendado para você" brilha. A mão clica em outro card só para mostrar que dá para trocar, depois volta. | Gê apontando para o selo. | Você pode trocar | Clique. | `telas/04-formato-1-modelo.jpg` |
| 4 | 0:24–0:37 | Padrão 30/30/40 | E repare nesta barra. Numa pós de trezentas e sessenta horas, só trinta por cento é hora-aula. São cento e oito horas para gravar, não trezentas e sessenta. | Uma barra cheia "360h" se divide em três blocos: verde "108h hora-aula", verde-escuro "autoestudo", areia "prática". Uma câmera de vídeo pousa só sobre o bloco verde. | Gê limpa o suor da testa, aliviado. | Você grava 108h, não 360h | Três cliques + suspiro de alívio. | quadro desenhado |
| 5 | 0:37–0:43 | Nome do curso | Confira o nome do curso. Dá para editar ou pedir uma sugestão à IA. | Zoom no campo "Nome do curso" e no botão "Sugerir com IA", que troca o nome com faíscas. | Gê com um balão "ideias". | Nome editável | Brilho. | `telas/04-formato-1-modelo.jpg` |
| 6 | 0:43–0:59 | Investimento | Por último, o investimento do aluno. Em pós-graduação, a gente vende a parcela, não o valor total, porque o aluno compara com a mensalidade de uma faculdade. Escolha o valor que faz sentido para o seu público. | Um bloco grande com o valor total se quebra em 12 blocos pequenos de parcela, que se alinham como um calendário. Corte para a tela das opções de parcela com a mão escolhendo uma. | Gê segura uma calculadora. | Venda a parcela | Moedinhas leves. | `telas/04-formato-2-ticket.jpg` |
| 7 | 0:59–1:05 | Encerramento | Formato escolhido. Agora vem a parte que mais surpreende: o seu potencial. | Barra verde revela "Próxima seção: Seu potencial". | Gê com olhar curioso. | Próxima seção: Seu potencial | Whoosh. | quadro desenhado |

## Seção 5 · Seu potencial  (chave `potencial`, ~50s, fundo escuro)

**Objetivo:** Mostrar quanto a primeira turma pode faturar e o valor que vem só da base que já confia na pessoa. Deixar claro que é projeção.

### Narração completa

> Esta é a seção que mais surpreende. Você vai ver quanto a primeira turma pode faturar com quem já te conhece.
>
> Em base quente, coloque quantas pessoas já foram seus alunos, pacientes ou clientes. Elas já confiam em você.
>
> Em audiência fria, entram os seus seguidores, a sua lista de e-mail e os seus contatos.
>
> Agora olhe o número verde: é o potencial da sua primeira turma. E a frase embaixo mostra quanto vem só da base quente, sem gastar nada com anúncio. É o dinheiro que já está na sua mesa.
>
> Gostou do número? Então vamos planejar o lançamento.

### Cenas

| # | Tempo | Cena | Narração | Visual | Gê | Texto na tela | Som | Tela |
|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Vinheta | (sem fala) | Vinheta escura: "Seção 5 de 7 · SEU POTENCIAL". | Gê entra. | Seção 5 de 7 · SEU POTENCIAL | Whoosh. | quadro desenhado |
| 2 | 0:03–0:13 | Por que importa | Esta é a seção que mais surpreende. Você vai ver quanto a primeira turma pode faturar com quem já te conhece. | Um gráfico de barras desenhado cresce atrás do Gê. | Gê surpreso olhando o gráfico. | Quanto a 1ª turma pode faturar? | Barras subindo. | quadro desenhado |
| 3 | 0:13–0:21 | Base quente | Em base quente, coloque quantas pessoas já foram seus alunos, pacientes ou clientes. Elas já confiam em você. | Um grupo de pessoinhas com um brilho verde em volta (confiança). A mão arrasta o controle da base quente no app. | Gê abraçando o grupo. | Base quente = quem já confia em você | Arraste do controle. | `telas/05-potencial-1-audiencia.jpg` |
| 4 | 0:21–0:29 | Audiência fria | Em audiência fria, entram os seus seguidores, a sua lista de e-mail e os seus contatos. | Ícones genéricos de redes, e-mail e agenda flutuam como bolhas e entram no segundo controle. | Gê com um binóculo. | Audiência fria = quem te acompanha | Bolhas. | `telas/05-potencial-1-audiencia.jpg` |
| 5 | 0:29–0:45 | Resultado | Agora olhe o número verde: é o potencial da sua primeira turma. E a frase embaixo mostra quanto vem só da base quente, sem gastar nada com anúncio. É o dinheiro que já está na sua mesa. | Zoom no card verde: o contador sobe. Depois, a frase de baixo é sublinhada à mão em verde. Plano final: uma mesa desenhada com uma pilha de contratos (folhas com um check), nada de dinheiro voando. | Gê comemorando. | Projeção com os seus números, não é garantia. | Contador + "ding". | quadro desenhado |
| 6 | 0:45–0:49 | Encerramento | Gostou do número? Então vamos planejar o lançamento. | Barra verde revela "Próxima seção: Lançamento". | Gê aponta. | Próxima seção: Lançamento | Whoosh. | quadro desenhado |

## Seção 6 · Lançamento  (chave `lancamento`, ~53s, fundo claro)

**Objetivo:** Ajudar a escolher o modelo de campanha e marcar a aula magna, entendendo os 90 dias de implantação.

### Narração completa

> Curso pronto que ninguém conhece não vira turma. Aqui você escolhe como vai abrir as matrículas e marca a data da aula magna.
>
> Não existe um jeito certo. Tem base de alunos? Campanha interna. Tem audiência nas redes? Aula magna ao vivo. Base pequena e engajada? Lançamento relâmpago no WhatsApp. Escolha o que tem mais a ver com você hoje.
>
> Depois, marque a aula magna, a abertura oficial da turma. A implantação com a Faculdade FEX Educação® leva noventa dias, por isso a data mínima é daqui a noventa dias. E a ferramenta já mostra quando as suas matrículas abrem.
>
> Data marcada é projeto de verdade. Vamos para o último passo.

### Cenas

| # | Tempo | Cena | Narração | Visual | Gê | Texto na tela | Som | Tela |
|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Vinheta | (sem fala) | Vinheta clara: "Seção 6 de 7 · LANÇAMENTO". | Gê entra com um megafone. | Seção 6 de 7 · LANÇAMENTO | Whoosh. | quadro desenhado |
| 2 | 0:03–0:13 | Por que importa | Curso pronto que ninguém conhece não vira turma. Aqui você escolhe como vai abrir as matrículas e marca a data da aula magna. | Uma porta desenhada com a placa "Matrículas" se abre e entra luz verde. | Gê abre a porta. | Como abrir as matrículas | Porta abrindo. | quadro desenhado |
| 3 | 0:13–0:29 | Modelo de campanha | Não existe um jeito certo. Tem base de alunos? Campanha interna. Tem audiência nas redes? Aula magna ao vivo. Base pequena e engajada? Lançamento relâmpago no WhatsApp. Escolha o que tem mais a ver com você hoje. | Os 6 cards do app passam como um carrossel. Cada vez que a narração cita um modelo, o card correspondente sobe e acende. A mão escolhe "Aula magna ao vivo". | Gê de apresentador, apontando para cada card. | Escolha o que combina com você hoje | Tick a cada card. | `telas/06-lancamento-1-campanha.jpg` |
| 4 | 0:29–0:47 | Aula magna | Depois, marque a aula magna, a abertura oficial da turma. A implantação com a Faculdade FEX Educação® leva noventa dias, por isso a data mínima é daqui a noventa dias. E a ferramenta já mostra quando as suas matrículas abrem. | Calendário desenhado: 90 quadradinhos se preenchem de verde rapidamente. Um marcador "Matrículas abrem" e uma estrela "Aula magna" aparecem. Corte para a tela do app com a data e a frase destacada. | Gê circula a data com um pincel verde. | 90 dias até a aula magna | Ticks rápidos + "ding". | `telas/06-lancamento-2-magna.jpg` |
| 5 | 0:47–0:52 | Encerramento | Data marcada é projeto de verdade. Vamos para o último passo. | Barra verde revela "Próxima seção: Envio". | Gê acena. | Próxima seção: Envio | Whoosh. | quadro desenhado |

## Seção 7 · Envio  (chave `envio`, ~69s, fundo escuro)

**Objetivo:** Pedir o contato, mostrar a prévia gratuita, apresentar o plano completo de R$ 97 e o próximo passo com o especialista FEX.

### Narração completa

> Último passo! Aqui você deixa o seu contato e vê o seu curso montado na sua frente.
>
> Escreva o seu e-mail e o seu WhatsApp. É para lá que vai o seu plano, e é por onde um especialista da FEX pode falar com você, se você quiser.
>
> Clique em Ver meu curso pronto. A ferramenta organiza tudo o que você contou...
>
> ...e pronto: a capa do seu curso, as disciplinas, as primeiras aulas e o potencial da primeira turma. Tudo isso de graça.
>
> Quer o resto? O plano completo libera todas as aulas, o roteiro de gravação, o funil de vendas, o texto da sua página e o cronograma até a aula magna, por noventa e sete reais.
>
> E no final do plano, um especialista da Faculdade FEX Educação® te ajuda a transformar tudo isso em uma pós-graduação com validade acadêmica. Agora é com você!

### Cenas

| # | Tempo | Cena | Narração | Visual | Gê | Texto na tela | Som | Tela |
|---|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Vinheta | (sem fala) | Vinheta escura: "Seção 7 de 7 · ENVIO". | Gê entra segurando um envelope verde. | Seção 7 de 7 · ENVIO | Whoosh. | quadro desenhado |
| 2 | 0:03–0:11 | Por que importa | Último passo! Aqui você deixa o seu contato e vê o seu curso montado na sua frente. | O envelope abre e de dentro sai a capa de um curso. | Gê animado. | Seu curso montado | Papel. | quadro desenhado |
| 3 | 0:11–0:25 | Contato | Escreva o seu e-mail e o seu WhatsApp. É para lá que vai o seu plano, e é por onde um especialista da FEX pode falar com você, se você quiser. | Tela de contato, digitação nos campos. A caixa de consentimento recebe o check. | Gê segurando um celular. | Seu plano vai para o seu contato | Digitação. | `telas/07-envio-1-contato.jpg` |
| 4 | 0:25–0:31 | Montagem | Clique em Ver meu curso pronto. A ferramenta organiza tudo o que você contou... | Tela de análise: a esfera verde pulsa e a lista ganha checks um a um (acelerar se precisar). | Gê com os olhos fechados, concentrado, mãos brilhando. | Organizando… | Ticks de checklist. | `telas/07-envio-2-analise.jpg` |
| 5 | 0:31–0:41 | Prévia | ...e pronto: a capa do seu curso, as disciplinas, as primeiras aulas e o potencial da primeira turma. Tudo isso de graça. | A capa do curso entra com inclinação 3D. A câmera desce pela matriz e abre a primeira disciplina mostrando as aulas. | Gê comemorando. | Grátis | Revelação. | `telas/07-envio-3-previa.jpg` |
| 6 | 0:41–0:57 | Plano completo | Quer o resto? O plano completo libera todas as aulas, o roteiro de gravação, o funil de vendas, o texto da sua página e o cronograma até a aula magna, por noventa e sete reais. | Os cards com cadeado se abrem um a um (cadeado salta e some). Termina no botão "Desbloquear plano completo por R$ 97". | Gê girando uma chave. | Plano completo · R$ 97 | Cadeados abrindo. | `telas/07-envio-5-previa-desbloquear.jpg` |
| 7 | 0:57–1:09 | Próximo passo | E no final do plano, um especialista da Faculdade FEX Educação® te ajuda a transformar tudo isso em uma pós-graduação com validade acadêmica. Agora é com você! | Botão verde gigante pulsando com o ícone do WhatsApp. Confete verde. Fecha com o logo FEX Educação e #sejaFEX. | Gê comemorando, depois acena para a câmera. | Faculdade FEX Educação® · #sejaFEX | Acorde final. | quadro desenhado |

## Prompt de referência do personagem (para geradores de imagem e vídeo)

```
2D flat cartoon mascot named "Gê": a friendly genie made of bright green (#32CD32) with darker green shading (#1E9E1E), thick black outline, no legs, body tapering into a curled smoke tail, large white oval eyes with black pupils, expressive black eyebrows, simple smile, a black graduation cap (mortarboard) tilted on the head with a light green tassel, thin rounded arms with simple mitten hands. Clean vector style, flat colors, no gradients except subtle shading, modern premium explainer animation look, not childish. Background: dark green textured (#040805) or warm sand (#F4F2EC).
```
