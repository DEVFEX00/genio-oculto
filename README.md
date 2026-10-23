# Crie sua Formação · Faculdade FEX Educação®

Site estático do funil **Crie sua Formação**: capa do aplicativo, construtor passo a passo (16 telas) com "Sugerir com IA", prévia grátis, checkout de R$ 97 na Hubla, plano completo e CTA do Plano Bronze. O curso é montado como **extensão universitária**, com indicação automática da titulação (Iniciação, Atualização, Capacitação ou Aperfeiçoamento).

**Não tem etapa de build.** O site é o `index.html` da raiz. Editou no GitHub, a Vercel publica.

## Estrutura
- `index.html`: o site inteiro (HTML, CSS e JavaScript).
- `assets/`: logos FEX (branco e preto) e favicon.
- `vercel.json`: configuração da Vercel (cache dos assets).
- `api/ia.js`: função da Vercel que chama o Claude para o nome do curso, a promessa e o "Sugerir com IA". `package.json` traz a dependência dela.
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
| `CHECKOUT_URL` | Link do pagamento de R$ 97 | Hubla: `https://pay.hub.la/3MBwoxpx8wevYDD06Tkt` (`null` = modo demonstração) |
| `WHATSAPP_ESPECIALISTA` | Destino do botão do especialista | 5511915612544 (secretaria e B2B) |
| `LEAD_WEBHOOK_URL` | Envia o lead para o CRM | `null` |
| `META_PIXEL_ID`, `GTM_ID` | Rastreamento | `null` |
| `IA_ENDPOINT` | Função de IA do site | `/api/ia` (se falhar, as sugestões vêm das regras do navegador) |
| `VIDEOS` | Vídeo de cada seção (voce, aluno, metodo, formato, potencial, lancamento, envio): ID do YouTube ou MP4 em `assets/videos/` | |

**Depois do pagamento (Hubla):** na área de membros, cadastre o link `https://genio-oculto-one.vercel.app/?pago=1`. No mesmo navegador em que a pessoa preencheu, o plano completo abre direto. Em outro aparelho ou navegador, aparece uma tela para colar o **link pessoal do curso** (mostrado antes do pagamento, com botão de copiar e de enviar para o próprio WhatsApp), que guarda as respostas no próprio endereço.

## IA (nome do curso, promessa e "Sugerir com IA")
A função `api/ia.js` usa o Claude (modelo `claude-opus-5-5`). Para ligar:
1. Crie uma chave em console.anthropic.com (API Keys).
2. Na Vercel: projeto → Settings → Environment Variables → `ANTHROPIC_API_KEY` = a chave (Production).
3. Faça um novo deploy (Deployments → Redeploy).

Sem a chave, o site funciona igual, com as regras locais no lugar da IA. As instruções da IA estão no topo de `api/ia.js` (tom, regras da FEX e o perfil do público: síndrome do impostor, medo de julgamento e de ser enganado).

## Atalhos
- `seudominio/#construtor`: abre direto no construtor (bom para remarketing).
