# Uso (resumo curto)

Comandos em `plugin/bin/` (adicionar ao `PATH` ou chamar pelo caminho):

- `pii-allow` — gerencia domínios/termos permitidos.
- `pii-check` — verifica texto/arquivo em busca de PII.
- `pii-exec` — executa comando mascarando saída.
- `pii-mask` — mascara texto/arquivo.
- `pii-reveal` — revela token autorizado.
- `pii-scrub` — remove PII de texto.
- `pii-selfcheck` — auto-verificação (usa `PII_SELFCHECK_MODEL`).
- `pii-sheet` — processa planilhas.
- `pii-unmask` — reverte mascaramento autorizado.

Configuração: ver `docs/configuracao.md` e `.env.example`. Documentação completa
da base: <https://github.com/oLucasAguilar/pii-tokens>.

## Exemplo: mascarar e reverter

Dados sintéticos. Rode a partir da raiz do repositório, com o ambiente de
`docs/ambiente.md` pronto.

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

Para voltar ao valor original, use `pii-unmask` com o token. Ele só imprime em
terminal interativo (fora do Claude, que usa `pii-reveal`):

```bash
plugin/bin/pii-unmask CPF#67ce50b52876
```

```text
CPF#67ce50b52876	29141777638
```

O CPF volta sem pontuação (o cofre guarda só os dígitos). Os tokens dependem do
cofre local e podem diferir na sua máquina. `example.com` e `example.org` não
são mascarados (lista de domínios permitidos), por isso o exemplo usa
`empresa.test`.
