# Contribuindo para o Contextuva

Obrigado pelo interesse em contribuir. Este projeto é um derivado de
[pii-tokens](https://github.com/oLucasAguilar/pii-tokens) (MIT, Copyright (c)
2026 Lucas Aguilar); a licença e a atribuição upstream são preservadas em
`LICENSE` e `NOTICE`.

## Antes de começar

- Leia `docs/ambiente.md` para pré-requisitos e instalação.
- Leia `docs/limites.md` para o escopo do MVP.
- Respeite o `CODE_OF_CONDUCT.md`.

## Desenvolvimento local

```bash
python3 -m venv .venv
.venv/bin/pip install -r plugin/requirements.txt
.venv/bin/pip install keyrings.alt
make test
```

Toda alteração deve manter `make test` verde. Novos testes são bem-vindos
quando cobrirem comportamento novo.

## Regras de contribuição

- Pull requests pequenos e focados, um tema por PR.
- Não commitar segredos, tokens, credenciais ou dados pessoais reais.
- Usar apenas dados sintéticos em exemplos, testes e issues.
- Preservar a licença MIT e a atribuição a Lucas Aguilar / pii-tokens
  (`LICENSE`, `NOTICE`).
- Não alterar lógica de mascaramento sem discussão prévia em issue.
- Não modificar `~/.bashrc` automaticamente nem adicionar dependências sem
  justificativa.

## Reporte de vulnerabilidades

Não abra issue pública com detalhes de exploração. Veja `SECURITY.md`.

## Estilo

- Markdown em português (Brasil), termos técnicos oficiais do GitHub em inglês.
- Manter consistência com a documentação existente em `docs/`.