# Ambiente (Linux/Bash)

## Requisitos

- Python 3.10+ (testado com 3.12.3).
- Dependências do plugin: ver `plugin/requirements.txt` (cryptography, keyring, openpyxl, pillow).
- Para testes: `keyrings.alt` (backend de arquivo para ambientes sem keyring do sistema).
- Para mascaramento de imagens: `tesseract-ocr` (opcional; sem ele, imagens passam com aviso).

## Instalação de dependências (local, sem modificar o sistema além do necessário)

```bash
python3 -m venv .venv
.venv/bin/pip install -r plugin/requirements.txt
.venv/bin/pip install keyrings.alt
# opcional, para testes de imagem:
# sudo apt-get install -y tesseract-ocr
```

## Variáveis de ambiente

Em Linux com Bash interativo, o arquivo usual é `~/.bashrc`, não `/.bashrc`.
Este projeto **não modifica** `~/.bashrc` automaticamente. Configure manualmente
e recarregue com `source ~/.bashrc`.

Outros shells e sessões de login podem usar arquivos diferentes
(`~/.profile`, `~/.bash_profile`). Serviços, containers e CI precisam de
configuração própria de ambiente; não presumir que carreguem `~/.bashrc`.

Variável de ambiente não torna segredo seguro por si só: processos filhos,
diagnósticos e permissões podem expô-lo. Evitar hardcode, impressão de valores
e segredos no histórico, logs, mensagens de erro ou exemplos.

### Variáveis realmente implementadas (herdadas da base)

| Variável | Uso |
|---|---|
| `XDG_CONFIG_HOME` | Onde `config.json` é lido (padrão `~/.config`). |
| `CLAUDE_CONFIG_DIR` | Diretório de configuração do Claude (usado pelo CLI). |
| `CLAUDE_PLUGIN_ROOT` / `CLAUDE_PLUGIN_DATA` | Usados pelo setup/hook. |
| `CLAUDE_PLUGIN_OPTION_*` | Sobrescreve opções do `config.json`. |
| `PYTHON_KEYRING_BACKEND` | Backend de keyring (ex.: `keyrings.alt.file.PlaintextKeyring` em CI). |
| `PII_SELFCHECK_MODEL` | Modelo usado pelo self-check (padrão `haiku`). |

### Configuração por arquivo

`config.json` em `$XDG_CONFIG_HOME/pii-tokens/config.json` (ou `~/.config/pii-tokens/config.json`):

```json
{
  "data_dir": "~/.local/share/pii-tokens",
  "keyring_service": "pii-tokens",
  "allowed_email_domains": ["acme.example"],
  "table_tools": ["mcp__db__"]
}
```

Se o arquivo estiver ausente ou inválido, os padrões são usados (sem erro).

## Testes reproduzíveis

```bash
make test
```

Equivalente a:

```bash
PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring python3 tests/test_pii.py
PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring python3 tests/test_desktop.py
```

Os dados são exclusivamente sintéticos (gerados em tempo de execução).

Na CI (GitHub Actions, Ubuntu), `make test` roda com `tesseract-ocr` e
`fastmcp==4.1.4` instalados, para que os testes de imagem e de proxy não
sejam pulados; ver `.github/workflows/tests.yml`. A dependência `fastmcp`
é necessária para os testes de proxy (além de `keyrings.alt` e tesseract).
