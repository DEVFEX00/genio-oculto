# Gênio Oculto · Roteiros dos vídeos tutoriais

Um vídeo por tela do construtor. Cada um tem de 40 a 70 segundos, é narrado em tom de "professora que todo mundo queria ter tido" (simples, próxima, com exemplo) e mostra a tela da ferramenta com animação no visual FEX (fundo preto, linhas de luz verde, Montserrat).

**Como ligar o vídeo na página:** suba no YouTube (pode ser "não listado") e cole o ID no `CONFIG.VIDEOS` do arquivo `src/index.src.html`, na chave indicada em cada roteiro. Depois rode `python3 build.py`. O ID é o trecho depois de `watch?v=` no link do YouTube.

**Regras de texto (base de conhecimento FEX):**
- Sempre "Faculdade FEX Educação®". Nunca "reconhecido pelo MEC", "chancela" ou "certificação MEC". Use "validade acadêmica".
- "Para", nunca "pra". Sem gíria.
- Toda fala termina com uma ação clara: o que a pessoa faz agora.

Estrutura padrão de cada vídeo:
1. **Gancho (0 a 5s):** a pergunta da tela, em tela cheia.
2. **Por que importa (5 a 20s):** o que essa resposta vira dentro do curso.
3. **Exemplo (20 a 45s):** a tela sendo preenchida com o caso da Ana (fisioterapeuta esportiva, 18 anos de prática), e o painel "Seu curso, ao vivo" mudando ao lado.
4. **Ação (últimos 5s):** "Agora é a sua vez. Escreva e clique em Continuar."

---

## 0. Boas-vindas · chave `boasvindas` (abre na 1ª tela se `nome` estiver vazio)
**Duração:** 60s · **Visual:** hero da landing, depois o mock do curso se montando.

> Você sabe muito mais do que imagina. Os atalhos, os erros que você não comete mais, o jeito certo de fazer. Para você, isso é óbvio. Para quem está começando, vale uma formação inteira.
>
> O Gênio Oculto faz uma coisa simples: tira esse conhecimento da sua cabeça e organiza no formato de uma pós-graduação. São perguntas curtas, uma por tela, e em cada uma tem um vídeo como este explicando o que responder.
>
> Do lado direito, você vai ver o seu curso se montando enquanto responde: nome, disciplinas, aulas e quanto ele pode faturar.
>
> Leva uns 15 minutos. Tudo fica salvo no seu navegador. Vamos começar?

## 1. Seu nome · chave `nome`
**Duração:** 40s · **Visual:** campo de nome, painel com "Especialista responsável".

> Primeiro, o seu nome. Parece detalhe, mas não é: é o seu nome que assina o curso como especialista responsável. É a sua trajetória que dá valor à formação.
>
> Escreva nome e sobrenome do jeito que você quer que apareça para os seus alunos. Pronto? Clique em Continuar.

## 2. Sua área · chave `area`
**Duração:** 55s · **Visual:** campo de área, chips de sugestão, título do curso aparecendo no painel.

> Agora, a sua área. Aqui vale uma dica de quem vende pós-graduação há anos: quanto mais específica, mais fácil de vender.
>
> "Fisioterapia" é amplo. "Fisioterapia esportiva" já é melhor. "Fisioterapia esportiva para corredores" é ainda melhor, porque a pessoa certa se reconhece na hora.
>
> Escreva com as suas palavras ou clique em uma das opções e ajuste. Olhe o painel ao lado: o nome do seu curso já começou a aparecer.

## 3. Anos de experiência · chave `anos`
**Duração:** 45s · **Visual:** slider, número de anos grande, frase das horas de prática.

> Quanto tempo você trabalha com isso? Conta tudo: emprego, consultório, empresa própria, atendimentos.
>
> Arraste a barra e repare no número que aparece embaixo. Com 18 anos, a Ana tem mais de 31 mil horas de prática. Uma pós-graduação inteira tem 360. Esse é o tamanho do conhecimento que está parado.
>
> Arraste até os seus anos e continue.

## 4. O que as pessoas te perguntam · chave `perguntas`
**Duração:** 65s · **Visual:** textarea com as perguntas da Ana sendo digitadas.

