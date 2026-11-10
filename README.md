# Contextuva (nome de trabalho, provisório; slug ASCII `contextuva`)

[![Testes](https://github.com/YVTOMAZ/pii-guard-br/actions/workflows/tests.yml/badge.svg)](https://github.com/YVTOMAZ/pii-guard-br/actions/workflows/tests.yml)

Derivado atribuído de [pii-tokens](https://github.com/oLucasAguilar/pii-tokens)
(MIT, Copyright (c) 2026 Lucas Aguilar). Preserva avisos MIT e autoria.
Ver `NOTICE` e `LICENSE`.

## Escopo deste MVP

Foco em **configuração segura e validação reproduzível em Linux/Bash**.
Reaproveita o escopo central da base (mascaramento reversível de CPF, CNPJ,
email, telefone, nomes em tabelas, termos) sem adicionar provedores, interface
web, OCR próprio ou suporte universal.

Não afirma superioridade sobre a base. Comparação base/derivado não está incluída
nesta entrega; fica como tarefa própria. Resultados da suíte local do derivado:
ver `docs/resultados-testes.md`.

## Instalação (Linux)

Ver `docs/ambiente.md`. Resumo:

```bash
python3 -m venv .venv
.venv/bin/pip install -r plugin/requirements.txt
.venv/bin/pip install keyrings.alt
make test
```

## Uso

Comandos disponíveis em `plugin/bin/`:

- `pii-allow`
- `pii-check`
- `pii-exec`
- `pii-mask`
- `pii-reveal`
- `pii-scrub`
- `pii-selfcheck`
- `pii-sheet`
- `pii-unmask`

Ver também `docs/uso.md` (resumo curto) e documentação da base em
<https://github.com/oLucasAguilar/pii-tokens> (origem).

## Configuração

Ver `docs/configuracao.md` e `.env.example`. Não modifica `~/.bashrc`
automaticamente.

## Limites

Ver `docs/limites.md`. Não promete proteção total nem conformidade automática
com LGPD.

## Testes

```bash
make test
```

Dados exclusivamente sintéticos. Resultado da última execução local do derivado:
ver `docs/resultados-testes.md`.

## Origem e licença

MIT (Lucas Aguilar, 2026). Avisos preservados. Modificações próprias
registradas em `NOTICE`.
