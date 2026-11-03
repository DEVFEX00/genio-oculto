"""Fonte única dos 7 vídeos tutoriais (um por seção do construtor), versão extensão universitária.
Gera docs/ROTEIROS-VIDEOS.md e dist/roteiros.html (página com as telas, para o produtor de motion).
Uso: python3 tools/roteiros.py"""
import base64, html, io, pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
TELAS = ROOT / "docs" / "telas"
WPS = 2.4  # palavras por segundo de narração (cerca de 145 por minuto)

ESTILO = [
    ("Formato", "16:9, 1920×1080, 30 fps. Entre 45 e 75 segundos por vídeo. O vídeo abre dentro do próprio app, num player 16:9."),
    ("Linguagem", "Motion design 2D: as telas reais do app (pasta docs/telas) aparecem num notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto sendo digitado letra a letra. Palavras-chave da narração viram tipografia animada. Ícones e formas se desenhando entre as telas. Nada de tela parada: a cada segundo algo se constrói."),
    ("Personagem", "O Gênio Oculto (opcional): mascote 2D em verde FEX, com capelo de formatura e cauda de fumaça no lugar das pernas, contorno preto, cores chapadas. Acolhedor, nunca infantil. Aparece na abertura, aponta para o campo da vez e comemora no fim de cada seção."),
    ("Fundo", "Igual à fase no app: seções 1, 3, 5 e 7 em verde quase preto com textura leve de granulado; seções 2, 4 e 6 em areia clara (#F4F2EC). Sem faixas de luz exageradas."),
    ("Cores e fonte", "Verde #32CD32, verde brilho #00D84F, preto #040805, areia #E8E4D9. Montserrat: palavras-chave em Bold grande, frases em Light."),
    ("Abertura e transição", "Vinheta de 3 s: a barra verde do meio do \"E\" do logo FEX atravessa a tela e revela \"Seção N de 7 · NOME\". Use a mesma barra verde como transição entre cenas."),
    ("Encerramento", "Toda seção termina com a mensagem de conquista que o app mostra (está em cada roteiro) e o card \"Próxima seção: ...\"."),
    ("Voz", "Feminina, calorosa e clara, ritmo de conversa. Tom de quem acredita na pessoa: o público duvida de si (síndrome do impostor, medo de julgamento, medo de ser enganado). Encorajar sem exagerar e sem prometer resultado."),
    ("Som", "Trilha leve e otimista bem baixa sob a voz. Pop quando um card aparece, digitação suave, whoosh na transição, \"ding\" quando algo se completa."),
    ("Legendas", "Recomendadas (muita gente assiste no celular): Montserrat Bold branca em pílula preta, na parte de baixo."),
    ("Regras de texto", "Sempre \"Faculdade FEX Educação\". Falar em extensão universitária, nunca em pós-graduação ou MBA. Nunca dizer \"reconhecido pelo MEC\", \"chancela\" ou \"certificação MEC\". Na carga horária, nunca usar \"autoestudo\" nem \"o resto\". Valores do simulador são projeção, não garantia."),
]