> Esta é a pergunta mais importante de todas. É aqui que mora o seu gênio oculto.
>
> Pense nas dúvidas que você responde toda semana. No trabalho, no Instagram, no WhatsApp. Aquelas que você responde no automático, sem nem pensar.
>
> A Ana escreveu: "Como voltar a correr depois de uma lesão no joelho?", "Quantas sessões preciso?", "Que exercício posso fazer em casa?".
>
> Cada pergunta dessas é uma aula esperando para ser gravada. Escreva uma por linha, do jeito que as pessoas falam com você. Não precisa caprichar.

## 5. Quem é o seu aluno · chave `persona`
**Duração:** 55s · **Visual:** campo de persona, chips, aviso da graduação.

> Quem é a pessoa que mais precisa do que você sabe?
>
> Um detalhe importante: para fazer uma pós-graduação, o aluno precisa ter uma graduação concluída. Então pense em profissionais formados.
>
> A Ana escolheu "fisioterapeutas formados que querem atender atletas". Quanto mais você conseguir enxergar essa pessoa, mais a sua página de vendas vai falar com ela.
>
> Clique em uma opção ou descreva com as suas palavras.

## 6. A promessa · chave `promessa`
**Duração:** 65s · **Visual:** frase "Ele vai conseguir…" completando, promessa aparecendo na capa do curso.

> Agora, a promessa. É a frase que faz alguém querer comprar o seu curso.
>
> Termine a frase "Depois do seu curso, o aluno vai conseguir…" pensando na segunda-feira de manhã dele. O que muda na vida ou no trabalho?
>
> Evite promessas vagas como "crescer na carreira". Prefira algo que dá para ver: "avaliar, tratar e liberar atletas para voltar ao esporte com segurança".
>
> Escreva a sua e veja ela aparecer na capa do curso, ao lado.

## 7. Os grandes temas · chave `temas`
**Duração:** 70s · **Visual:** temas sendo adicionados um a um e virando disciplinas no painel.

> Agora o seu curso ganha forma. Quais são os grandes temas que você ensinaria?
>
> Cada tema vira uma disciplina, e cada disciplina ganha quatro aulas. Escreva um tema e aperte Enter. Veja: ele aparece na hora no painel, como disciplina.
>
> Três a cinco temas é o ideal. Se travar, use as sugestões embaixo: algumas vêm das perguntas que você escreveu antes.
>
> A disciplina de fundamentos, a de ferramentas e o projeto aplicado a ferramenta já cria para você.

## 8. Ferramentas e protocolos · chave `ferramentas`
**Duração:** 50s · **Visual:** tags de ferramentas, disciplina "Ferramentas, protocolos e prática profissional".

> Que ferramentas, protocolos ou passo a passo você usa no trabalho? Fichas, checklists, testes, roteiros, técnicas próprias.
>
> Isso é o que diferencia o seu curso de qualquer outro da internet: o seu jeito de fazer. Cada ferramenta vira uma aula prática.
>
> Se não lembrar de nenhuma agora, tudo bem. Clique em "Pular esta".

## 9. Referências · chave `referencias`
**Duração:** 45s · **Visual:** textarea, disciplina de fundamentos citando as referências.

> Em quem você se apoia? Autores, livros, diretrizes, metodologias.
>
> Isso dá base científica ao curso. Não precisa ser acadêmico: escreva o que você já usa e confia. Se não lembrar, pule. O time acadêmico da Faculdade FEX Educação® ajuda nessa parte depois.

## 10. Você já ensina? · chave `ensina`
**Duração:** 45s · **Visual:** cards de opção.

> Você já ensina hoje? Mentoria, curso online, turma presencial?
>
> Se sim, ótimo: em 9 de cada 10 casos da FEX, a pós-graduação entrou depois, em cima de algo que o expert já vendia. Quem já tem alunos tem um atalho para a primeira turma.
>
> Se ainda não ensina, sem problema. Escolha "Ainda não" e siga.

## 11. O formato · chave `modelo`
**Duração:** 70s · **Visual:** cards de formato, barra 30/30/40, nome do curso editável.

