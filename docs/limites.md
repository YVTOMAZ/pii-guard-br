# Limites

Herda da base `pii-tokens`. Protege contra vazamento por descuido, não contra
um modelo decidido a extrair o dado. O que o detector não reconhece passa como está.

Passam sem máscara:
- nome em texto livre (salvo lista de termos ou opção de nomes);
- comando que falha e comando com `!`;
- chave, senha e token de API (o foco é dado pessoal).

Também:
- Em imagem, o OCR acha quase todo CPF e CNPJ, não todos.
- O token é pseudônimo, não anônimo.
- Detecção pode falhar; nomes livres dependem de configuração.

Caminhos não cobertos por esta missão:
- Desktop (extensão MCP) não validado em Linux (testado no Windows pela base).
- OCR sem tesseract não executado com imagem real.
- claude.ai não tem suporte (declaração da base).

Não alegar ausência global de vazamentos: apenas evidência nos caminhos testados.
