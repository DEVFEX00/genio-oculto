# Gênio Oculto · Faculdade FEX Educação®

Site estático do funil Gênio Oculto: capa do aplicativo, construtor passo a passo (16 telas) com "Sugerir com IA", prévia grátis, checkout de R$ 97, plano completo e CTA do Plano Prata.

**Não tem etapa de build.** O site é o `index.html` da raiz. Editou no GitHub, a Vercel publica.

## Estrutura
- `index.html`: o site inteiro (HTML, CSS e JavaScript).
- `assets/`: logos FEX (branco e preto) e favicon.
- `vercel.json`: configuração da Vercel (cache dos assets).
- `docs/ROTEIROS-VIDEOS.md`: roteiro de narração de cada vídeo tutorial.
- `docs/ESTRATEGIA-FUNIL.md`: estratégia de tráfego, eventos e recuperação.
- `tools/build-artifact.py`: só para gerar a prévia no Claude. Não é usado pela Vercel.

## Publicar na Vercel
1. Vercel → Add New → Project → importe `DEVFEX00/genio-oculto`.
2. Framework Preset: **Other**. Build Command: vazio. Output Directory: vazio (raiz).
3. Deploy. Cada commit na branch `main` publica sozinho; outras branches geram link de prévia.

## O que configurar
No `index.html`, procure `const CONFIG = {` (início do `<script>`):

| Campo | Para quê | Hoje |
|---|---|---|
| `CHECKOUT_URL` | Link do pagamento de R$ 97 | `null` = modo demonstração (libera sem cobrar) |
| `WHATSAPP_ESPECIALISTA` | Destino do botão do especialista | 5511915612544 (secretaria e B2B) |
| `LEAD_WEBHOOK_URL` | Envia o lead para o CRM | `null` |
| `META_PIXEL_ID`, `GTM_ID` | Rastreamento | `null` |
| `IA_ENDPOINT` | Liga o "Sugerir com IA" a um modelo de verdade (POST `{campo, respostas}` → `{sugestao}`) | `null` = sugestões montadas no navegador a partir das respostas |
| `VIDEOS` | ID do YouTube de cada tela | vazio = "vídeo em produção" |

**Pagamento real:** na plataforma de checkout, configure a página de obrigado para voltar ao site com `?pago=1` (ex.: `https://seudominio/?pago=1`). O plano abre no mesmo navegador em que a pessoa preencheu.

## Atalhos
- `seudominio/#construtor`: abre direto no construtor (bom para remarketing).
