# Convite de casamento — Márcia & Alessandro

Site estático (HTML + CSS + JavaScript), publicado pela Vercel a partir da branch `main`.

## Onde alterar as informações

Quase tudo fica no começo do `<script>`, no final do `index.html`:

| O quê | Variável |
| --- | --- |
| Chave Pix, nome e cidade de quem recebe | `pixConfig` |
| Lista de presentes | `presentes` |
| Cartão de "valor livre" | `permitirValorLivre` |
| WhatsApp para confirmar presença (vazio esconde o botão) | `whatsappConfirmacao` |
| Máximo de acompanhantes (0 = não pergunta) | `maxAcompanhantes` |
| Informações úteis: traje, estacionamento etc. (vazio esconde a seção) | `informacoesUteis` |
| Música de fundo: nome do arquivo .mp3 (vazio esconde o botão) | `musica` |
| Data e horário da cerimônia | `weddingDateStr` |

Textos fixos, como o endereço da igreja e o cartão da festa, ficam direto no HTML.

Se a **data ou o horário** mudarem, atualize também o arquivo `casamento.ics`, que é o "Adicionar à agenda" do iPhone e do Outlook.

Se o **endereço do site** mudar, atualize as URLs `og:url` e `og:image` no `<head>`. São elas que geram a prévia ao compartilhar o link no WhatsApp.

## Imagens

- `capa.jpg`: foto da capa.
- `og-image.jpg`: imagem da prévia no WhatsApp e redes sociais (1200×630).
- `flores-topo.webp` e `flores-base.webp`: hortênsias recortadas da arte do convite.
- `favicon.svg` e `apple-touch-icon.png`: ícones do site.

## Estilos (Tailwind)

O `styles.css` é gerado a partir das classes usadas no `index.html`. Se você **adicionar classes novas** do Tailwind no HTML, gere o arquivo de novo:

```bash
npx tailwindcss@3.4.17 -i tailwind.css -o styles.css --content index.html --minify
```

Trocar textos, presentes ou outras configurações **não** exige gerar o arquivo de novo.
