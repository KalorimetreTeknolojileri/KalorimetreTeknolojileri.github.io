#!/usr/bin/env python3
"""Create SHA-384 audit manifest for first-party assets, without HTML SRI attributes.

This preserves local file:// opening. Production servers apply CSP via response headers.
"""
from pathlib import Path
import base64, hashlib

ROOT=Path(__file__).resolve().parents[1]
ASSETS=('assets/styles.css','assets/real-photos.css','assets/no-script.css','assets/script.js','assets/guide.css','assets/service-pages.css')
OUTPUT=ROOT/'assets/asset-hashes.sha384'

def refresh():
    lines=[]
    for rel in ASSETS:
        digest=base64.b64encode(hashlib.sha384((ROOT/rel).read_bytes()).digest()).decode('ascii')
        lines.append(f'sha384-{digest}  {rel}')
    OUTPUT.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'Updated SHA-384 development audit manifest: {OUTPUT.name}')

if __name__=='__main__': refresh()
