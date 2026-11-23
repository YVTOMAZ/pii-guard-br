# Contextuva (nome de trabalho, provisório; slug ASCII `contextuva`)

[![Testes](https://github.com/YVTOMAZ/pii-guard-br/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YVTOMAZ/pii-guard-br/actions/workflows/tests.yml)
[![Release](https://img.shields.io/github/v/release/YVTOMAZ/pii-guard-br)](https://github.com/YVTOMAZ/pii-guard-br/releases)
[![Licença: MIT](https://img.shields.io/github/license/YVTOMAZ/pii-guard-br)](LICENSE)

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

## Exemplo rápido

Depois da instalação abaixo, a partir da raiz do repositório. Dados 100% sintéticos.

```bash
printf 'Cliente: Fulana de Tal\nCPF: 291.417.776-38\nE-mail: fulana@empresa.test\nTelefone: (11) 91234-5678\n' > exemplo.txt
plugin/bin/pii-mask exemplo.txt
```

```text
Cliente: Fulana de Tal
CPF: CPF#67ce50b52876
E-mail: EMAIL#a6cc9835b589
Telefone: PHONE#37ad8a434c42
```

Saída copiada de uma execução real. Os tokens dependem do cofre local e podem
variar entre instalações. Nomes em texto livre não são mascarados por padrão, e `example.com` e `example.org` ficam de fora de
propósito. Ver `docs/limites.md`.

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

## Contribuindo / Segurança

- Guia de contribuição: [CONTRIBUTING.md](CONTRIBUTING.md)
- Código de conduta: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- Política de segurança: [SECURITY.md](SECURITY.md)
- Suporte: [SUPPORT.md](SUPPORT.md)
- Registro de mudanças: [CHANGELOG.md](CHANGELOG.md)

Dados exclusivamente sintéticos. Resultado da última execução local do derivado:
ver `docs/resultados-testes.md`.

## Origem e licença

MIT (Lucas Aguilar, 2026). Avisos preservados. Modificações próprias
registradas em `NOTICE`.
