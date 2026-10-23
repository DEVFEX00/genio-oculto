"""Fonte única dos roteiros dos vídeos tutoriais (um por seção do construtor).
Gera docs/ROTEIROS-VIDEOS.md e docs/storyboard.html (com as telas de docs/telas embutidas).
Uso: python3 tools/roteiros.py"""
import base64, html, io, json, pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
TELAS = ROOT / "docs" / "telas"
WPS = 2.5  # palavras por segundo (150 por minuto)

# Cada cena: tipo, narração, visual, personagem, texto na tela, som, tela de referência (arquivo em docs/telas) ou quadro desenhado.
# "frame" desenha um quadro de referência: {"bg": "dark|light", "word": "...", "pose": "...", "sub": "..."}
SECOES = [
 {"n": 1, "key": "voce", "nome": "Você", "fundo": "dark",
  "objetivo": "Mostrar que o curso nasce da experiência da pessoa e ensinar as 4 primeiras respostas: nome, área, anos de prática e as perguntas que ela mais ouve.",
  "cenas": [
   {"t": "Vinheta", "fixo": 3.5, "narr": "",
    "vis": "Fundo verde-escuro com textura. A barra verde do logo FEX atravessa a tela da esquerda para a direita e, por onde passa, revela o selo \"Seção 1 de 7\" e a palavra VOCÊ em Montserrat Bold gigante.",
    "per": "Gê surge de uma espiral de fumaça verde no canto direito e acena.", "txt": "Seção 1 de 7 · VOCÊ", "som": "Whoosh curto + nota de abertura.",
    "frame": {"bg": "dark", "word": "VOCÊ", "pose": "acenando", "sub": "Seção 1 de 7"}},
   {"t": "Por que importa", "narr": "Oi! Eu sou o Gê, e vou te acompanhar na criação do seu curso. Esta primeira seção é sobre a parte mais importante dele: você. O seu curso nasce da sua experiência, e isso ninguém consegue copiar.",
    "vis": "Gê no centro. Quando a narração diz \"você\", ele aponta para a câmera e a palavra VOCÊ pulsa atrás dele. Três ícones orbitam o Gê: maleta (área), relógio (anos), balão de fala (perguntas).",
    "per": "Apontando para a câmera, depois mão no peito em \"isso ninguém consegue copiar\".", "txt": "Seu curso nasce da sua experiência", "som": "Pop leve em cada ícone.",
    "frame": {"bg": "dark", "word": "VOCÊ", "pose": "apontando", "sub": "Seu curso nasce da sua experiência"}},
   {"t": "Nome", "narr": "Primeiro, escreva o seu nome e sobrenome. É ele que assina o curso como especialista responsável.",
    "vis": "Tela do app dentro de um notebook flutuando. Zoom no campo Nome. A mão-cursor clica e o texto \"Carla Exemplo\" aparece letra a letra. Corte rápido para o painel \"Seu curso, ao vivo\": o nome surge num chip.",
    "per": "Gê pequeno no canto segurando um crachá em branco que ganha o nome.", "txt": "Seu nome assina o curso", "som": "Digitação suave.", "tela": "01-voce-1-nome.jpg"},
   {"t": "Área", "narr": "Depois, a sua área. Pode ser ampla ou bem específica, e quanto mais específica, mais fácil de vender. Se ela estiver nos botões, é só clicar.",
    "vis": "Zoom no campo de área, digitação de \"Sua área\". Os botões de atalho embaixo acendem em cascata, um por um. No painel ao lado, o título do curso aparece sozinho.",
    "per": "Gê com uma lupa sobre os botões.", "txt": "Quanto mais específica, mais fácil de vender", "som": "Ticks em cascata nos botões.", "tela": "01-voce-2-area.jpg"},
   {"t": "Anos de experiência", "narr": "Agora, arraste a barra até os seus anos de experiência. Repare no número que aparece: são milhares de horas de prática. Uma pós-graduação inteira tem trezentas e sessenta.",
    "vis": "A mão arrasta o controle. O contador de horas sobe rápido. Ao lado, uma pilha de relógios cresce até ficar maior que um único bloco escrito \"360h\".",
    "per": "Gê de queixo caído (pose surpreso).", "txt": "Milhares de horas × 360h", "som": "Contador subindo + \"ding\".", "tela": "01-voce-3-anos.jpg"},
   {"t": "Perguntas", "narr": "E aqui mora o seu gênio oculto: o que as pessoas sempre te perguntam? Escreva uma por linha, do jeito que você ouve no dia a dia. Cada pergunta dessas é uma aula esperando para ser gravada.",
    "vis": "Balões de fala saem de vários celulares desenhados e caem dentro do campo, virando linhas de texto. Em seguida cada linha se transforma num mini-card com um ícone de play escrito \"Aula\".",
    "per": "Gê pensando, depois sorriso quando os cards viram aulas.", "txt": "Cada pergunta é uma aula", "som": "Pops dos balões.", "tela": "01-voce-4-perguntas.jpg"},
   {"t": "Encerramento", "narr": "Pronto! Clique em Continuar e vamos conhecer o seu aluno.",
    "vis": "O botão Continuar pulsa em verde. A barra verde do logo passa e revela o card \"Próxima seção: Seu aluno\".",
    "per": "Gê aponta para o botão e acena.", "txt": "Próxima seção: Seu aluno", "som": "Whoosh de saída.",
    "frame": {"bg": "dark", "word": "CONTINUAR", "pose": "apontando", "sub": "Próxima seção: Seu aluno"}},
  ]},
 {"n": 2, "key": "aluno", "nome": "Seu aluno", "fundo": "light",
  "objetivo": "Fazer a pessoa escolher um aluno ideal concreto e escrever uma promessa que dá para enxergar acontecendo.",
  "cenas": [
   {"t": "Vinheta", "fixo": 3.5, "narr": "", "vis": "Mesma vinheta, agora em fundo areia claro (como a fase no app). Revela \"Seção 2 de 7 · SEU ALUNO\".",
    "per": "Gê entra flutuando pela esquerda.", "txt": "Seção 2 de 7 · SEU ALUNO", "som": "Whoosh.",
    "frame": {"bg": "light", "word": "SEU ALUNO", "pose": "acenando", "sub": "Seção 2 de 7"}},
   {"t": "Por que importa", "narr": "Um curso que fala com todo mundo não vende para ninguém. Nesta seção você decide para quem é o seu curso e o que essa pessoa vai conseguir fazer no final.",
    "vis": "Uma multidão de silhuetas cinza. Um holofote verde varre a multidão e para em uma única pessoa, que ganha cor.",
    "per": "Gê segurando o holofote.", "txt": "Para quem é o seu curso?", "som": "Clique de holofote.",
    "frame": {"bg": "light", "word": "PARA QUEM?", "pose": "explicando", "sub": "Um curso para todo mundo não vende para ninguém"}},
   {"t": "Aluno ideal", "narr": "Primeiro, descreva o seu aluno ideal em uma frase. Lembre: para fazer uma pós-graduação, a pessoa precisa ter uma graduação concluída. Se travar, clique em Sugerir com IA ou escolha uma das opções.",
    "vis": "Tela do app em fundo claro. A mão clica em \"Sugerir com IA\": faíscas verdes saem do botão e o texto se escreve sozinho no campo.",
    "per": "Gê segura um diploma com a etiqueta \"graduação concluída\".", "txt": "Pós exige graduação concluída", "som": "Brilho mágico curto no clique da IA.", "tela": "02-aluno-1-persona.jpg"},
   {"t": "Promessa", "narr": "Agora, a promessa. Termine a frase: depois do meu curso, o meu aluno vai conseguir... Pense na segunda-feira de manhã dele. O que muda no trabalho ou na vida?",
    "vis": "Uma folhinha de calendário vira e mostra SEGUNDA. A frase \"Ele vai conseguir…\" aparece grande, depois a tela do app com a promessa sendo escrita. A frase voa até a capa do curso no painel.",
    "per": "Gê pensando, com um balão mostrando o calendário.", "txt": "O que muda na segunda-feira?", "som": "Virada de página.", "tela": "02-aluno-2-promessa.jpg"},
   {"t": "Dica", "narr": "Evite promessas vagas, como crescer na carreira. Prefira algo que dá para ver acontecendo.",
    "vis": "Card cinza \"crescer na carreira\" ganha um X e se desfaz em pó. Card verde \"aplicar o método com segurança e ter resultado nos primeiros casos\" entra com um check.",
    "per": "Gê faz \"não\" com o dedo e depois joinha.", "txt": "Vago ✕ · Concreto ✓", "som": "Erro suave + acerto.",
    "frame": {"bg": "light", "word": "CONCRETO", "pose": "explicando", "sub": "Prefira o que dá para ver acontecendo"}},
   {"t": "Encerramento", "narr": "Promessa escrita? Continue, porque agora o seu curso vai ganhar forma.",
    "vis": "Botão Continuar pulsa. Barra verde revela \"Próxima seção: Seu método\".", "per": "Gê acena.", "txt": "Próxima seção: Seu método", "som": "Whoosh.",
    "frame": {"bg": "light", "word": "CONTINUAR", "pose": "apontando", "sub": "Próxima seção: Seu método"}},
  ]},
 {"n": 3, "key": "metodo", "nome": "Seu método", "fundo": "dark",
  "objetivo": "Mostrar a mágica principal: tema vira disciplina, disciplina vira quatro aulas. Ensinar temas, ferramentas, referências e a pergunta \"você já ensina?\".",
  "cenas": [
   {"t": "Vinheta", "fixo": 3.5, "narr": "", "vis": "Vinheta em fundo escuro: \"Seção 3 de 7 · SEU MÉTODO\".", "per": "Gê gira e para de frente.", "txt": "Seção 3 de 7 · SEU MÉTODO", "som": "Whoosh.",
    "frame": {"bg": "dark", "word": "SEU MÉTODO", "pose": "acenando", "sub": "Seção 3 de 7"}},
   {"t": "Por que importa", "narr": "É nesta seção que o seu curso ganha forma. Cada tema vira uma disciplina, e cada disciplina ganha quatro aulas, no padrão pedagógico da Faculdade FEX Educação®.",
    "vis": "Diagrama animado: um bloco \"Tema\" encaixa e vira um bloco maior \"Disciplina\", que se divide em quatro blocos \"Aula\" que se alinham embaixo, como peças de montar.",
    "per": "Gê empilha os blocos com as mãos.", "txt": "Tema → Disciplina → 4 aulas", "som": "Cliques de encaixe.",
    "frame": {"bg": "dark", "word": "TEMA → 4 AULAS", "pose": "explicando", "sub": "Cada tema vira uma disciplina"}},
   {"t": "Temas", "narr": "Escreva um grande tema que você ensinaria e aperte Enter. Olha só: ele aparece na hora no painel, como disciplina. De três a cinco temas é o ideal.",
    "vis": "Digitação de \"Tema 01\" + Enter. Uma seta curva desenhada liga o campo ao painel e o card da disciplina voa até lá. Repete rápido com Tema 02 e Tema 03 (acelerado 2x).",
    "per": "Gê acompanha o card voando com os olhos.", "txt": "Enter ↵ = nova disciplina", "som": "Whoosh pequeno a cada card.", "tela": "03-metodo-1-temas.jpg"},
   {"t": "O que vem pronto", "narr": "A disciplina de fundamentos, a de ferramentas e o projeto final, a gente já cria para você.",
    "vis": "No painel, três cards ganham uma estrelinha e o selo \"automático\".", "per": "Gê com uma varinha de condão (estrelas verdes).", "txt": "3 disciplinas automáticas", "som": "Brilho.",
    "frame": {"bg": "dark", "word": "AUTOMÁTICO", "pose": "comemorando", "sub": "Fundamentos · Ferramentas · Projeto final"}},
   {"t": "Ferramentas", "narr": "Depois, as ferramentas que você usa no trabalho: fichas, checklists, roteiros, o seu passo a passo. É isso que deixa o seu curso diferente de qualquer outro.",
    "vis": "Uma caixa de ferramentas desenhada abre e os itens saltam para a lista do app. Clique em \"Sugerir com IA\" mostra três sugestões entrando.",
    "per": "Gê segura a caixa de ferramentas.", "txt": "O seu jeito de fazer", "som": "Metais leves (tim tim).", "tela": "03-metodo-2-ferramentas.jpg"},
   {"t": "Referências e \"você já ensina?\"", "narr": "Se tiver autores ou livros que você segue, escreva. Se não lembrar agora, pode pular. Por último, conte se você já ensina hoje.",
    "vis": "Tela das referências com o link \"Pular esta\" circulado à mão em verde. Corte para a tela de opções: a mão escolhe \"Curso online\".",
    "per": "Gê folheando um livro.", "txt": "Pode pular se não lembrar", "som": "Página virando.", "tela": "03-metodo-3-referencias.jpg"},
   {"t": "Encerramento", "narr": "Olha o seu curso tomando forma ali do lado. Clique em Continuar para escolher o formato.",
    "vis": "Câmera passeia pelo painel com todas as disciplinas. Barra verde revela \"Próxima seção: Seu formato\".", "per": "Gê aplaude.", "txt": "Próxima seção: Seu formato", "som": "Whoosh.", "tela": "03-metodo-4-ensina.jpg"},
  ]},
 {"n": 4, "key": "formato", "nome": "Seu formato", "fundo": "light",
  "objetivo": "Explicar a recomendação de formato, o padrão 30/30/40 (grava-se muito menos do que se imagina) e a lógica de vender a parcela.",
  "cenas": [
   {"t": "Vinheta", "fixo": 3.5, "narr": "", "vis": "Vinheta em fundo claro: \"Seção 4 de 7 · SEU FORMATO\".", "per": "Gê entra.", "txt": "Seção 4 de 7 · SEU FORMATO", "som": "Whoosh.",
    "frame": {"bg": "light", "word": "SEU FORMATO", "pose": "acenando", "sub": "Seção 4 de 7"}},
   {"t": "Por que importa", "narr": "Agora você decide o formato do curso e quanto o seu aluno vai investir. Fica tranquilo: a ferramenta já sugere o melhor caminho para você.",
    "vis": "Quatro cards (Pós 6 meses, Pós 12 meses, MBA 6 meses, MBA 12 meses) giram como cartas e um deles se destaca com o selo \"Recomendado para você\".",
    "per": "Gê embaralhando as cartas.", "txt": "A sugestão já vem pronta", "som": "Cartas embaralhando.",
    "frame": {"bg": "light", "word": "PÓS OU MBA?", "pose": "pensando", "sub": "A ferramenta sugere o melhor caminho"}},
   {"t": "Formato recomendado", "narr": "MBA combina com gestão e negócios. O formato com mediação ao vivo combina com áreas mais práticas. Se quiser, é só trocar.",
    "vis": "Tela do app em fundo claro. O selo \"Recomendado para você\" brilha. A mão clica em outro card só para mostrar que dá para trocar, depois volta.",
    "per": "Gê apontando para o selo.", "txt": "Você pode trocar", "som": "Clique.", "tela": "04-formato-1-modelo.jpg"},
   {"t": "Padrão 30/30/40", "narr": "E repare nesta barra. Numa pós de trezentas e sessenta horas, só trinta por cento é hora-aula. São cento e oito horas para gravar, não trezentas e sessenta.",
    "vis": "Uma barra cheia \"360h\" se divide em três blocos: verde \"108h hora-aula\", verde-escuro \"autoestudo\", areia \"prática\". Uma câmera de vídeo pousa só sobre o bloco verde.",
    "per": "Gê limpa o suor da testa, aliviado.", "txt": "Você grava 108h, não 360h", "som": "Três cliques + suspiro de alívio.",
    "frame": {"bg": "light", "word": "108h", "pose": "comemorando", "sub": "Só 30% é hora-aula"}},
   {"t": "Nome do curso", "narr": "Confira o nome do curso. Dá para editar ou pedir uma sugestão à IA.",
    "vis": "Zoom no campo \"Nome do curso\" e no botão \"Sugerir com IA\", que troca o nome com faíscas.", "per": "Gê com um balão \"ideias\".", "txt": "Nome editável", "som": "Brilho.", "tela": "04-formato-1-modelo.jpg"},
   {"t": "Investimento", "narr": "Por último, o investimento do aluno. Em pós-graduação, a gente vende a parcela, não o valor total, porque o aluno compara com a mensalidade de uma faculdade. Escolha o valor que faz sentido para o seu público.",
    "vis": "Um bloco grande com o valor total se quebra em 12 blocos pequenos de parcela, que se alinham como um calendário. Corte para a tela das opções de parcela com a mão escolhendo uma.",
    "per": "Gê segura uma calculadora.", "txt": "Venda a parcela", "som": "Moedinhas leves.", "tela": "04-formato-2-ticket.jpg"},
   {"t": "Encerramento", "narr": "Formato escolhido. Agora vem a parte que mais surpreende: o seu potencial.",
    "vis": "Barra verde revela \"Próxima seção: Seu potencial\".", "per": "Gê com olhar curioso.", "txt": "Próxima seção: Seu potencial", "som": "Whoosh.",
    "frame": {"bg": "light", "word": "CONTINUAR", "pose": "apontando", "sub": "Próxima seção: Seu potencial"}},
  ]},
 {"n": 5, "key": "potencial", "nome": "Seu potencial", "fundo": "dark",
  "objetivo": "Mostrar quanto a primeira turma pode faturar e o valor que vem só da base que já confia na pessoa. Deixar claro que é projeção.",
  "cenas": [
   {"t": "Vinheta", "fixo": 3.5, "narr": "", "vis": "Vinheta escura: \"Seção 5 de 7 · SEU POTENCIAL\".", "per": "Gê entra.", "txt": "Seção 5 de 7 · SEU POTENCIAL", "som": "Whoosh.",
    "frame": {"bg": "dark", "word": "SEU POTENCIAL", "pose": "acenando", "sub": "Seção 5 de 7"}},
   {"t": "Por que importa", "narr": "Esta é a seção que mais surpreende. Você vai ver quanto a primeira turma pode faturar com quem já te conhece.",
    "vis": "Um gráfico de barras desenhado cresce atrás do Gê.", "per": "Gê surpreso olhando o gráfico.", "txt": "Quanto a 1ª turma pode faturar?", "som": "Barras subindo.",
    "frame": {"bg": "dark", "word": "R$ ?", "pose": "surpreso", "sub": "O potencial da sua primeira turma"}},
   {"t": "Base quente", "narr": "Em base quente, coloque quantas pessoas já foram seus alunos, pacientes ou clientes. Elas já confiam em você.",
    "vis": "Um grupo de pessoinhas com um brilho verde em volta (confiança). A mão arrasta o controle da base quente no app.",
    "per": "Gê abraçando o grupo.", "txt": "Base quente = quem já confia em você", "som": "Arraste do controle.", "tela": "05-potencial-1-audiencia.jpg"},
   {"t": "Audiência fria", "narr": "Em audiência fria, entram os seus seguidores, a sua lista de e-mail e os seus contatos.",
    "vis": "Ícones genéricos de redes, e-mail e agenda flutuam como bolhas e entram no segundo controle.", "per": "Gê com um binóculo.", "txt": "Audiência fria = quem te acompanha", "som": "Bolhas.", "tela": "05-potencial-1-audiencia.jpg"},
   {"t": "Resultado", "narr": "Agora olhe o número verde: é o potencial da sua primeira turma. E a frase embaixo mostra quanto vem só da base quente, sem gastar nada com anúncio. É o dinheiro que já está na sua mesa.",
    "vis": "Zoom no card verde: o contador sobe. Depois, a frase de baixo é sublinhada à mão em verde. Plano final: uma mesa desenhada com uma pilha de contratos (folhas com um check), nada de dinheiro voando.",
    "per": "Gê comemorando.", "txt": "Projeção com os seus números, não é garantia.", "som": "Contador + \"ding\".",
    "frame": {"bg": "dark", "word": "NA SUA MESA", "pose": "comemorando", "sub": "Projeção com os seus números, não é garantia"}},
   {"t": "Encerramento", "narr": "Gostou do número? Então vamos planejar o lançamento.",
    "vis": "Barra verde revela \"Próxima seção: Lançamento\".", "per": "Gê aponta.", "txt": "Próxima seção: Lançamento", "som": "Whoosh.",
    "frame": {"bg": "dark", "word": "CONTINUAR", "pose": "apontando", "sub": "Próxima seção: Lançamento"}},
  ]},
 {"n": 6, "key": "lancamento", "nome": "Lançamento", "fundo": "light",
  "objetivo": "Ajudar a escolher o modelo de campanha e marcar a aula magna, entendendo os 90 dias de implantação.",
  "cenas": [
   {"t": "Vinheta", "fixo": 3.5, "narr": "", "vis": "Vinheta clara: \"Seção 6 de 7 · LANÇAMENTO\".", "per": "Gê entra com um megafone.", "txt": "Seção 6 de 7 · LANÇAMENTO", "som": "Whoosh.",
    "frame": {"bg": "light", "word": "LANÇAMENTO", "pose": "acenando", "sub": "Seção 6 de 7"}},
   {"t": "Por que importa", "narr": "Curso pronto que ninguém conhece não vira turma. Aqui você escolhe como vai abrir as matrículas e marca a data da aula magna.",
    "vis": "Uma porta desenhada com a placa \"Matrículas\" se abre e entra luz verde.", "per": "Gê abre a porta.", "txt": "Como abrir as matrículas", "som": "Porta abrindo.",
    "frame": {"bg": "light", "word": "MATRÍCULAS", "pose": "explicando", "sub": "Como você vai abrir a primeira turma"}},
   {"t": "Modelo de campanha", "narr": "Não existe um jeito certo. Tem base de alunos? Campanha interna. Tem audiência nas redes? Aula magna ao vivo. Base pequena e engajada? Lançamento relâmpago no WhatsApp. Escolha o que tem mais a ver com você hoje.",
    "vis": "Os 6 cards do app passam como um carrossel. Cada vez que a narração cita um modelo, o card correspondente sobe e acende. A mão escolhe \"Aula magna ao vivo\".",
    "per": "Gê de apresentador, apontando para cada card.", "txt": "Escolha o que combina com você hoje", "som": "Tick a cada card.", "tela": "06-lancamento-1-campanha.jpg"},
   {"t": "Aula magna", "narr": "Depois, marque a aula magna, a abertura oficial da turma. A implantação com a Faculdade FEX Educação® leva noventa dias, por isso a data mínima é daqui a noventa dias. E a ferramenta já mostra quando as suas matrículas abrem.",
    "vis": "Calendário desenhado: 90 quadradinhos se preenchem de verde rapidamente. Um marcador \"Matrículas abrem\" e uma estrela \"Aula magna\" aparecem. Corte para a tela do app com a data e a frase destacada.",
    "per": "Gê circula a data com um pincel verde.", "txt": "90 dias até a aula magna", "som": "Ticks rápidos + \"ding\".", "tela": "06-lancamento-2-magna.jpg"},
   {"t": "Encerramento", "narr": "Data marcada é projeto de verdade. Vamos para o último passo.",
    "vis": "Barra verde revela \"Próxima seção: Envio\".", "per": "Gê acena.", "txt": "Próxima seção: Envio", "som": "Whoosh.",
    "frame": {"bg": "light", "word": "DATA MARCADA", "pose": "comemorando", "sub": "Próxima seção: Envio"}},
  ]},
 {"n": 7, "key": "envio", "nome": "Envio", "fundo": "dark",
  "objetivo": "Pedir o contato, mostrar a prévia gratuita, apresentar o plano completo de R$ 97 e o próximo passo com o especialista FEX.",
  "cenas": [
   {"t": "Vinheta", "fixo": 3.5, "narr": "", "vis": "Vinheta escura: \"Seção 7 de 7 · ENVIO\".", "per": "Gê entra segurando um envelope verde.", "txt": "Seção 7 de 7 · ENVIO", "som": "Whoosh.",
    "frame": {"bg": "dark", "word": "ENVIO", "pose": "acenando", "sub": "Seção 7 de 7"}},
   {"t": "Por que importa", "narr": "Último passo! Aqui você deixa o seu contato e vê o seu curso montado na sua frente.",
    "vis": "O envelope abre e de dentro sai a capa de um curso.", "per": "Gê animado.", "txt": "Seu curso montado", "som": "Papel.",
    "frame": {"bg": "dark", "word": "ÚLTIMO PASSO", "pose": "explicando", "sub": "Seu curso montado na sua frente"}},
   {"t": "Contato", "narr": "Escreva o seu e-mail e o seu WhatsApp. É para lá que vai o seu plano, e é por onde um especialista da FEX pode falar com você, se você quiser.",
    "vis": "Tela de contato, digitação nos campos. A caixa de consentimento recebe o check.", "per": "Gê segurando um celular.", "txt": "Seu plano vai para o seu contato", "som": "Digitação.", "tela": "07-envio-1-contato.jpg"},
   {"t": "Montagem", "narr": "Clique em Ver meu curso pronto. A ferramenta organiza tudo o que você contou...",
    "vis": "Tela de análise: a esfera verde pulsa e a lista ganha checks um a um (acelerar se precisar).", "per": "Gê com os olhos fechados, concentrado, mãos brilhando.", "txt": "Organizando…", "som": "Ticks de checklist.", "tela": "07-envio-2-analise.jpg"},
   {"t": "Prévia", "narr": "...e pronto: a capa do seu curso, as disciplinas, as primeiras aulas e o potencial da primeira turma. Tudo isso de graça.",
    "vis": "A capa do curso entra com inclinação 3D. A câmera desce pela matriz e abre a primeira disciplina mostrando as aulas.", "per": "Gê comemorando.", "txt": "Grátis", "som": "Revelação.", "tela": "07-envio-3-previa.jpg"},
   {"t": "Plano completo", "narr": "Quer o resto? O plano completo libera todas as aulas, o roteiro de gravação, o funil de vendas, o texto da sua página e o cronograma até a aula magna, por noventa e sete reais.",
    "vis": "Os cards com cadeado se abrem um a um (cadeado salta e some). Termina no botão \"Desbloquear plano completo por R$ 97\".", "per": "Gê girando uma chave.", "txt": "Plano completo · R$ 97", "som": "Cadeados abrindo.", "tela": "07-envio-5-previa-desbloquear.jpg"},
   {"t": "Próximo passo", "narr": "E no final do plano, um especialista da Faculdade FEX Educação® te ajuda a transformar tudo isso em uma pós-graduação com validade acadêmica. Agora é com você!",
    "vis": "Botão verde gigante pulsando com o ícone do WhatsApp. Confete verde. Fecha com o logo FEX Educação e #sejaFEX.", "per": "Gê comemorando, depois acena para a câmera.", "txt": "Faculdade FEX Educação® · #sejaFEX", "som": "Acorde final.",
    "frame": {"bg": "dark", "word": "#sejaFEX", "pose": "comemorando", "sub": "Fale com o especialista FEX"}},
  ]},
]

