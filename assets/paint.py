import random, math, sys
out = sys.argv[1]
R = random.Random(2233)
W, H, HOR = 1200, 520, 404
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
SKY=[(0,'#10163a'),(.30,'#1f2a66'),(.55,'#3c3f8f'),(.74,'#7a5aa6'),(.88,'#e07f86'),(1,'#ffc58c')]
o=[]
A=o.append
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Oil painting: a girl with headphones sits on a rooftop beside a glowing laptop and a cat, watching tall clouds over a city at blue hour. 2233admin, software that keeps working after the lights go out.">')
A('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">''' + ''.join(f'<stop offset="{t*HOR/H:.3f}" stop-color="{c}"/>' for t,c in SKY) + '''<stop offset="1" stop-color="#ffc58c"/></linearGradient>
<filter id="oil" filterUnits="userSpaceOnUse" x="-30" y="-30" width="1260" height="580" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency="0.018 0.03" numOctaves="2" seed="7" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="9" xChannelSelector="R" yChannelSelector="G" result="d"/>
<feTurbulence type="fractalNoise" baseFrequency="0.9 0.35" numOctaves="2" seed="3" result="g"/>
<feDiffuseLighting in="g" surfaceScale="1.6" diffuseConstant="1.12" lighting-color="#ffffff" result="l"><feDistantLight azimuth="235" elevation="62"/></feDiffuseLighting>
<feBlend in="d" in2="l" mode="multiply"/>
</filter>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#9ff5ea" stop-opacity=".75"/><stop offset="1" stop-color="#9ff5ea" stop-opacity="0"/></radialGradient>
<radialGradient id="moon" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff3d6" stop-opacity=".5"/><stop offset="1" stop-color="#fff3d6" stop-opacity="0"/></radialGradient>
<clipPath id="frame"><rect width="1200" height="520" rx="14"/></clipPath>
</defs>''')
A('<g clip-path="url(#frame)"><g filter="url(#oil)">')
A(f'<rect x="-30" y="-30" width="{W+60}" height="{H+60}" fill="url(#sky)"/>')
# sky strokes
A('<g stroke-linecap="round" fill="none">')
for i in range(950):
    x=R.uniform(-40,W+40); y=R.uniform(-10,HOR+5)
    c=jit(ramp(SKY,(y+R.gauss(0,16))/HOR), 7)
    ang=math.radians(R.gauss(-4,9)); L=R.uniform(35,95); w=R.uniform(7,19)
    dx,dy=math.cos(ang)*L/2,math.sin(ang)*L/2
    A(f'<path d="M{x-dx:.0f} {y-dy:.0f}Q{x:.0f} {y+R.gauss(0,5):.0f} {x+dx:.0f} {y+dy:.0f}" stroke="{rgbhex(c)}" stroke-width="{w:.0f}" opacity="{R.uniform(.55,.9):.2f}"/>')
A('</g>')
# moon
A('<circle cx="968" cy="96" r="70" fill="url(#moon)"/><path d="M986 62a36 36 0 1 0 14 62a30 30 0 1 1-14-62z" fill="#fff1d0"/>')
# clouds
CL=[(0,'#ffe2bd'),(.25,'#ffb89c'),(.5,'#e98aa0'),(.72,'#8f68b4'),(1,'#3b4590')]
def cloud(puffs, n, top, bot):
    dabs=[]
    for (cx,cy,rx,ry) in puffs:
        for i in range(int(n*rx*ry/3000)):
            a=R.uniform(0,2*math.pi); r=math.sqrt(R.random())
            x=cx+math.cos(a)*r*rx; y=cy+math.sin(a)*r*ry
            # local light: upper-right of each puff brighter
            loc=( -math.sin(a)*r*0.5 + math.cos(a)*r*0.35 )  # -1..1 ; positive = lit
            t=(y-top)/(bot-top) - loc*0.28 + R.gauss(0,.05)
            dabs.append((t,x,y,R.uniform(9,22)))
    dabs.sort(key=lambda d:-d[0])
    for t,x,y,rad in dabs:
        c=jit(ramp(CL,t),5)
        A(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rad*1.25:.0f}" ry="{rad*.85:.0f}" fill="{rgbhex(c)}" opacity="{R.uniform(.75,.97):.2f}" transform="rotate({R.gauss(-10,14):.0f} {x:.0f} {y:.0f})"/>')
