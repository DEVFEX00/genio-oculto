"""Gera docs/planilha-leads.xlsx: a planilha que o n8n preenche com os leads do site.
A aba Leads tem um cabeçalho por campo, com o mesmo nome das chaves que o site envia ao webhook."""
import json, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SECOES = {  # cor do cabeçalho por seção do site
 "Envio do lead":"1F2937", "1 · Você":"00A63E", "2 · Seu aluno":"0E7490", "3 · Seu método":"6D28D9",
 "4 · Seu formato":"B45309", "5 · Seu potencial":"BE123C", "6 · Lançamento":"1D4ED8", "7 · Envio":"00A63E", "Origem":"4B5563"}
# (coluna, seção, pergunta ou origem no site, formato, campo sugerido no RD Station)
C = [
 ("lead_id","Envio do lead","Código único do lead, criado ao ver a prévia","Texto (CF-...)","Campo personalizado"),
 ("etapa","Envio do lead","Momento do envio: prévia, checkout, compra ou especialista","Texto","Campo personalizado ou tag"),
 ("data_hora","Envio do lead","Data e hora do envio","ISO 8601 (UTC)",""),
 ("nome","1 · Você","Qual é o seu nome?","Texto",""),
 ("sobrenome","1 · Você","Sobrenome","Texto",""),
 ("nome_completo","1 · Você","Nome + sobrenome","Texto","Nome (padrão)"),
 ("area","1 · Você","Qual é a sua área?","Texto","Campo personalizado"),
 ("anos_experiencia","1 · Você","Há quantos anos você atua?","Número","Campo personalizado"),
 ("qtd_perguntas","1 · Você","Quantas perguntas o aluno faz (mínimo 7)","Número","Campo personalizado"),
 ("perguntas","1 · Você","As perguntas que os alunos sempre fazem","Texto, separado por |","Campo personalizado"),
 ("persona","2 · Seu aluno","Para quem é o curso?","Texto","Campo personalizado"),
 ("promessa","2 · Seu aluno","O que o aluno vai conseguir no fim?","Texto","Campo personalizado"),
 ("ferramentas","3 · Seu método","Ferramentas, protocolos ou passo a passo","Texto, separado por |","Campo personalizado"),
 ("referencias","3 · Seu método","Autores, livros ou metodologias","Texto","Campo personalizado"),
 ("ja_ensina","3 · Seu método","Você já ensina hoje?","Ainda não / Mentoria ou consultoria / Curso online / Curso ou evento presencial","Campo personalizado"),
 ("objetivo","4 · Seu formato","O que o curso deve ser para o aluno?","Uma porta de entrada / Atualizar quem já atua / Capacitar para aplicar / Uma formação aprofundada","Campo personalizado"),
 ("titulacao","4 · Seu formato","Titulação escolhida","Iniciação / Atualização / Capacitação / Aperfeiçoamento","Campo personalizado"),
 ("carga_horaria","4 · Seu formato","Carga horária escolhida","Número (horas)","Campo personalizado"),
 ("qtd_modulos","4 · Seu formato","Módulos montados pela ferramenta","Número",""),
 ("modulos","4 · Seu formato","Nome dos módulos","Texto, separado por |",""),
 ("qtd_aulas","4 · Seu formato","Aulas do curso","Número",""),
 ("titulo_curso","4 · Seu formato","Nome do curso","Texto","Campo personalizado"),
 ("parcela","5 · Seu potencial","Valor da parcela (12x)","Número (R$)","Campo personalizado"),
 ("preco_total","5 · Seu potencial","Preço do curso (parcela x 12)","Número (R$)",""),
 ("base_quente","5 · Seu potencial","Quantas pessoas já te conhecem: base quente","Número","Campo personalizado"),
 ("audiencia_fria","5 · Seu potencial","Audiência fria (seguidores, lista)","Número","Campo personalizado"),
 ("conv_quente_pct","5 · Seu potencial","Conversão usada na base quente","Número (%)",""),
 ("conv_fria_pct","5 · Seu potencial","Conversão usada na audiência fria","Número (%)",""),
 ("matriculas_previstas","5 · Seu potencial","Matrículas previstas na 1ª turma","Número",""),
 ("faturamento_previsto","5 · Seu potencial","Faturamento previsto na 1ª turma","Número (R$)","Campo personalizado"),
 ("campanha","6 · Lançamento","Como quer lançar a primeira turma?","Texto","Campo personalizado"),
 ("inicio_turma","6 · Lançamento","Quando a primeira turma começa?","Data (AAAA-MM-DD)","Campo personalizado"),
 ("email","7 · Envio","E-mail","Texto","E-mail (padrão, chave do contato)"),
 ("telefone","7 · Envio","WhatsApp, como a pessoa digitou","Texto",""),
 ("whatsapp","7 · Envio","WhatsApp só com números, com 55","Texto (5511...)","Celular (padrão)"),
 ("instagram","7 · Envio","Instagram (opcional)","Texto","Campo personalizado"),
 ("aceite_contato","7 · Envio","Aceite para receber o plano e falar com a FEX","sim / não","Base legal / consentimento"),
 ("pago","Origem","Pagou os R$ 97?","sim / não","Tag ou etapa do funil"),
 ("link_pessoal","Origem","Link que reabre o curso da pessoa","URL","Campo personalizado"),
 ("utm_source","Origem","Origem do anúncio","Texto","Origem (traffic_source)"),
 ("utm_medium","Origem","Mídia","Texto","Campo personalizado"),
 ("utm_campaign","Origem","Campanha","Texto","Campo personalizado"),
 ("utm_content","Origem","Criativo","Texto","Campo personalizado"),
 ("utm_term","Origem","Termo / público","Texto","Campo personalizado"),
 ("fbclid","Origem","Clique do Facebook/Instagram","Texto",""),
 ("pagina","Origem","Página em que a pessoa estava","URL",""),
]
exemplo = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}

