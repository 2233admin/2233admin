import random, math, sys
out = sys.argv[1]
R = random.Random(2233)
W, H, HOR = 1200, 520, 410
MX, MY, MR = 970, 304, 122
def hexrgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def rgbhex(c): return '#%02x%02x%02x' % tuple(max(0,min(255,int(round(v)))) for v in c)
def lerp(a,b,t): return tuple(a[i]+(b[i]-a[i])*t for i in range(3))
def ramp(stops, t):
    t=max(0,min(1,t))
    for (t0,c0),(t1,c1) in zip(stops,stops[1:]):
        if t<=t1: return lerp(hexrgb(c0),hexrgb(c1),(t-t0)/(t1-t0) if t1>t0 else 0)
    return hexrgb(stops[-1][1])
def jit(c,a):
    d=R.gauss(0,a); return (c[0]+d+R.gauss(0,a/3), c[1]+d+R.gauss(0,a/3), c[2]+d+R.gauss(0,a/3))
SKY=[(0,'#060a22'),(.28,'#0e1845'),(.55,'#1c2b68'),(.76,'#3f478c'),(.9,'#96608f'),(1,'#eea07c')]
def sky_at(x,y):
    c=ramp(SKY,y/HOR)
    d=math.hypot(x-MX,y-MY)
    g=max(0,1-d/300)**2
    return lerp(c,hexrgb('#8fa2e6'),g*.6)
o=[]; A=o.append
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Thick-paint style painting: a girl in headphones sits under a vermilion torii gate with a laptop and a cat, silhouetted against a huge full moon over a city, rings of glowing danmaku bullets turning in the night sky. 2233admin, software that keeps working after the lights go out.">')
FILT='''<filter id="{id}" filterUnits="userSpaceOnUse" x="-30" y="-30" width="1260" height="580" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency="0.016 0.028" numOctaves="2" seed="{seed}" result="n"/>
<feGaussianBlur in="SourceGraphic" stdDeviation="{blur}" result="soft"/><feDisplacementMap in="soft" in2="n" scale="{scale}" xChannelSelector="R" yChannelSelector="G" result="d"/>
<feColorMatrix in="d" type="luminanceToAlpha" result="lum"/>
<feGaussianBlur in="lum" stdDeviation="2.2" result="bump"/>
<feDiffuseLighting in="bump" surfaceScale="2.4" diffuseConstant="1.2" lighting-color="#ffffff" result="rel"><feDistantLight azimuth="225" elevation="56"/></feDiffuseLighting>
<feSpecularLighting in="bump" surfaceScale="2.4" specularConstant=".1" specularExponent="16" lighting-color="#fff4e0" result="spec"><feDistantLight azimuth="225" elevation="56"/></feSpecularLighting>
<feTurbulence type="fractalNoise" baseFrequency="0.85 0.3" numOctaves="2" seed="3" result="g"/>
<feDiffuseLighting in="g" surfaceScale="1.2" diffuseConstant="1.12" lighting-color="#ffffff" result="l"><feDistantLight azimuth="235" elevation="62"/></feDiffuseLighting>
<feBlend in="d" in2="rel" mode="multiply" result="p1"/>
<feBlend in="p1" in2="l" mode="multiply" result="p2"/>
<feComposite in="spec" in2="p2" operator="arithmetic" k1="0" k2="1" k3="1" k4="0" result="p3"/>
<feComposite in="p3" in2="d" operator="in"/>
</filter>'''
A('<defs>'+FILT.format(id='oil',seed=7,scale=10,blur=1.3)+FILT.format(id='oil2',seed=11,scale=4,blur=.5)+f'''
<radialGradient id="halo" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff2cf" stop-opacity=".85"/><stop offset=".35" stop-color="#cfd8ff" stop-opacity=".35"/><stop offset="1" stop-color="#9fb2ff" stop-opacity="0"/></radialGradient>
<radialGradient id="moonf" cx="42%" cy="38%" r="65%"><stop offset="0" stop-color="#fffbe9"/><stop offset=".7" stop-color="#fbe6b4"/><stop offset="1" stop-color="#e9c592"/></radialGradient>
<radialGradient id="warm" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ffc56b" stop-opacity=".8"/><stop offset="1" stop-color="#ff9a4a" stop-opacity="0"/></radialGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#9ff5ea" stop-opacity=".7"/><stop offset="1" stop-color="#9ff5ea" stop-opacity="0"/></radialGradient>
<radialGradient id="bR"><stop offset="0" stop-color="#fff"/><stop offset=".35" stop-color="#ff5d78"/><stop offset="1" stop-color="#ff2d55" stop-opacity="0"/></radialGradient>
<radialGradient id="bC"><stop offset="0" stop-color="#fff"/><stop offset=".35" stop-color="#7fe7ff"/><stop offset="1" stop-color="#3cc8ff" stop-opacity="0"/></radialGradient>
<radialGradient id="bG"><stop offset="0" stop-color="#fff"/><stop offset=".35" stop-color="#ffd76a"/><stop offset="1" stop-color="#ffb02e" stop-opacity="0"/></radialGradient>
<linearGradient id="skyg" x1="0" y1="0" x2="0" y2="1">''' + ''.join(f'<stop offset="{t*HOR/H:.3f}" stop-color="{c}"/>' for t,c in SKY) + '''<stop offset="1" stop-color="#eea07c"/></linearGradient>
<clipPath id="frame"><rect width="1200" height="520" rx="14"/></clipPath>
<clipPath id="above"><rect width="1200" height="402"/></clipPath>
</defs>''')
A('<g clip-path="url(#frame)">')
# ---------- background layer ----------
A('<g filter="url(#oil)">')
A(f'<rect x="-30" y="-30" width="{W+60}" height="{H+60}" fill="url(#skyg)"/>')
A('<g stroke-linecap="round" fill="none">')
for i in range(1150):
    x=R.uniform(-40,W+40); y=R.uniform(-10,HOR+5)
    c=jit(sky_at(x,y+R.gauss(0,14)), 6)
    # strokes swirl gently around the moon
    d=math.hypot(x-MX,y-MY)
    if d<330: ang=math.atan2(y-MY,x-MX)+math.pi/2+R.gauss(0,.25)
    else: ang=math.radians(R.gauss(-4,10))
    L=R.uniform(30,85); w=R.uniform(8,22)
    dx,dy=math.cos(ang)*L/2,math.sin(ang)*L/2
    A(f'<path d="M{x-dx:.0f} {y-dy:.0f}Q{x+R.gauss(0,5):.0f} {y+R.gauss(0,5):.0f} {x+dx:.0f} {y+dy:.0f}" stroke="{rgbhex(c)}" stroke-width="{w:.0f}" opacity="{R.uniform(.6,.92):.2f}"/>')
