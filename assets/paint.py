import random, math, sys
out=sys.argv[1]
R=random.Random(41)
W,H=1200,520
o=[];A=o.append
SERIF="'Iowan Old Style','Palatino Linotype',Palatino,'Book Antiqua',Georgia,serif"
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="A page in the manner of an illuminated manuscript: a dark iridescent moth with gold-ringed eyespots rests across a gold-leaf panel strewn with small flowers, casting a shadow over lines of brown script. 2233admin — software that keeps working after the lights go out.">')
A('''<defs>
<filter id="vellum" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".008 .012" numOctaves="3" seed="8" result="a"/><feColorMatrix in="a" type="matrix" values="0 0 0 0 .45  0 0 0 0 .33  0 0 0 0 .18  0 0 0 1.5 -.62" result="blot"/><feTurbulence type="fractalNoise" baseFrequency=".75" numOctaves="2" seed="2" result="b"/><feColorMatrix in="b" type="matrix" values="0 0 0 0 .36  0 0 0 0 .27  0 0 0 0 .16  0 0 0 1.3 -.62" result="spk"/><feMerge><feMergeNode in="blot"/><feMergeNode in="spk"/></feMerge></filter>
<linearGradient id="goldbase" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b98f3c"/><stop offset=".3" stop-color="#e2c36c"/><stop offset=".55" stop-color="#c39a45"/><stop offset=".8" stop-color="#ecd58a"/><stop offset="1" stop-color="#a47a2c"/></linearGradient>
<filter id="gold" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feTurbulence type="fractalNoise" baseFrequency=".09 .011" numOctaves="3" seed="4" result="t"/><feSpecularLighting in="t" surfaceScale="4" specularConstant="1" specularExponent="11" lighting-color="#fff1bd" result="s"><feDistantLight azimuth="200" elevation="34"/></feSpecularLighting><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="1" seed="9" result="g"/><feColorMatrix in="g" type="matrix" values="0 0 0 0 1  0 0 0 0 .95  0 0 0 0 .7  0 0 0 3 -2.2" result="glit"/><feComposite in="s" in2="SourceGraphic" operator="arithmetic" k1="0" k2=".7" k3=".8" k4="0" result="lit"/><feMerge result="m"><feMergeNode in="lit"/><feMergeNode in="glit"/></feMerge><feComposite in="m" in2="SourceGraphic" operator="in"/></filter>
<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="7"/></filter>
<filter id="sh2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="wob" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".04" numOctaves="2" seed="6"/><feDisplacementMap in="SourceGraphic" scale="2.2"/></filter>
<linearGradient id="glint" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff6d0" stop-opacity=".5"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="edge" cx="50%" cy="50%" r="72%"><stop offset=".7" stop-color="#5a3d1c" stop-opacity="0"/><stop offset="1" stop-color="#5a3d1c" stop-opacity=".32"/></radialGradient>
<linearGradient id="hind" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22306e"/><stop offset=".6" stop-color="#4a68c8"/><stop offset="1" stop-color="#8fa6ea"/></linearGradient>
<clipPath id="frame"><rect width="1200" height="520" rx="12"/></clipPath><clipPath id="gp"><rect x="704" y="34" width="452" height="452"/></clipPath>
</defs>''')
A('<g clip-path="url(#frame)">')
A(f'<rect width="{W}" height="{H}" fill="#efe5cd"/><rect width="{W}" height="{H}" filter="url(#vellum)" opacity=".55"/>')
INK='#3d2a18'
# ruling + script
ys=list(range(214,490,34))
for y in ys: A(f'<path d="M58 {y+3}H690" stroke="#c0564a" stroke-width=".7" opacity=".45"/>')
A('<path d="M62 30V500M688 30V500" stroke="#c0564a" stroke-width=".7" opacity=".4"/>')
def script(x0,x1,y,scale=1.0):
    x=x0; s=[]
    while x<x1-30:
        n=R.randint(2,8)
        for i in range(n):
            if x>x1-8: break
            t=R.random(); w=R.uniform(2.6,3.4)*scale; op=R.uniform(.72,.98)
            def st(d,wd=w): s.append(f'<path d="{d}" stroke="{INK}" stroke-width="{wd:.1f}" opacity="{op:.2f}"/>')
            if t<.5:
                k=R.choice([1,2,2,3])
                for j in range(k):
                    st(f'M{x:.1f} {y-13*scale:.1f}l{2.2*scale:.1f} {2.4*scale:.1f}l{.6*scale:.1f} {9*scale:.1f}l{2.4*scale:.1f} {1.8*scale:.1f}'); x+=5.6*scale
                x+=1.5
            elif t<.66:
                st(f'M{x:.1f} {y-R.uniform(26,31)*scale:.1f}q{3*scale:.1f} {2*scale:.1f} {2.6*scale:.1f} {8*scale:.1f}l{.6*scale:.1f} {18*scale:.1f}l{2.4*scale:.1f} {1.8*scale:.1f}')
                if R.random()<.5: st(f'M{x+3*scale:.1f} {y-11*scale:.1f}q{6*scale:.1f} {-4*scale:.1f} {6.5*scale:.1f} {5*scale:.1f}t{-5*scale:.1f} {6*scale:.1f}',w*.8); x+=5*scale
                x+=6.5*scale
            elif t<.78:
                st(f'M{x:.1f} {y-13*scale:.1f}l{2.2*scale:.1f} {2.4*scale:.1f}l{.4*scale:.1f} {20*scale:.1f}q{-1*scale:.1f} {4*scale:.1f} {-5*scale:.1f} {3*scale:.1f}',w*.9); x+=6*scale
            elif t<.93:
                st(f'M{x+6*scale:.1f} {y-11*scale:.1f}q{-6.5*scale:.1f} {-3*scale:.1f} {-6*scale:.1f} {5*scale:.1f}t{6.5*scale:.1f} {5.5*scale:.1f}',w*.85)
                if R.random()<.5: st(f'M{x+6*scale:.1f} {y-11*scale:.1f}q{3.5*scale:.1f} {5*scale:.1f} {-.5*scale:.1f} {10.5*scale:.1f}',w*.85)
                x+=9*scale
            else:
                st(f'M{x+7*scale:.1f} {y-28*scale:.1f}q{-5*scale:.1f} {-3*scale:.1f} {-5*scale:.1f} {6*scale:.1f}l{.4*scale:.1f} {22*scale:.1f}',w*.9); x+=7*scale
        x+=R.uniform(9,14)*scale
    return ''.join(s)