SECOES = [
 {"n": 1, "key": "voce", "nome": "Você", "fundo": "escuro",
  "porque": "O curso nasce da experiência da pessoa. Aqui ela conta quem é, a área, os anos de prática e no mínimo 7 perguntas que sempre ouve. Cada pergunta vira uma aula.",
  "narracao": [
   "Oi! Eu sou o Gênio Oculto, e vou te acompanhar na criação da sua formação. Esta primeira seção é sobre a parte mais importante dela: você. O seu curso nasce da sua experiência, e isso ninguém consegue copiar.",
   "Primeiro, escreva o seu nome e sobrenome. É ele que assina o curso como especialista responsável.",
   "Depois, a sua área. Pode ser ampla ou bem específica. Se ela estiver nos botões, é só clicar.",
   "Agora, arraste a barra até os seus anos de experiência. Repare no número que aparece: são milhares de horas de prática. E experiência não precisa de diploma para valer.",
   "E aqui mora o seu gênio oculto: o que as pessoas sempre te perguntam? Escreva no mínimo sete perguntas, uma por linha, do jeito que você ouve no dia a dia. Não existe pergunta boba. Cada uma vira uma aula, e a gente organiza tudo em módulos para você. Se travar, clique em Sugerir com IA.",
   "Pronto! Clique em Continuar e vamos conhecer o seu aluno.",
  ],
  "cenas": [
   ("Vinheta", "", "Barra verde do logo revela \"Seção 1 de 7 · VOCÊ\". O Gênio surge de uma espiral de fumaça e acena.", "VOCÊ"),
   ("Por que importa", "", "A palavra VOCÊ cresce atrás do Gênio, que aponta para a câmera. Ícones orbitam: maleta (área), relógio (anos), balão de fala (perguntas).", "Seu curso nasce da sua experiência"),
   ("Nome", "1-voce-a-nome.jpg", "Zoom no campo Nome. A mão-cursor clica e \"Carla Exemplo\" é digitado letra a letra.", "Seu nome assina o curso"),
   ("Área", "1-voce-b-area.jpg", "Digitação de \"Sua área\". Os botões de atalho acendem em cascata.", ""),
   ("Anos", "1-voce-c-anos.jpg", "A mão arrasta a barra. O contador de horas sobe rápido; ao lado, uma pilha de relógios cresce.", "Milhares de horas de prática"),
   ("Perguntas", "1-voce-d-perguntas-3-de-7.jpg", "Três perguntas digitadas. O contador mostra \"3 de 7 · faltam 4\" e a barrinha verde avança.", "No mínimo 7 perguntas"),
   ("Cada pergunta vira aula", "1-voce-e-perguntas-ok.jpg", "Clique em Sugerir com IA: as perguntas completam a lista e o contador fica verde. Cada linha se transforma num mini-card com ícone de play escrito \"Aula\".", "Não existe pergunta boba"),
   ("Encerramento", "2-aluno-a-conquista-e-aluno-ideal.jpg", "Mostra o banner verde de conquista da seção. Card \"Próxima seção: Seu aluno\".", "Você acabou de mostrar as aulas que só você sabe dar"),
  ]},
 {"n": 2, "key": "aluno", "nome": "Seu aluno", "fundo": "claro",
  "porque": "Curso que fala com todo mundo não vende para ninguém. Aqui a pessoa define o aluno ideal e a promessa: o que ele vai conseguir fazer no final.",
  "narracao": [
   "Um curso que fala com todo mundo não vende para ninguém. Nesta seção você decide para quem é o seu curso e o que essa pessoa vai conseguir fazer no final.",
   "Primeiro, descreva o seu aluno ideal em uma frase. Você não precisa ensinar para todo mundo: basta ensinar para quem precisa do que você já sabe. Se travar, clique em Sugerir com IA ou escolha uma das opções.",
   "Agora, a promessa. Complete a frase: ele vai conseguir. Pense na segunda-feira de manhã do seu aluno. O que muda no trabalho ou na vida dele?",
   "Prometa só o que você já entrega na prática. Sem exagero: a sua verdade é o que convence.",
   "Promessa escrita? Continue, porque agora vem o seu método.",
  ],
  "cenas": [
   ("Vinheta", "", "Vinheta em fundo areia: \"Seção 2 de 7 · SEU ALUNO\".", "SEU ALUNO"),
   ("Por que importa", "", "Uma multidão de silhuetas cinza. Um holofote verde varre e para em uma pessoa, que ganha cor.", "Para quem é o seu curso?"),
   ("Aluno ideal", "2-aluno-a-conquista-e-aluno-ideal.jpg", "Zoom no campo do aluno ideal e na frase de apoio com borda verde.", "Ensine para quem precisa do que você sabe"),
   ("Sugerir com IA", "2-aluno-b-sugerir-com-ia.jpg", "Clique em Sugerir com IA: faíscas verdes e o texto se escreve sozinho.", ""),
   ("Promessa", "2-aluno-c-promessa.jpg", "Folhinha de calendário vira e mostra SEGUNDA. \"Ele vai conseguir…\" grande, e a promessa sendo escrita.", "O que muda na segunda-feira?"),
   ("Dica", "", "Card cinza \"crescer na carreira\" ganha um X e se desfaz. Card verde com uma promessa concreta entra com um check.", "Sem exagero: a sua verdade convence"),
   ("Encerramento", "3-metodo-a-conquista-e-ferramentas.jpg", "Banner de conquista da seção e card \"Próxima seção: Seu método\".", "Agora o seu curso tem endereço certo"),
  ]},
 {"n": 3, "key": "metodo", "nome": "Seu método", "fundo": "escuro",
  "porque": "As perguntas já viraram aulas e módulos (quem organiza é a ferramenta, não a pessoa). Aqui ela conta o que deixa o curso único: ferramentas, referências e se já ensina.",
  "narracao": [
   "Lembra das perguntas que você escreveu? Cada uma já virou uma aula, e a gente organizou tudo em módulos para você. Nesta seção, você conta o que deixa o seu curso diferente.",
   "Primeiro, as ferramentas que você usa no trabalho: fichas, checklists, roteiros, o seu passo a passo. Escreva e aperte Enter, ou clique em Sugerir com IA. Aquilo que parece simples para você é o atalho que o seu aluno procura há anos.",
   "Se tiver autores, livros ou métodos que você segue, escreva. Se não lembrar agora, pode pular.",
   "Por último, conte se você já ensina hoje. Isso ajuda a escolher o melhor jeito de lançar.",
   "Clique em Continuar para descobrir o formato ideal do seu curso.",
  ],
  "cenas": [
   ("Vinheta", "", "Vinheta escura: \"Seção 3 de 7 · SEU MÉTODO\".", "SEU MÉTODO"),
   ("Perguntas viram módulos", "", "Os cards de pergunta da seção 1 voam e se encaixam em blocos de módulo (Primeiros passos, O método na prática, Erros comuns...), como peças de montar.", "Pergunta → Aula → Módulo"),
   ("Ferramentas", "3-metodo-a-conquista-e-ferramentas.jpg", "Uma caixa de ferramentas desenhada abre. Digitação + Enter adiciona uma ferramenta na lista.", "O seu jeito de fazer"),
   ("Sugerir com IA", "3-metodo-b-ferramentas-ok.jpg", "Clique em Sugerir com IA: três ferramentas entram na lista com pop.", "O simples para você é o atalho do aluno"),
   ("Referências", "3-metodo-c-referencias.jpg", "Livro se desenha ao lado. O link \"Pular esta\" é circulado à mão em verde.", "Pode pular se não lembrar"),
   ("Já ensina?", "3-metodo-d-ja-ensina.jpg", "A mão escolhe \"Curso online\" entre as quatro opções.", ""),
   ("Encerramento", "4-formato-a-conquista-e-objetivo.jpg", "Banner de conquista e card \"Próxima seção: Seu formato\".", "Suas ferramentas são o que ninguém copia"),
  ]},
 {"n": 4, "key": "formato", "nome": "Seu formato", "fundo": "claro",
  "porque": "Seção mais importante para a FEX: sem a FEX é curso livre, com a FEX é extensão universitária. A pessoa diz o objetivo, a ferramenta indica uma das 4 titulações, ela ajusta a carga horária, confere o nome e escolhe o preço em parcelas.",
  "narracao": [
   "Agora vem uma parte importante. Sem a FEX, o seu curso é um curso livre. Com a FEX, ele vira um curso de extensão universitária, com certificado emitido pela Faculdade FEX Educação.",
   "Primeiro, escolha o que você quer que o curso seja para o aluno.",
   "Com isso, a ferramenta indica a titulação ideal entre as quatro da extensão: Iniciação, Atualização, Capacitação e Aperfeiçoamento. Você ajusta as horas na barra.",
   "A carga horária soma tudo o que é acompanhado pelo professor: aulas, leituras, estudos de caso, encontros de perguntas e respostas e prática. Você não precisa gravar todas as horas.",
   "Confira o nome do curso e, por último, o investimento: escolha uma faixa de parcela ou arraste a barra até o valor certo para o seu público. O seu conhecimento tem valor.",
   "Formato escolhido. Agora vem a parte que mais surpreende: o seu potencial.",
  ],
  "cenas": [
   ("Vinheta", "", "Vinheta em areia: \"Seção 4 de 7 · SEU FORMATO\".", "SEU FORMATO"),
   ("Curso livre × extensão", "", "Tela dividida: à esquerda um certificado simples, cinza, \"Curso livre\" (riscado). À direita, um certificado verde com o logo FEX: \"Extensão universitária\".", "Com a FEX, vira extensão universitária"),
   ("Objetivo", "4-formato-b-objetivo-escolhido.jpg", "As quatro opções de objetivo entram em cascata; a mão escolhe \"Capacitar para aplicar\".", ""),
   ("Titulação recomendada", "4-formato-c-titulacao-recomendada.jpg", "Os 4 cards (Iniciação, Atualização, Capacitação, Aperfeiçoamento) giram como cartas; o recomendado sobe com o selo verde.", "4 titulações de extensão"),
   ("Carga horária", "4-formato-d-carga-horaria.jpg", "A mão arrasta a barra de horas. Ícones aparecem um a um: aula, livro, estudo de caso, balão de perguntas, prática.", "Tudo acompanhado pelo professor"),
   ("Nome do curso", "4-formato-e-nome-do-curso.jpg", "Zoom no nome do curso; clique em Sugerir com IA troca o nome com faíscas.", ""),
   ("Preço", "4-formato-f-preco.jpg", "As faixas de 12x entram em cascata; a mão escolhe uma.", "12x de R$ 97 a 12x de R$ 5.000"),
   ("Barra da parcela", "4-formato-g-barra-da-parcela.jpg", "A mão arrasta a barra e o valor da parcela muda ao vivo.", "O seu conhecimento tem valor"),
   ("Encerramento", "5-potencial-a-conquista-e-audiencias.jpg", "Banner de conquista e card \"Próxima seção: Seu potencial\".", "Você não está sozinho nisso"),
  ]},
 {"n": 5, "key": "potencial", "nome": "Seu potencial", "fundo": "escuro",
  "porque": "Mostra quanto a primeira turma pode faturar com quem já conhece a pessoa, com a conta visível. Deixa claro que é projeção, não promessa.",
  "narracao": [
   "Esta é a seção que mais surpreende. Você vai ver quanto a primeira turma pode faturar com quem já te conhece.",
   "Em base quente, coloque quantas pessoas já foram seus alunos, pacientes ou clientes. Elas já confiam em você. A referência da FEX é três por cento de conversão.",
   "Em audiência fria, entram os seus seguidores, a sua lista de e-mail e os seus contatos. Aqui a referência é zero vírgula três por cento. Você pode mudar as duas, e a conta aparece embaixo de cada barra.",
   "Agora olhe o número verde: é o potencial da sua primeira turma. É uma projeção feita com os seus números, não uma promessa. E começar pequeno é normal: a primeira turma costuma vir de poucas pessoas que já confiam em você.",
   "Gostou do número? Então vamos planejar o lançamento.",
  ],
  "cenas": [
   ("Vinheta", "", "Vinheta escura: \"Seção 5 de 7 · SEU POTENCIAL\".", "SEU POTENCIAL"),
   ("Por que importa", "", "Um gráfico de barras se desenha atrás do Gênio, que fica surpreso.", "Quanto a 1ª turma pode faturar?"),
   ("Base quente", "5-potencial-a-conquista-e-audiencias.jpg", "Grupo de pessoinhas com brilho verde (confiança). A mão arrasta a barra; a conta \"800 pessoas × 3% = 24 matrículas\" aparece com destaque.", "Base quente: 3%"),
   ("Audiência fria", "5-potencial-a-conquista-e-audiencias.jpg", "Ícones de redes, e-mail e agenda flutuam como bolhas e entram na segunda barra; a conta com 0,3% aparece.", "Audiência fria: 0,3%"),
   ("Resultado", "5-potencial-b-resultado.jpg", "Zoom no card verde: o valor conta até o número. Uma etiqueta discreta: \"projeção, não promessa\".", "Projeção com os seus números"),
   ("Encerramento", "6-lancamento-a-conquista-e-campanhas.jpg", "Banner de conquista e card \"Próxima seção: Lançamento\".", "Vale a pena começar"),
  ]},
 {"n": 6, "key": "lancamento", "nome": "Lançamento", "fundo": "claro",
  "porque": "Escolher como abrir as matrículas e marcar o início da turma. O registro com a FEX leva até 30 dias.",
  "narracao": [
   "Curso pronto que ninguém conhece não vira turma. Aqui você escolhe como vai abrir as matrículas e quando a primeira turma começa.",
   "Não existe um jeito certo. Tem base de alunos? Campanha interna. Tem audiência nas redes? Aula ao vivo. Base pequena e engajada? Lançamento relâmpago no WhatsApp. Também dá para aproveitar datas como Black Friday, Natal e Ano Novo, nas campanhas sazonais.",
   "Depois, marque a data de início da turma. O registro do curso com a Faculdade FEX Educação leva até trinta dias, por isso a data mínima é daqui a trinta dias. A ferramenta já mostra quando as suas matrículas abrem.",
   "Ninguém se sente cem por cento pronto. Marcar a data é o que transforma vontade em projeto. Vamos para o último passo.",
  ],
  "cenas": [
   ("Vinheta", "", "Vinheta em areia: \"Seção 6 de 7 · LANÇAMENTO\". O Gênio entra com um megafone.", "LANÇAMENTO"),
   ("Por que importa", "", "Uma porta com a placa \"Matrículas\" se abre e entra luz verde.", "Como abrir as matrículas"),
   ("Campanhas", "6-lancamento-a-conquista-e-campanhas.jpg", "Os 6 cards passam em carrossel; cada um acende quando a narração cita. Mini ícones de Black Friday, Natal e Ano Novo no card de campanhas sazonais.", "Escolha o que combina com você hoje"),
   ("Início da turma", "6-lancamento-b-inicio-da-turma.jpg", "Calendário: 30 quadradinhos se preenchem (registro). Marcador \"Matrículas abrem\" e estrela \"Turma 1\".", "Registro em até 30 dias"),
   ("Encerramento", "7-envio-a-conquista-e-contato.jpg", "Banner de conquista e card \"Próxima seção: Envio\".", "Data marcada é projeto de verdade"),
  ]},
 {"n": 7, "key": "envio", "nome": "Envio", "fundo": "escuro",
  "porque": "Deixar o contato, ver o curso montado de graça, conhecer o plano completo de R$ 97 e o próximo passo com o Plano Bronze.",
  "narracao": [
   "Último passo! Aqui você deixa o seu contato e vê o seu curso montado na sua frente.",
   "Escreva o seu e-mail e o seu WhatsApp. É para lá que vai o seu plano, e é por onde um especialista da FEX pode falar com você, se você quiser.",
   "Clique em Ver meu curso pronto. A ferramenta organiza tudo o que você contou e mostra a capa do seu curso, os módulos, as primeiras aulas e o potencial da primeira turma. Tudo isso de graça. Você já sabia tudo isso. Agora está organizado.",
   "Quer o resto? O plano completo libera todas as aulas, o roteiro de gravação, o funil de vendas, o texto da sua página e o cronograma até a primeira turma, por noventa e sete reais.",
   "E no final do plano, um especialista da Faculdade FEX Educação te mostra como transformar o seu curso em extensão universitária, com o Plano Bronze. Agora é com você!",
  ],
  "cenas": [
   ("Vinheta", "", "Vinheta escura: \"Seção 7 de 7 · ENVIO\". O Gênio segura um envelope verde.", "ENVIO"),
   ("Contato", "7-envio-b-contato-preenchido.jpg", "Digitação nos campos de e-mail e WhatsApp; a caixa de consentimento recebe o check.", "Seu plano vai para o seu contato"),
   ("Organizando", "7-envio-c-organizando.jpg", "A esfera verde pulsa e a lista ganha checks um a um.", ""),
   ("Prévia", "7-envio-d-previa-capa.jpg", "A capa do curso entra com inclinação 3D; a câmera desce até os módulos.", "Grátis"),
   ("Módulos", "7-envio-e-previa-modulos.jpg", "O primeiro módulo abre e mostra as aulas (as perguntas da pessoa).", "Você já sabia. Agora está organizado"),
   ("Plano completo", "7-envio-f-previa-desbloquear.jpg", "Os cadeados dos cards saltam e somem um a um; termina no botão \"Desbloquear por R$ 97\".", "Plano completo · R$ 97"),
   ("Plano Bronze", "7-envio-j-plano-bronze-card.jpg", "O card do Plano Bronze entra com borda verde girando; os itens aparecem em sequência.", "Curso livre → extensão universitária"),
   ("Especialista", "7-envio-k-botao-especialista.jpg", "O botão verde gigante pulsa com o ícone do WhatsApp. Confete verde. Fecha com o logo FEX e #sejaFEX.", "Agora é com você!"),
  ]},
]