wb = Workbook(); fino = Side(style="thin", color="D1D5DB")
def cab(ws, row, cols, cores):
    for i,(t,cor) in enumerate(zip(cols,cores),1):
        c = ws.cell(row=row, column=i, value=t)
        c.font = Font(bold=True, color="FFFFFF", name="Calibri", size=11)
        c.fill = PatternFill("solid", fgColor=cor); c.alignment = Alignment(vertical="center", wrap_text=True)
        c.border = Border(bottom=fino, right=fino)
    ws.row_dimensions[row].height = 30; ws.freeze_panes = ws.cell(row=row+1, column=1)

# Aba 1: Leads (o n8n escreve aqui; o cabeçalho tem que ficar na linha 1)
ws = wb.active; ws.title = "Leads"
cab(ws, 1, [c[0] for c in C], [SECOES[c[1]] for c in C])
for i,c in enumerate(C,1):
    largo = 48 if c[0] in ("perguntas","modulos","ferramentas","promessa","link_pessoal","titulo_curso") else max(14, len(c[0])+4)
    ws.column_dimensions[get_column_letter(i)].width = largo
ws.auto_filter.ref = f"A1:{get_column_letter(len(C))}1"

# Aba 2: Dicionário (o que é cada coluna e de onde vem)
d = wb.create_sheet("Dicionário")
cab(d, 1, ["Coluna","Seção do site","Pergunta / origem","Formato","Sugestão no RD Station"], ["1F2937"]*5)
for r,c in enumerate(C,2):
    for k,v in enumerate(c,1):
        cell = d.cell(row=r, column=k, value=v); cell.alignment = Alignment(vertical="top", wrap_text=True)
    d.cell(row=r, column=2).font = Font(bold=True, color=SECOES[c[1]])
for k,w in enumerate([24,18,52,40,30],1): d.column_dimensions[get_column_letter(k)].width = w

# Aba 3: Exemplo (um envio de teste, para conferir o mapeamento)
e = wb.create_sheet("Exemplo")
cab(e, 1, ["Coluna","Valor de exemplo"], ["1F2937","1F2937"])
for r,c in enumerate(C,2):
    v = exemplo.get(c[0], "")
    if c[0]=="link_pessoal" and v: v = "https://genio-oculto-one.vercel.app/#p=..."
    if c[0]=="pagina": v = "https://genio-oculto-one.vercel.app/?utm_source=facebook"
    e.cell(row=r, column=1, value=c[0]).font = Font(bold=True)
    e.cell(row=r, column=2, value=v).alignment = Alignment(wrap_text=True, vertical="top")
e.column_dimensions["A"].width = 24; e.column_dimensions["B"].width = 90

# Aba 4: Como ligar no n8n
n = wb.create_sheet("Como usar")
txt = [
 ("Como ligar esta planilha no n8n", True),
 ("1. O site envia um POST em JSON para o webhook genio-oculto-... a cada momento importante (coluna etapa).", False),
 ("2. As chaves do JSON têm exatamente o mesmo nome dos cabeçalhos da aba Leads. No nó da planilha (Excel 365 ou Google Sheets), use \"Map automatically\" / mapear automaticamente.", False),
 ("3. Use a operação \"Append or Update\" com a coluna lead_id como chave: assim cada pessoa fica numa linha só, e a linha é atualizada quando ela vai ao checkout, paga ou chama o especialista.", False),
 ("   Se preferir guardar o histórico de cada momento, use \"Append\": cada envio vira uma linha nova.", False),
 ("4. No RD Station, use email como chave do contato. A aba Dicionário traz a sugestão de campo para cada coluna.", False),
 ("5. Não mude o nome dos cabeçalhos da linha 1 da aba Leads. Pode mudar cores, largura e a ordem das outras abas.", False),
 ("Quando cada envio acontece (coluna etapa)", True),
 ("prévia: a pessoa preencheu tudo e viu a prévia do curso (é o lead).", False),
 ("checkout: clicou para pagar os R$ 97.", False),
 ("compra: voltou da Hubla com o pagamento (link ?pago=1).", False),
 ("especialista: clicou no botão do WhatsApp do especialista FEX no plano completo.", False),
]
for r,(t,b) in enumerate(txt,1):
    c = n.cell(row=r, column=1, value=t); c.font = Font(bold=b, size=13 if b else 11, color="00A63E" if b else "111827")
    c.alignment = Alignment(wrap_text=True, vertical="top")
n.column_dimensions["A"].width = 120
wb.save("docs/planilha-leads.xlsx"); print("ok", len(C), "colunas")
