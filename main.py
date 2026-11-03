"""Servidor simples para visualizar o convite (preview).

O site é estático (index.html + fotos); este arquivo só serve os arquivos
desta pasta. Usa apenas a biblioteca padrão do Python, sem dependências.

Uso: python main.py   (porta padrão 8000, ou a definida na variável PORT)
"""

import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PASTA = os.path.dirname(os.path.abspath(__file__))
PORTA = int(os.environ.get("PORT", "8000"))


def main():
    handler = partial(SimpleHTTPRequestHandler, directory=PASTA)
    servidor = ThreadingHTTPServer(("0.0.0.0", PORTA), handler)
    print(f"Convite disponível em http://localhost:{PORTA}", flush=True)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