big=[(250,395,190,45),(430,390,170,48),(180,345,95,52),(300,325,110,62),(410,335,95,56),(330,272,82,52),(255,248,58,40),(395,252,52,36),(322,222,44,30),(500,358,75,38),(120,382,90,33),(585,387,90,28)]
cloud(big, 60, 190, 425)
small=[(1010,372,95,26),(1100,360,70,24),(1060,338,45,22),(700,392,80,18)]
cloud(small, 60, 310, 410)
# thin streak clouds
for (x,y,l) in [(640,250,220),(820,210,160),(60,120,0)]:
    for i in range(int(l/9)):
        xx=x+R.uniform(0,l); yy=y+R.gauss(0,5)
        A(f'<ellipse cx="{xx:.0f}" cy="{yy:.0f}" rx="{R.uniform(18,40):.0f}" ry="{R.uniform(3,6):.0f}" fill="{rgbhex(jit(hexrgb("#c98ab8"),10))}" opacity=".55"/>')
# horizon glow + city
A(f'<rect x="0" y="{HOR-14}" width="{W}" height="40" fill="#ffd9a0" opacity=".35"/>')
x=-10
blds=[]
while x<W+10:
    w=R.uniform(18,52); h=R.uniform(14,58) if R.random()>.12 else R.uniform(60,92)
    blds.append((x,w,h)); x+=w+R.uniform(-4,6)
for (x,w,h) in blds:
    A(f'<rect x="{x:.0f}" y="{438-h:.0f}" width="{w:.0f}" height="{h+10:.0f}" fill="{rgbhex(jit(hexrgb("#1a1d48"),4))}"/>')
    if h>60: A(f'<rect x="{x+w/2-1:.0f}" y="{438-h-16:.0f}" width="2" height="16" fill="#1a1d48"/>')
    for i in range(int(w*h/75)):
        A(f'<rect x="{x+R.uniform(3,w-5):.0f}" y="{438-h+R.uniform(4,h-4):.0f}" width="3" height="3.5" fill="{R.choice(["#ffd58a","#ffe7b5","#ffb46b","#9ff0e6"])}" opacity="{R.uniform(.5,1):.2f}"/>')
# pole + wires
A('<g stroke="#0d1030" fill="none" stroke-linecap="round"><path d="M1136 520V150" stroke-width="9"/><path d="M1096 178h82M1104 206h66" stroke-width="5"/>')
for (y0,y1,s) in [(176,318,40),(178,336,46),(204,352,44)]:
    A(f'<path d="M1100 {y0}Q620 {(y0+y1)/2+s} -10 {y1}" stroke-width="1.6"/><path d="M1174 {y0}Q1190 {y0+14} 1210 {y0+8}" stroke-width="1.6"/>')
A('</g>')
for bx in (300,470,655): A(f'<ellipse cx="{bx}" cy="{ {300:316,470:309,655:296}[bx] }" rx="5" ry="3.4" fill="#0d1030"/>')
# ledge
A('<rect x="-30" y="434" width="1260" height="120" fill="#12153a"/>')
for i in range(170):
    x=R.uniform(-20,W); y=R.uniform(440,520); 
    A(f'<path d="M{x:.0f} {y:.0f}h{R.uniform(30,90):.0f}" stroke="{rgbhex(jit(hexrgb("#171b46"),7))}" stroke-width="{R.uniform(6,14):.0f}" stroke-linecap="round" opacity=".8"/>')
