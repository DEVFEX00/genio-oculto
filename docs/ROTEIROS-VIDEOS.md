# Crie sua Formação · Vídeos tutoriais por seção (extensão universitária)

Material para a produção dos 7 vídeos de motion 2D, um por seção do construtor. Cada seção traz o objetivo, a narração final, as cenas com a tela do app e um **prompt pronto** para o produtor.

As telas estão em `docs/telas/` (versão computador e `celular-`), preenchidas com um exemplo genérico.

Depois de prontos, os vídeos entram no `CONFIG.VIDEOS` do `index.html` (ID do YouTube ou MP4 em `assets/videos/`), nas chaves abaixo.

| Seção | Chave | Fundo | Duração estimada |
|---|---|---|---|
| 1. Você | `voce` | escuro | ~76s |
| 2. Seu aluno | `aluno` | claro | ~57s |
| 3. Seu método | `metodo` | escuro | ~55s |
| 4. Seu formato | `formato` | claro | ~66s |
| 5. Seu potencial | `potencial` | escuro | ~63s |
| 6. Lançamento | `lancamento` | claro | ~58s |
| 7. Envio | `envio` | escuro | ~71s |

## Direção geral

- **Formato:** 16:9, 1920×1080, 30 fps. Entre 45 e 75 segundos por vídeo. O vídeo abre dentro do próprio app, num player 16:9.
- **Linguagem:** Motion design 2D: as telas reais do app (pasta docs/telas) aparecem num notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto sendo digitado letra a letra. Palavras-chave da narração viram tipografia animada. Ícones e formas se desenhando entre as telas. Nada de tela parada: a cada segundo algo se constrói.
- **Personagem:** O Gênio Oculto (opcional): mascote 2D em verde FEX, com capelo de formatura e cauda de fumaça no lugar das pernas, contorno preto, cores chapadas. Acolhedor, nunca infantil. Aparece na abertura, aponta para o campo da vez e comemora no fim de cada seção.
- **Fundo:** Igual à fase no app: seções 1, 3, 5 e 7 em verde quase preto com textura leve de granulado; seções 2, 4 e 6 em areia clara (#F4F2EC). Sem faixas de luz exageradas.
- **Cores e fonte:** Verde #32CD32, verde brilho #00D84F, preto #040805, areia #E8E4D9. Montserrat: palavras-chave em Bold grande, frases em Light.
- **Abertura e transição:** Vinheta de 3 s: a barra verde do meio do "E" do logo FEX atravessa a tela e revela "Seção N de 7 · NOME". Use a mesma barra verde como transição entre cenas.
- **Encerramento:** Toda seção termina com a mensagem de conquista que o app mostra (está em cada roteiro) e o card "Próxima seção: ...".
- **Voz:** Feminina, calorosa e clara, ritmo de conversa. Tom de quem acredita na pessoa: o público duvida de si (síndrome do impostor, medo de julgamento, medo de ser enganado). Encorajar sem exagerar e sem prometer resultado.
- **Som:** Trilha leve e otimista bem baixa sob a voz. Pop quando um card aparece, digitação suave, whoosh na transição, "ding" quando algo se completa.
- **Legendas:** Recomendadas (muita gente assiste no celular): Montserrat Bold branca em pílula preta, na parte de baixo.
- **Regras de texto:** Sempre "Faculdade FEX Educação". Falar em extensão universitária, nunca em pós-graduação ou MBA. Nunca dizer "reconhecido pelo MEC", "chancela" ou "certificação MEC". Na carga horária, nunca usar "autoestudo" nem "o resto". Valores do simulador são projeção, não garantia.

## 1. Você  (chave `voce`, ~76s, fundo escuro)

**Por que importa:** O curso nasce da experiência da pessoa. Aqui ela conta quem é, a área, os anos de prática e no mínimo 7 perguntas que sempre ouve. Cada pergunta vira uma aula.

### Narração

> Oi! Eu sou o Gênio Oculto, e vou te acompanhar na criação da sua formação. Esta primeira seção é sobre a parte mais importante dela: você. O seu curso nasce da sua experiência, e isso ninguém consegue copiar.
>
> Primeiro, escreva o seu nome e sobrenome. É ele que assina o curso como especialista responsável.
>
> Depois, a sua área. Pode ser ampla ou bem específica. Se ela estiver nos botões, é só clicar.
>
> Agora, arraste a barra até os seus anos de experiência. Repare no número que aparece: são milhares de horas de prática. E experiência não precisa de diploma para valer.
>
> E aqui mora o seu gênio oculto: o que as pessoas sempre te perguntam? Escreva no mínimo sete perguntas, uma por linha, do jeito que você ouve no dia a dia. Não existe pergunta boba. Cada uma vira uma aula, e a gente organiza tudo em módulos para você. Se travar, clique em Sugerir com IA.
>
> Pronto! Clique em Continuar e vamos conhecer o seu aluno.

### Cenas

| # | Cena | O que acontece | Tela | Texto na tela |
|---|---|---|---|---|
| 1 | Vinheta | Barra verde do logo revela "Seção 1 de 7 · VOCÊ". O Gênio surge de uma espiral de fumaça e acena. | animação | VOCÊ |
| 2 | Por que importa | A palavra VOCÊ cresce atrás do Gênio, que aponta para a câmera. Ícones orbitam: maleta (área), relógio (anos), balão de fala (perguntas). | animação | Seu curso nasce da sua experiência |
| 3 | Nome | Zoom no campo Nome. A mão-cursor clica e "Carla Exemplo" é digitado letra a letra. | `telas/1-voce-a-nome.jpg` | Seu nome assina o curso |
| 4 | Área | Digitação de "Sua área". Os botões de atalho acendem em cascata. | `telas/1-voce-b-area.jpg` |  |
| 5 | Anos | A mão arrasta a barra. O contador de horas sobe rápido; ao lado, uma pilha de relógios cresce. | `telas/1-voce-c-anos.jpg` | Milhares de horas de prática |
| 6 | Perguntas | Três perguntas digitadas. O contador mostra "3 de 7 · faltam 4" e a barrinha verde avança. | `telas/1-voce-d-perguntas-3-de-7.jpg` | No mínimo 7 perguntas |
| 7 | Cada pergunta vira aula | Clique em Sugerir com IA: as perguntas completam a lista e o contador fica verde. Cada linha se transforma num mini-card com ícone de play escrito "Aula". | `telas/1-voce-e-perguntas-ok.jpg` | Não existe pergunta boba |
| 8 | Encerramento | Mostra o banner verde de conquista da seção. Card "Próxima seção: Seu aluno". | `telas/2-aluno-a-conquista-e-aluno-ideal.jpg` | Você acabou de mostrar as aulas que só você sabe dar |

### Prompt para o produtor

```
Crie um vídeo tutorial em motion design 2D, 16:9 (1920×1080), com cerca de 76 segundos, para a seção "Você" (seção 1 de 7) do aplicativo Crie sua Formação, da Faculdade FEX Educação. O vídeo ensina a pessoa a preencher esta seção e abre com uma introdução curta sobre por que ela importa para a criação do curso.

Objetivo da seção: O curso nasce da experiência da pessoa. Aqui ela conta quem é, a área, os anos de prática e no mínimo 7 perguntas que sempre ouve. Cada pergunta vira uma aula.

Estilo: telas reais do app dentro de um notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto digitado letra a letra; palavras-chave em tipografia animada (Montserrat Bold); ícones e formas se desenhando; mascote Gênio Oculto (gênio verde com capelo de formatura) apontando e reagindo. Fundo verde quase preto com textura leve. Verde #32CD32, preto #040805, areia #E8E4D9. Vinheta de 3 s com a barra verde do logo FEX revelando "Seção 1 de 7 · VOCÊ". Ritmo dinâmico: algo se constrói a cada segundo.

Narração (voz feminina, calorosa, encorajadora; o público costuma duvidar de si):
"Oi! Eu sou o Gênio Oculto, e vou te acompanhar na criação da sua formação. Esta primeira seção é sobre a parte mais importante dela: você. O seu curso nasce da sua experiência, e isso ninguém consegue copiar. Primeiro, escreva o seu nome e sobrenome. É ele que assina o curso como especialista responsável. Depois, a sua área. Pode ser ampla ou bem específica. Se ela estiver nos botões, é só clicar. Agora, arraste a barra até os seus anos de experiência. Repare no número que aparece: são milhares de horas de prática. E experiência não precisa de diploma para valer. E aqui mora o seu gênio oculto: o que as pessoas sempre te perguntam? Escreva no mínimo sete perguntas, uma por linha, do jeito que você ouve no dia a dia. Não existe pergunta boba. Cada uma vira uma aula, e a gente organiza tudo em módulos para você. Se travar, clique em Sugerir com IA. Pronto! Clique em Continuar e vamos conhecer o seu aluno."

Cenas, na ordem da narração:
1. Vinheta: Barra verde do logo revela "Seção 1 de 7 · VOCÊ". O Gênio surge de uma espiral de fumaça e acena. Texto na tela: "VOCÊ".
2. Por que importa: A palavra VOCÊ cresce atrás do Gênio, que aponta para a câmera. Ícones orbitam: maleta (área), relógio (anos), balão de fala (perguntas). Texto na tela: "Seu curso nasce da sua experiência".
3. Nome: Zoom no campo Nome. A mão-cursor clica e "Carla Exemplo" é digitado letra a letra. Tela: docs/telas/1-voce-a-nome.jpg. Texto na tela: "Seu nome assina o curso".
4. Área: Digitação de "Sua área". Os botões de atalho acendem em cascata. Tela: docs/telas/1-voce-b-area.jpg.
5. Anos: A mão arrasta a barra. O contador de horas sobe rápido; ao lado, uma pilha de relógios cresce. Tela: docs/telas/1-voce-c-anos.jpg. Texto na tela: "Milhares de horas de prática".
6. Perguntas: Três perguntas digitadas. O contador mostra "3 de 7 · faltam 4" e a barrinha verde avança. Tela: docs/telas/1-voce-d-perguntas-3-de-7.jpg. Texto na tela: "No mínimo 7 perguntas".
7. Cada pergunta vira aula: Clique em Sugerir com IA: as perguntas completam a lista e o contador fica verde. Cada linha se transforma num mini-card com ícone de play escrito "Aula". Tela: docs/telas/1-voce-e-perguntas-ok.jpg. Texto na tela: "Não existe pergunta boba".
8. Encerramento: Mostra o banner verde de conquista da seção. Card "Próxima seção: Seu aluno". Tela: docs/telas/2-aluno-a-conquista-e-aluno-ideal.jpg. Texto na tela: "Você acabou de mostrar as aulas que só você sabe dar".

Regras: falar em extensão universitária (nunca pós-graduação ou MBA); nunca dizer "reconhecido pelo MEC" ou "chancela"; não usar "autoestudo" nem "o resto" para carga horária; números do simulador são projeção, não promessa.
```

## 2. Seu aluno  (chave `aluno`, ~57s, fundo claro)

**Por que importa:** Curso que fala com todo mundo não vende para ninguém. Aqui a pessoa define o aluno ideal e a promessa: o que ele vai conseguir fazer no final.

### Narração

> Um curso que fala com todo mundo não vende para ninguém. Nesta seção você decide para quem é o seu curso e o que essa pessoa vai conseguir fazer no final.
>
> Primeiro, descreva o seu aluno ideal em uma frase. Você não precisa ensinar para todo mundo: basta ensinar para quem precisa do que você já sabe. Se travar, clique em Sugerir com IA ou escolha uma das opções.
>
> Agora, a promessa. Complete a frase: ele vai conseguir. Pense na segunda-feira de manhã do seu aluno. O que muda no trabalho ou na vida dele?
>
> Prometa só o que você já entrega na prática. Sem exagero: a sua verdade é o que convence.
>
> Promessa escrita? Continue, porque agora vem o seu método.

### Cenas

| # | Cena | O que acontece | Tela | Texto na tela |
|---|---|---|---|---|
| 1 | Vinheta | Vinheta em fundo areia: "Seção 2 de 7 · SEU ALUNO". | animação | SEU ALUNO |
| 2 | Por que importa | Uma multidão de silhuetas cinza. Um holofote verde varre e para em uma pessoa, que ganha cor. | animação | Para quem é o seu curso? |
| 3 | Aluno ideal | Zoom no campo do aluno ideal e na frase de apoio com borda verde. | `telas/2-aluno-a-conquista-e-aluno-ideal.jpg` | Ensine para quem precisa do que você sabe |
| 4 | Sugerir com IA | Clique em Sugerir com IA: faíscas verdes e o texto se escreve sozinho. | `telas/2-aluno-b-sugerir-com-ia.jpg` |  |
| 5 | Promessa | Folhinha de calendário vira e mostra SEGUNDA. "Ele vai conseguir…" grande, e a promessa sendo escrita. | `telas/2-aluno-c-promessa.jpg` | O que muda na segunda-feira? |
| 6 | Dica | Card cinza "crescer na carreira" ganha um X e se desfaz. Card verde com uma promessa concreta entra com um check. | animação | Sem exagero: a sua verdade convence |
| 7 | Encerramento | Banner de conquista da seção e card "Próxima seção: Seu método". | `telas/3-metodo-a-conquista-e-ferramentas.jpg` | Agora o seu curso tem endereço certo |

### Prompt para o produtor

```
Crie um vídeo tutorial em motion design 2D, 16:9 (1920×1080), com cerca de 57 segundos, para a seção "Seu aluno" (seção 2 de 7) do aplicativo Crie sua Formação, da Faculdade FEX Educação. O vídeo ensina a pessoa a preencher esta seção e abre com uma introdução curta sobre por que ela importa para a criação do curso.

Objetivo da seção: Curso que fala com todo mundo não vende para ninguém. Aqui a pessoa define o aluno ideal e a promessa: o que ele vai conseguir fazer no final.

Estilo: telas reais do app dentro de um notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto digitado letra a letra; palavras-chave em tipografia animada (Montserrat Bold); ícones e formas se desenhando; mascote Gênio Oculto (gênio verde com capelo de formatura) apontando e reagindo. Fundo areia clara (#F4F2EC). Verde #32CD32, preto #040805, areia #E8E4D9. Vinheta de 3 s com a barra verde do logo FEX revelando "Seção 2 de 7 · SEU ALUNO". Ritmo dinâmico: algo se constrói a cada segundo.

Narração (voz feminina, calorosa, encorajadora; o público costuma duvidar de si):
"Um curso que fala com todo mundo não vende para ninguém. Nesta seção você decide para quem é o seu curso e o que essa pessoa vai conseguir fazer no final. Primeiro, descreva o seu aluno ideal em uma frase. Você não precisa ensinar para todo mundo: basta ensinar para quem precisa do que você já sabe. Se travar, clique em Sugerir com IA ou escolha uma das opções. Agora, a promessa. Complete a frase: ele vai conseguir. Pense na segunda-feira de manhã do seu aluno. O que muda no trabalho ou na vida dele? Prometa só o que você já entrega na prática. Sem exagero: a sua verdade é o que convence. Promessa escrita? Continue, porque agora vem o seu método."

Cenas, na ordem da narração:
1. Vinheta: Vinheta em fundo areia: "Seção 2 de 7 · SEU ALUNO". Texto na tela: "SEU ALUNO".
2. Por que importa: Uma multidão de silhuetas cinza. Um holofote verde varre e para em uma pessoa, que ganha cor. Texto na tela: "Para quem é o seu curso?".
3. Aluno ideal: Zoom no campo do aluno ideal e na frase de apoio com borda verde. Tela: docs/telas/2-aluno-a-conquista-e-aluno-ideal.jpg. Texto na tela: "Ensine para quem precisa do que você sabe".
4. Sugerir com IA: Clique em Sugerir com IA: faíscas verdes e o texto se escreve sozinho. Tela: docs/telas/2-aluno-b-sugerir-com-ia.jpg.
5. Promessa: Folhinha de calendário vira e mostra SEGUNDA. "Ele vai conseguir…" grande, e a promessa sendo escrita. Tela: docs/telas/2-aluno-c-promessa.jpg. Texto na tela: "O que muda na segunda-feira?".
6. Dica: Card cinza "crescer na carreira" ganha um X e se desfaz. Card verde com uma promessa concreta entra com um check. Texto na tela: "Sem exagero: a sua verdade convence".
7. Encerramento: Banner de conquista da seção e card "Próxima seção: Seu método". Tela: docs/telas/3-metodo-a-conquista-e-ferramentas.jpg. Texto na tela: "Agora o seu curso tem endereço certo".

Regras: falar em extensão universitária (nunca pós-graduação ou MBA); nunca dizer "reconhecido pelo MEC" ou "chancela"; não usar "autoestudo" nem "o resto" para carga horária; números do simulador são projeção, não promessa.
```

## 3. Seu método  (chave `metodo`, ~55s, fundo escuro)

**Por que importa:** As perguntas já viraram aulas e módulos (quem organiza é a ferramenta, não a pessoa). Aqui ela conta o que deixa o curso único: ferramentas, referências e se já ensina.

### Narração

> Lembra das perguntas que você escreveu? Cada uma já virou uma aula, e a gente organizou tudo em módulos para você. Nesta seção, você conta o que deixa o seu curso diferente.
>
> Primeiro, as ferramentas que você usa no trabalho: fichas, checklists, roteiros, o seu passo a passo. Escreva e aperte Enter, ou clique em Sugerir com IA. Aquilo que parece simples para você é o atalho que o seu aluno procura há anos.
>
> Se tiver autores, livros ou métodos que você segue, escreva. Se não lembrar agora, pode pular.
>
> Por último, conte se você já ensina hoje. Isso ajuda a escolher o melhor jeito de lançar.
>
> Clique em Continuar para descobrir o formato ideal do seu curso.

### Cenas

| # | Cena | O que acontece | Tela | Texto na tela |
|---|---|---|---|---|
| 1 | Vinheta | Vinheta escura: "Seção 3 de 7 · SEU MÉTODO". | animação | SEU MÉTODO |
| 2 | Perguntas viram módulos | Os cards de pergunta da seção 1 voam e se encaixam em blocos de módulo (Primeiros passos, O método na prática, Erros comuns...), como peças de montar. | animação | Pergunta → Aula → Módulo |
| 3 | Ferramentas | Uma caixa de ferramentas desenhada abre. Digitação + Enter adiciona uma ferramenta na lista. | `telas/3-metodo-a-conquista-e-ferramentas.jpg` | O seu jeito de fazer |
| 4 | Sugerir com IA | Clique em Sugerir com IA: três ferramentas entram na lista com pop. | `telas/3-metodo-b-ferramentas-ok.jpg` | O simples para você é o atalho do aluno |
| 5 | Referências | Livro se desenha ao lado. O link "Pular esta" é circulado à mão em verde. | `telas/3-metodo-c-referencias.jpg` | Pode pular se não lembrar |
| 6 | Já ensina? | A mão escolhe "Curso online" entre as quatro opções. | `telas/3-metodo-d-ja-ensina.jpg` |  |
| 7 | Encerramento | Banner de conquista e card "Próxima seção: Seu formato". | `telas/4-formato-a-conquista-e-objetivo.jpg` | Suas ferramentas são o que ninguém copia |

### Prompt para o produtor

```
Crie um vídeo tutorial em motion design 2D, 16:9 (1920×1080), com cerca de 55 segundos, para a seção "Seu método" (seção 3 de 7) do aplicativo Crie sua Formação, da Faculdade FEX Educação. O vídeo ensina a pessoa a preencher esta seção e abre com uma introdução curta sobre por que ela importa para a criação do curso.

Objetivo da seção: As perguntas já viraram aulas e módulos (quem organiza é a ferramenta, não a pessoa). Aqui ela conta o que deixa o curso único: ferramentas, referências e se já ensina.

Estilo: telas reais do app dentro de um notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto digitado letra a letra; palavras-chave em tipografia animada (Montserrat Bold); ícones e formas se desenhando; mascote Gênio Oculto (gênio verde com capelo de formatura) apontando e reagindo. Fundo verde quase preto com textura leve. Verde #32CD32, preto #040805, areia #E8E4D9. Vinheta de 3 s com a barra verde do logo FEX revelando "Seção 3 de 7 · SEU MÉTODO". Ritmo dinâmico: algo se constrói a cada segundo.

Narração (voz feminina, calorosa, encorajadora; o público costuma duvidar de si):
"Lembra das perguntas que você escreveu? Cada uma já virou uma aula, e a gente organizou tudo em módulos para você. Nesta seção, você conta o que deixa o seu curso diferente. Primeiro, as ferramentas que você usa no trabalho: fichas, checklists, roteiros, o seu passo a passo. Escreva e aperte Enter, ou clique em Sugerir com IA. Aquilo que parece simples para você é o atalho que o seu aluno procura há anos. Se tiver autores, livros ou métodos que você segue, escreva. Se não lembrar agora, pode pular. Por último, conte se você já ensina hoje. Isso ajuda a escolher o melhor jeito de lançar. Clique em Continuar para descobrir o formato ideal do seu curso."

Cenas, na ordem da narração:
1. Vinheta: Vinheta escura: "Seção 3 de 7 · SEU MÉTODO". Texto na tela: "SEU MÉTODO".
2. Perguntas viram módulos: Os cards de pergunta da seção 1 voam e se encaixam em blocos de módulo (Primeiros passos, O método na prática, Erros comuns...), como peças de montar. Texto na tela: "Pergunta → Aula → Módulo".
3. Ferramentas: Uma caixa de ferramentas desenhada abre. Digitação + Enter adiciona uma ferramenta na lista. Tela: docs/telas/3-metodo-a-conquista-e-ferramentas.jpg. Texto na tela: "O seu jeito de fazer".
4. Sugerir com IA: Clique em Sugerir com IA: três ferramentas entram na lista com pop. Tela: docs/telas/3-metodo-b-ferramentas-ok.jpg. Texto na tela: "O simples para você é o atalho do aluno".
5. Referências: Livro se desenha ao lado. O link "Pular esta" é circulado à mão em verde. Tela: docs/telas/3-metodo-c-referencias.jpg. Texto na tela: "Pode pular se não lembrar".
6. Já ensina?: A mão escolhe "Curso online" entre as quatro opções. Tela: docs/telas/3-metodo-d-ja-ensina.jpg.
7. Encerramento: Banner de conquista e card "Próxima seção: Seu formato". Tela: docs/telas/4-formato-a-conquista-e-objetivo.jpg. Texto na tela: "Suas ferramentas são o que ninguém copia".

Regras: falar em extensão universitária (nunca pós-graduação ou MBA); nunca dizer "reconhecido pelo MEC" ou "chancela"; não usar "autoestudo" nem "o resto" para carga horária; números do simulador são projeção, não promessa.
```

## 4. Seu formato  (chave `formato`, ~66s, fundo claro)

**Por que importa:** Seção mais importante para a FEX: sem a FEX é curso livre, com a FEX é extensão universitária. A pessoa diz o objetivo, a ferramenta indica uma das 4 titulações, ela ajusta a carga horária, confere o nome e escolhe o preço em parcelas.

### Narração

> Agora vem uma parte importante. Sem a FEX, o seu curso é um curso livre. Com a FEX, ele vira um curso de extensão universitária, com certificado emitido pela Faculdade FEX Educação.
>
> Primeiro, escolha o que você quer que o curso seja para o aluno.
>
> Com isso, a ferramenta indica a titulação ideal entre as quatro da extensão: Iniciação, Atualização, Capacitação e Aperfeiçoamento. Você ajusta as horas na barra.
>
> A carga horária soma tudo o que é acompanhado pelo professor: aulas, leituras, estudos de caso, encontros de perguntas e respostas e prática. Você não precisa gravar todas as horas.
>
> Confira o nome do curso e, por último, o investimento: escolha uma faixa de parcela ou arraste a barra até o valor certo para o seu público. O seu conhecimento tem valor.
>
> Formato escolhido. Agora vem a parte que mais surpreende: o seu potencial.

### Cenas

| # | Cena | O que acontece | Tela | Texto na tela |
|---|---|---|---|---|
| 1 | Vinheta | Vinheta em areia: "Seção 4 de 7 · SEU FORMATO". | animação | SEU FORMATO |
| 2 | Curso livre × extensão | Tela dividida: à esquerda um certificado simples, cinza, "Curso livre" (riscado). À direita, um certificado verde com o logo FEX: "Extensão universitária". | animação | Com a FEX, vira extensão universitária |
| 3 | Objetivo | As quatro opções de objetivo entram em cascata; a mão escolhe "Capacitar para aplicar". | `telas/4-formato-b-objetivo-escolhido.jpg` |  |
| 4 | Titulação recomendada | Os 4 cards (Iniciação, Atualização, Capacitação, Aperfeiçoamento) giram como cartas; o recomendado sobe com o selo verde. | `telas/4-formato-c-titulacao-recomendada.jpg` | 4 titulações de extensão |
| 5 | Carga horária | A mão arrasta a barra de horas. Ícones aparecem um a um: aula, livro, estudo de caso, balão de perguntas, prática. | `telas/4-formato-d-carga-horaria.jpg` | Tudo acompanhado pelo professor |
| 6 | Nome do curso | Zoom no nome do curso; clique em Sugerir com IA troca o nome com faíscas. | `telas/4-formato-e-nome-do-curso.jpg` |  |
| 7 | Preço | As faixas de 12x entram em cascata; a mão escolhe uma. | `telas/4-formato-f-preco.jpg` | 12x de R$ 97 a 12x de R$ 5.000 |
| 8 | Barra da parcela | A mão arrasta a barra e o valor da parcela muda ao vivo. | `telas/4-formato-g-barra-da-parcela.jpg` | O seu conhecimento tem valor |
| 9 | Encerramento | Banner de conquista e card "Próxima seção: Seu potencial". | `telas/5-potencial-a-conquista-e-audiencias.jpg` | Você não está sozinho nisso |

### Prompt para o produtor

```
Crie um vídeo tutorial em motion design 2D, 16:9 (1920×1080), com cerca de 66 segundos, para a seção "Seu formato" (seção 4 de 7) do aplicativo Crie sua Formação, da Faculdade FEX Educação. O vídeo ensina a pessoa a preencher esta seção e abre com uma introdução curta sobre por que ela importa para a criação do curso.

Objetivo da seção: Seção mais importante para a FEX: sem a FEX é curso livre, com a FEX é extensão universitária. A pessoa diz o objetivo, a ferramenta indica uma das 4 titulações, ela ajusta a carga horária, confere o nome e escolhe o preço em parcelas.

Estilo: telas reais do app dentro de um notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto digitado letra a letra; palavras-chave em tipografia animada (Montserrat Bold); ícones e formas se desenhando; mascote Gênio Oculto (gênio verde com capelo de formatura) apontando e reagindo. Fundo areia clara (#F4F2EC). Verde #32CD32, preto #040805, areia #E8E4D9. Vinheta de 3 s com a barra verde do logo FEX revelando "Seção 4 de 7 · SEU FORMATO". Ritmo dinâmico: algo se constrói a cada segundo.

Narração (voz feminina, calorosa, encorajadora; o público costuma duvidar de si):
"Agora vem uma parte importante. Sem a FEX, o seu curso é um curso livre. Com a FEX, ele vira um curso de extensão universitária, com certificado emitido pela Faculdade FEX Educação. Primeiro, escolha o que você quer que o curso seja para o aluno. Com isso, a ferramenta indica a titulação ideal entre as quatro da extensão: Iniciação, Atualização, Capacitação e Aperfeiçoamento. Você ajusta as horas na barra. A carga horária soma tudo o que é acompanhado pelo professor: aulas, leituras, estudos de caso, encontros de perguntas e respostas e prática. Você não precisa gravar todas as horas. Confira o nome do curso e, por último, o investimento: escolha uma faixa de parcela ou arraste a barra até o valor certo para o seu público. O seu conhecimento tem valor. Formato escolhido. Agora vem a parte que mais surpreende: o seu potencial."

Cenas, na ordem da narração:
1. Vinheta: Vinheta em areia: "Seção 4 de 7 · SEU FORMATO". Texto na tela: "SEU FORMATO".
2. Curso livre × extensão: Tela dividida: à esquerda um certificado simples, cinza, "Curso livre" (riscado). À direita, um certificado verde com o logo FEX: "Extensão universitária". Texto na tela: "Com a FEX, vira extensão universitária".
3. Objetivo: As quatro opções de objetivo entram em cascata; a mão escolhe "Capacitar para aplicar". Tela: docs/telas/4-formato-b-objetivo-escolhido.jpg.
4. Titulação recomendada: Os 4 cards (Iniciação, Atualização, Capacitação, Aperfeiçoamento) giram como cartas; o recomendado sobe com o selo verde. Tela: docs/telas/4-formato-c-titulacao-recomendada.jpg. Texto na tela: "4 titulações de extensão".
5. Carga horária: A mão arrasta a barra de horas. Ícones aparecem um a um: aula, livro, estudo de caso, balão de perguntas, prática. Tela: docs/telas/4-formato-d-carga-horaria.jpg. Texto na tela: "Tudo acompanhado pelo professor".
6. Nome do curso: Zoom no nome do curso; clique em Sugerir com IA troca o nome com faíscas. Tela: docs/telas/4-formato-e-nome-do-curso.jpg.
7. Preço: As faixas de 12x entram em cascata; a mão escolhe uma. Tela: docs/telas/4-formato-f-preco.jpg. Texto na tela: "12x de R$ 97 a 12x de R$ 5.000".
8. Barra da parcela: A mão arrasta a barra e o valor da parcela muda ao vivo. Tela: docs/telas/4-formato-g-barra-da-parcela.jpg. Texto na tela: "O seu conhecimento tem valor".
9. Encerramento: Banner de conquista e card "Próxima seção: Seu potencial". Tela: docs/telas/5-potencial-a-conquista-e-audiencias.jpg. Texto na tela: "Você não está sozinho nisso".

Regras: falar em extensão universitária (nunca pós-graduação ou MBA); nunca dizer "reconhecido pelo MEC" ou "chancela"; não usar "autoestudo" nem "o resto" para carga horária; números do simulador são projeção, não promessa.
```

## 5. Seu potencial  (chave `potencial`, ~63s, fundo escuro)

**Por que importa:** Mostra quanto a primeira turma pode faturar com quem já conhece a pessoa, com a conta visível. Deixa claro que é projeção, não promessa.

### Narração

> Esta é a seção que mais surpreende. Você vai ver quanto a primeira turma pode faturar com quem já te conhece.
>
> Em base quente, coloque quantas pessoas já foram seus alunos, pacientes ou clientes. Elas já confiam em você. A referência da FEX é três por cento de conversão.
>
> Em audiência fria, entram os seus seguidores, a sua lista de e-mail e os seus contatos. Aqui a referência é zero vírgula três por cento. Você pode mudar as duas, e a conta aparece embaixo de cada barra.
>
> Agora olhe o número verde: é o potencial da sua primeira turma. É uma projeção feita com os seus números, não uma promessa. E começar pequeno é normal: a primeira turma costuma vir de poucas pessoas que já confiam em você.
>
> Gostou do número? Então vamos planejar o lançamento.

### Cenas

| # | Cena | O que acontece | Tela | Texto na tela |
|---|---|---|---|---|
| 1 | Vinheta | Vinheta escura: "Seção 5 de 7 · SEU POTENCIAL". | animação | SEU POTENCIAL |
| 2 | Por que importa | Um gráfico de barras se desenha atrás do Gênio, que fica surpreso. | animação | Quanto a 1ª turma pode faturar? |
| 3 | Base quente | Grupo de pessoinhas com brilho verde (confiança). A mão arrasta a barra; a conta "800 pessoas × 3% = 24 matrículas" aparece com destaque. | `telas/5-potencial-a-conquista-e-audiencias.jpg` | Base quente: 3% |
| 4 | Audiência fria | Ícones de redes, e-mail e agenda flutuam como bolhas e entram na segunda barra; a conta com 0,3% aparece. | `telas/5-potencial-a-conquista-e-audiencias.jpg` | Audiência fria: 0,3% |
| 5 | Resultado | Zoom no card verde: o valor conta até o número. Uma etiqueta discreta: "projeção, não promessa". | `telas/5-potencial-b-resultado.jpg` | Projeção com os seus números |
| 6 | Encerramento | Banner de conquista e card "Próxima seção: Lançamento". | `telas/6-lancamento-a-conquista-e-campanhas.jpg` | Vale a pena começar |

### Prompt para o produtor

```
Crie um vídeo tutorial em motion design 2D, 16:9 (1920×1080), com cerca de 63 segundos, para a seção "Seu potencial" (seção 5 de 7) do aplicativo Crie sua Formação, da Faculdade FEX Educação. O vídeo ensina a pessoa a preencher esta seção e abre com uma introdução curta sobre por que ela importa para a criação do curso.

Objetivo da seção: Mostra quanto a primeira turma pode faturar com quem já conhece a pessoa, com a conta visível. Deixa claro que é projeção, não promessa.

Estilo: telas reais do app dentro de um notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto digitado letra a letra; palavras-chave em tipografia animada (Montserrat Bold); ícones e formas se desenhando; mascote Gênio Oculto (gênio verde com capelo de formatura) apontando e reagindo. Fundo verde quase preto com textura leve. Verde #32CD32, preto #040805, areia #E8E4D9. Vinheta de 3 s com a barra verde do logo FEX revelando "Seção 5 de 7 · SEU POTENCIAL". Ritmo dinâmico: algo se constrói a cada segundo.

Narração (voz feminina, calorosa, encorajadora; o público costuma duvidar de si):
"Esta é a seção que mais surpreende. Você vai ver quanto a primeira turma pode faturar com quem já te conhece. Em base quente, coloque quantas pessoas já foram seus alunos, pacientes ou clientes. Elas já confiam em você. A referência da FEX é três por cento de conversão. Em audiência fria, entram os seus seguidores, a sua lista de e-mail e os seus contatos. Aqui a referência é zero vírgula três por cento. Você pode mudar as duas, e a conta aparece embaixo de cada barra. Agora olhe o número verde: é o potencial da sua primeira turma. É uma projeção feita com os seus números, não uma promessa. E começar pequeno é normal: a primeira turma costuma vir de poucas pessoas que já confiam em você. Gostou do número? Então vamos planejar o lançamento."

Cenas, na ordem da narração:
1. Vinheta: Vinheta escura: "Seção 5 de 7 · SEU POTENCIAL". Texto na tela: "SEU POTENCIAL".
2. Por que importa: Um gráfico de barras se desenha atrás do Gênio, que fica surpreso. Texto na tela: "Quanto a 1ª turma pode faturar?".
3. Base quente: Grupo de pessoinhas com brilho verde (confiança). A mão arrasta a barra; a conta "800 pessoas × 3% = 24 matrículas" aparece com destaque. Tela: docs/telas/5-potencial-a-conquista-e-audiencias.jpg. Texto na tela: "Base quente: 3%".
4. Audiência fria: Ícones de redes, e-mail e agenda flutuam como bolhas e entram na segunda barra; a conta com 0,3% aparece. Tela: docs/telas/5-potencial-a-conquista-e-audiencias.jpg. Texto na tela: "Audiência fria: 0,3%".
5. Resultado: Zoom no card verde: o valor conta até o número. Uma etiqueta discreta: "projeção, não promessa". Tela: docs/telas/5-potencial-b-resultado.jpg. Texto na tela: "Projeção com os seus números".
6. Encerramento: Banner de conquista e card "Próxima seção: Lançamento". Tela: docs/telas/6-lancamento-a-conquista-e-campanhas.jpg. Texto na tela: "Vale a pena começar".

Regras: falar em extensão universitária (nunca pós-graduação ou MBA); nunca dizer "reconhecido pelo MEC" ou "chancela"; não usar "autoestudo" nem "o resto" para carga horária; números do simulador são projeção, não promessa.
```

## 6. Lançamento  (chave `lancamento`, ~58s, fundo claro)

**Por que importa:** Escolher como abrir as matrículas e marcar o início da turma. O registro com a FEX leva até 30 dias.

### Narração

> Curso pronto que ninguém conhece não vira turma. Aqui você escolhe como vai abrir as matrículas e quando a primeira turma começa.
>
> Não existe um jeito certo. Tem base de alunos? Campanha interna. Tem audiência nas redes? Aula ao vivo. Base pequena e engajada? Lançamento relâmpago no WhatsApp. Também dá para aproveitar datas como Black Friday, Natal e Ano Novo, nas campanhas sazonais.
>
> Depois, marque a data de início da turma. O registro do curso com a Faculdade FEX Educação leva até trinta dias, por isso a data mínima é daqui a trinta dias. A ferramenta já mostra quando as suas matrículas abrem.
>
> Ninguém se sente cem por cento pronto. Marcar a data é o que transforma vontade em projeto. Vamos para o último passo.

### Cenas

| # | Cena | O que acontece | Tela | Texto na tela |
|---|---|---|---|---|
| 1 | Vinheta | Vinheta em areia: "Seção 6 de 7 · LANÇAMENTO". O Gênio entra com um megafone. | animação | LANÇAMENTO |
| 2 | Por que importa | Uma porta com a placa "Matrículas" se abre e entra luz verde. | animação | Como abrir as matrículas |
| 3 | Campanhas | Os 6 cards passam em carrossel; cada um acende quando a narração cita. Mini ícones de Black Friday, Natal e Ano Novo no card de campanhas sazonais. | `telas/6-lancamento-a-conquista-e-campanhas.jpg` | Escolha o que combina com você hoje |
| 4 | Início da turma | Calendário: 30 quadradinhos se preenchem (registro). Marcador "Matrículas abrem" e estrela "Turma 1". | `telas/6-lancamento-b-inicio-da-turma.jpg` | Registro em até 30 dias |
| 5 | Encerramento | Banner de conquista e card "Próxima seção: Envio". | `telas/7-envio-a-conquista-e-contato.jpg` | Data marcada é projeto de verdade |

### Prompt para o produtor

```
Crie um vídeo tutorial em motion design 2D, 16:9 (1920×1080), com cerca de 58 segundos, para a seção "Lançamento" (seção 6 de 7) do aplicativo Crie sua Formação, da Faculdade FEX Educação. O vídeo ensina a pessoa a preencher esta seção e abre com uma introdução curta sobre por que ela importa para a criação do curso.

Objetivo da seção: Escolher como abrir as matrículas e marcar o início da turma. O registro com a FEX leva até 30 dias.

Estilo: telas reais do app dentro de um notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto digitado letra a letra; palavras-chave em tipografia animada (Montserrat Bold); ícones e formas se desenhando; mascote Gênio Oculto (gênio verde com capelo de formatura) apontando e reagindo. Fundo areia clara (#F4F2EC). Verde #32CD32, preto #040805, areia #E8E4D9. Vinheta de 3 s com a barra verde do logo FEX revelando "Seção 6 de 7 · LANÇAMENTO". Ritmo dinâmico: algo se constrói a cada segundo.

Narração (voz feminina, calorosa, encorajadora; o público costuma duvidar de si):
"Curso pronto que ninguém conhece não vira turma. Aqui você escolhe como vai abrir as matrículas e quando a primeira turma começa. Não existe um jeito certo. Tem base de alunos? Campanha interna. Tem audiência nas redes? Aula ao vivo. Base pequena e engajada? Lançamento relâmpago no WhatsApp. Também dá para aproveitar datas como Black Friday, Natal e Ano Novo, nas campanhas sazonais. Depois, marque a data de início da turma. O registro do curso com a Faculdade FEX Educação leva até trinta dias, por isso a data mínima é daqui a trinta dias. A ferramenta já mostra quando as suas matrículas abrem. Ninguém se sente cem por cento pronto. Marcar a data é o que transforma vontade em projeto. Vamos para o último passo."

Cenas, na ordem da narração:
1. Vinheta: Vinheta em areia: "Seção 6 de 7 · LANÇAMENTO". O Gênio entra com um megafone. Texto na tela: "LANÇAMENTO".
2. Por que importa: Uma porta com a placa "Matrículas" se abre e entra luz verde. Texto na tela: "Como abrir as matrículas".
3. Campanhas: Os 6 cards passam em carrossel; cada um acende quando a narração cita. Mini ícones de Black Friday, Natal e Ano Novo no card de campanhas sazonais. Tela: docs/telas/6-lancamento-a-conquista-e-campanhas.jpg. Texto na tela: "Escolha o que combina com você hoje".
4. Início da turma: Calendário: 30 quadradinhos se preenchem (registro). Marcador "Matrículas abrem" e estrela "Turma 1". Tela: docs/telas/6-lancamento-b-inicio-da-turma.jpg. Texto na tela: "Registro em até 30 dias".
5. Encerramento: Banner de conquista e card "Próxima seção: Envio". Tela: docs/telas/7-envio-a-conquista-e-contato.jpg. Texto na tela: "Data marcada é projeto de verdade".

Regras: falar em extensão universitária (nunca pós-graduação ou MBA); nunca dizer "reconhecido pelo MEC" ou "chancela"; não usar "autoestudo" nem "o resto" para carga horária; números do simulador são projeção, não promessa.
```

## 7. Envio  (chave `envio`, ~71s, fundo escuro)

**Por que importa:** Deixar o contato, ver o curso montado de graça, conhecer o plano completo de R$ 97 e o próximo passo com o Plano Bronze.

### Narração

> Último passo! Aqui você deixa o seu contato e vê o seu curso montado na sua frente.
>
> Escreva o seu e-mail e o seu WhatsApp. É para lá que vai o seu plano, e é por onde um especialista da FEX pode falar com você, se você quiser.
>
> Clique em Ver meu curso pronto. A ferramenta organiza tudo o que você contou e mostra a capa do seu curso, os módulos, as primeiras aulas e o potencial da primeira turma. Tudo isso de graça. Você já sabia tudo isso. Agora está organizado.
>
> Quer o resto? O plano completo libera todas as aulas, o roteiro de gravação, o funil de vendas, o texto da sua página e o cronograma até a primeira turma, por noventa e sete reais.
>
> E no final do plano, um especialista da Faculdade FEX Educação te mostra como transformar o seu curso em extensão universitária, com o Plano Bronze. Agora é com você!

### Cenas

| # | Cena | O que acontece | Tela | Texto na tela |
|---|---|---|---|---|
| 1 | Vinheta | Vinheta escura: "Seção 7 de 7 · ENVIO". O Gênio segura um envelope verde. | animação | ENVIO |
| 2 | Contato | Digitação nos campos de e-mail e WhatsApp; a caixa de consentimento recebe o check. | `telas/7-envio-b-contato-preenchido.jpg` | Seu plano vai para o seu contato |
| 3 | Organizando | A esfera verde pulsa e a lista ganha checks um a um. | `telas/7-envio-c-organizando.jpg` |  |
| 4 | Prévia | A capa do curso entra com inclinação 3D; a câmera desce até os módulos. | `telas/7-envio-d-previa-capa.jpg` | Grátis |
| 5 | Módulos | O primeiro módulo abre e mostra as aulas (as perguntas da pessoa). | `telas/7-envio-e-previa-modulos.jpg` | Você já sabia. Agora está organizado |
| 6 | Plano completo | Os cadeados dos cards saltam e somem um a um; termina no botão "Desbloquear por R$ 97". | `telas/7-envio-f-previa-desbloquear.jpg` | Plano completo · R$ 97 |
| 7 | Plano Bronze | O card do Plano Bronze entra com borda verde girando; os itens aparecem em sequência. | `telas/7-envio-j-plano-bronze-card.jpg` | Curso livre → extensão universitária |
| 8 | Especialista | O botão verde gigante pulsa com o ícone do WhatsApp. Confete verde. Fecha com o logo FEX e #sejaFEX. | `telas/7-envio-k-botao-especialista.jpg` | Agora é com você! |

### Prompt para o produtor

```
Crie um vídeo tutorial em motion design 2D, 16:9 (1920×1080), com cerca de 71 segundos, para a seção "Envio" (seção 7 de 7) do aplicativo Crie sua Formação, da Faculdade FEX Educação. O vídeo ensina a pessoa a preencher esta seção e abre com uma introdução curta sobre por que ela importa para a criação do curso.

Objetivo da seção: Deixar o contato, ver o curso montado de graça, conhecer o plano completo de R$ 97 e o próximo passo com o Plano Bronze.

Estilo: telas reais do app dentro de um notebook ou celular desenhado, com zoom no campo da vez, mão-cursor clicando e texto digitado letra a letra; palavras-chave em tipografia animada (Montserrat Bold); ícones e formas se desenhando; mascote Gênio Oculto (gênio verde com capelo de formatura) apontando e reagindo. Fundo verde quase preto com textura leve. Verde #32CD32, preto #040805, areia #E8E4D9. Vinheta de 3 s com a barra verde do logo FEX revelando "Seção 7 de 7 · ENVIO". Ritmo dinâmico: algo se constrói a cada segundo.

Narração (voz feminina, calorosa, encorajadora; o público costuma duvidar de si):
"Último passo! Aqui você deixa o seu contato e vê o seu curso montado na sua frente. Escreva o seu e-mail e o seu WhatsApp. É para lá que vai o seu plano, e é por onde um especialista da FEX pode falar com você, se você quiser. Clique em Ver meu curso pronto. A ferramenta organiza tudo o que você contou e mostra a capa do seu curso, os módulos, as primeiras aulas e o potencial da primeira turma. Tudo isso de graça. Você já sabia tudo isso. Agora está organizado. Quer o resto? O plano completo libera todas as aulas, o roteiro de gravação, o funil de vendas, o texto da sua página e o cronograma até a primeira turma, por noventa e sete reais. E no final do plano, um especialista da Faculdade FEX Educação te mostra como transformar o seu curso em extensão universitária, com o Plano Bronze. Agora é com você!"

Cenas, na ordem da narração:
1. Vinheta: Vinheta escura: "Seção 7 de 7 · ENVIO". O Gênio segura um envelope verde. Texto na tela: "ENVIO".
2. Contato: Digitação nos campos de e-mail e WhatsApp; a caixa de consentimento recebe o check. Tela: docs/telas/7-envio-b-contato-preenchido.jpg. Texto na tela: "Seu plano vai para o seu contato".
3. Organizando: A esfera verde pulsa e a lista ganha checks um a um. Tela: docs/telas/7-envio-c-organizando.jpg.
4. Prévia: A capa do curso entra com inclinação 3D; a câmera desce até os módulos. Tela: docs/telas/7-envio-d-previa-capa.jpg. Texto na tela: "Grátis".
5. Módulos: O primeiro módulo abre e mostra as aulas (as perguntas da pessoa). Tela: docs/telas/7-envio-e-previa-modulos.jpg. Texto na tela: "Você já sabia. Agora está organizado".
6. Plano completo: Os cadeados dos cards saltam e somem um a um; termina no botão "Desbloquear por R$ 97". Tela: docs/telas/7-envio-f-previa-desbloquear.jpg. Texto na tela: "Plano completo · R$ 97".
7. Plano Bronze: O card do Plano Bronze entra com borda verde girando; os itens aparecem em sequência. Tela: docs/telas/7-envio-j-plano-bronze-card.jpg. Texto na tela: "Curso livre → extensão universitária".
8. Especialista: O botão verde gigante pulsa com o ícone do WhatsApp. Confete verde. Fecha com o logo FEX e #sejaFEX. Tela: docs/telas/7-envio-k-botao-especialista.jpg. Texto na tela: "Agora é com você!".

Regras: falar em extensão universitária (nunca pós-graduação ou MBA); nunca dizer "reconhecido pelo MEC" ou "chancela"; não usar "autoestudo" nem "o resto" para carga horária; números do simulador são projeção, não promessa.
```