A('<g fill="none" stroke-linejoin="miter">'+''.join(script(70,682,y) for y in ys)+'</g>')
# paragraph marks
for y in (ys[2],ys[5]): A(f'<path d="M70 {y-14}h9v15M74 {y-14}v15" stroke="#2c479a" stroke-width="2.4" fill="none"/>')
# ---- gold panel ----
A('<rect x="704" y="34" width="452" height="452" fill="url(#goldbase)"/><rect x="704" y="34" width="452" height="452" fill="url(#goldbase)" filter="url(#gold)"/>')
A('<g clip-path="url(#gp)"><rect x="560" y="34" width="120" height="452" fill="url(#glint)" transform="skewX(-18)"><animate attributeName="x" values="700;1500;1500" keyTimes="0;.35;1" dur="11s" repeatCount="indefinite"/></rect></g>')
A(f'<rect x="704" y="34" width="452" height="452" fill="none" stroke="{INK}" stroke-width="1.6" filter="url(#wob)"/><rect x="709" y="39" width="442" height="442" fill="none" stroke="#7a5a22" stroke-width=".8" opacity=".7"/>')
# flowers
def flower(x,y,r,col,n=5,rot=0):
    s=f'<g transform="translate({x} {y}) rotate({rot})">'
    s+=f'<g transform="translate(3 4)" opacity=".28" filter="url(#sh2)">'+''.join(f'<ellipse cx="0" cy="{-r*.62:.1f}" rx="{r*.46:.1f}" ry="{r*.62:.1f}" transform="rotate({i*360/n})" fill="#3a2408"/>' for i in range(n))+'</g>'
    for i in range(n):
        s+=f'<ellipse cx="0" cy="{-r*.62:.1f}" rx="{r*.46:.1f}" ry="{r*.62:.1f}" transform="rotate({i*360/n})" fill="{col}" stroke="{INK}" stroke-width=".7"/>'
        s+=f'<path d="M0 {-r*.25:.1f}V{-r*.95:.1f}" transform="rotate({i*360/n})" stroke="#fff" stroke-width="1" opacity=".55"/>'
    s+=f'<circle r="{r*.22:.1f}" fill="#e2a52a" stroke="{INK}" stroke-width=".7"/></g>'
    return s
