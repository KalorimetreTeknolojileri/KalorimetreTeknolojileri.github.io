#!/usr/bin/env python3
"""Build static technical SEO assets without touching site layout or JavaScript.

Run before going live, using the *actual canonical HTTPS domain*:
    python3 tools/build_seo.py --domain https://www.siteniz.com

With no domain, SEO metadata and structured data remain valid, but canonical,
Open Graph URLs, and sitemap are intentionally omitted rather than invented.
"""
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'index.html'
URL_START, URL_END = '<!-- SEO_URL_START -->', '<!-- SEO_URL_END -->'
JSON_START, JSON_END = '<!-- SEO_JSONLD_START -->', '<!-- SEO_JSONLD_END -->'
DESCRIPTION = (
    'Ultrasonik ve mekanik kalorimetre, ısı sayacı, ısı pay ölçer bilgileri ve '
    'sıcak-soğuk su sayacı modelleri. POLİMETER ve CALMET ürünlerini keşfedin.'
)
TITLE = 'Kalorimetre, Ultrasonik Isı Sayacı ve Su Sayaçları | D & E'
PRODUCTS = [
    'POLİMETER PM01-25 Ultrasonik Kalorimetre',
    'POLİMETER PM02-20 Ultrasonik Kalorimetre',
    'POLİMETER M-15 Mekanik Kalorimetre',
    'POLİMETER PU-50 Büyük Çaplı Kalorimetre',
    'CALMET U20 Ultrasonik Kalorimetre',
    'CALMET Ultrasonik Sıcak Su Sayacı',
    'CALMET Ultrasonik Soğuk Su Sayacı',
    'CALMET Mekanik Sıcak Su Sayacı',
    'CALMET Mekanik Soğuk Su Sayacı',
    'CALMET Single Jet Sıcak Su Sayacı',
    'CALMET Single Jet Soğuk Su Sayacı',
    'CALMET M-20 Mekanik Kalorimetre',
    'Mavi Kalorifer Temizleme Makinesi',
    'Kırmızı Kalorifer Temizleme Makinesi',
]


def canonical_domain(value: str) -> str:
    value = value.strip()
    if not value:
        return ''
    if '://' not in value:
        value = 'https://' + value
    parts = urlsplit(value)
    host = (parts.hostname or '').lower()
    if (parts.scheme != 'https' or parts.username or parts.password or parts.port
            or parts.path not in ('', '/') or parts.query or parts.fragment
            or not re.fullmatch(r'(?=.{4,253}$)[a-z0-9-]+(?:\.[a-z0-9-]+)+', host)
            or host.startswith('www.') and host.count('.') < 2
            or any(part.startswith('-') or part.endswith('-') for part in host.split('.'))
            or host.endswith(('.test', '.example', '.invalid', '.localhost'))):
        raise ValueError('HTTPS ve gerçek alan adı kullanın; yol, port veya sorgu eklemeyin.')
    return 'https://' + host


def insert_block(markup: str, start: str, end: str, body: str) -> str:
    pattern = re.escape(start) + r'.*?' + re.escape(end)
    replacement = start + ('\n' + body if body else '') + '\n' + end
    new, count = re.subn(pattern, lambda _: replacement, markup, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f'SEO işaretleri bulunamadı: {start} / {end}')
    return new


def build_schema(origin: str) -> dict:
    site = {
        '@type': 'WebSite',
        '@id': (origin + '/#website') if origin else '#website',
        'name': 'Kalorimetre Teknolojileri',
        'inLanguage': 'tr-TR',
        'publisher': {'@id': origin + '/#organization' if origin else '#organization'},
    }
    organization = {
        '@type': 'Organization',
        '@id': origin + '/#organization' if origin else '#organization',
        'name': 'D & E | Kalorimetre Teknolojileri',
        'logo': origin + '/favicon.svg' if origin else 'favicon.svg',
    }
    page = {
        '@type': 'CollectionPage',
        '@id': origin + '/#webpage' if origin else '#webpage',
        'name': TITLE,
        'description': DESCRIPTION,
        'inLanguage': 'tr-TR',
        'isPartOf': {'@id': origin + '/#website' if origin else '#website'},
        'mainEntity': {
            '@type': 'ItemList',
            'name': 'POLİMETER ve CALMET Sayaç Koleksiyonu',
            'numberOfItems': len(PRODUCTS),
            'itemListElement': [
                {'@type': 'ListItem', 'position': i, 'name': name}
                for i, name in enumerate(PRODUCTS, start=1)
            ],
        },
    }
    if origin:
        site['url'] = origin + '/'
        organization['url'] = origin + '/'
        page['url'] = origin + '/'
    return {'@context': 'https://schema.org', '@graph': [site, organization, page]}


def run(origin: str) -> None:
    html = INDEX.read_text(encoding='utf-8')
    tags = ''
    if origin:
        homepage = escape(origin + '/', quote=True)
        image = escape(origin + '/assets/industrial-night.jpg', quote=True)
        tags = '\n'.join([
            f'<link rel="canonical" href="{homepage}"/>',
            f'<meta property="og:url" content="{homepage}"/>',
            f'<meta property="og:image" content="{image}"/>',
            '<meta property="og:image:alt" content="Kalorimetre Teknolojileri - koyu endüstriyel vitrin"/>',
            f'<meta name="twitter:image" content="{image}"/>',
        ])
    html = insert_block(html, URL_START, URL_END, tags)
    schema = json.dumps(build_schema(origin), ensure_ascii=False, indent=2).replace('<', '\\u003c')
    html = insert_block(html, JSON_START, JSON_END,
                        '<script type="application/ld+json" id="structured-data">\n'
                        + schema + '\n</script>')
    INDEX.write_text(html, encoding='utf-8')
    robots = 'User-agent: *\nAllow: /\n'
    if origin:
        robots += '\nSitemap: ' + origin + '/sitemap.xml\n'
        # Include genuinely distinct, user-readable technical guides in the sitemap.
        # HTML fragments (#koleksiyon, #iletisim etc.) are not separate pages.
        guide_urls = sorted('/rehber/' + p.parent.name + '/' for p in (ROOT / 'rehber').glob('*/index.html'))
        service_urls = sorted('/hizmetler/' + p.parent.name + '/' for p in (ROOT / 'hizmetler').glob('*/index.html'))
        urls = [origin + '/'] + [origin + u for u in guide_urls + service_urls]
        sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                   + ''.join('  <url>\n    <loc>' + escape(u) + '</loc>\n  </url>\n' for u in urls)
                   + '</urlset>\n')
        (ROOT / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    else:
        (ROOT / 'sitemap.xml').unlink(missing_ok=True)
    (ROOT / 'robots.txt').write_text(robots, encoding='utf-8')
    print('SEO metadata ve schema.org yapılandırılmış verileri hazır.')
    if origin:
        print('Canonical, sosyal paylaşım URL’leri, robots.txt, sitemap.xml:', origin)
    else:
        print('Alan adı henüz bilinmiyor. Yayına almadan önce --domain seçeneğini çalıştırın.')


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--domain', default='', help='Örn: https://www.siteniz.com (gerçek alan adınız)')
    args = p.parse_args()
    try:
        run(canonical_domain(args.domain))
    except ValueError as exc:
        p.error(str(exc))


if __name__ == '__main__':
    main()
