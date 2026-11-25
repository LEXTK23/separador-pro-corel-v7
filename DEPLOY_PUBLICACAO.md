# Publicar o Separador Pro Corel

## Conteúdo necessário
- `web/index.html`: interface web.
- `backend/main.py`: servidor FastAPI.
- `backend/requirements.txt`: dependências.
- `render.yaml`: configuração do serviço no Render.

## GitHub e Render
1. Crie um repositório no GitHub.
2. Envie o conteúdo desta pasta (não envie apenas o ZIP fechado).
3. No Render, escolha **New +** → **Blueprint**.
4. Conecte o repositório e confira a configuração lida de `render.yaml`.
5. Aguarde o deploy e copie a URL pública fornecida pelo Render.
6. Teste a página inicial e o caminho `/api/health`.

## Limitações desta versão
O recorte manual está implementado no navegador. A separação automática por IA, a classificação de escudo/número/grafismos e a exportação vetorial SVG ainda não estão implementadas. Não divulgue essas funções como disponíveis antes de serem desenvolvidas e testadas.
