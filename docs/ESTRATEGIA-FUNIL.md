# Gênio Oculto · Estratégia de funil e tráfego

Leitura de gestor de tráfego sobre como esse produto vende. O objetivo do funil não é o R$ 97: é gerar **conversas qualificadas com o especialista** para o Plano Prata. O R$ 97 paga a mídia e filtra quem tem intenção real.

## 1. A lógica do funil

```
Anúncio → Landing (prévia grátis) → Construtor (16 telas) → Lead capturado → Prévia do curso
  → Checkout R$ 97 → Plano completo → Botão do especialista (WhatsApp) → Diagnóstico → Plano Prata
```

Três momentos de valor que a página já explora:
1. **"Eu sei muito"**: calculadora de anos → horas de prática (landing e tela 3).
2. **"Meu curso existe"**: capa, disciplinas e aulas aparecendo ao vivo e na prévia.
3. **"Isso dá dinheiro"**: simulador com a frase "só com a sua base quente".

O lead é capturado **antes** da prévia (tela 16). Quem abandona o checkout já é lead: dá para recuperar por WhatsApp e remarketing.

## 2. As duas formas de vender (como você comentou)

| | Rota A · Direto para a ferramenta | Rota B · VSL |
|---|---|---|
| Para quem | Expert que já ensina e entende "pós" | Público frio, que ainda não se vê como "dono de curso" |
| Anúncio leva para | Landing do Gênio Oculto | Página de VSL (3 a 6 min) com botão para a landing |
| Promessa do anúncio | "Veja o seu curso montado em 15 minutos" | "O seu óbvio é o milagre de alguém" (história + virada) |
| Métrica de corte | Custo por lead (tela 16) | Retenção do VSL a 50% e cliques no botão |

Comece pela Rota A: é mais barata de testar e a própria ferramenta é o "VSL interativo".

## 3. Públicos para testar (Meta)

1. **Profissionais liberais com 10+ anos**: interesses em fisioterapia, odontologia, psicologia, nutrição, estética, direito + comportamento "administradores de página" / "pequenos empresários". Faixa 32 a 58 anos.
2. **Infoprodutores e mentores**: interesses em Hotmart, Kiwify, Hubla, lançamento, mentoria.
3. **Lookalike 1%** da base de experts da FEX (50 parceiros atuais + leads de pós dos últimos 12 meses) e dos compradores de R$ 97 assim que houver 100.
4. **Remarketing**: quem começou o construtor e não terminou (evento `genio_inicio` sem `genio_lead`), e quem viu a prévia e não comprou.

## 4. Ângulos de criativo (5 para começar)

1. **Calculadora**: "Você tem 18 anos de experiência? São 31.680 horas de prática. Uma pós inteira tem 360." (vídeo com o slider na tela)
2. **Tela gravada**: o curso se montando ao vivo enquanto alguém digita os temas. Sem narração, com legenda.
3. **Pergunta que abre conversa**: "O que as pessoas sempre te perguntam? Cada resposta é uma aula que você ainda não gravou."
4. **Objeção da gravação**: "Você acha que precisa gravar 360 horas. São 108." (padrão 30/30/40)
5. **Prova**: casos de experts FEX com números (confirmar autorização de uso de nome antes de anunciar).

Todos terminam com uma ação: "Descubra o seu Gênio Oculto. Começa grátis."

## 5. Eventos de rastreamento (já no código)

| Evento na página (`dataLayer`) | Evento Meta | Quando |
|---|---|---|
| `genio_inicio` | ViewContent | Passou da 1ª tela do construtor |
| `genio_lead` | Lead | Enviou o contato (tela 16) |
| `genio_checkout` | InitiateCheckout | Abriu o checkout |
| `genio_compra` | Purchase (R$ 97) | Pagou (volta com `?pago=1`) ou demo |
| `genio_especialista` | Contact | Clicou no botão do especialista |
| `genio_video` | (só GTM) | Abriu um vídeo tutorial |

Otimize a campanha para **Lead** até ter volume; depois teste otimizar para **Purchase**.

## 6. Metas iniciais para julgar o teste

| Etapa | Referência para começar |
|---|---|
| Clique da landing para o construtor | 25% ou mais |
| Início → lead (tela 16) | 35% ou mais |
| Lead → compra R$ 97 | 5% a 10% |
| Compra → clique no especialista | 30% ou mais |
| Clique → diagnóstico agendado | 40% ou mais |

São pontos de partida para calibrar, não números da FEX. Ajuste depois das primeiras 2 semanas.

## 7. Recuperação (onde está o dinheiro rápido)

- **Lead sem compra (até 1h):** WhatsApp completo, no tom FEX: o que é, o que inclui, CTA. Exemplo: "Oi, Marcos. Vi que você montou a prévia do MBA em Gestão de Clínicas Odontológicas. O plano completo traz as 28 aulas, o roteiro de gravação, o texto da sua página de vendas e o cronograma até a aula magna, por R$ 97. Quer que eu te mande o link?"
- **Comprador sem clique no especialista (D+1):** ligação ou WhatsApp do comercial digital com a pergunta "Qual a data que você marcou para a aula magna?".
- **Regra de ouro FEX:** não dar desconto no Plano Prata. Se achar caro, oferecer o degrau de baixo (registro avulso ou Plano Bronze).

## 8. Antes de ligar o tráfego

- [ ] Link do checkout no `CONFIG.CHECKOUT_URL`, com página de obrigado voltando para `.../?pago=1`
- [ ] Confirmar o WhatsApp do especialista (hoje está o da secretaria/B2B da base de conhecimento)
- [ ] `META_PIXEL_ID` e/ou `GTM_ID`
- [ ] `LEAD_WEBHOOK_URL` para o CRM (RD Station via Make/Zapier/n8n), para o comercial receber o lead no mesmo dia
- [ ] Validar a página com a secretaria (secretaria@fexeducacao.edu.br), como pede o Manual de Comunicação
- [ ] Confirmar autorização dos experts citados nos cases da landing
