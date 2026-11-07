# PII Guard BR (nome de trabalho, provisório)

Derivado atribuído de [pii-tokens](https://github.com/oLucasAguilar/pii-tokens)
(MIT, Copyright (c) 2026 Lucas Aguilar). Preserva avisos MIT e autoria.
Ver `NOTICE` e `LICENSE`.

## Escopo deste MVP

Foco em **configuração segura e validação reproduzível em Linux/Bash**.
Reaproveita o escopo central da base (mascaramento reversível de CPF, CNPJ,
email, telefone, nomes em tabelas, termos) sem adicionar provedores, interface
web, OCR próprio ou suporte universal.

Não afirma superioridade sobre a base. Comparação base/derivado com os mesmos
casos e ambiente está registrada em `docs/` e nos resultados de testes.

## Instalação (Linux)

Ver `docs/ambiente.md`. Resumo:

```bash
python3 -m venv .venv
.venv/bin/pip install -r plugin/requirements.txt
.venv/bin/pip install keyrings.alt
make test
```

## Uso

Herda comandos da base (`pii-check`, `pii-mask`, `pii-unmask`, `pii-exec`,
`pii-reveal`, `pii-scrub`, `pii-selfcheck`). Ver documentação da base em
`docs/usage.md` (não incluído; consultar origem).

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

Dados exclusivamente sintéticos. Resultados: base e derivado executados com as
mesmas dependências (`keyrings.alt`, tesseract instalado).

## Origem e licença

MIT (Lucas Aguilar, 2026). Avisos preservados. Modificações próprias
registradas em `NOTICE`.