def palavras(s): return len(s.split())
def dur(s): return round(sum(palavras(p) for p in s["narracao"]) / WPS + 6)


def prompt(s):
    cenas = "\n".join(f"{i}. {c[0]}: {c[2]}" + (f" Tela: docs/telas/{c[1]}." if c[1] else "") + (f" Texto na tela: \"{c[3]}\"." if c[3] else "") for i, c in enumerate(s["cenas"], 1))
    narr = " ".join(s["narracao"])
    return (f"Crie um vídeo tutorial em motion design 2D, 16:9 (1920×1080), com cerca de {dur(s)} segundos, para a seção \"{s['nome']}\" "
            f"(seção {s['n']} de 7) do aplicativo Crie sua Formação, da Faculdade FEX Educação. O vídeo ensina a pessoa a preencher esta seção e abre "
            f"com uma introdução curta sobre por que ela importa para a criação do curso.\n\n"
            f"Objetivo da seção: {s['porque']}\n\n"
            f"Estilo: telas reais do app dentro de um notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto digitado letra a letra; "
            f"palavras-chave em tipografia animada (Montserrat Bold); ícones e formas se desenhando; mascote Gênio Oculto (gênio verde com capelo de formatura) "
            f"apontando e reagindo. Fundo {'verde quase preto com textura leve' if s['fundo']=='escuro' else 'areia clara (#F4F2EC)'}. Verde #32CD32, preto #040805, areia #E8E4D9. "
            f"Vinheta de 3 s com a barra verde do logo FEX revelando \"Seção {s['n']} de 7 · {s['nome'].upper()}\". Ritmo dinâmico: algo se constrói a cada segundo.\n\n"
            f"Narração (voz feminina, calorosa, encorajadora; o público costuma duvidar de si):\n\"{narr}\"\n\n"
            f"Cenas, na ordem da narração:\n{cenas}\n\n"
            f"Regras: falar em extensão universitária (nunca pós-graduação ou MBA); nunca dizer \"reconhecido pelo MEC\" ou \"chancela\"; "
            f"não usar \"autoestudo\" nem \"o resto\" para carga horária; números do simulador são projeção, não promessa.")


