# Resultados de testes (derivado Contextuva)

Data/hora (BRT): 2026-11-07 14:01:02 -03 (execução registrada nesta rodada).

## Ambiente

- Python: `Python 3.12.3` (`.venv/bin/python`)
- keyring: 25.7.0
- keyrings.alt: 5.0.2
- fastmcp: 4.1.4
- Pillow: 12.3.0
- tesseract: 5.3.4 (leptonica 1.82.0)
- cryptography: 50.0.2; openpyxl: 3.1.5
- Sistema: Linux (sem remote configurado; branch `docs/config-real`)

## Comando executado

```bash
make test PYTHON=.venv/bin/python
```

Equivalente:

```bash
PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring .venv/bin/python tests/test_pii.py
PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring .venv/bin/python tests/test_desktop.py
```

Log completo: `/tmp/pii-guard-br-test.log` (cópia em `/tmp/opencode/pii-guard-br-test.log`).

## Resultado

- Saída: `254` casos `ok`, `16` casos `FAIL`, `failures: 16`.
- Código de saída: `2` (`make: *** [Makefile:6: test] Erro 1`).

## Falhas registradas (sem correção de código nesta missão)

1. `pii-check: through the hook, the command output reaches Claude as tokens`
2. `pii-check: through the hook, the file it wrote reaches Claude as tokens`
3. `pii-check: with a working keyring, no warning about irreversible tokens`
4. `pii-exec: a formatted CPF searched by digits finds nothing, and says to use .fmt`
5. `pii-exec: TOKEN.fmt finds the formatted CPF, with no hint`
6. `pii-exec: a CPF written as digits is found, with no hint`
7. `pii-exec: CNPJ.fmt finds the formatted CNPJ`
8. `pii-exec --stdin: TOKEN.fmt is given back formatted`
9. `allowed email passes the prompt`
10. `allowed value is not masked in tool output`
11. `writing a live token into a repository file asks first`
12. `an Edit with a live token asks too`
13. `a commit message with a live token asks first`
14. `pii-scrub keeps the value reversible`
15. `Read of an image: the note names the token`
16. `Read of an image: the token is reversible`

As falhas acima são registradas como ocorreram. Correção de código fica como
tarefa separada; esta missão é restrita a documentação/configuração.

## Regressão da sobrescrita (dados sintéticos, diretórios temporários)

```bash
TMP=$(mktemp -d)
XDG_CONFIG_HOME="$TMP/cfg" \
CLAUDE_PLUGIN_OPTION_DATA_DIR="$TMP/data" \
CLAUDE_PLUGIN_OPTION_ALLOWED_EMAIL_DOMAINS='empresa.example,outra.example' \
.venv/bin/python -c 'import sys; sys.path.insert(0,"plugin/scripts"); import pii; print(pii.DATA_DIR); print(pii.ALLOWED_EMAIL_DOMAINS)'
rm -rf "$TMP"
```

Resultado: `DATA_DIR` dentro de `$TMP/data`; domínios `empresa.example` e
`outra.example` presentes em `ALLOWED_EMAIL_DOMAINS` (além dos embutidos).
Import de `pii` não criou diretórios nem acessou keyring. Código de saída: 0.

## Observação

O suíte completo não foi mascarado nem alterado. Falhas acima devem ser
investigadas em tarefa própria (provavelmente dependem de ambiente/chave/git).
Nenhuma alteração em código Python foi feita nesta missão.