> Com base nas suas respostas, a ferramenta sugere o formato ideal: pós-graduação ou MBA, 6 ou 12 meses, EAD ou com mediação ao vivo.
>
> MBA combina com temas de gestão e negócios. O formato híbrido combina com áreas muito práticas.
>
> Agora olhe esta barra. É o padrão FEX 30/30/40. Numa pós de 360 horas, só 30% é hora-aula: 108 horas. O resto é autoestudo e prática do aluno. Você grava muito menos do que imagina.
>
> Confira o nome do curso, ajuste se quiser e continue.

## 12. O preço · chave `ticket`
**Duração:** 55s · **Visual:** cards de parcela, total por aluno.

> Quanto o seu aluno vai investir por mês?
>
> Em pós-graduação, a gente vende a parcela, não o valor total. O aluno compara com a mensalidade de uma faculdade, não com um curso de internet.
>
> Os valores na tela vêm de clientes reais da FEX. Escolha o que faz sentido para o seu público. Na próxima tela você vê o efeito disso no faturamento.

## 13. O potencial · chave `audiencia`
**Duração:** 70s · **Visual:** sliders, número do faturamento subindo.

> Quantas pessoas já te conhecem?
>
> Separe em duas. Base quente: quem já foi seu aluno, paciente ou cliente. Audiência fria: seguidores, lista de e-mail, contatos.
>
> A referência da FEX é 5% de conversão na base quente e 1% na fria. Você pode ajustar.
>
> Arraste e veja o faturamento da primeira turma. Repare na frase de baixo: quanto você fatura só com a base quente, sem gastar nada com anúncio. Esse é o dinheiro que já está na sua mesa.

## 14. O lançamento · chave `campanha`
**Duração:** 60s · **Visual:** seis cards de campanha.

> Como você quer lançar a primeira turma?
>
> Não existe um jeito certo. O que muda é onde está a confiança do seu público. Tem base de alunos? Campanha interna. Tem audiência nas redes? Aula magna ao vivo. Área prática? Imersão presencial. Base pequena e engajada? Lançamento relâmpago no WhatsApp.
>
> Escolha o que tem mais a ver com você hoje. O plano completo traz o passo a passo do modelo escolhido.

## 15. A aula magna · chave `magna`
**Duração:** 50s · **Visual:** calendário, frase com a data de abertura das matrículas.

> Quando vai ser a aula magna? É a abertura oficial da sua turma.
>
> A implantação com a Faculdade FEX Educação® leva 90 dias, entre validar a matriz, registrar e produzir. Por isso a data mínima é daqui a 90 dias.
>
> Marcar a data é o que transforma intenção em projeto. Escolha e veja quando as suas matrículas abrem.

## 16. Contato · chave `contato`
**Duração:** 40s · **Visual:** campos de contato, depois a tela "Organizando o que você sabe".

> Pronto. O seu curso está montado.
>
> Deixe o seu e-mail e o seu WhatsApp para salvar o plano. Na próxima tela você vê a capa do curso, as disciplinas, as primeiras aulas e o potencial de faturamento. De graça.
>
> Clique em "Ver meu curso pronto".

## 17. O plano completo · chave `plano` (vídeo de boas-vindas pós-compra e para anúncio de remarketing)
**Duração:** 90s · **Visual:** rolagem pelo plano completo, terminando no botão verde do especialista.

> Este é o seu plano completo. Vamos passear por ele.
>
> Primeiro, o resumo da sua formação em uma página. Depois, a matriz: todas as disciplinas, com ementa, objetivos e as quatro aulas de cada uma.
>
> Aqui está o roteiro modelo de aula: gancho, conceito, demonstração, erros comuns e tarefa. Use em todas as gravações. E o plano de gravação, com o checklist do seu estúdio caseiro.
>
> Mais abaixo, o potencial de faturamento, o passo a passo do seu lançamento, o texto da página de vendas e a mensagem pronta para mandar para a sua base. E o cronograma de 90 dias, com o dia exato em que as matrículas abrem.
>
> No final, o próximo passo. Com a Faculdade FEX Educação®, este plano vira uma pós-graduação com validade acadêmica, com estrutura de faculdade ao seu lado. Clique no botão verde e fale com o nosso especialista. O seu plano já vai junto na mensagem.
