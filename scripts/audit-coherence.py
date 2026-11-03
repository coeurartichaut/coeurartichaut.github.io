"""Contrôles de cohérence (grille QUALITE.md) sur un site Hugo généré.
Usage : python scripts/audit-coherence.py <dossier du site généré>"""
import re, glob, html, os, sys
os.chdir(sys.argv[1])
pages = {}
for f in glob.glob('**/index.html', recursive=True):
    k = f.replace(os.sep, '/').replace('index.html', '') or '/'
    pages[k] = re.sub(r'\s+', ' ', html.unescape(re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<[^>]+>', ' ', open(f, encoding='utf-8').read())))
# Mentions qui ne doivent plus exister
interdits = {
    'chèque': r'ch[èe]que', 'PayPal': r'paypal', '48 h': r'48 ?h', '4 étapes': r'4 étapes|quatre étapes',
    '3 phases': r'3 phases', 'ateliers bientôt': r'ateliers?[^.]{0,40}bient[ôo]t', 'dates dépassées': r'19 octobre|Toussaint',
    'EHPAD': r'EHPAD', '+20 €': r'\+ ?20 ?€', '1 h à deux': r'1 ?h à deux', 'horaires 9h-18h': r'9 ?h ?[-–à] ?18 ?h',
    'date d’article': r'Publié le [0-9]',
}
for k, p in interdits.items():
    hits = [(u, m.group(0)[:80]) for u, t in pages.items() for m in re.finditer(p, t, re.I)]
    print(f'{"OK " if not hits else "!! "}{k}: {len(hits)}', *hits[:5], sep='\n    ')
# Prix : chaque tarif, sur quelles pages
tarifs = {'60 €': r'\b60 ?(€|euros)', '50 €': r'\b50 ?(€|euros)', '30 € Pause émotion': r'Pause émotion[^.]{0,40}30 ?€|30 ?€[^.]{0,30}Pause émotion',
          '40 € duo': r'40 ?(€|euros)[^.]{0,20}par personne', '10 € atelier': r'\b10 ?(€|euros)', '80 € privatisé': r'\b80 ?(€|euros)', '100 € chez vous': r'\b100 ?(€|euros)'}
for k, p in tarifs.items():
    print(f'   {k}: {sorted(u for u, t in pages.items() if re.search(p, t, re.I))}')
# Phrases à surveiller (à relire à la main)
for k, p in {'samedi': r'samedi[^.]{0,70}', 'matériel fourni': r'mat[ée]riel[^.]{0,30}fourni[^.]{0,40}'}.items():
    print(f'?? {k}:', *sorted({(u, m.group(0)[:70]) for u, t in pages.items() for m in re.finditer(p, t, re.I)}), sep='\n    ')
