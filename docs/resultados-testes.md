# Resultados de testes (derivado Contextuva)

Data/hora (BRT): 2026-11-07 18:04:26 -03 (execução registrada nesta rodada).

## Ambiente

- Python: `Python 3.12.3` (`.venv/bin/python`)
- keyring: 25.7.0
- keyrings.alt: 5.0.2
- fastmcp: 4.1.4
- Pillow: 12.3.0
- tesseract: 5.3.4 (leptonica 1.82.0)
- cryptography: 50.0.2; openpyxl: 3.1.5
- Sistema: Linux (branch `main`, HEAD `00eb994`)

## Comando executado

```bash
make test PYTHON=.venv/bin/python
```

Equivalente:

```bash
PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring .venv/bin/python tests/test_pii.py
PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring .venv/bin/python tests/test_desktop.py
```

Log completo: `cronjob/estado/evidencias-github_manutencao-contextuva-16-testes-falhando_2026-11-07/make_test_depois_1.log`
e `.../make_test_depois_2.log`.

## Resultado

- Execução 1: `355` casos `ok`, `0` casos `FAIL`, código de saída `0`.
- Execução 2: `355` casos `ok`, `0` casos `FAIL`, código de saída `0`.

## Causa das 16 falhas anteriores (todas corrigidas)

As 16 falhas eram de ambiente/teste: os testes disparavam subprocessos com o
executável fixo `python3` (Python do sistema, sem `keyring`/dependências), em
vez do mesmo interpretador que roda a suíte (`.venv/bin/python`). Com
`keyring` indisponível, `Vault.token_for` devolvia `CPF#????????` e as
asserções falhavam. Correção: usar `sys.executable` nas chamadas
`subprocess.run` de `tests/test_pii.py` (12 ocorrências). Nenhum código de
produção foi alterado.

| # | Teste | Causa | Evidência |
|---|---|---|---|
| 1 | pii-check: through the hook, command output reaches Claude as tokens | (a) ambiente/teste | log antes: `CPF#????????`; após: `CPF#[0-9a-f]{12}` |
| 2 | pii-check: through the hook, file written reaches Claude as tokens | (a) ambiente/teste | idem |
| 3 | pii-check: with a working keyring, no warning about irreversible tokens | (a) ambiente/teste | `Warning` sumiu com `.venv` |
| 4 | pii-exec: formatted CPF searched by digits finds nothing, says .fmt | (a) ambiente/teste | dependência de `keyring` no subprocesso |
| 5 | pii-exec: TOKEN.fmt finds formatted CPF, no hint | (a) ambiente/teste | idem |
| 6 | pii-exec: CPF written as digits found, no hint | (a) ambiente/teste | idem |
| 7 | pii-exec: CNPJ.fmt finds formatted CNPJ | (a) ambiente/teste | idem |
| 8 | pii-exec --stdin: TOKEN.fmt given back formatted | (a) ambiente/teste | idem |
| 9 | allowed email passes the prompt | (a) ambiente/teste | `pii-allow` rodava em Python sem deps |
| 10 | allowed value is not masked in tool output | (a) ambiente/teste | idem |
| 11 | writing a live token into a repository file asks first | (a) ambiente/teste | `pre` rodava em Python sem deps |
| 12 | an Edit with a live token asks too | (a) ambiente/teste | idem |
| 13 | a commit message with a live token asks first | (a) ambiente/teste | idem |
| 14 | pii-scrub keeps the value reversible | (a) ambiente/teste | subprocesso `pii-scrub` sem deps |
| 15 | Read of an image: the note names the token | (a) ambiente/teste | hook subprocesso sem deps |
| 16 | Read of an image: the token is reversible | (a) ambiente/teste | idem |

## Comparação com upstream

Suíte equivalente em `referencias/pii-tokens` (somente leitura) executada com
as mesmas versões: `270` casos `ok` em `test_pii.py` e `85` em
`test_desktop.py`, `0` falhas. Logs:
`cronjob/estado/evidencias-github_manutencao-contextuva-16-testes-falhando_2026-11-07/upstream_test_pii.log`
e `.../upstream_test_desktop.log`.

## Regressão da sobrescrita (dados sintéticos, diretórios temporários)

Mantida a verificação documentada anteriormente; `make test` verde duas vezes
seguidas sem remoção de casos.
