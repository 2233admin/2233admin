import random, math, sys
out = sys.argv[1]
R = random.Random(1957)
W, H, HOR = 1200, 520, 404
o=[]; A=o.append
def hexrgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def rgbhex(c): return '#%02x%02x%02x' % tuple(max(0,min(255,int(round(v)))) for v in c)
def mix(a,b,t): a,b=hexrgb(a),hexrgb(b); return rgbhex(tuple(a[i]+(b[i]-a[i])*t for i in range(3)))
SANS="'DIN Condensed','Bahnschrift','Arial Narrow','Helvetica Neue',Arial,'PingFang SC',sans-serif"
MONO="ui-monospace,'SF Mono',Menlo,Consolas,monospace"
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Digital painting: a doomer maid in a striped tracksuit jacket, with a mechanical arm and a bottle of kvass, squats on a panel-block rooftop next to a cat. Beyond a red rooftop sign reading NOCHNAYA SMENA (night shift), a derelict giant robot slumps among apartment blocks, a rocket climbs past a ringed planet at dusk, and snow falls. 2233admin.">')
A('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070d18"/><stop offset=".28" stop-color="#12233a"/><stop offset=".5" stop-color="#2f4257"/><stop offset=".64" stop-color="#75605f"/><stop offset=".73" stop-color="#cf8456"/><stop offset=".79" stop-color="#f6c27c"/><stop offset="1" stop-color="#f6c27c"/></linearGradient>
<radialGradient id="sun" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ffe2a8" stop-opacity=".95"/><stop offset=".3" stop-color="#ff9a52" stop-opacity=".55"/><stop offset="1" stop-color="#ff7a3a" stop-opacity="0"/></radialGradient>
<linearGradient id="haze" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e79a68" stop-opacity="0"/><stop offset="1" stop-color="#f0a873" stop-opacity=".75"/></linearGradient>
<linearGradient id="planet" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1b3147"/><stop offset=".55" stop-color="#5d7f95"/><stop offset="1" stop-color="#e9c7a4"/></linearGradient>
<linearGradient id="pfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".75" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="pm"><rect x="700" y="-60" width="560" height="400" fill="url(#pfade)"/></mask>
<linearGradient id="trail" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ffb070" stop-opacity="0"/><stop offset=".5" stop-color="#ffc79a" stop-opacity=".7"/><stop offset="1" stop-color="#fff"/></linearGradient>
<linearGradient id="robot" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8d6a5a"/><stop offset=".18" stop-color="#3a4250"/><stop offset="1" stop-color="#1a222e"/></linearGradient>
<linearGradient id="rfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b98a70" stop-opacity="0"/><stop offset="1" stop-color="#c9906c" stop-opacity=".8"/></linearGradient>
<linearGradient id="roof" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b212b"/><stop offset="1" stop-color="#07090d"/></linearGradient>
<linearGradient id="jacket" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5b4a52"/><stop offset=".25" stop-color="#232c44"/><stop offset="1" stop-color="#0e1424"/></linearGradient>
<linearGradient id="pants" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4c4250"/><stop offset=".3" stop-color="#1c2338"/><stop offset="1" stop-color="#0b0f1c"/></linearGradient>
<linearGradient id="skin" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffd9bd"/><stop offset=".55" stop-color="#e8b9a4"/><stop offset="1" stop-color="#9c7f8c"/></linearGradient>
<linearGradient id="hair" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff0dc"/><stop offset=".4" stop-color="#c9d0da"/><stop offset="1" stop-color="#5d6b84"/></linearGradient>
<linearGradient id="metal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9d6c0"/><stop offset=".35" stop-color="#8b95a3"/><stop offset="1" stop-color="#2b3240"/></linearGradient>
<linearGradient id="glass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c8793a"/><stop offset=".4" stop-color="#6a3414"/><stop offset="1" stop-color="#2a1408"/></linearGradient>
<radialGradient id="vig" cx="50%" cy="46%" r="75%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".62"/></radialGradient>
<radialGradient id="eye" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff"/><stop offset=".25" stop-color="#ff5a3c"/><stop offset="1" stop-color="#ff2a1a" stop-opacity="0"/></radialGradient>
<filter id="b1"><feGaussianBlur stdDeviation="1"/></filter><filter id="b2"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="b6" x="-30%" y="-80%" width="160%" height="260%"><feGaussianBlur stdDeviation="7"/></filter>
<filter id="b18" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="16"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/><feColorMatrix type="matrix" values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  .9 .9 .9 0 -1.05"/></filter>
<clipPath id="frame"><rect width="1200" height="520" rx="14"/></clipPath>
</defs>''')
A('<g clip-path="url(#frame)">')
A(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
A('<ellipse cx="250" cy="410" rx="560" ry="250" fill="url(#sun)"/>')
# stars
for i in range(70):
    x=R.uniform(0,W); y=R.uniform(0,170)*R.random()**.5
    A(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{R.uniform(.5,1.4):.1f}" fill="#eaf2ff" opacity="{R.uniform(.3,.9):.2f}"/>')
# ringed planet
A('''<g mask="url(#pm)" opacity=".62"><g transform="rotate(-20 985 120)">
<path d="M725 120a260 44 0 0 1 520 0" fill="none" stroke="#c9d3dc" stroke-width="13" opacity=".5"/>
<circle cx="985" cy="120" r="148" fill="url(#planet)"/>
<path d="M850 80q135 34 270-10M842 128q143 30 286-6M860 176q125 22 250-8" stroke="#dfe7ee" stroke-width="9" fill="none" opacity=".12"/>
<path d="M725 120a260 44 0 0 0 520 0" fill="none" stroke="#e6edf2" stroke-width="13" opacity=".8"/><path d="M745 120a240 36 0 0 0 480 0" fill="none" stroke="#31465a" stroke-width="3" opacity=".8"/>
</g></g>''')
# clouds: dark bodies with lit bellies
A('<g filter="url(#b18)">')
for i in range(16):
    x=R.uniform(-80,1250); y=R.uniform(150,330); rx=R.uniform(120,300); ry=R.uniform(10,26)
    t=(y-150)/180
    A(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="{mix("#16263a","#5a4a56",t)}" opacity=".85"/>')
    k=max(0,1-abs(x-250)/900)
    A(f'<ellipse cx="{x-30:.0f}" cy="{y+ry*.9:.0f}" rx="{rx*.8:.0f}" ry="{ry*.35:.0f}" fill="{mix("#c06a58","#ffb074",k)}" opacity="{.25+.55*k*t:.2f}"/>')
A('</g>')
# rocket
A('''<path d="M548 404C552 320 590 210 700 96" stroke="#ffb884" stroke-width="16" fill="none" opacity=".35" filter="url(#b6)"/>
<path d="M548 404C552 320 590 210 700 96" stroke="url(#trail)" stroke-width="3.2" fill="none" stroke-linecap="round"/>
<circle cx="700" cy="96" r="16" fill="#fff3d8" opacity=".55" filter="url(#b6)"><animate attributeName="opacity" values=".55;.9;.55" dur="1.6s" repeatCount="indefinite"/></circle>
<path d="M698 99l8-16 4 12z" fill="#eef2f6"/><circle cx="700" cy="97" r="2.6" fill="#fff"/>
<g filter="url(#b6)" fill="#f3c9a0" opacity=".7"><ellipse cx="548" cy="398" rx="46" ry="14"/><ellipse cx="520" cy="388" rx="26" ry="12"/><ellipse cx="580" cy="390" rx="24" ry="10"/></g>''')
# far skyline (hazy)
A('<g filter="url(#b1)">')
x=-10
while x<W+10:
    w=R.uniform(26,70); h=R.uniform(16,52)
    A(f'<rect x="{x:.0f}" y="{412-h:.0f}" width="{w:.0f}" height="{h+30:.0f}" fill="{mix("#8a6660","#5b5562",R.random())}"/>')
    x+=w+R.uniform(-6,10)
# TV tower + swooping rocket monument
A('''<g fill="#5a5262"><path d="M176 412l7-150h2l7 150zM181 262h8v-70h-2l-2-60-2 60h-2z"/><ellipse cx="185" cy="268" rx="13" ry="7"/><rect x="179" y="300" width="12" height="5"/></g>
<path d="M330 412C352 330 392 262 452 214L446 222C404 276 378 338 372 412Z" fill="#6a5a66"/><path d="M452 214l14-16-4 20z" fill="#7b6c78"/>''')
A('</g>')
A(f'<rect x="0" y="300" width="{W}" height="116" fill="url(#haze)"/>')
# derelict giant robot
A('''<g>
<path d="M664 440C660 372 672 318 700 300L812 300C842 318 852 372 848 440Z" fill="url(#robot)"/>
<circle cx="686" cy="312" r="32" fill="url(#robot)"/><circle cx="828" cy="312" r="32" fill="#1c2430"/>
<path d="M660 318C640 350 636 400 646 440L676 440C668 400 672 356 688 330Z" fill="url(#robot)"/>
<path d="M838 322C866 352 874 400 868 440L842 440C846 400 840 360 826 336Z" fill="#161d28"/>
<g transform="rotate(-9 748 262)"><rect x="734" y="284" width="30" height="22" fill="#1d2531"/>
<path d="M700 262a50 46 0 0 1 100 0v10a50 22 0 0 1-100 0z" fill="url(#robot)"/>
<path d="M722 224l-14-40M782 226l10-34" stroke="#2b3340" stroke-width="3" stroke-linecap="round"/><circle cx="708" cy="184" r="4" fill="#3a4250"/><circle cx="792" cy="192" r="4" fill="#2b3340"/>
<circle cx="738" cy="262" r="19" fill="#0b0f16"/><circle cx="738" cy="262" r="12" fill="#2a0c0c"/>
<circle cx="738" cy="262" r="26" fill="url(#eye)" opacity=".85"><animate attributeName="opacity" values=".85;.25;.7;.15;.85" keyTimes="0;.45;.5;.56;1" dur="6s" repeatCount="indefinite"/></circle>
<path d="M702 256a50 46 0 0 1 30-36" stroke="#f0b98a" stroke-width="2.5" fill="none" stroke-linecap="round" opacity=".8"/></g>
<path d="M756 372l7 15 16 2-12 11 3 16-14-8-14 8 3-16-12-11 16-2z" fill="#9a2f2a" opacity=".75"/>
<path d="M700 340h112M704 352h30M768 352h40" stroke="#0e141c" stroke-width="2" opacity=".7"/>
<path d="M662 330C646 360 642 400 648 436M672 296C664 310 660 330 662 350" stroke="#f0b98a" stroke-width="2.5" fill="none" stroke-linecap="round" opacity=".75"/>
</g>''')
# mid panel blocks
def block(x,w,h,base=442,tone=0.0):
    body=mix('#222a38','#3a3c4a',tone); y=base-h
    A(f'<rect x="{x}" y="{y}" width="{w}" height="{h+20}" fill="{body}"/>')
    A(f'<rect x="{x}" y="{y}" width="9" height="{h+20}" fill="#b0765a" opacity=".85"/>')
    A(f'<rect x="{x}" y="{y}" width="{w}" height="3" fill="#d79a72" opacity=".7"/>')
    cols=int((w-18)/13); rows=int((h-8)/13)
    for r in range(rows):
        for c in range(cols):
            wx=x+14+c*13; wy=y+8+r*13
            p=R.random()
            if p<.2: col=R.choice(['#ffc878','#ffd9a0','#ffae5c','#ffc878','#9fdcec']); op=R.uniform(.7,1)
            else: col='#121824'; op=.9
            A(f'<rect x="{wx}" y="{wy}" width="7" height="8" fill="{col}" opacity="{op:.2f}"/>')
    for i in range(R.randint(1,3)):
        ax=x+R.uniform(12,w-12); A(f'<path d="M{ax:.0f} {y}v-{R.uniform(12,26):.0f}m-6 6h12m-9 5h6" stroke="#1a202c" stroke-width="1.5" fill="none"/>')
for (x,w,h,t) in [(-20,150,96,.5),(140,120,128,.3),(270,170,84,.5),(452,96,140,.2),(556,84,70,.5),(880,110,92,.4),(1000,150,120,.2),(1140,90,150,.1)]:
    block(x,w,h,tone=t)
A(f'<rect x="0" y="360" width="{W}" height="82" fill="url(#haze)" opacity=".55"/>')
# rooftop
A(f'<rect x="0" y="436" width="{W}" height="90" fill="url(#roof)"/><path d="M0 436.5h{W}" stroke="#e9a878" stroke-width="2" opacity=".8"/><path d="M0 446h{W}" stroke="#05070a" stroke-width="3"/>')
for i in range(60):
    x=R.uniform(0,W); y=R.uniform(450,520)
    A(f'<path d="M{x:.0f} {y:.0f}h{R.uniform(20,90):.0f}" stroke="#2a313d" stroke-width="{R.uniform(1,3):.1f}" opacity="{R.uniform(.2,.6):.2f}"/>')
# sign frame + neon
A('<g stroke="#0c1016" stroke-width="3" fill="none">'+''.join(f'<path d="M{x} 436V352M{x} 436l22-56"/>' for x in range(70,660,84))+'<path d="M50 424h596M50 356h596"/></g>')
SIGN=f'<text x="60" y="418" font-family="{SANS}" font-weight="800" font-size="72" letter-spacing="7" textLength="576" lengthAdjust="spacingAndGlyphs">НОЧНАЯ СМЕНА</text>'
A(f'<g fill="#ff3b2e" opacity=".9" filter="url(#b6)">{SIGN}</g><g fill="#ff6a55" stroke="#ffd2c4" stroke-width="1.2">{SIGN}<animate attributeName="opacity" values="1;1;.55;1;.7;1;1" keyTimes="0;.6;.62;.64;.66;.68;1" dur="7s" repeatCount="indefinite"/></g>')
A('<rect x="40" y="440" width="620" height="40" fill="#ff4a38" opacity=".16" filter="url(#b6)"/>')
# roof clutter
A('''<rect x="700" y="408" width="70" height="30" fill="#141a23"/><rect x="700" y="408" width="70" height="4" fill="#c58a66" opacity=".7"/><path d="M712 414h46M712 421h46M712 428h46" stroke="#05070a" stroke-width="2"/>
<path d="M820 436v-92m-22 10h44m-36 12h28m-20 12h12" stroke="#0c1016" stroke-width="2.5" fill="none"/><path d="M1168 436v-70" stroke="#0c1016" stroke-width="3"/><path d="M1150 372a20 20 0 0 1 36-14z" fill="#1a212c"/>''')
# cat
A('''<g transform="translate(1102 436)"><path d="M-16 0c-4-18 2-34 14-38c13 3 20 20 16 38z" fill="#0c1016"/><circle cx="-2" cy="-44" r="11" fill="#0c1016"/><path d="M-12-48l1-14 9 8zM8-48l0-14-9 8z" fill="#0c1016"/><path d="M12-4c16 4 26-2 26-16" stroke="#0c1016" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M-12-50l1-11M-16-4c-3-14 1-26 8-32M-12-40c-2-6 0-10 3-13" stroke="#f0b98a" stroke-width="1.6" fill="none" stroke-linecap="round"/></g>''')
# radio
A('''<g transform="translate(906 436)"><rect x="-26" y="-22" width="52" height="22" rx="3" fill="#1b222d"/><circle cx="-12" cy="-11" r="7" fill="#0b0f15"/><circle cx="-12" cy="-11" r="3" fill="#39424f"/><rect x="2" y="-17" width="18" height="6" fill="#ffb060" opacity=".9"/><path d="M20-22l26-44" stroke="#8b95a3" stroke-width="1.5"/><path d="M-26-22h52" stroke="#d79a72" stroke-width="1.5" opacity=".8"/></g>''')
# ---- the maid (gopnik squat, profile facing left) ----
A('<g transform="translate(1012 436) scale(1.28)">')
A('<ellipse cx="-8" cy="2" rx="62" ry="6" fill="#000" opacity=".5" filter="url(#b2)"/>')
A('''<path d="M26 -62c18-12 36-8 44 4c-12 2-22 8-30 16c10 2 18 10 20 22c-14-8-28-10-40-8z" fill="#f4efe8"/><path d="M26 -62c18-12 36-8 44 4M40-42c10 2 18 10 20 22" stroke="#8fa0b8" stroke-width="1.5" fill="none"/><circle cx="26" cy="-58" r="7" fill="#e3ddd4"/>
<path d="M30-34C34-20 30-8 20 0L-16 0C-8-10 0-22 6-36Z" fill="#0f1420"/>
<path d="M32-30q6 6 4 12q-6 2-9-3q4 5 0 10q-6 1-8-4q2 6-3 9q-6 0-7-5q1 6-5 8" stroke="#f4efe8" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M-44-66C-30-76 -8-66 22-46C30-40 34-30 28-22C10-28 -20-40 -40-50Z" fill="url(#pants)"/>
<path d="M-46-66C-52-48 -34-24 -20-8L-2-8C-10-26 -22-48 -30-70Z" fill="url(#pants)"/>
<path d="M-38-62C-22-60 2-48 24-34M-34-56C-20-54 2-43 22-29" stroke="#f1eee8" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<path d="M-44-58C-40-40 -28-22 -16-9M-39-60C-35-42 -23-24 -11-10" stroke="#f1eee8" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<path d="M-46-66C-50-52 -40-34 -30-20" stroke="#ffb884" stroke-width="2" fill="none" stroke-linecap="round" opacity=".85"/>
<path d="M-46 0C-48-8 -36-14 -22-13L0-10C6-8 8-2 6 0Z" fill="#ece6dc"/><path d="M-46 0h52" stroke="#b9372c" stroke-width="3"/><path d="M-30-11l8 8M-22-12l8 8" stroke="#b9372c" stroke-width="1.6"/><path d="M-46-2C-46-8 -38-13 -28-13" stroke="#ffd9b0" stroke-width="1.6" fill="none"/>
<path d="M24-40C34-62 30-96 14-116C2-124 -14-120 -20-108C-24-90 -18-62 -4-42Z" fill="url(#jacket)"/>
<path d="M-16-110C-22-94 -20-74 -12-56L-2-44C-10-62 -12-88 -8-110Z" fill="#11141c"/><path d="M-13-104C-18-90 -16-74 -10-60" stroke="#f4efe8" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="1 7"/>
<path d="M24-40C34-62 30-96 14-116" stroke="#6fa0bc" stroke-width="1.6" fill="none" opacity=".7"/>
<path d="M-18-120c6-6 26-6 32 2l-2 10c-10 4-22 4-30-2z" fill="#1a2238"/><path d="M-18-120c6-6 26-6 32 2" stroke="#f1eee8" stroke-width="2" fill="none"/>
<path d="M10-112C-6-108 -30-92 -46-76C-42-68 -36-66 -30-68C-16-78 4-88 18-96Z" fill="url(#jacket)"/>
<path d="M8-108C-8-102 -28-88 -42-74M12-102C-4-96 -22-84 -36-70" stroke="#f1eee8" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<circle cx="-40" cy="-72" r="8" fill="#39424f"/><circle cx="-40" cy="-72" r="4.5" fill="#ff9a4a"><animate attributeName="opacity" values="1;.5;1" dur="3s" repeatCount="indefinite"/></circle>
<path d="M-46-76L-74-52L-68-44L-38-66Z" fill="url(#metal)"/><path d="M-52-70l-18 16M-60-58l4 5M-54-63l4 5" stroke="#1a2029" stroke-width="1.4" fill="none"/><path d="M-46-76L-74-52" stroke="#ffe2c0" stroke-width="1.4"/>
<rect x="-78" y="-54" width="12" height="5" rx="2" transform="rotate(-40 -72 -52)" fill="#ff9a4a"/>
<path d="M-76-52c-6 2-9 8-6 13c5 2 10-2 12-8z" fill="url(#metal)"/>
<g transform="rotate(8 -80 -40)"><rect x="-84" y="-50" width="7" height="14" fill="url(#glass)"/><path d="M-88-36h15l3 8v24a3 3 0 0 1-3 3h-15a3 3 0 0 1-3-3v-24z" fill="url(#glass)"/><rect x="-90" y="-24" width="19" height="13" fill="#e9dcc0"/><path d="M-87-20h13M-87-16h9" stroke="#b9372c" stroke-width="1.6"/><path d="M-89-34v28" stroke="#ffc890" stroke-width="1.4" opacity=".9"/><rect x="-85" y="-53" width="9" height="4" fill="#d9b24a"/></g>
<g transform="translate(4 -114) scale(.8) translate(-4 114)"><path d="M-6-118l2 12 10-2-2-12z" fill="url(#skin)"/>
<path d="M-26-146C-28-160 -14-170 2-168C16-166 24-154 22-140C20-128 10-120 0-119C-8-118 -16-120 -19-126L-21-131L-27-133L-24-138Z" fill="url(#skin)"/>
<path d="M-22-134q3 2 6 0" stroke="#7a3b3b" stroke-width="1.3" fill="none" stroke-linecap="round"/>
<path d="M-21-146q5-3 10 0" stroke="#2a2030" stroke-width="2.2" fill="none" stroke-linecap="round"/><path d="M-19-145.5a3.2 2.6 0 0 0 6 0z" fill="#b9372c"/><path d="M-20-141q4 2 8 0" stroke="#8a6078" stroke-width="1.6" fill="none" opacity=".55"/>
<path d="M-24-151l9-3" stroke="#8f98a8" stroke-width="1.6" stroke-linecap="round"/><ellipse cx="-10" cy="-136" rx="5" ry="2.6" fill="#ff8a7a" opacity=".35"/>
<path d="M-26-150C-30-166 -14-178 4-176C22-174 32-158 28-138C26-126 20-118 12-114C16-126 14-138 8-146C4-138 0-134 -4-134C-2-142 -4-150 -8-156C-12-152 -18-150 -26-150Z" fill="url(#hair)"/>
<path d="M-8-156C-4-150 -2-142 -4-134M8-146C14-138 16-126 12-114M-20-158C-12-166 0-168 10-164" stroke="#6d7a92" stroke-width="1.3" fill="none" opacity=".8"/>
<path d="M-27-152C-30-166 -16-177 0-177" stroke="#ffe9c8" stroke-width="1.8" fill="none" stroke-linecap="round"/><path d="M28-140C26-128 20-119 13-115" stroke="#6fa0bc" stroke-width="1.5" fill="none" opacity=".8"/>
<path d="M-20-170C-10-180 10-182 22-170" stroke="#12151c" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M-22-172q3-9 9-6q2-9 9-5q4-8 10-3q6-6 10 1q7-3 8 5" stroke="#f8f4ee" stroke-width="5.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M6-146v10" stroke="#d9b24a" stroke-width="1.5"/><circle cx="6" cy="-134" r="2.4" fill="#b9372c"/></g>
<path d="M30-44C38-64 34-94 18-114C24-92 24-66 14-42Z" fill="#05070c" opacity=".45" filter="url(#b2)"/>''')
A('</g>')
# front haze + snow + grade
A(f'<rect x="0" y="330" width="{W}" height="110" fill="url(#haze)" opacity=".16"/>')
for i in range(46):
    x0=R.uniform(-40,1240); dur=R.uniform(9,20); beg=-R.uniform(0,20); r=R.uniform(.9,2.6); dx=R.uniform(-90,-20)
    A(f'<circle r="{r:.1f}" fill="#fff4e6" opacity="{R.uniform(.35,.9):.2f}"><animateTransform attributeName="transform" type="translate" values="{x0:.0f},-10;{x0+dx:.0f},530" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/></circle>')
A(f'<rect width="{W}" height="{H}" fill="url(#vig)"/><rect width="{W}" height="{H}" filter="url(#grain)" opacity=".22"/>')
# title
A(f'''<rect x="70" y="52" width="6" height="96" fill="#e0382c"/>
<text x="92" y="108" font-family="{SANS}" font-weight="800" font-size="68" letter-spacing="3" fill="#f6eede">2233ADMIN</text>
<text x="94" y="140" font-family="{MONO}" font-size="13.5" letter-spacing="2.6" fill="#f0b48c">SOFTWARE THAT KEEPS WORKING AFTER THE LIGHTS GO OUT</text>
<text x="1176" y="506" text-anchor="end" font-family="{MONO}" font-size="10.5" letter-spacing="2" fill="#6f7a8c">НОЧНАЯ СМЕНА · NIGHT SHIFT</text>''')
A('</g></svg>')
open(out,'w').write('\n'.join(o))