def sprig(pts, flowers, leaves):
    d='M'+' '.join(f'{x} {y}' if i==0 else ('Q' if i%2 else '')+f'{x} {y}' for i,(x,y) in enumerate(pts))
    A(f'<path d="{d}" transform="translate(3 4)" stroke="#3a2408" stroke-width="2.4" fill="none" opacity=".25" filter="url(#sh2)"/><path d="{d}" stroke="#56684a" stroke-width="2" fill="none" stroke-linecap="round"/><path d="{d}" stroke="{INK}" stroke-width=".6" fill="none" opacity=".7" transform="translate(.8 .5)"/>')
    for (x,y,a) in leaves:
        A(f'<path d="M0 0q9-9 22-3q-10 9-22 3z" transform="translate({x} {y}) rotate({a})" fill="#6f8a66" stroke="{INK}" stroke-width=".7"/><path d="M0 0q10-3 20-2" transform="translate({x} {y}) rotate({a})" stroke="#e9f0d8" stroke-width=".8" fill="none"/>')
    for f in flowers: A(flower(*f))
sprig([(1120,476),(1090,400),(1128,330),(1150,270),(1104,236)],[(1104,232,15,'#f3c9cf',5,10),(1134,318,11,'#f7f1e6',5,40),(1080,404,9,'#f3c9cf',5,0)],[(1098,390,-150),(1124,356,-20),(1138,292,-160)])
sprig([(730,60),(790,84),(850,62),(900,70),(950,52)],[(952,52,13,'#9fb4ea',5,20),(852,60,10,'#f7f1e6',5,0),(788,88,8,'#9fb4ea',5,30)],[(812,80,30),(884,66,-40),(760,70,160)])
sprig([(1000,474),(960,440),(920,452),(880,430),(850,446)],[(848,448,12,'#f7f1e6',5,15),(922,454,9,'#f3c9cf',5,0)],[(950,444,200),(896,438,-30)])
for (x,y) in [(1030,110),(1070,160),(770,430),(1010,60),(1130,96),(800,470)]:
    A(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#b9372c" stroke="{INK}" stroke-width=".6"/>')
# ---- moth ----
def interp(tab,th):
    for (a,ra),(b,rb) in zip(tab,tab[1:]):
        if a<=th<=b:
            t=(th-a)/(b-a); t=t*t*(3-2*t); return ra+(rb-ra)*t
    return tab[-1][1]
FORE=[(-70,96),(-60,188),(-48,238),(-36,236),(-22,204),(-8,172),(6,146),(20,96)]
HINDW=[(8,92),(24,148),(42,170),(58,164),(72,142),(84,150),(96,92)]
def P(base,th,r): a=math.radians(th); return (base[0]+math.cos(a)*r, base[1]+math.sin(a)*r)
def outline(base,tab,j=0):
    pts=[base]
    th=tab[0][0]
    while th<=tab[-1][0]:
        x,y=P(base,th,interp(tab,th)+R.gauss(0,j)); pts.append((x,y)); th+=2
    return 'M'+'L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+'Z'
def wing(side):
    g=[]; a=g.append
    fb=(9,-10); hb=(7,10); cid='R' if side>0 else 'L'
    # hind wing
    a(f'<clipPath id="ch{cid}"><path d="{outline(hb,HINDW)}"/></clipPath><clipPath id="cf{cid}"><path d="{outline(fb,FORE)}"/></clipPath>')
    a(f'<path d="{outline(hb,HINDW)}" fill="url(#hind)"/><g clip-path="url(#ch{cid})">')
    for i in range(800):
        th=R.uniform(8,96); rr=interp(HINDW,th); u=R.random()**.7; r=u*rr
        x,y=P(hb,th,r); L=R.uniform(7,16); x2,y2=P(hb,th+R.gauss(0,2),min(r+L,rr))
        if u>.9: col=R.choice(['#0e1220','#141a2c','#f4efe2'])
        elif u>.72: col=R.choice(['#7f98e6','#a9baf0','#5a76d2'])
        elif u>.35: col=R.choice(['#3552b4','#4563c6','#2c469e'])
        else: col=R.choice(['#141a36','#1d2852','#0e1220'])
        a(f'<path d="M{x:.1f} {y:.1f}L{x2:.1f} {y2:.1f}" stroke="{col}" stroke-width="{R.uniform(1,2.3):.1f}" stroke-linecap="round" opacity="{R.uniform(.6,.95):.2f}"/>')
    a('</g>')
    for th in range(14,96,9):
        x,y=P(hb,th,interp(HINDW,th)*.97); mx,my=P(hb,th+4,interp(HINDW,th)*.5)
        a(f'<path d="M{hb[0]} {hb[1]}Q{mx:.1f} {my:.1f} {x:.1f} {y:.1f}" stroke="#0b0e1a" stroke-width=".8" fill="none" opacity=".75"/>')
    ex,ey=P(hb,50,104)
    a(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="19" fill="#0b0e1a"/><circle cx="{ex:.1f}" cy="{ey:.1f}" r="15" fill="none" stroke="url(#goldbase)" stroke-width="5"/><circle cx="{ex:.1f}" cy="{ey:.1f}" r="15" fill="none" stroke="#fff3c4" stroke-width="1" stroke-dasharray="2 9" opacity=".9"/><circle cx="{ex:.1f}" cy="{ey:.1f}" r="8.5" fill="#b9372c"/><circle cx="{ex:.1f}" cy="{ey:.1f}" r="4.5" fill="#0b0e1a"/><circle cx="{ex-3:.1f}" cy="{ey-3:.1f}" r="1.8" fill="#fff"/>')
    a(f'<path d="{outline(hb,HINDW,.8)}" fill="none" stroke="#0b0e1a" stroke-width="1.3"/>')
    # fore wing
    a(f'<path d="{outline(fb,FORE)}" fill="#0d1019"/><g clip-path="url(#cf{cid})">')
    irA=[];irB=[]
    for i in range(1500):
        th=R.uniform(-70,20); rr=interp(FORE,th); u=R.random()**.6; r=u*rr
        x,y=P(fb,th,r); L=R.uniform(7,17); x2,y2=P(fb,th+R.gauss(0,2),min(r+L,rr))
        w=R.uniform(1,2.4); op=R.uniform(.6,.95)
        band = .60<u<.70+0.04*math.sin(th/6)
        if u>.93: col=R.choice(['#f4efe2','#0b0e1a','#0b0e1a'])
        elif band: col=R.choice(['#f4efe2','#e9e0cc','#fff9ec','#d9cfb8'])
        elif .2<u<.56 and R.random()<.62:
            ca=R.choice(['#2fb7b0','#3fd0c0','#1f8f9c','#57e0c8']); cb=R.choice(['#8a63d8','#b07ae8','#5a6fe0','#d07ad0'])
            irA.append(f'<path d="M{x:.1f} {y:.1f}L{x2:.1f} {y2:.1f}" stroke="{ca}" stroke-width="{w+.8:.1f}" stroke-linecap="round" opacity="{op:.2f}"/>')
            irB.append(f'<path d="M{x:.1f} {y:.1f}L{x2:.1f} {y2:.1f}" stroke="{cb}" stroke-width="{w+.8:.1f}" stroke-linecap="round" opacity="{op:.2f}"/>')
            continue
        else: col=R.choice(['#0b0e1a','#141a2c','#1a2238','#10141f','#232c48'])
        a(f'<path d="M{x:.1f} {y:.1f}L{x2:.1f} {y2:.1f}" stroke="{col}" stroke-width="{w:.1f}" stroke-linecap="round" opacity="{op:.2f}"/>')
    ph='0s' if side>0 else '-3.5s'
    a(f'<g>{"".join(irA)}<animate attributeName="opacity" values="1;.15;1" dur="7s" begin="{ph}" repeatCount="indefinite"/></g>')
    a(f'<g opacity=".15">{"".join(irB)}<animate attributeName="opacity" values=".15;1;.15" dur="7s" begin="{ph}" repeatCount="indefinite"/></g>')
    for i in range(60):
        th=R.uniform(-66,16); rr=interp(FORE,th); x,y=P(fb,th,R.uniform(.22,.55)*rr)
        a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{R.uniform(.5,1.2):.1f}" fill="#eafff8" opacity="{R.uniform(.5,1):.2f}"/>')
    a('</g>')
    for th in range(-64,20,8):
        x,y=P(fb,th,interp(FORE,th)*.98); mx,my=P(fb,th-5,interp(FORE,th)*.5)
        a(f'<path d="M{fb[0]} {fb[1]}Q{mx:.1f} {my:.1f} {x:.1f} {y:.1f}" stroke="#05070c" stroke-width=".8" fill="none" opacity=".8"/>')
    for th in range(-62,20,7):
        x,y=P(fb,th,interp(FORE,th)*.955)
        a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="#f4efe2"/>')
    ex,ey=P(fb,-40,168)
    a(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="12" fill="#0b0e1a"/><circle cx="{ex:.1f}" cy="{ey:.1f}" r="9" fill="none" stroke="url(#goldbase)" stroke-width="3.5"/><circle cx="{ex:.1f}" cy="{ey:.1f}" r="4" fill="#3552b4"/><circle cx="{ex-2:.1f}" cy="{ey-2:.1f}" r="1.3" fill="#fff"/>')
    a(f'<path d="{outline(fb,FORE,.9)}" fill="none" stroke="#05070c" stroke-width="1.4"/><path d="{outline(fb,FORE,1.6)}" fill="none" stroke="#05070c" stroke-width=".6" opacity=".7"/>')
    # antenna
    pts=[(4+ t*58, -52 - 78*math.sin(t*1.45)) for t in [i/22 for i in range(23)]]
    a('<path d="M'+'L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+'" stroke="#05070c" stroke-width="1.6" fill="none"/>')
    for i,(x,y) in enumerate(pts[3:],3):
        l=9*math.sin(i/22*math.pi)+2
        a(f'<path d="M{x:.1f} {y:.1f}l{l:.1f} {l*.5:.1f}M{x:.1f} {y:.1f}l{-l*.6:.1f} {-l*.7:.1f}" stroke="#2a1e12" stroke-width=".9"/>')
    return f'<g transform="scale({side} 1)" stroke-linejoin="round">{"".join(g)}</g>'
def shadow():
    fb=(9,-10); hb=(7,10)
    return ''.join(f'<g transform="scale({s} 1)"><path d="{outline(hb,HINDW)}"/><path d="{outline(fb,FORE)}"/></g>' for s in (1,-1))
T='translate(770 292) rotate(11)'
A(f'<g transform="translate(14 18)"><g transform="{T}" fill="#2a1806" opacity=".42" filter="url(#sh)">{shadow()}<ellipse cx="0" cy="20" rx="16" ry="80"/></g></g>')
A(f'<g transform="{T}">{wing(1)}{wing(-1)}')
# body
b=['<ellipse cx="0" cy="48" rx="13" ry="62" fill="#0d1019"/><ellipse cx="0" cy="-18" rx="19" ry="26" fill="#161a26"/><ellipse cx="0" cy="-46" rx="11" ry="9" fill="#0d1019"/>']
for yy in range(8,104,13):
    wd=13*math.sqrt(max(0,1-((yy-48)/62)**2))
    b.append(f'<path d="M{-wd:.1f} {yy}q{wd:.1f} 6 {2*wd:.1f} 0" stroke="url(#goldbase)" stroke-width="3" fill="none"/><path d="M{-wd*.5:.1f} {yy+1}h{wd*.5:.1f}" stroke="#fff3c4" stroke-width="1"/>')
for i in range(170):
    a_=R.uniform(0,6.283); rr=math.sqrt(R.random()); x=math.cos(a_)*rr*19; y=-18+math.sin(a_)*rr*26
    col=R.choice(['#f4efe2','#cfc7b4','#8f98a8','#2a3148','#f4efe2'])
    b.append(f'<path d="M{x:.1f} {y:.1f}l{R.gauss(0,2):.1f} {R.uniform(5,11):.1f}" stroke="{col}" stroke-width="{R.uniform(.8,1.6):.1f}" stroke-linecap="round" opacity="{R.uniform(.5,.95):.2f}"/>')
b.append('<circle cx="-7" cy="-49" r="4" fill="#05070c"/><circle cx="7" cy="-49" r="4" fill="#05070c"/><circle cx="-8.2" cy="-50.4" r="1.2" fill="#fff"/><circle cx="5.8" cy="-50.4" r="1.2" fill="#fff"/>')
A(''.join(b)+'</g>')
# ---- title ----
A(f'''<g transform="translate(70 58)"><rect width="86" height="86" fill="url(#goldbase)"/><rect width="86" height="86" fill="url(#goldbase)" filter="url(#gold)"/><rect x="5" y="5" width="76" height="76" fill="#2c479a"/><rect width="86" height="86" fill="none" stroke="{INK}" stroke-width="1.4" filter="url(#wob)"/>
<path d="M12 14q10 10 0 22M74 14q-10 10 0 22M12 72q10-10 0-22M74 72q-10-10 0-22" stroke="#9fb4ea" stroke-width="1.2" fill="none"/><circle cx="14" cy="43" r="2" fill="#f4efe2"/><circle cx="72" cy="43" r="2" fill="#f4efe2"/>
<text x="43" y="70" text-anchor="middle" font-family="{SERIF}" font-size="76" fill="#f4efe2" stroke="{INK}" stroke-width=".8">2</text></g>
<text x="170" y="118" font-family="{SERIF}" font-size="64" letter-spacing="-.5" fill="#2e1f12">233admin</text>
<text x="172" y="146" font-family="{SERIF}" font-style="italic" font-size="19.5" fill="#a8322a">software that keeps working after the lights go out</text>
<path d="M70 168h468" stroke="#a8322a" stroke-width="1"/><path d="M546 168l6-5 6 5-6 5z" fill="#2c479a"/>''')
A(f'<rect width="{W}" height="{H}" fill="url(#edge)"/></g></svg>')
open(out,'w').write('\n'.join(o))
