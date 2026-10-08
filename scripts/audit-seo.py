import sys,os,re,json,html
sp=sys.argv[1]; pages={}
for root,_,fs in os.walk(sp):
  for f in fs:
    if f in ('index.html','404.html'):
      p=os.path.join(root,f); r=os.path.relpath(p,sp).replace(os.sep,'/')
      pages['/'+r.replace('index.html','')]=open(p,encoding='utf-8').read()
descs={}
for u,h in sorted(pages.items()):
  t=html.unescape(re.search(r'<title>(.*?)</title>',h,re.S).group(1).strip())
  d=re.search(r'name="description" content="([^"]*)"',h); d=html.unescape(d.group(1)) if d else ''
  descs.setdefault(d,[]).append(u)
  body=re.sub(r'(?s)<head.*?</head>|<script.*?</script>|<style.*?</style>','',h); words=len(re.findall(r'\w+',re.sub('<[^>]+>',' ',body)))
  imgs=re.findall(r'<img[^>]*>',h)
  ld=[]
  for j in re.findall(r'(?s)<script type="application/ld\+json">(.*?)</script>',h):
    try: json.loads(j); ld.append('ok')
    except Exception: ld.append('INVALID')
  canon=re.search(r'rel="?canonical"? href="([^"]*)"',h)
  emo='OUI' if re.search('[\U0001F300-\U0001FAFF]',t) else 'non'
  print(f"{u:28} T{len(t):3} D{len(d):3} h1={h.count('<h1')} h2={h.count('<h2')} mots={words:5} img={len(imgs)} sansalt={sum('alt=' not in i for i in imgs)} altvide={sum('alt=\"\"' in i for i in imgs)} ld={ld} canon={'ok' if canon else 'NON'} emoji={emo}")
  print(f"   titre: {t}")
print("DESCRIPTIONS DUPLIQUEES:",[(k[:50],v) for k,v in descs.items() if len(v)>1])
bad=set()
for u,h in pages.items():
  for l in re.findall(r'href="(/[^"#?]*)',h):
    if not os.path.exists(sp+l) and not os.path.exists(sp+l+'index.html'): bad.add((u,l))
  for s in re.findall(r'src="(/[^"]*)"',h):
    if not os.path.exists(sp+s): bad.add((u,s))
print("LIENS/IMAGES CASSES:",bad)
sm=open(sp+'/sitemap.xml',encoding='utf-8').read(); print("sitemap:",len(re.findall('<loc>',sm)),"urls; 404 dans sitemap:", '404' in sm)