def dur(c):
    return c.get("fixo") or round(len(c["narr"].split()) / WPS + 1.2, 1)

def tc(sec):
    return f"{int(sec // 60)}:{int(sec % 60):02d}"

def total(s):
    return sum(dur(c) for c in s["cenas"])

def thumb(name):
    im = Image.open(TELAS / name).convert("RGB")
    im.thumbnail((720, 720))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=72)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

# ---------------- Markdown ----------------
def markdown():
    out = ["# Gênio Oculto · Roteiros dos vídeos tutoriais (um por seção)", "",
           "Sete vídeos curtos, um para cada seção do construtor. Cada vídeo abre com a importância da seção e depois mostra o preenchimento na tela do aplicativo, com o personagem Gê narrando e apontando. Estilo: motion 2D (desenho animado chapado) sobre as telas reais do app.",
           "", "A versão visual, com as telas e o desenho do personagem, está em `docs/storyboard.html`. As telas de referência estão em `docs/telas/`.", "",
           "## Como ligar cada vídeo no app", "Suba no YouTube (pode ser não listado) e cole o ID no `CONFIG.VIDEOS` do `index.html`, na chave da seção:", "",
           "| Seção | Chave | Fundo do vídeo | Duração estimada |", "|---|---|---|---|"]
    for s in SECOES:
        out.append(f"| {s['n']}. {s['nome']} | `{s['key']}` | {'Escuro' if s['fundo']=='dark' else 'Claro (areia)'} | ~{round(total(s))}s |")
    out += ["", "## Direção geral",
            "- **Formato:** 16:9, 1920×1080 (é o formato do player do app). Opcional: versão 9:16 reaproveitando as cenas para Reels e remarketing.",
            "- **Voz:** feminina, calorosa e clara, a \"professora que todo mundo queria ter tido\". Ritmo de ~150 palavras por minuto. É a voz do Gê.",
            "- **Personagem Gê:** gênio da lâmpada em verde FEX, com capelo de formatura, cauda de fumaça em espiral no lugar das pernas, contorno preto e cores chapadas. Inteligente e acolhedor, nunca infantil. Poses: acenando, apontando, explicando, pensando, surpreso, comemorando.",
            "- **Telas:** use as capturas de `docs/telas/` dentro de um notebook flutuante desenhado (ou em tela cheia com zoom). Mão-cursor 2D branca com contorno preto. Texto digitado aparece letra a letra.",
            "- **Fundo:** igual à fase no app. Seções 1, 3, 5 e 7 em verde-escuro com textura leve; seções 2, 4 e 6 em areia claro (#F4F2EC).",
            "- **Transição assinatura:** a barra verde do meio do \"E\" do logo FEX atravessa a tela e revela a cena seguinte.",
            "- **Tipografia:** Montserrat. Palavras-chave em Bold gigante (VOCÊ, SEU ALUNO…), frases de apoio em Light.",
            "- **Legendas:** sempre queimadas (muita gente assiste sem som), Montserrat Bold branca em pílula preta 80% opaca, na parte de baixo.",
            "- **Som:** trilha leve e otimista bem baixa sob a voz; pops em cards, digitação suave, whoosh nas transições, \"ding\" quando algo se completa.",
            "- **Cores:** verde #32CD32, verde brilho #00D84F, preto #040805, areia #E8E4D9 / #F4F2EC.",
            "- **Regras de texto:** sempre \"Faculdade FEX Educação®\"; nunca \"reconhecido pelo MEC\" ou \"chancela\"; use \"validade acadêmica\". Valores do simulador são projeção, não garantia.",
            ""]
    for s in SECOES:
        out += [f"## Seção {s['n']} · {s['nome']}  (chave `{s['key']}`, ~{round(total(s))}s, fundo {'escuro' if s['fundo']=='dark' else 'claro'})", "", f"**Objetivo:** {s['objetivo']}", "",
                "### Narração completa", ""]
        out.append("> " + "\n>\n> ".join(c["narr"] for c in s["cenas"] if c["narr"]))
        out += ["", "### Cenas", "", "| # | Tempo | Cena | Narração | Visual | Gê | Texto na tela | Som | Tela |", "|---|---|---|---|---|---|---|---|---|"]
        t = 0
        for i, c in enumerate(s["cenas"], 1):
            d = dur(c)
            esc = lambda x: x.replace("|", "\\|")
            out.append(f"| {i} | {tc(t)}–{tc(t+d)} | {esc(c['t'])} | {esc(c['narr']) or '(sem fala)'} | {esc(c['vis'])} | {esc(c['per'])} | {esc(c['txt'])} | {esc(c['som'])} | {('`telas/'+c['tela']+'`') if c.get('tela') else 'quadro desenhado'} |")
            t += d
        out.append("")
    out += ["## Prompt de referência do personagem (para geradores de imagem e vídeo)", "",
            "```", "2D flat cartoon mascot named \"Gê\": a friendly genie made of bright green (#32CD32) with darker green shading (#1E9E1E), thick black outline, no legs, body tapering into a curled smoke tail, large white oval eyes with black pupils, expressive black eyebrows, simple smile, a black graduation cap (mortarboard) tilted on the head with a light green tassel, thin rounded arms with simple mitten hands. Clean vector style, flat colors, no gradients except subtle shading, modern premium explainer animation look, not childish. Background: dark green textured (#040805) or warm sand (#F4F2EC).", "```", ""]
    return "\n".join(out)

# ---------------- HTML ----------------
def page():
    data = []
    for s in SECOES:
        t = 0; cenas = []
        for c in s["cenas"]:
            d = dur(c); cc = dict(c); cc["ini"] = tc(t); cc["fim"] = tc(t + d)
            if c.get("tela"): cc["img"] = thumb(c["tela"])
            cenas.append(cc); t += d
        data.append({**s, "cenas": cenas, "total": round(t)})
    tpl = (ROOT / "tools" / "storyboard.tpl.html").read_text(encoding="utf-8")
    return tpl.replace("/*DATA*/", "const SECOES = " + json.dumps(data, ensure_ascii=False) + ";")

if __name__ == "__main__":
    (ROOT / "docs" / "ROTEIROS-VIDEOS.md").write_text(markdown(), encoding="utf-8")
    (ROOT / "docs" / "storyboard.html").write_text(page(), encoding="utf-8")
    for s in SECOES: print(s["key"], round(total(s)), "s")