def markdown():
    o = ["# Crie sua Formação · Vídeos tutoriais por seção (extensão universitária)", "",
         "Material para a produção dos 7 vídeos de motion 2D, um por seção do construtor. Cada seção traz o objetivo, a narração final, as cenas com a tela do app e um **prompt pronto** para o produtor.",
         "", "As telas estão em `docs/telas/` (versão computador e `celular-`), preenchidas com um exemplo genérico.", "",
         "Depois de prontos, os vídeos entram no `CONFIG.VIDEOS` do `index.html` (ID do YouTube ou MP4 em `assets/videos/`), nas chaves abaixo.", "",
         "| Seção | Chave | Fundo | Duração estimada |", "|---|---|---|---|"]
    o += [f"| {s['n']}. {s['nome']} | `{s['key']}` | {s['fundo']} | ~{dur(s)}s |" for s in SECOES]
    o += ["", "## Direção geral", ""] + [f"- **{k}:** {v}" for k, v in ESTILO] + [""]
    for s in SECOES:
        o += [f"## {s['n']}. {s['nome']}  (chave `{s['key']}`, ~{dur(s)}s, fundo {s['fundo']})", "", f"**Por que importa:** {s['porque']}", "", "### Narração", ""]
        o += ["> " + "\n>\n> ".join(s["narracao"]), "", "### Cenas", "", "| # | Cena | O que acontece | Tela | Texto na tela |", "|---|---|---|---|---|"]
        o += [f"| {i} | {c[0]} | {c[2]} | {('`telas/'+c[1]+'`') if c[1] else 'animação'} | {c[3]} |" for i, c in enumerate(s["cenas"], 1)]
        o += ["", "### Prompt para o produtor", "", "```", prompt(s), "```", ""]
    return "\n".join(o)


