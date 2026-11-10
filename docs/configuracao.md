# Configuração

Herda da base `pii-tokens`. Documenta apenas o que está implementado e verificado.

## Identificadores de persistência (legados, preservados)

O nome de marca do derivado mudou para "Contextuva", mas os identificadores de
persistência e contratos permanecem com os valores legados por compatibilidade:
`pii-tokens` em `~/.config/pii-tokens`, `~/.local/share/pii-tokens`,
`~/.cache/pii-tokens` e no serviço de keyring. Não renomear esses caminhos
sem migração reversível, consentimento e backup verificado.

## config.json

Chaves suportadas (todas opcionais, com padrão):

- `data_dir`: diretório do cofre (padrão `~/.local/share/pii-tokens`).
- `keyring_service`: nome do serviço no keyring (padrão `pii-tokens`).
- `allowed_email_domains`: domínios de email que não são mascarados.
- `table_tools`: ferramentas cujas colunas são mascaradas.
- `allowed_tokens`, `terms`, `mask_ip`, `mask_names`, `copy_read_request`, `dev_tool_names`: opções avançadas.

Configuração ausente ou inválida (JSON malformado) resulta no uso de padrões,
sem exceção. Verificado em `tests/test_pii.py` (ambiente com `XDG_CONFIG_HOME`
apontando para diretório temporário).

## Sobrescrita por ambiente

Variáveis `CLAUDE_PLUGIN_OPTION_<CHAVE>` sobrescrevem o arquivo.

## Validação

- `python3 tests/test_pii.py` exerce mascaramento, reversão autorizada,
  entradas inválidas e inspeção de saídas/erros.
- Casos não cobertos: ver `docs/limites.md`.

## Marca dos avisos

Os avisos visíveis de hooks, CLI, instalação e extensão desktop (proxy MCP) usam o
prefixo `[Contextuva]`. A nota enviada ao modelo e o `ToolError` do proxy também
usam `Contextuva` como marca.

Os comandos `pii-*`, o escape `pii-ok`, os eventos e campos de hooks, os caminhos
legados de configuração/cofre, o serviço de keyring `pii-tokens`, o `name` do
manifest da extensão desktop, o `client_name` OAuth, o nome do proxy
(`create_proxy(..., name="pii-tokens")`), o pacote `pii-tokens-desktop` e o arquivo
de saída `build/pii-tokens.mcpb` permanecem idênticos por compatibilidade; a
mudança de marca não migra nem recria dados.

A extensão desktop mantém, por compatibilidade: `manifest.json` `name`
(`pii-tokens`), `version` e `author` (Lucas Aguilar, MIT). `repository.url`
passa a apontar para este repositório (`YVTOMAZ/pii-guard-br`) e a
`description` registra a derivação de `pii-tokens` (Lucas Aguilar, MIT).
Somente `display_name` muda de marca (`Contextuva`).