A('</g>')
# moon
A(f'<circle cx="{MX}" cy="{MY}" r="{MR*2.6}" fill="url(#halo)"/><circle cx="{MX}" cy="{MY}" r="{MR}" fill="url(#moonf)"/>')
for i in range(70):
    a=R.uniform(0,6.283); r=math.sqrt(R.random())*(MR-10)
    x=MX+math.cos(a)*r; y=MY+math.sin(a)*r
    c=R.choice(['#e3c89a','#f3dcae','#fff7dc','#d9b98c','#fff'])
    A(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{R.uniform(6,16):.0f}" ry="{R.uniform(4,9):.0f}" fill="{c}" opacity="{R.uniform(.25,.6):.2f}" transform="rotate({R.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>')
# clouds (moonlit from the right)
CL=[(0,'#f4f1ff'),(.14,'#aebbf0'),(.36,'#6470bb'),(.62,'#343c84'),(.84,'#5a4484'),(1,'#d07f8c')]
def cloud(puffs, n, top, bot, lx=.45):
    dabs=[]
    for (cx,cy,rx,ry) in puffs:
        for i in range(int(n*rx*ry/3000)):
            a=R.uniform(0,2*math.pi); r=math.sqrt(R.random())
            x=cx+math.cos(a)*r*rx; y=cy+math.sin(a)*r*ry
            loc=(-math.sin(a)*r*0.45 + math.cos(a)*r*lx)
            t=(y-top)/(bot-top)*.75 - loc*0.5 + R.gauss(0,.05)+.22
            dabs.append((t,x,y,R.uniform(7,16),a))
    dabs.sort(key=lambda d:-d[0])
    for t,x,y,rad,a in dabs:
        c=jit(ramp(CL,t),5)
        A(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rad*1.3:.0f}" ry="{rad*.8:.0f}" fill="{rgbhex(c)}" opacity="{R.uniform(.78,.98):.2f}" transform="rotate({math.degrees(a)+90+R.gauss(0,20):.0f} {x:.0f} {y:.0f})"/>')
big=[(240,398,190,40),(420,394,170,42),(170,350,95,50),(290,330,110,60),(400,340,95,54),(320,278,82,50),(245,254,58,40),(385,258,52,36),(312,226,44,30),(490,362,75,36),(110,386,90,30),(575,392,90,24)]
cloud(big, 110, 192, 428, .6)
cloud([(690,250,70,14),(760,244,50,12),(610,256,50,10),(1150,150,70,14),(1090,158,50,10)], 80, 228, 275, .2)
# city
A(f'<rect x="-30" y="{HOR-16}" width="{W+60}" height="46" fill="#ffc79a" opacity=".3"/>')
x=-10; blds=[]
while x<W+10:
    w=R.uniform(16,46); h=R.uniform(10,44) if R.random()>.1 else R.uniform(50,74)
    blds.append((x,w,h)); x+=w+R.uniform(-4,5)
for (x,w,h) in blds:
    A(f'<rect x="{x:.0f}" y="{440-h:.0f}" width="{w:.0f}" height="{h+10:.0f}" fill="{rgbhex(jit(hexrgb("#141840"),4))}"/>')
    A(f'<rect x="{x+w-3:.0f}" y="{440-h:.0f}" width="3" height="{h:.0f}" fill="#5a67b4" opacity=".5"/>')
    for i in range(int(w*h/70)):
        A(f'<rect x="{x+R.uniform(3,w-6):.0f}" y="{440-h+R.uniform(4,h-4):.0f}" width="3" height="3.5" fill="{R.choice(["#ffd58a","#ffe7b5","#ffb46b","#9ff0e6"])}" opacity="{R.uniform(.5,1):.2f}"/>')
A('</g>')
# ---------- danmaku (unfiltered, turning) ----------
A('<g clip-path="url(#above)">')
def ring(n, r, kind, rad, phase, dur, cw):
    s=[]
    for i in range(n):
        a=phase+2*math.pi*i/n
        s.append(f'<circle cx="{MX+math.cos(a)*r:.1f}" cy="{MY+math.sin(a)*r:.1f}" r="{rad}" fill="url(#b{kind})"/>')
    to = 360 if cw else -360
    A(f'<g opacity=".95">{"".join(s)}<animateTransform attributeName="transform" type="rotate" from="0 {MX} {MY}" to="{to} {MX} {MY}" dur="{dur}s" repeatCount="indefinite"/></g>')
ring(30,170,'R',9,0,160,True)
ring(36,222,'C',8,.09,200,False)
ring(42,276,'G',7.5,.04,240,True)
ring(48,332,'R',7,.07,280,False)
ring(54,390,'C',6.5,0,320,True)
# spiral arms of rice-grain bullets
s=[]
for arm in range(6):
    for k in range(9):
        r=150+k*29; a=arm*math.pi/3+k*.17
        x=MX+math.cos(a)*r; y=MY+math.sin(a)*r
        s.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="9" ry="3.6" fill="#fff" opacity="{.9-k*.06:.2f}" transform="rotate({math.degrees(a):.0f} {x:.1f} {y:.1f})"/><ellipse cx="{x:.1f}" cy="{y:.1f}" rx="13" ry="6" fill="#ff4d6d" opacity=".28" transform="rotate({math.degrees(a):.0f} {x:.1f} {y:.1f})"/>')
A(f'<g>{"".join(s)}<animateTransform attributeName="transform" type="rotate" from="0 {MX} {MY}" to="360 {MX} {MY}" dur="220s" repeatCount="indefinite"/></g>')
A('</g>')
# ---------- foreground layer ----------
A('<g filter="url(#oil2)">')
# ground
LX0=668
A('<rect x="-30" y="436" width="1260" height="120" fill="#0f1233"/>')
for i in range(260):
    x=R.uniform(-30,W); y=R.uniform(440,524)
    k=max(0,1-abs(x-MX)/(60+(y-436)*3.2))
    c=lerp(hexrgb('#141842'),hexrgb('#8f9fe0'),k*R.uniform(.3,1))
    A(f'<path d="M{x:.0f} {y:.0f}h{R.uniform(26,80):.0f}" stroke="{rgbhex(jit(c,6))}" stroke-width="{R.uniform(5,12):.0f}" stroke-linecap="round" opacity=".85"/>')
for i in range(40):
    x=R.gauss(LX0,55); y=R.uniform(440,470)
    A(f'<path d="M{x:.0f} {y:.0f}h{R.uniform(20,50):.0f}" stroke="{rgbhex(jit(hexrgb("#c9783f"),12))}" stroke-width="{R.uniform(4,9):.0f}" stroke-linecap="round" opacity="{R.uniform(.3,.7):.2f}"/>')
for yy in (462,492): A(f'<path d="M-30 {yy}h1260" stroke="#070920" stroke-width="2.5" opacity=".7"/>')
A('<path d="M-30 437h1260" stroke="#aab6f0" stroke-width="2.5" opacity=".7"/>')
# stone lantern
LX=668
A(f'<circle cx="{LX}" cy="352" r="95" fill="url(#warm)" opacity=".8"/>')
A(f'''<g>
<path d="M{LX-30} 436h60l-6-12h-48z" fill="#2a2e58"/><path d="M{LX-9} 424h18l-3-44h-12z" fill="#343a6c"/><path d="M{LX+3} 424h6l-3-44h-3z" fill="#8f9fe0"/>
<path d="M{LX-24} 380h48l-4-8h-40z" fill="#2a2e58"/>
<rect x="{LX-17}" y="338" width="34" height="34" fill="#20244c"/><rect x="{LX-10}" y="344" width="20" height="23" rx="2" fill="#ffd27a"/><path d="M{LX} 344v23M{LX-10} 355h20" stroke="#8a4a1c" stroke-width="2"/>
<path d="M{LX-38} 338q10-4 16-18h44q6 14 16 18q-38 5-76 0z" fill="#1c2046"/><path d="M{LX+10} 320h12q6 13 15 17" stroke="#aab6f0" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M{LX-6} 320q6-16 12 0z" fill="#1c2046"/><circle cx="{LX}" cy="306" r="5" fill="#2a2e58"/>
</g>''')
# torii
A('''<g>
<path d="M790 436L800 222h26l-4 214z" fill="#6a1622"/><path d="M1150 436L1140 222h-26l4 214z" fill="#6a1622"/>
<path d="M812 436l3-214h11l-4 214z" fill="#a82a2a"/><path d="M1128 436l-3-214h-11l4 214z" fill="#a82a2a"/>
<path d="M824 426l2-200" stroke="#ffe2b8" stroke-width="2.5" stroke-linecap="round"/><path d="M1116 426l-2-200" stroke="#ffe2b8" stroke-width="2.5" stroke-linecap="round"/>
<path d="M792 430l5-120" stroke="#ff9a52" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M784 438l2-24h42l2 24z" fill="#0b0c22"/><path d="M1156 438l-2-24h-42l-2 24z" fill="#0b0c22"/>
<rect x="752" y="236" width="436" height="20" fill="#7a1a26"/><rect x="752" y="251" width="436" height="5" fill="#ffd9a8" opacity=".75"/><rect x="752" y="236" width="436" height="5" fill="#b53030"/>
<rect x="957" y="204" width="26" height="34" fill="#0f1030"/><rect x="961" y="208" width="18" height="26" fill="#c9a24a"/>
<path d="M722 176Q970 204 1218 176L1212 204Q970 226 728 204Z" fill="#8a1e28"/><path d="M728 204Q970 226 1212 204" stroke="#ffd9a8" stroke-width="2.5" fill="none" opacity=".8"/>
<path d="M712 160Q970 190 1228 160L1220 182Q970 208 720 182Z" fill="#0d0e26"/><path d="M714 161Q970 191 1226 161" stroke="#aab6f0" stroke-width="3" fill="none" opacity=".85"/>
<path d="M826 258h288" stroke="#cdb97c" stroke-width="7" stroke-linecap="round"/><path d="M826 258h288" stroke="#6f5f34" stroke-width="7" stroke-dasharray="3 9"/>''')
for sx in (866,926,1014,1074):
    A(f'<path d="M{sx} 261l-7 9h7l-7 9h7l-7 9h13l7-9h-7l7-9h-7l7-9z" fill="#f6f3ea"/>')
A('</g>')
# pine branch
A('<g stroke-linecap="round" fill="none"><path d="M1210 18Q1130 30 1060 78M1150 36Q1120 70 1110 110M1190 22Q1180 60 1160 92" stroke="#0a0f1c" stroke-width="7"/>')
for (px,py) in [(1060,78),(1090,58),(1110,110),(1130,44),(1160,92),(1125,84),(1175,56),(1196,96),(1040,96),(1085,104),(1150,120)]:
    for i in range(26):
        a=math.radians(R.uniform(200,340)) if R.random()<.8 else R.uniform(0,6.28)
        L=R.uniform(16,30)
        col=R.choice(['#0c1a22','#0c1a22','#12303a','#1d4a4a','#6fa8a0'])
        A(f'<path d="M{px} {py}l{math.cos(a)*L:.0f} {-abs(math.sin(a))*L:.0f}" stroke="{col}" stroke-width="2.2"/>')
A('</g>')
# higanbana
def lily(x,y,s):
    A(f'<path d="M{x} {y+70*s:.0f}Q{x+4*s:.0f} {y+30*s:.0f} {x} {y}" stroke="#1d4a3a" stroke-width="{3*s:.1f}" fill="none"/>')
    for i in range(12):
        a=math.radians(-90+R.uniform(-110,110)); L=R.uniform(16,26)*s
        ex=x+math.cos(a)*L; ey=y+math.sin(a)*L
        cx_=x+math.cos(a)*L*1.2; cy_=y+math.sin(a)*L*.2-10*s
        col=R.choice(['#c81e2c','#e23b3b','#ff5a4a','#a01428'])
        A(f'<path d="M{x} {y}Q{cx_:.0f} {cy_:.0f} {ex:.0f} {ey-6*s:.0f}" stroke="{col}" stroke-width="{R.uniform(2.5,4.5)*s:.1f}" fill="none" stroke-linecap="round"/>')
    for i in range(7):
        a=math.radians(-90+R.uniform(-80,80)); L=R.uniform(26,38)*s
        A(f'<path d="M{x} {y}Q{x+math.cos(a)*L*.5:.0f} {y+math.sin(a)*L*1.2:.0f} {x+math.cos(a)*L:.0f} {y+math.sin(a)*L*.9:.0f}" stroke="#ff9a8a" stroke-width="{1.1*s:.1f}" fill="none" stroke-linecap="round"/>')
for (x,y,s) in [(60,452,1.25),(128,470,1.5),(205,448,1.1),(268,474,1.45),(340,456,1.15),(410,478,1.3),(20,486,1.5),(480,462,.95),(545,480,1.1)]:
    lily(x,y,s)
# figure group
A('<g transform="translate(970 436) scale(1.22) translate(-821 -436)">')
A('<ellipse cx="770" cy="408" rx="95" ry="62" fill="url(#glow)"/>')
A('<path d="M780 438l30 70h40l20-70z" fill="#05061a" opacity=".55"/>')
A('''<g fill="#0c0e2a"><path d="M887 436c-4-18 2-34 14-38c13 3 20 20 16 38z"/><circle cx="901" cy="392" r="11"/><path d="M891 388l1-14 9 8zM911 388l0-14-9 8z"/><path d="M915 432c16 4 26-2 26-16" stroke="#0c0e2a" stroke-width="6" fill="none" stroke-linecap="round"/></g>
<path d="M890 384l2-9M912 384l-1-9M887 430c-3-14 1-26 8-32M917 430c2-12 0-24-6-32M941 416c0 8-6 14-14 16" stroke="#ffe9bd" stroke-width="1.8" fill="none" stroke-linecap="round" opacity=".9"/>''')
A('''<g>
<path d="M800 316C772 320 748 332 722 326C736 342 756 346 774 344C760 356 744 360 730 358C748 372 774 370 792 362C790 380 792 396 800 408L842 408C852 380 852 344 846 318Z" fill="#12163c"/>
<path d="M786 436C780 404 786 372 798 356C812 346 830 346 844 356C856 372 862 404 856 436Z" fill="#1d2152"/>
<path d="M792 436C790 410 794 384 802 366C812 380 814 410 814 436Z" fill="#2c3170"/>
<path d="M786 436C781 408 785 380 794 362C800 384 800 412 802 436Z" fill="#3fa9b5" opacity=".6"/>
<path d="M844 356C856 372 862 404 856 436" stroke="#ffe9bd" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M798 357C790 368 786 384 785 400" stroke="#ffe9bd" stroke-width="1.6" fill="none" stroke-linecap="round" opacity=".8"/>
<ellipse cx="821" cy="356" rx="27" ry="10" fill="#262b62"/><path d="M797 354q24-9 48 0" stroke="#ffe9bd" stroke-width="1.8" fill="none" opacity=".8"/>
<circle cx="821" cy="322" r="25" fill="#12163c"/>
<path d="M800 330C792 352 794 380 802 404C808 384 808 360 812 344ZM842 330C848 350 846 376 838 398C834 378 836 358 832 344Z" fill="#12163c"/>
<path d="M806 338C802 356 802 376 806 392M730 332C748 336 768 332 786 324M740 360C756 362 774 356 788 346M812 318c4-8 14-10 20-4" stroke="#4f6fd6" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".85"/>
<path d="M799 308C804 299 814 296 821 296C830 296 840 300 844 310M846 334C850 356 848 380 842 396M797 334C794 350 794 366 796 380M722 326C740 330 760 326 780 320" stroke="#ffe9bd" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M797 320C797 288 845 288 845 320" stroke="#f6f1e6" stroke-width="5.5" fill="none" stroke-linecap="round"/>
<path d="M803 299l2-15 11 8zM839 299l-2-15-11 8z" fill="#f6f1e6"/>
<rect x="790" y="312" width="11" height="24" rx="5.5" fill="#e77f63"/><rect x="841" y="312" width="11" height="24" rx="5.5" fill="#e77f63"/><path d="M850 315v18" stroke="#ffd9b0" stroke-width="1.6" stroke-linecap="round"/>
<ellipse cx="786" cy="430" rx="13" ry="8" fill="#1d2152"/><ellipse cx="857" cy="430" rx="13" ry="8" fill="#1d2152"/>
</g>''')
A('''<g transform="translate(20 0)"><path d="M716 434l-8-50 50-6 6 56z" fill="#0b0c22"/><path d="M712 387l42-5 5 48-40 2z" fill="#c9fbf3"/>
<path d="M718 394h20M719 401h28M720 408h14M721 415h24M722 422h17" stroke="#2c8f9c" stroke-width="2.2" stroke-linecap="round"/>
<path d="M704 434h66" stroke="#0b0c22" stroke-width="5" stroke-linecap="round"/></g>''')
A('</g></g>')
# ---------- unfiltered top: stars, petals, text ----------
for i in range(80):
    x=R.uniform(0,W); y=R.uniform(4,210)*R.random()**.6+4; r=R.uniform(.6,1.8)
    if 1030<x and y<130: continue
    an=''
    if i%6==0: an=f'<animate attributeName="opacity" values="1;.2;1" dur="{R.uniform(3,7):.1f}s" begin="{R.uniform(0,5):.1f}s" repeatCount="indefinite"/>'
    A(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#fff6e0" opacity="{R.uniform(.5,1):.2f}">{an}</circle>')
for i in range(9):
    x0=R.uniform(100,1150); dur=R.uniform(11,19); beg=R.uniform(0,12); dx=R.uniform(-160,-60)
    A(f'<path d="M0 0q5-7 10 0q-5 5-10 0z" fill="{R.choice(["#e23b3b","#ff7a6a","#ffb3a8"])}" opacity="0"><animateTransform attributeName="transform" type="translate" values="{x0:.0f},-10;{x0+dx/2:.0f},260;{x0+dx:.0f},530" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.9;.9;0" keyTimes="0;.1;.85;1" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/></path>')
SERIF="'Iowan Old Style','Palatino Linotype',Palatino,'Book Antiqua',Georgia,serif"
A(f'''<g font-family="{SERIF}"><text x="70" y="104" font-size="66" fill="#fbf3e4" letter-spacing="-1">2233admin</text>
<text x="73" y="143" font-size="25" font-style="italic" fill="#ffc9a8">software that keeps working after the lights go out</text></g>
<text x="1176" y="506" text-anchor="end" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="11" letter-spacing="2" fill="#8d90c4">NIGHT SHIFT · OIL ON SVG</text>''')
A('</g></svg>')
open(out,'w').write('\n'.join(o))