A('<path d="M0 435h1200" stroke="#e58f8a" stroke-width="2.5" opacity=".75"/><path d="M560 436h200" stroke="#9ff5ea" stroke-width="3" opacity=".7"/>')
# laptop glow
A('<g transform="translate(821 436) scale(1.5) translate(-821 -436)">')
A('<ellipse cx="748" cy="405" rx="120" ry="80" fill="url(#glow)"/>')
# cat
A('''<g fill="#0e1130"><path d="M905 436c-4-18 2-34 14-38c13 3 20 20 16 38z"/><circle cx="919" cy="392" r="11"/><path d="M909 388l1-14 9 8zM929 388l0-14-9 8z"/><path d="M933 432c22 4 40 0 46-12" stroke="#0e1130" stroke-width="6" fill="none" stroke-linecap="round"/></g>
<path d="M929 376l1 12M931 398c5 8 6 22 4 34M979 421c-3 6-10 10-18 12" stroke="#ffb89c" stroke-width="2" fill="none" stroke-linecap="round" opacity=".9"/>''')
# girl (from behind)
A('''<g>
<path d="M800 316C770 318 742 330 712 322C728 340 752 344 772 342C756 356 738 360 722 358C742 374 772 372 792 362C790 380 792 396 800 408L842 408C852 380 852 344 846 318Z" fill="#1b2150"/>
<path d="M786 436C780 404 786 372 798 356C812 346 830 346 844 356C856 372 862 404 856 436Z" fill="#2a2f6a"/>
<path d="M786 436C780 404 786 372 798 356C806 380 806 410 808 436Z" fill="#3fa9b5" opacity=".55"/>
<path d="M844 356C856 372 862 404 856 436" stroke="#ffb89c" stroke-width="3" fill="none" stroke-linecap="round"/>
<ellipse cx="821" cy="356" rx="27" ry="10" fill="#353b80"/>
<circle cx="821" cy="322" r="25" fill="#1b2150"/>
<path d="M800 330C792 352 794 380 802 404C808 384 808 360 812 344ZM842 330C848 350 846 376 838 398C834 378 836 358 832 344Z" fill="#1b2150"/>
<path d="M803 312C812 300 830 298 840 310M806 338C802 356 802 376 806 392M728 330C748 334 768 330 786 322M738 360C756 362 774 356 788 346" stroke="#5f7fe6" stroke-width="2.5" fill="none" stroke-linecap="round" opacity=".85"/>
<path d="M838 302C846 308 850 318 848 330M846 344C850 362 848 382 842 396" stroke="#ffb89c" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M797 320C797 288 845 288 845 320" stroke="#f3eef6" stroke-width="5.5" fill="none" stroke-linecap="round"/>
<path d="M803 299l2-15 11 8zM839 299l-2-15-11 8z" fill="#f3eef6"/>
<rect x="790" y="312" width="11" height="24" rx="5.5" fill="#e77f63"/><rect x="841" y="312" width="11" height="24" rx="5.5" fill="#e77f63"/>
<ellipse cx="786" cy="430" rx="13" ry="8" fill="#2a2f6a"/><ellipse cx="857" cy="430" rx="13" ry="8" fill="#2a2f6a"/>
</g>''')
# laptop + mug
A('''<path d="M716 434l-8-50 50-6 6 56z" fill="#0e1130"/><path d="M712 387l42-5 5 48-40 2z" fill="#c9fbf3"/>
<path d="M718 394h20M719 401h28M720 408h14M721 415h24M722 422h17" stroke="#2c8f9c" stroke-width="2.2" stroke-linecap="round"/>
<path d="M704 434h66" stroke="#0e1130" stroke-width="5" stroke-linecap="round"/>
<rect x="668" y="418" width="16" height="17" rx="3" fill="#f3eef6"/><path d="M684 422q8 3 0 9" stroke="#f3eef6" stroke-width="2.5" fill="none"/>
<path d="M673 412q-5-8 1-14q5-6 0-13M680 410q4-7-1-12" stroke="#ffffff" stroke-width="2" fill="none" stroke-linecap="round" opacity=".5"/>''')
A('</g></g>')
# unfiltered: stars, beacons, shooting star, text
for i in range(90):
    x=R.uniform(0,W); y=R.uniform(4,230)*R.random()**.6+4; r=R.uniform(.6,1.9)
    an=''
    if i%7==0: an=f'<animate attributeName="opacity" values="1;.2;1" dur="{R.uniform(3,7):.1f}s" begin="{R.uniform(0,5):.1f}s" repeatCount="indefinite"/>'
    A(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#fff6e0" opacity="{R.uniform(.5,1):.2f}">{an}</circle>')
for (x,w,h) in blds:
    if h>60: A(f'<circle cx="{x+w/2:.0f}" cy="{438-h-17:.0f}" r="2.6" fill="#ff5a4d"><animate attributeName="opacity" values="1;.15;1" dur="2.4s" begin="{R.uniform(0,2):.1f}s" repeatCount="indefinite"/></circle>')
A('''<path d="M0 0l-90 26" stroke="#fff6e0" stroke-width="2" stroke-linecap="round" opacity="0"><animateTransform attributeName="transform" type="translate" values="760,40;560,98" dur="9s" keyTimes="0;1" repeatCount="indefinite" calcMode="spline" keySplines="0 0 .1 1"/><animate attributeName="opacity" values="0;0;.9;0;0" keyTimes="0;.02;.06;.14;1" dur="9s" repeatCount="indefinite"/></path>''')
SERIF="'Iowan Old Style','Palatino Linotype',Palatino,'Book Antiqua',Georgia,serif"
A(f'''<g font-family="{SERIF}"><text x="70" y="104" font-size="66" fill="#fbf3e4" letter-spacing="-1">2233admin</text>
<text x="73" y="143" font-size="25" font-style="italic" fill="#ffc9a8">software that keeps working after the lights go out</text></g>
<text x="1124" y="504" text-anchor="end" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="11" letter-spacing="2" fill="#8d90c4">NIGHT SHIFT · OIL ON SVG</text>''')
A('</g></svg>')
open(out,'w').write('\n'.join(o))
