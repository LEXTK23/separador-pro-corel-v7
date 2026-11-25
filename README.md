# Separador Pro Corel — pacote inicial de publicação

Esta reconstrução parte do protótipo HTML salvo na biblioteca. Ela fornece uma interface web para importar imagens, selecionar uma área retangular e exportar o recorte em PNG.

## Estado das funções

- Importar imagens no navegador: disponível.
- Selecionar uma área manualmente: disponível.
- Exportar o recorte em PNG: disponível.
- Separação automática por IA: ainda não implementada nem conectada.
- Exportação SVG/vetorial e camadas editáveis: etapa futura.

## Executar localmente

```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

Abra http://127.0.0.1:8000. Verifique a API em http://127.0.0.1:8000/api/health.

## Publicar no Render

1. Envie o conteúdo desta pasta para um repositório GitHub.
2. No Render, escolha **New +** → **Blueprint**.
3. Conecte o repositório que contém `render.yaml`.
4. Confira o serviço e inicie a publicação.
5. Quando o Render fornecer a URL, abra-a e teste a página inicial e `/api/health`.

A publicação só estará concluída depois que o Render terminar o deploy e os testes forem aprovados.
