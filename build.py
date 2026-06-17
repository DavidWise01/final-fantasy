#!/usr/bin/env python3
"""Build the original Final Fantasy (FF1) — Square, Famicom 1987 / NES 1990 — as a
UD0 game-world: the first light, the game that launched the franchise and saved
Square. Themed to the source — deep crystal-night blue + Orb-gold + crystal-cyan;
the title is a STATIC ORIGINAL ONE-LINE PENCIL DRAWING (a single continuous
contour of a Warrior of Light and the crystal, hand-drawn wobble via SVG
turbulence, a one-time self-drawing reveal that settles to a static line — a
fan-art tribute, NOT Square's logo or sprites). Genesis, the loop of time, and the
.dlw birth. Render-not-invent. Final Fantasy is © Square Enix; a fan tribute.
Cross-links FF6 (the apex of the line it began)."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "FINAL FANTASY", "axiom": "FF1",
 "position": "Final Fantasy · Square · Famicom 1987 / NES 1990 — the four Light Warriors and the loop of time",
 "origin": "the kingdom of Cornelia and a darkened world — four youths bearing four dimmed Orbs set out to restore the light and break a 2000-year loop",
 "mechanism": "Crystallized from the original Final Fantasy (Square, Famicom 1987 / NES 1990).",
 "crystallization": "Four silent warriors carry four lightless crystals into a broken world, defeat its four elemental Fiends, and chase the demon Chaos back through a closed loop of time to its source.",
 "nature": "The first Final Fantasy — the near-last gamble that became a dynasty: four blank-slate heroes, the four Orbs and their Fiends, the fallen knight Garland who becomes the demon Chaos, a paradox of time, and Nobuo Uematsu's first Prelude.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Final Fantasy; the Light Warriors; the four Orbs; Garland; Chaos; the four Fiends",
 "witness": "Named “Final” for a studio that thought it might be their last game — it instead began one of the largest series in all of gaming.",
 "role": "the first light — the source of the line",
 "seal": "Carry four dead crystals into a dying world, kill its four Fiends, and break the loop that keeps remaking the demon at the root of time.",
 "source": "Final Fantasy, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#6fae6a", "of flesh and the world — the fallen knight, the captive princess, the dragons and sea-beasts"),
 "ethereal":  ("#9a7cff", "of the unmade and the void — the four elemental Fiends, the demon Chaos, the closed loop of time"),
 "spiritual": ("#e8c45a", "of the soul, the light, and the calling — the four Orbs, the prophesied warriors, the trial, the Prelude"),
 "electrical":("#4fd0e0", "of the ancient machine — the buried Lufenian airship and the steel WarMECH on the sky fortress"),
}

# ── the title scene · STATIC ORIGINAL ONE-LINE PENCIL DRAWING ─────
# A single continuous contour (a Warrior of Light + the crystal + a raised sword),
# given a hand-drawn pencil wobble by an SVG turbulence filter and a one-time
# self-drawing reveal that settles into a static line. Original fan tribute — not
# Square's logo, art, or sprites.
COVER_ART = r'''<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Final Fantasy — an original one-line pencil-style title drawing (fan tribute, not Square's logo or art)" style="width:100%;height:auto;display:block;background:#070912">
<defs>
 <radialGradient id="ff_sky" cx="50%" cy="34%" r="90%"><stop offset="0%" stop-color="#101a36"/><stop offset="58%" stop-color="#0a1024"/><stop offset="100%" stop-color="#05070f"/></radialGradient>
 <radialGradient id="ff_glow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(79,208,224,.42)"/><stop offset="70%" stop-color="rgba(79,208,224,.08)"/><stop offset="100%" stop-color="rgba(79,208,224,0)"/></radialGradient>
 <filter id="ff_pencil" x="-6%" y="-6%" width="112%" height="112%"><feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.6" xChannelSelector="R" yChannelSelector="G"/></filter>
 <style>
  .oneline{fill:none;stroke:#d3dae8;stroke-width:2.1;stroke-linecap:round;stroke-linejoin:round;
    pathLength:1;stroke-dasharray:1;stroke-dashoffset:1;animation:ffdraw 3.4s cubic-bezier(.6,.05,.25,1) .25s forwards;}
  .oneline.ghost{stroke:#7f8aa6;stroke-width:1.1;opacity:.4;animation-delay:.05s;}
  .ffword{opacity:0;animation:fffade 1.3s ease 3.0s forwards;}
  .ffstar{opacity:0;animation:fffade 1.1s ease 3.4s forwards;}
  @keyframes ffdraw{to{stroke-dashoffset:0;}}
  @keyframes fffade{to{opacity:1;}}
  @media (prefers-reduced-motion: reduce){.oneline{animation:none;stroke-dashoffset:0;}.ffword,.ffstar{animation:none;opacity:1;}}
 </style>
</defs>
<rect width="700" height="320" fill="url(#ff_sky)"/>
<ellipse cx="350" cy="172" rx="150" ry="120" fill="url(#ff_glow)"/>
<g class="ffstar" fill="#cfe0f0"><circle cx="120" cy="48" r="1.3" opacity=".8"/><circle cx="250" cy="36" r="1" opacity=".6"/><circle cx="470" cy="44" r="1.2" opacity=".7"/><circle cx="600" cy="60" r="1" opacity=".6"/><circle cx="64" cy="150" r="1" opacity=".5"/><circle cx="650" cy="180" r="1.1" opacity=".6"/><circle cx="540" cy="250" r="1" opacity=".5"/><circle cx="180" cy="268" r="1" opacity=".5"/></g>
<!-- THE ONE LINE — a single continuous contour (drawn twice: a faint ghost + the line, for a pencil feel) -->
<path class="oneline ghost" filter="url(#ff_pencil)" d="M 96 268 C 138 214, 138 150, 196 128 C 224 117, 228 84, 206 74 C 186 65, 168 84, 180 100 C 190 114, 218 112, 236 98 C 268 74, 312 96, 332 134 L 350 100 L 396 158 L 350 216 L 304 158 L 350 100 C 350 72, 351 44, 352 24 C 353 44, 354 72, 354 116 L 392 138 L 318 138 C 360 168, 430 198, 532 224 C 576 235, 612 244, 648 266"/>
<path class="oneline" filter="url(#ff_pencil)" d="M 96 268 C 138 214, 138 150, 196 128 C 224 117, 228 84, 206 74 C 186 65, 168 84, 180 100 C 190 114, 218 112, 236 98 C 268 74, 312 96, 332 134 L 350 100 L 396 158 L 350 216 L 304 158 L 350 100 C 350 72, 351 44, 352 24 C 353 44, 354 72, 354 116 L 392 138 L 318 138 C 360 168, 430 198, 532 224 C 576 235, 612 244, 648 266"/>
<!-- wordmark (fades in once the line is drawn) -->
<g class="ffword">
 <text x="350" y="294" text-anchor="middle" font-family="'Newsreader',Georgia,serif" font-size="38" font-weight="400" letter-spacing="7" fill="#eef3fb">FINAL&#8201;FANTASY</text>
 <text x="350" y="312" text-anchor="middle" font-family="'Space Mono',monospace" font-size="10" letter-spacing="5" fill="#e8c45a">SQUARE · NES · 1987 · THE FIRST LIGHT</text>
</g>
<rect x="6" y="6" width="688" height="308" fill="none" stroke="#1d2742" stroke-width="2"/>
</svg>'''

GENESIS = [
 ("The “Final” Gamble", "Japan 1987 → US 1990",
  "Square was small and struggling, and Hironobu Sakaguchi reportedly meant this to be his last game if it failed — hence, the legend goes, “Final.” (Sakaguchi has also said any title abbreviating to “FF” would have done, and they simply wanted “Fantasy.”) Designed by Sakaguchi, scored by Nobuo Uematsu, with character art by Yoshitaka Amano and programming by Nasir Gebelli. It did not fail — it founded a dynasty."),
 ("Four Orbs, Four Heroes", "the blank-slate party",
  "You name and class four silent Light Warriors — from Fighter, Thief, Black Belt, Red Mage, White Mage and Black Mage — each carrying one of four Orbs (the NES localization's word; later versions restored “Crystals”) gone dark. No personalities, no dialogue: a party you author and project a story onto."),
 ("The Prelude", "Uematsu's first arpeggio",
  "Over the opening, a rising-and-falling harp arpeggio plays — Nobuo Uematsu's “Prelude,” written for this game and carried, in some form, into nearly every Final Fantasy since. The first note of a forty-year score."),
]

ARC = [
 ("Cornelia and the Knight", "the false beginning",
  "The knight Garland kidnaps Princess Sara of Cornelia; the Light Warriors cross the kingdom's broken bridge, find him in the Chaos Shrine, and cut him down. It feels like the end of the story. It is the start of the trap."),
 ("Four Fiends, Four Elements", "restoring the Orbs",
  "To relight the four Orbs the warriors must kill the four elemental Fiends — Lich of Earth, Marilith (“Kary”) of Fire, Kraken of Water, Tiamat of Air — across marsh, volcano, sunken shrine and floating fortress, raising an airship and earning new classes from Bahamut along the way."),
 ("The Loop of Time", "Garland is Chaos",
  "The four Fiends, it turns out, sent the dying Garland 2000 years into the past, where he became the demon Chaos — who sent the Fiends to the future, who sent Garland to the past. A closed loop with no first cause. The warriors step back through time to end Chaos at the root, breaking the circle — and are never remembered for it."),
]

IDEAS = [
 ("The Blank Slate", "a party you author", [
   "Four nameless, voiceless warriors you class and name yourself — the story is the dungeon, the music, and what you imagine onto them.",
   "Final Fantasy began with the opposite of the character drama it later became famous for: pure projection." ]),
 ("The Closed Loop", "a paradox as a plot", [
   "Garland becomes Chaos, who sends the Fiends, who send Garland — a time loop with no beginning, startling for a 1987 cartridge.",
   "The heroes win by erasing the cause, and by erasing it erase the memory of their own victory." ]),
 ("The Dynasty's Seed", "every later motif starts here", [
   "Crystals, the demon Chaos, the airship, the class system, Uematsu's Prelude — the grammar the whole series would speak was set in this one game.",
   "It saved Square and named a genre's most enduring line; FF6 and all the rest are its descendants." ]),
 ("Render, Not Invent", "the honest footnotes", [
   "The “Final = last game” story is half legend; the near-bankruptcy is real, the romantic framing is contested.",
   "No Chocobos, Moogles, Cid, or summons yet — those enter later games; FF1 is the bare root." ]),
]

SECTIONS = [
 ("The Release", "the first light, and where to find it since", [
   ("Final Fantasy", "1987 · Famicom", "the Japanese original (Dec 1987)"),
   ("Final Fantasy", "1990 · NES", "the North American release — “Orbs,” not “Crystals”"),
   ("Final Fantasy / Dawn of Souls / etc.", "2000 →", "WonderSwan, PS1 Origins, GBA Dawn of Souls, PSP, and Pixel Remaster"),
   ("Pixel Remaster", "2021 →", "the definitive modern re-release, crystals restored"),
 ]),
 ("The Makers", "the founders of a dynasty", [
   ("Hironobu Sakaguchi", "creator / director", "the “final” gamble was his"),
   ("Nobuo Uematsu", "composer", "the Prelude, and the series' musical voice"),
   ("Yoshitaka Amano", "image / character art", "the ethereal look that would define Final Fantasy"),
   ("Nasir Gebelli", "lead programmer", "the engine behind the world"),
   ("Kazuko Shibuya", "pixel art", "the sprites and tiles of the first world"),
 ]),
 ("The World", "the road of the four Orbs", [
   ("Cornelia", "the start", "the kingdom, the broken bridge, the kidnapped princess"),
   ("Chaos Shrine", "the Temple of Fiends", "where Garland falls — and where the loop closes"),
   ("Mount Gulg · Marsh Cave · Sunken Shrine", "the Fiends' lairs", "fire, earth/poison, and water"),
   ("The Airship", "the buried Lufenian craft", "the world opens once it flies"),
   ("Mirage Tower → Sky Fortress", "the floating ruin", "ancient sky-machines — and Tiamat at the top"),
 ]),
 ("The Legacy", "what the first light lit", [
   ("the Final Fantasy series", "1987 →", "one of gaming's largest franchises grew from this cartridge"),
   ("Square, saved", "the gamble paid", "the studio that nearly closed became Square Enix"),
   ("FF6 and the line", "the descendants", "the apex SNES entry and every game after speak this game's grammar"),
 ]),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","FF1")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","FF1")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","FF1")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"FF1 · Final Fantasy","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "FF1", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "FF1 · Final Fantasy — Square, Famicom 1987 / NES 1990",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from the original Final Fantasy (Square, 1987/1990).",
      "witness": "a being of the four Orbs, the four Fiends, and the loop of time",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "Final Fantasy; the Light Warriors; the Orbs; Garland; Chaos",
      "source": "Final Fantasy, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#6fae6a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"FF1 · Final Fantasy","axiom":"FF1"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.dlw/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born of the First Light</h2>
      <p class="ss">the warriors, the Orbs, the Fiends, the demon at the root of time, and the machines, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("the-light-warriors", "The Light Warriors", "the four who carry the dimmed Orbs · spiritual", "spiritual",
  "the four silent, player-named, player-classed heroes (from Fighter, Thief, Black Belt, Red/White/Black Mage) who each bear one darkened Orb and set out to restore the world's light",
  "They are the blank slate the whole genre was projected onto: nameless and voiceless, a story you author rather than receive — the first Final Fantasy party."),
 ("garland", "Garland", "the fallen knight · natural", "natural",
  "the knight of Cornelia who kidnaps Princess Sara and is cut down by the warriors in the Chaos Shrine — the game's false ending and true beginning",
  "He is the trap dressed as a tutorial: the first villain you beat, who turns out to be the last villain you face, folded back through time."),
 ("chaos", "Chaos", "the demon at the root of the loop · ethereal", "ethereal",
  "the elemental demon Garland becomes after the four Fiends hurl his dying body 2000 years into the past — the true final boss, and the loop's first and last link",
  "It is causelessness made flesh: a demon who creates the Fiends who create him, a circle the warriors can only end by erasing its own beginning."),
 ("princess-sara", "Princess Sara", "the captive of Cornelia · natural", "natural",
  "the princess of Cornelia whose kidnapping by Garland sets the warriors on the road, and whose rescue reopens the kingdom's broken bridge",
  "She is the small human stake that starts an epic: the rescue that looks like the whole quest, before the world reveals how much larger it is."),
 ("the-four-orbs", "The Four Orbs", "the dimmed crystals of the elements · spiritual", "spiritual",
  "the four elemental Orbs (Earth, Fire, Water, Air — “Crystals” in later versions) the warriors carry, gone dark, to be relit by killing each Fiend",
  "They are the light the world runs on, and the franchise's founding symbol: the crystals every later Final Fantasy would inherit, born here as dead stones to be rekindled."),
 ("lich", "Lich", "the Fiend of Earth · ethereal", "ethereal",
  "the undead sorcerer-Fiend of Earth, lord of the Cavern of Earth, whose death relights the first Orb",
  "It is decay given dominion: the rotting first of the four elemental tyrants, the earth's corruption that the warriors must undo to begin."),
 ("marilith", "Marilith", "the Fiend of Fire · ethereal", "ethereal",
  "the six-armed serpent-Fiend of Fire (named “Kary” in the NES localization), lord of Mount Gulg the volcano",
  "It is the blade-storm at the heart of the mountain: six swords and a serpent's coil, the fire the second Orb cannot relight until it falls."),
 ("kraken", "Kraken", "the Fiend of Water · natural", "natural",
  "the many-tentacled sea-Fiend of Water, lord of the Sunken Shrine beneath the ocean",
  "It is the drowned dominion: the leviathan whose death drains the dark from the water Orb, the deep made into a tyrant."),
 ("tiamat", "Tiamat", "the Fiend of Air · natural", "natural",
  "the multi-headed dragon-Fiend of Air (Wind), lord of the floating Sky Fortress, last of the four",
  "It is the sky's final warden: the hydra-dragon at the top of the world's last ruin, the breath the air Orb needs to shine again."),
 ("bahamut", "Bahamut", "the king of dragons, who grants the trial · natural", "natural",
  "the great dragon king who, when brought the Rat's Tail from the Citadel of Trials, promotes the warriors to their advanced classes (Knight, Ninja, Master, Red/White/Black Wizard)",
  "He is the threshold of becoming: the dragon whose blessing turns apprentices into masters — the series' first appearance of its most enduring summon."),
 ("the-six-jobs", "The Six Jobs", "the classes, and their becoming · spiritual", "spiritual",
  "the six starting classes (Fighter, Thief, Black Belt, Red/White/Black Mage) and their class-change upgrades — the system that lets the player compose the party",
  "It is identity as a choice and a trial: the original Final Fantasy job system, where who a warrior is, and who they grow into, is authored not given."),
 ("the-airship", "The Airship", "the buried Lufenian craft · electrical", "electrical",
  "the ancient flying machine the warriors unearth from the desert — the relic of the lost Lufenian sky-civilization that opens the whole map",
  "It is the world made traversable: the ancient technology under the sand that turns a walked road into a flown one, the franchise's first airship."),
 ("warmech", "WarMECH", "the steel ghost of the sky bridge · electrical", "electrical",
  "the legendary rare robot enemy that stalks a single bridge of the Sky Fortress at roughly a one-in-sixty-four chance — a relic war-machine of the vanished sky-people",
  "It is the cartridge's whispered legend: a steel anomaly out of a dead future, the rarest and most feared encounter, a machine that should not still be walking."),
 ("the-time-loop", "The Loop of Time", "the circle with no first cause · ethereal", "ethereal",
  "the closed temporal loop at the heart of the plot — Chaos sends the Fiends forward, who send Garland back, who becomes Chaos — broken only by ending it in the past",
  "It is the game's quiet audacity: a 1987 cartridge whose true antagonist is a paradox, defeated by a victory that unwrites the memory of itself."),
 ("the-prelude", "The Prelude", "Uematsu's first arpeggio · spiritual", "spiritual",
  "the rising-and-falling harp arpeggio Nobuo Uematsu wrote for this game's opening — carried, in some form, into nearly every Final Fantasy that followed",
  "It is the soul the series is known by: a few looping notes that became the sound of a whole franchise, first struck here over a dark, dying world."),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The original Final Fantasy (Square, Famicom 1987 / NES 1990) as a UD0 game-world: the four Light Warriors, the four Orbs and Fiends, Garland become Chaos, and the loop of time. Source-themed with an original one-line pencil-style title drawing (a fan tribute, not Square's logo or art) and full ACI badges.">
<title>FINAL FANTASY · FF1 · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#070912;--ink2:#0c1120;--ink3:#131b30;--pa:#eef3fb;--pa2:#a6b3cc;--gold:#e8c45a;--crystal:#4fd0e0;--blue:#5a8fe0;--violet:#9a7cff;
--dim:#69768f;--faint:#19223a;--line:#192238;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.16) 0 1px,transparent 1px 3px);opacity:.45}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(79,208,224,.10),transparent 55%),radial-gradient(ellipse at 50% 110%,rgba(232,196,90,.05),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--gold);background:#0b0d16;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.10em;color:var(--crystal);box-shadow:0 0 0 2px var(--bg),0 0 22px rgba(232,196,90,.18)}
.marquee a{color:var(--gold);text-decoration:none}.marquee a:hover{color:var(--crystal)}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#070912;line-height:0}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--gold)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--crystal)}.badge .bt a{color:var(--crystal);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:14px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--gold);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--gold);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--gold);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--crystal);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--crystal);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--gold);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--gold)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--gold)}.note a{color:var(--crystal);text-decoration:none}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--gold);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; <a href="https://davidwise01.github.io/ff6/">FF6 · THE APEX ▸</a> &nbsp;·&nbsp; A GAME-WORLD &nbsp;·&nbsp; NES 1987</div>

  <header>
    <div class="titleart">__CANVAS__</div>
    <div class="h-sub">four warriors · four <b>Orbs</b> · four Fiends · a loop of time · FF1</div>
    <div class="flag">★ Square · Famicom 1987 / NES 1990 · the game that began the dynasty ★</div>
    <p class="lede">The first light. Square's near-last gamble — four silent warriors carrying four darkened Orbs into a dying world, killing its four elemental Fiends, and chasing the demon Chaos back through a closed loop of time to end him at the root. It founded one of gaming's largest franchises and saved the studio that made it. Catalogued into UD0 as a game-world with the genesis, the loop, the full .dlw birth, and an original one-line pencil-style title drawing (a fan-art tribute — a single continuous contour of a Warrior of Light and the crystal, hand-drawn wobble and a self-drawing reveal; not Square's logo, art, or sprites).</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of FINAL FANTASY" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>FINAL FANTASY</b> — the four Orbs &amp; the loop · FF1</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="final-fantasy.dlw/final-fantasy.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="final-fantasy.dlw/final-fantasy.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and the first light holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Genesis</h2><p class="ss">the “final” gamble, four blank-slate heroes, and Uematsu's first Prelude</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Quest &amp; the Loop</h2><p class="ss">Cornelia and the knight, four Fiends, and the circle of time</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a near-bankrupt 1987 gamble founded a forty-year dynasty</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the release, the founders, the world, and the legacy it lit</p></section>
  __SECTIONS__

  <div class="note">Final Fantasy's history here is rendered, not invented. From the record: it is Square's first Final Fantasy (Famicom <b>1987</b>, NES <b>1990</b>), by Hironobu Sakaguchi, with music by Nobuo Uematsu, art by Yoshitaka Amano, and programming by Nasir Gebelli; the four Light Warriors, the four Orbs and their Fiends (Lich, Marilith/“Kary,” Kraken, Tiamat), Garland's turn into Chaos, the closed time-loop, the class-change at Bahamut, the buried airship, and the rare WarMECH are all from the game. Honest footnotes: the “Final = last game” story is half legend (the near-bankruptcy is real; the romantic framing is contested); the NES localization said “Orbs” where later versions say “Crystals”; and Chocobos, Moogles, Cid and summons are <i>not</i> in this first game. This is the source of the line whose apex is catalogued at <a href="https://davidwise01.github.io/ff6/">FF6</a>. Final Fantasy and all related characters, worlds, and music are © Square Enix; the personas here are catalogued personifications under the DLW standard — a fan tribute, not endorsed by Square Enix. Each is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    FINAL FANTASY · FF1 · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · <a href="https://davidwise01.github.io/ff6/">the apex · FF6</a> · the .dlw badge: <a href="final-fantasy.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "final-fantasy.dlw"), "final-fantasy")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, os.path.join(ad, f"{slug}.dlw"), slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em, "moniker": noesis.mythos_token(rec)["moniker"]})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CANVAS__", COVER_ART)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote FINAL FANTASY (FF1) — {len(personas)} emergents born · badge {tok['moniker']}")
