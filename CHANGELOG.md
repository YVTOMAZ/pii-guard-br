# Changelog

Todas as mudanças notáveis deste projeto são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Desktop: `desktop/pyproject.toml` passa a declarar a versão `0.1.2`, a mesma de
  `desktop/manifest.json` (antes `0.1.0`, herdada do upstream).

### Added

- Teste `tests/test_versions.py`, que falha se as versões do pyproject e do manifest divergirem.

## [0.1.1] - 2026-11-11

### Changed

- CI instala as dependências do desktop a partir de `desktop/pyproject.toml`,
  para que atualizações do Dependabot sejam de fato testadas (#7, `12db3f8`).
- Desktop: `fastmcp` atualizado de 4.1.4 para 4.1.6 (#1, Dependabot, `5807306`).

### Fixed

- Plugin: adicionado `plugin/requirements.in`, que o cabeçalho de
  `plugin/requirements.txt` citava como `req.in` inexistente (#6, `055c13a`;
  fecha #5).

### Notes

- `desktop/pyproject.toml` (`0.1.0`) e `desktop/manifest.json` (`0.1.2`)
  não foram alterados nesta release; a uniformização de versões fica para
  tarefa própria.

## [0.1.0] - 2026-11-10

Primeira release pública etiquetada do derivado Contextuva
(repositório https://github.com/YVTOMAZ/pii-guard-br).

Este derivado parte de [pii-tokens](https://github.com/oLucasAguilar/pii-tokens)
(MIT, Copyright (c) 2026 Lucas Aguilar). A atribuição é preservada em
`LICENSE` e `NOTICE`.

### Added

- MVP inicial do derivado, com foco em configuração segura e validação
  reproduzível em Linux/Bash, reaproveitando o mascaramento reversível de
  CPF, CNPJ, e-mail, telefone, nomes em tabelas e termos (`44a7625`).
- Comandos do plugin em `plugin/bin/` (`5016ecc`).
- Workflow GitHub Actions "Testes" (`.github/workflows/tests.yml`) que roda
  `make test` em push de `main` e em pull requests, com actions fixadas por
  SHA (`c921621`).
- Arquivos de saúde da comunidade: `CONTRIBUTING.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md`, `SUPPORT.md`, templates de issue e de pull request
  (`3645a6a`).
- Dependabot para `pip` em `/plugin` e `/desktop` e para GitHub Actions
  na raiz (`93d7342`).

### Changed

- Documentação e `.env.example` alinhados às variáveis realmente lidas
  pelo código (`CLAUDE_PLUGIN_OPTION_*` e correlatas) (`68ae560`).
- Marca de trabalho renomeada para Contextuva (slug ASCII `contextuva`).
  Identificadores de persistência, cofre, keyring, cache e contratos Claude
  (`CLAUDE_PLUGIN_OPTION_*`, `PII_PROXY_*`, `name` do manifesto desktop)
  permanecem com os valores legados, por compatibilidade (`00eb994`).
- Avisos públicos (hooks, CLI, keyring, instalação) alinhados à marca
  Contextuva, sem mudar a lógica de mascaramento (`e11335f`).
- Extensão desktop: `display_name` passou a "Contextuva"; o `name`
  `pii-tokens` e demais identificadores de compatibilidade foram
  mantidos (`7684986`, `b6670a9`).

### Fixed

- Testes passaram a usar `sys.executable` nos subprocessos spawned,
  eliminando falhas da suíte (`e113708`).
- Referências de HEAD nos resultados de testes publicados foram
  alinhadas (`66ec471`, `8a348bb`, `5b69f06`, `48d1e98`).

### Notes

- A tag Git e a GitHub Release desta versão são `v0.1.0`.
- `desktop/pyproject.toml` já declara `version = "0.1.0"` desde o commit
  inicial e não foi alterado nesta release.
- `desktop/manifest.json` declara `"version": "0.1.2"` desde o commit
  inicial (valor herdado da linha upstream pii-tokens) e **não foi
  rebaixado** para 0.1.0.
- Não há `plugin.json` neste repositório.

[Unreleased]: https://github.com/YVTOMAZ/pii-guard-br/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/YVTOMAZ/pii-guard-br/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/YVTOMAZ/pii-guard-br/releases/tag/v0.1.0
