"""Avisos públicos de Contextuva; usa doubles, sem acessar chaves ou dados reais."""
import contextlib
import io
from pathlib import Path
import subprocess
import sys
import types
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'plugin/scripts'))
import hook
import cli
import pii


class BrandMessages(unittest.TestCase):
    def test_imagem_sem_ocr_mantem_politica_e_mostra_contextuva(self):
        resposta = {'type': 'image'}
        resultado, aviso = hook._mask_images(types.SimpleNamespace(available=lambda: False), resposta, None)
        self.assertEqual(resultado, resposta)
        self.assertTrue(aviso.startswith('[Contextuva]'))
        self.assertIn('install tesseract', aviso)

    def test_bloqueio_de_arquivo_mantem_decisao_e_escape(self):
        with patch.object(hook, '_mentioned_files_with_pii', return_value=['synthetic.txt']), patch.object(hook, 'emit') as emitir:
            hook.prompt({'prompt': '@synthetic.txt'})
        payload = emitir.call_args.args[0]
        self.assertEqual(payload['decision'], 'block')
        self.assertTrue(payload['reason'].startswith('[Contextuva]'))
        self.assertIn('pii-ok', payload['reason'])

    def test_confirmacao_pii_exec_preserva_contrato_do_hook(self):
        with patch.object(hook, 'emit') as emitir:
            self.assertTrue(hook._asks_for_real_values('pii-exec --stdin -- cat'))
        payload = emitir.call_args.args[0]['hookSpecificOutput']
        self.assertEqual(payload['permissionDecision'], 'ask')
        self.assertEqual(payload['hookEventName'], 'PreToolUse')
        self.assertTrue(payload['permissionDecisionReason'].startswith('[Contextuva]'))
        self.assertIn('pii-exec', payload['permissionDecisionReason'])

    def test_aviso_de_keyring_nao_altera_servico_legado(self):
        saida = io.StringIO()
        with patch.object(pii.Vault, '_load_keys', side_effect=RuntimeError('synthetic failure')), contextlib.redirect_stderr(saida):
            pii.Vault()
        self.assertTrue(saida.getvalue().startswith('[Contextuva]'))
        self.assertIn('tokens cannot be reversed', saida.getvalue())
        self.assertEqual(pii.KEYRING_SERVICE, 'pii-tokens')

    def test_cli_preserva_codigo_de_saida_e_instrucao_fmt(self):
        token = 'CPF#000000000000'
        fake = types.SimpleNamespace(Vault=lambda: object(), unmask_text=lambda t, v: t,
                                     mask_text=lambda t, v: t, mask_table_text=lambda t, v: t)
        saida = io.StringIO()
        with patch.object(cli, 'pii', fake), patch.object(cli, '_digits_only_tokens', return_value=[token]), patch.object(cli.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1, '', '')), contextlib.redirect_stderr(saida):
            with self.assertRaises(SystemExit) as erro:
                cli.cmd_exec(['--', 'grep', token])
        self.assertEqual(erro.exception.code, 1)
        self.assertTrue(saida.getvalue().startswith('[Contextuva]'))
        self.assertIn(token + '.fmt', saida.getvalue())


if __name__ == '__main__':
    unittest.main()