def thumb(nome):
    im = Image.open(TELAS / nome).convert("RGB"); im.thumbnail((960, 960))
    b = io.BytesIO(); im.save(b, "JPEG", quality=72)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def pagina():
    e = html.escape
    sec = []
    for s in SECOES:
        cenas = "".join(f"""<li class="cena"><div class="cn">{i:02d}</div><div class="cb"><b>{e(c[0])}</b><p>{e(c[2])}</p>{f'<p class="tx">Texto na tela: “{e(c[3])}”</p>' if c[3] else ''}{f'<p class="arq">docs/telas/{e(c[1])}</p>' if c[1] else '<p class="arq">Animação (sem tela do app)</p>'}</div>{f'<img loading="lazy" src="{thumb(c[1])}" alt="Tela: {e(c[0])}">' if c[1] else '<div class="semtela">animação</div>'}</li>""" for i, c in enumerate(s["cenas"], 1))
        sec.append(f"""<section class="sec" id="{s['key']}"><div class="sh"><span class="num">{s['n']}</span><div><h2>{e(s['nome'])}</h2><p class="meta">Chave <code>{s['key']}</code> · ~{dur(s)} s · fundo {s['fundo']}</p></div></div>
<p class="pq">{e(s['porque'])}</p>
<h3>Narração</h3><blockquote>{''.join(f'<p>{e(p)}</p>' for p in s['narracao'])}</blockquote>
<h3>Cenas</h3><ol class="cenas">{cenas}</ol>
<h3>Prompt para o produtor <button class="cp" data-c="p{s['n']}">Copiar prompt</button></h3><pre id="p{s['n']}">{e(prompt(s))}</pre></section>""")
    nav = "".join(f'<a href="#{s["key"]}">{s["n"]}. {e(s["nome"])}</a>' for s in SECOES)
    est = "".join(f"<div><b>{e(k)}</b><p>{e(v)}</p></div>" for k, v in ESTILO)
    return f"""<title>Vídeos Crie sua Formação</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<style>
/* Documento de produção: claro, editorial, com a identidade FEX */
:root{{--bg:#F4F2EC;--card:#fff;--ink:#0A0F0B;--mut:#585E58;--line:rgba(10,15,11,.12);--g:#32CD32;--gd:#178a17;--dark:#040805;--sand:#E8E4D9;color-scheme:light}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 Montserrat,system-ui,sans-serif}}
.wrap{{max-width:1080px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
header{{background:var(--dark);color:var(--sand)}} header .wrap{{padding-block:48px 40px}}
header small{{color:var(--g);font-weight:800;letter-spacing:.24em;text-transform:uppercase;font-size:12px}}
h1{{font-weight:300;font-size:clamp(32px,5vw,56px);letter-spacing:-.03em;line-height:1.05;margin:14px 0 10px;color:#fff;text-wrap:balance}} h1 b{{font-weight:800}}
header p{{max-width:70ch;color:#cfd6cf;margin:0}}
nav{{display:flex;gap:8px;flex-wrap:wrap;margin-top:22px}} nav a{{color:var(--sand);text-decoration:none;border:1px solid rgba(232,228,217,.25);border-radius:999px;padding:6px 12px;font-size:14px;font-weight:600}} nav a:hover{{border-color:var(--g);color:#fff}}
.estilo{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin:32px 0}}
.estilo div{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;min-width:0}} .estilo b{{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--gd)}} .estilo p{{margin:6px 0 0;font-size:14.5px;color:var(--mut)}}
.sec{{padding-block:44px;border-top:1px solid var(--line)}}
.sh{{display:flex;gap:16px;align-items:center}} .num{{flex:none;width:52px;height:52px;border-radius:14px;background:var(--dark);color:var(--g);display:grid;place-items:center;font-weight:800;font-size:22px}}
h2{{margin:0;font-size:30px;letter-spacing:-.02em}} .meta{{margin:2px 0 0;color:var(--mut);font-size:14px}} code{{background:var(--sand);padding:1px 6px;border-radius:6px;font-size:13px}}
.pq{{font-size:17px;max-width:72ch}} h3{{font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--gd);margin:28px 0 12px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}}
blockquote{{margin:0;background:var(--card);border-left:4px solid var(--g);border-radius:0 14px 14px 0;padding:6px 20px}} blockquote p{{font-size:17px}}
.cenas{{list-style:none;margin:0;padding:0;display:grid;gap:10px}}
.cena{{display:grid;grid-template-columns:44px minmax(0,1fr) 320px;gap:16px;align-items:start;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px}}
@media (max-width:760px){{.cena{{grid-template-columns:36px minmax(0,1fr)}} .cena img,.cena .semtela{{grid-column:1/-1}}}}
.cn{{font-weight:800;color:var(--gd)}} .cb b{{font-size:16px}} .cb p{{margin:4px 0 0;font-size:15px}} .tx{{color:var(--ink);font-weight:600}} .arq{{color:var(--mut);font-size:12.5px!important;overflow-wrap:anywhere}}
.cena img{{width:100%;border-radius:10px;border:1px solid var(--line)}} .semtela{{height:100%;min-height:90px;border-radius:10px;border:1.5px dashed var(--line);display:grid;place-items:center;color:var(--mut);font-size:13px}}
pre{{white-space:pre-wrap;background:var(--dark);color:#e7ece7;border-radius:14px;padding:18px;font:14px/1.6 Montserrat,system-ui,sans-serif;overflow-wrap:anywhere;margin:0}}
.cp{{border:0;background:var(--g);color:var(--ink);font:700 13px Montserrat,sans-serif;letter-spacing:0;text-transform:none;border-radius:999px;padding:7px 14px;cursor:pointer}}
footer{{padding-block:30px 50px;color:var(--mut);font-size:14px}}
</style>
<header><div class="wrap"><small>Faculdade FEX Educação · Crie sua Formação</small><h1>Vídeos tutoriais <b>por seção</b></h1>
<p>Material para o produtor de motion 2D: objetivo, narração final, cenas com a tela do app e um prompt pronto para cada uma das 7 seções. As telas em tamanho original estão no repositório, em docs/telas.</p><nav>{nav}</nav></div></header>
<main class="wrap"><div class="estilo">{est}</div>{''.join(sec)}</main>
<footer class="wrap">Gerado a partir de tools/roteiros.py · #sejaFEX</footer>
<script>document.addEventListener("click",e=>{{const b=e.target.closest(".cp");if(!b)return;const t=document.getElementById(b.dataset.c).textContent;const ok=()=>{{b.textContent="Copiado";setTimeout(()=>b.textContent="Copiar prompt",1600)}};try{{navigator.clipboard.writeText(t).then(ok).catch(()=>{{const r=document.createRange();r.selectNodeContents(document.getElementById(b.dataset.c));getSelection().removeAllRanges();getSelection().addRange(r)}})}}catch(_ ){{}}}});</script>
"""


if __name__ == "__main__":
    (ROOT / "docs" / "ROTEIROS-VIDEOS.md").write_text(markdown(), encoding="utf-8")
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "roteiros.html").write_text(pagina(), encoding="utf-8")
    for s in SECOES: print(s["n"], s["nome"], f"~{dur(s)}s", sum(1 for c in s["cenas"] if c[1]), "telas")
