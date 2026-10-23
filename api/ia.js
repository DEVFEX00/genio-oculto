// Sugestões com IA do Crie sua Formação (função da Vercel).
// Recebe { campo, respostas, evitar } e devolve { sugestao }.
// Precisa da variável de ambiente ANTHROPIC_API_KEY no projeto da Vercel.
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const REGRAS = `Você é a assistente de criação de cursos da Faculdade FEX Educação®.
A pessoa está montando um curso de extensão universitária a partir da experiência dela.
Escreva sempre em português do Brasil, simples, direto e com energia, como uma professora experiente que quer ver a pessoa vender.
Regras obrigatórias:
- Nunca use travessão. Use vírgula, dois-pontos ou ponto.
- Escreva "para", nunca "pra".
- Nunca fale em pós-graduação, MBA, MEC, "reconhecido", "chancela" ou "certificação MEC".
- Não invente números, resultados garantidos, prêmios ou dados que a pessoa não deu.
- Use o que a pessoa escreveu (área, aluno ideal, promessa, perguntas) para ser específico. Nada genérico.
Sobre quem está preenchendo: é um especialista que costuma duvidar de si. Tem síndrome do impostor, medo de ser julgado, medo de ser enganado e medo de que duvidem dele.
Por isso:
- Escreva de um jeito que dê confiança e orgulho do que a pessoa sabe, mostrando o valor da experiência dela.
- Seja motivador sem exagero: nada de promessas mágicas, "fique rico" ou garantias. Transparência gera confiança.
- O nome e a promessa devem soar profissionais e possíveis de cumprir, para a pessoa ter coragem de apresentar o curso.`;

const TAREFAS = {
  titulo: {
    pedido: (r) => `Crie UM nome de curso forte e específico para esta formação de ${r.titulacao || "extensão universitária"}.
O nome deve fazer o aluno ideal pensar "isso é para mim". Junte o tema com a transformação prometida.
Formato: até 70 caracteres. Pode usar a estrutura "Tema: transformação". Não comece com "Curso de" e não use só "${r.titulacao} em ${r.area}".
Não repita nenhum destes nomes: ${(r.evitar || []).join(" | ") || "nenhum"}.`,
    schema: { sugestao: { type: "string" } },
  },
  promessa: {
    pedido: () => `Reescreva a promessa do curso como uma frase clara do que o aluno vai conseguir fazer ao final.
Comece com um verbo no infinitivo (sem "vai conseguir" no começo), sem "ele" ou "ela", até 25 palavras, concreta e possível de ver acontecendo.
Se a pessoa ainda não escreveu promessa, crie uma a partir da área, do aluno ideal e das perguntas.`,
    schema: { sugestao: { type: "string" } },
  },
  persona: {
    pedido: () => `Descreva em uma frase curta (até 15 palavras) quem é o aluno ideal deste curso: quem é e o que quer. Sem "pessoas que" genérico.`,
    schema: { sugestao: { type: "string" } },
  },
  perguntas: {
    pedido: (r) => `Liste 8 perguntas reais que o público desta área costuma fazer para quem é especialista nela, escritas do jeito que as pessoas falam.
Cada pergunta vai virar uma aula. Varie entre começo, passo a passo, erros comuns, resultados e casos.
Não repita estas: ${(r.perguntasAtuais || []).join(" | ") || "nenhuma"}.`,
    schema: { sugestao: { type: "array", items: { type: "string" } } },
  },
  ferramentas: {
    pedido: (r) => `Liste 5 ferramentas, protocolos ou modelos de trabalho que um especialista desta área usa e poderia ensinar (fichas, checklists, roteiros, planilhas, métodos). Nomes curtos, até 6 palavras.
Não repita estas: ${(r.ferramentasAtuais || []).join(" | ") || "nenhuma"}.`,
    schema: { sugestao: { type: "array", items: { type: "string" } } },
  },
  capa: {
    pedido: (r) => `Crie a capa final do curso de ${r.titulacao || "extensão universitária"}:
- "titulo": um nome forte e específico, até 70 caracteres, que junte o tema com a transformação (pode usar "Tema: transformação"; não comece com "Curso de").
- "promessa": o que o aluno vai conseguir ao final, começando com verbo no infinitivo, até 25 palavras, sem "ele" ou "ela".`,
    schema: { titulo: { type: "string" }, promessa: { type: "string" } },
  },
};

const corta = (v, n) => String(v ?? "").slice(0, n);

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ erro: "Use POST" });
  const { campo, respostas = {}, evitar = [] } = req.body || {};
  const tarefa = TAREFAS[campo];
  if (!tarefa) return res.status(400).json({ erro: "Campo desconhecido" });
  const r = {
    nome: corta(respostas.nome, 60), area: corta(respostas.area, 120), anos: Number(respostas.anos) || null,
    persona: corta(respostas.persona, 300), promessa: corta(respostas.promessa, 500),
    perguntasAtuais: String(respostas.perguntas || "").split("\n").map((p) => p.trim()).filter(Boolean).slice(0, 30).map((p) => corta(p, 200)),
    ferramentasAtuais: (respostas.ferramentas || []).slice(0, 10).map((p) => corta(p, 80)),
    titulacao: corta(respostas.titulacao, 40), horas: Number(respostas.horas) || null,
    evitar: (Array.isArray(evitar) ? evitar : []).slice(0, 8).map((p) => corta(p, 120)),
  };
  const contexto = `Respostas da pessoa:
- Área: ${r.area || "não informada"}
- Anos de experiência: ${r.anos ?? "não informado"}
- Aluno ideal: ${r.persona || "não informado"}
- Promessa (texto da pessoa): ${r.promessa || "não informada"}
- Titulação escolhida: ${r.titulacao || "não definida"}${r.horas ? ` (${r.horas}h)` : ""}
- Perguntas que ela mais ouve: ${r.perguntasAtuais.join(" | ") || "não informadas"}
- Ferramentas: ${r.ferramentasAtuais.join(" | ") || "não informadas"}`;
  try {
    const response = await client.beta.messages.create({
      model: "claude-opus-5-5",
      max_tokens: 2000,
      betas: ["server-side-fallback-2026-07-01"],
      fallbacks: "default",
      system: REGRAS,
      output_config: {
        effort: "low",
        format: { type: "json_schema", schema: { type: "object", properties: tarefa.schema, required: Object.keys(tarefa.schema), additionalProperties: false } },
      },
      messages: [{ role: "user", content: `${contexto}\n\nTarefa:\n${tarefa.pedido(r)}` }],
    });
    if (response.stop_reason === "refusal") return res.status(422).json({ erro: "Sem sugestão" });
    const texto = response.content.filter((b) => b.type === "text").map((b) => b.text).join("");
    const dados = JSON.parse(texto);
    return res.status(200).json(campo === "capa" ? dados : { sugestao: dados.sugestao });
  } catch (e) {
    console.error("ia:", e?.status, e?.message);
    return res.status(502).json({ erro: "IA indisponível" });
  }
}
