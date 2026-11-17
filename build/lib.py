# Shared builder for the Summit v5 mockup page.
# Every frame is generated from these helpers so sizes, tokens and icons stay consistent.
import re, html

import os as _os
LOGO = open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'ascend-logo.svg')).read()

_mark_counter = [0]
def _mark_svg(cls, viewbox, fill_override=None):
    """Inline the brand SVG (mark only — viewBox crop, wordmark groups stripped), ids suffixed per instance."""
    _mark_counter[0] += 1
    suffix = f"m{_mark_counter[0]}"
    t = LOGO
    for i in set(re.findall(r'id="([^"]+)"', t)):
        t = t.replace(f'id="{i}"', f'id="{i}{suffix}"').replace(f'url(#{i})', f'url(#{i}{suffix})')
    t = re.sub(r'<svg [^>]*>', f'<svg xmlns="http://www.w3.org/2000/svg" class="lg {cls}" viewBox="{viewbox}">', t, count=1)
    body_start = t.index('</defs>') + 7
    body = t[body_start:t.rindex('</svg>')]
    tops = []; pos = 0
    while True:
        m = re.search(r'<g\b', body[pos:])
        if not m: break
        st = pos + m.start(); d = 0; en = st
        for mm in re.finditer(r'<g\b[^>]*>|</g>', body[st:]):
            d += 1 if mm.group().startswith('<g') else -1
            if d == 0: en = st + mm.end(); break
        tops.append(body[st:en]); pos = en
    chev = tops[:3]
    chev = [c.replace('<g', f'<g class="c{i+1}"', 1) for i, c in enumerate(chev)]
    out = t[:body_start] + ''.join(chev) + '</svg>'
    if fill_override:
        out = re.sub(r'fill="#(545454|737373)"', f'fill="{fill_override}"', out)
    elif "shim" not in cls and "rev" not in cls:
        out = warm(out)
    return out, suffix

# v5.1 — on light surfaces the brand greys are swapped for their Summit
# neighbours (same map as Logo.tsx WARM). The brand file itself is untouched.
WARM = {"545454": "#3C362B", "737373": "#77705F", "a6a6a6": "#857D6A"}
def warm(svg):
    return re.sub(r'fill="#(545454|737373|a6a6a6)"', lambda m: f'fill="{WARM[m.group(1)]}"', svg)

def mark(width, cls="", light=True, opacity=1):
    """Static logo mark. light=True → brand greys (on paper/cream). light=False → chalk reversed variant."""
    svg, _ = _mark_svg(cls + ("" if light else " rev"), "81 92 213 123")
    return f'<div style="width:{width}px;flex:0 0 auto;opacity:{opacity}">{svg}</div>'

def mark_neutral(width):
    """The mark in the brand file's own greys — shown once, beside the warm one, for comparison."""
    svg, _ = _mark_svg("shim", "81 92 213 123")
    return f'<div style="width:{width}px;flex:0 0 auto">{svg}</div>'

def logo_full(width):
    """The full brand logo (mark + wordmark), verbatim, as data for <img>."""
    import base64
    b = base64.b64encode(warm(LOGO).encode()).decode()
    return f'<img src="data:image/svg+xml;base64,{b}" width="{width}" alt="Ascend — Your Digital Coach" style="display:block">'

def shimmer(width, dark=True, label=None, label_cls=None):
    """LogoShimmer: the logo mark with a soft band of light sweeping across it (1.6 s loop). Replaces ThreeDotPulse."""
    base, _ = _mark_svg("rev" if dark else "", "81 92 213 123")
    top, sfx = _mark_svg("shim", "81 92 213 123")
    grad = (f'<linearGradient id="shg{sfx}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="110" y2="0">'
            f'<stop offset="0" stop-color="{"#F7F3E9" if dark else "#FFFFFF"}" stop-opacity="0"/>'
            f'<stop offset=".5" stop-color="{"#F7F3E9" if dark else "#FFFFFF"}" stop-opacity="{".95" if dark else ".9"}"/>'
            f'<stop offset="1" stop-color="{"#F7F3E9" if dark else "#FFFFFF"}" stop-opacity="0"/>'
            f'<animateTransform attributeName="gradientTransform" type="translate" from="-60 0" to="320 0" dur="1.6s" repeatCount="indefinite"/>'
            f'</linearGradient>')
    top = top.replace('<defs>', '<defs>' + grad, 1)
    top = re.sub(r'fill="#(545454|737373)"', f'fill="url(#shg{sfx})"', top)
    lab = ''
    if label:
        lab = f'<div class="{label_cls or ("wait-dark" if dark else "wait-light")}">{html.escape(label)}</div>'
    return (f'<div style="display:flex;flex-direction:column;align-items:center"><div class="shimwrap" style="width:{width}px">'
            f'<div class="shimbase" style="opacity:{".42" if dark else ".55"}">{base}</div>'
            f'<div class="shimtop">{top}</div></div>{lab}</div>')

# ---------- icons: one 2 px round-stroke family, same hand as the logo chevron ----------
ICONS = {
    'chev-up': '<polyline points="5,15 12,8 19,15"/>',
    'chev-right': '<polyline points="9,5 16,12 9,19"/>',
    'chev-down': '<polyline points="5,9 12,16 19,9"/>',
    'chev-left': '<polyline points="15,5 8,12 15,19"/>',
    'check': '<polyline points="5,12.5 10,17.5 19,7"/>',
    'close': '<line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/>',
    'back': '<line x1="19" y1="12" x2="6" y2="12"/><polyline points="12,6 6,12 12,18"/>',
    'camera': '<rect x="3" y="7" width="18" height="13" rx="3"/><circle cx="12" cy="13.5" r="3.5"/><path d="M8 7l1.5-2.5h5L16 7"/>',
    'swap': '<polyline points="4,8 17,8"/><polyline points="14,5 17,8 14,11"/><polyline points="20,16 7,16"/><polyline points="10,13 7,16 10,19"/>',
    'share': '<path d="M12 15V4"/><polyline points="8,8 12,4 16,8"/><path d="M5 12v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/>',
    'info': '<circle cx="12" cy="12" r="9"/><line x1="12" y1="11" x2="12" y2="16.5"/><circle cx="12" cy="7.8" r=".9" fill="currentColor" stroke="none"/>',
    'plus': '<line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>',
    'minus': '<line x1="5" y1="12" x2="19" y2="12"/>',
    'list': '<line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="16" y2="12"/><line x1="4" y1="17" x2="12" y2="17"/>',
    'ring': '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.2"/>',
    'timer': '<circle cx="12" cy="13" r="7.5"/><line x1="12" y1="13" x2="12" y2="9"/><line x1="9.5" y1="3" x2="14.5" y2="3"/>',
    'upload': '<path d="M12 16V5"/><polyline points="8,9 12,5 16,9"/><path d="M4 17v2a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-2"/>',
    'play': '<path d="M8 6l10 6-10 6z" fill="currentColor" stroke="none"/>',
    'settings': '<circle cx="12" cy="12" r="3.2"/><path d="M19.5 9.7 L22.2 10.3 L22.2 13.7 L19.5 14.3 L19.0 15.7 L20.4 17.9 L17.9 20.4 L15.7 19.0 L14.3 19.5 L13.7 22.2 L10.3 22.2 L9.7 19.5 L8.3 19.0 L6.1 20.4 L3.6 17.9 L5.0 15.7 L4.5 14.3 L1.8 13.7 L1.8 10.3 L4.5 9.7 L5.0 8.3 L3.6 6.1 L6.1 3.6 L8.3 5.0 L9.7 4.5 L10.3 1.8 L13.7 1.8 L14.3 4.5 L15.7 5.0 L17.9 3.6 L20.4 6.1 L19.0 8.3 Z"/>',
    'cal-dot': '<rect x="4" y="5" width="16" height="15" rx="3"/><line x1="4" y1="10" x2="20" y2="10"/><line x1="8" y1="3" x2="8" y2="7"/><line x1="16" y1="3" x2="16" y2="7"/><circle cx="12" cy="15" r="1.6" fill="currentColor" stroke="none"/>',
    'cal-grid': '<rect x="4" y="5" width="16" height="15" rx="3"/><line x1="4" y1="10" x2="20" y2="10"/><line x1="8" y1="3" x2="8" y2="7"/><line x1="16" y1="3" x2="16" y2="7"/><line x1="8" y1="14" x2="10" y2="14"/><line x1="11" y1="14" x2="13" y2="14"/><line x1="14" y1="14" x2="16" y2="14"/><line x1="8" y1="17" x2="10" y2="17"/><line x1="11" y1="17" x2="13" y2="17"/>',
    'fork': '<path d="M7 3v6a2.5 2.5 0 0 0 5 0V3"/><line x1="9.5" y1="3" x2="9.5" y2="21"/><path d="M17 3c-1.7 1.2-2.5 3.5-2.5 6.5V12h2.5v9"/>',
    'cal': '<rect x="4" y="5" width="16" height="15" rx="3"/><line x1="4" y1="10" x2="20" y2="10"/><line x1="8" y1="3" x2="8" y2="7"/><line x1="16" y1="3" x2="16" y2="7"/>',
}
def ic(name, size=20, color="currentColor", sw=2, style=""):
    return (f'<svg class="ic" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="flex:0 0 auto;{style}">{ICONS[name]}</svg>')

def chev(color, w=20, sw=3):
    """The logo chevron as UI (progress language)."""
    h = w // 2
    return f'<svg viewBox="0 0 20 10" width="{w}" height="{h}" style="flex:0 0 auto"><polyline points="2,8 10,2 18,8" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def rail(step, total=8, dark=False):
    done = "#F7F3E9" if dark else "#211E19"; cur = "#A05257" if dark else "#5C262B"; ahead = "#3C362B" if dark else "#E0D7C3"
    cs = ''.join(chev(done if i < step - 1 else cur if i == step - 1 else ahead, 14, 2.6) for i in range(total))
    return (f'<div style="display:flex;flex-direction:column;align-items:flex-end;gap:5px">'
            f'<div style="display:flex;gap:5px">{cs}</div>'
            f'<div class="label-faint" style="font-size:10px">Step {step} of {total}</div></div>')

# ---------- phone + chrome ----------
def phone(inner, dark=False, time="21:41", screen_style="", homebar=True, bg=None):
    cls = "phone dark" if dark else "phone"
    st = f' style="background:{bg}"' if bg else ''
    return (f'<div class="{cls}"{st}><div class="notch"></div>'
            f'<div class="statusbar"><span>{time}</span><span class="sb-icons">{sbicons(dark)}</span></div>'
            f'<div class="screen" style="{screen_style}">{inner}</div>'
            f'{"<div class=homebar></div>" if homebar else ""}</div>')

def sbicons(dark):
    c = "#F7F3E9" if dark else "#211E19"
    return (f'<svg width="52" height="12" viewBox="0 0 52 12" fill="{c}"><rect x="0" y="7" width="3" height="5" rx="1"/><rect x="4.5" y="5" width="3" height="7" rx="1"/><rect x="9" y="3" width="3" height="9" rx="1"/><rect x="13.5" y="1" width="3" height="11" rx="1"/>'
            f'<path d="M24 4.2a7 7 0 0 1 9 0l-1.1 1.2a5.4 5.4 0 0 0-6.8 0zM26 6.7a4 4 0 0 1 5 0l-1.1 1.2a2.4 2.4 0 0 0-2.8 0zM28.5 9.3l1.2 1.3-1.2 1.3-1.2-1.3z"/>'
            f'<rect x="37" y="1.5" width="12" height="9" rx="2.5" fill="none" stroke="{c}" stroke-width="1"/><rect x="38.5" y="3" width="8" height="6" rx="1.2"/><rect x="50" y="4.5" width="1.5" height="3" rx=".7"/></svg>')

def frame(id, label, inner, note="", dark=False, time="21:41", screen_style="", bg=None, homebar=True):
    return (f'<div class="frame-wrap" id="{id}"><div class="frame-label"><b>{label.split(" · ",1)[0]}</b> · {label.split(" · ",1)[1] if " · " in label else ""}</div>'
            f'{phone(inner, dark, time, screen_style, homebar, bg)}'
            f'{f"<div class=frame-note>{note}</div>" if note else ""}</div>')

def tabbar(active, variant="final"):
    items = [("Today","chev-up","today"),("Coach","list","coach"),("Nutrition","ring","nutrition")]
    if variant == "final":
        # words only: caps labels, burgundy index above the active one, cream bar, hairline, 84 pt with room to breathe
        def tab(name, icon, key):
            on = key == active; col = "#211E19" if on else "#857D6A"
            idx = '<div style="width:26px;height:3px;border-radius:2px;background:#5C262B"></div>' if on else '<div style="height:3px"></div>'
            return f'<div class="tab" style="gap:11px;color:{col};font-size:11px;letter-spacing:.12em;font-weight:{700 if on else 600};justify-content:flex-start;padding-top:0">{idx}{name}</div>'
        return '<div class="tabbar" style="background:#FCF9F1;padding:0 12px 26px;height:84px">' + ''.join(tab(*i) for i in items) + '</div>'
    if variant == "classic":
        def tab(name, icon, key):
            on = key == active; col = "#5C262B" if on else "#857D6A"
            return f'<div class="tab{" on" if on else ""}">{ic(icon, 22, col, 2)}<span>{name}</span></div>'
        return '<div class="tabbar">' + ''.join(tab(*i) for i in items) + '</div>'
    if variant == "index":
        # refined classic: cream bar, hairline, a short burgundy index above the active icon, filled weight on the active label
        def tab(name, icon, key):
            on = key == active; col = "#211E19" if on else "#857D6A"
            idx = '<div style="width:26px;height:3px;border-radius:2px;background:#5C262B;margin-bottom:8px"></div>' if on else '<div style="height:11px"></div>'
            return f'<div class="tab{" on" if on else ""}" style="gap:5px">{idx}{ic(icon, 22, col, 2)}<span style="font-weight:{700 if on else 600}">{name}</span></div>'
        return '<div class="tabbar" style="background:#FCF9F1;padding-top:0;height:88px">' + ''.join(tab(*i) for i in items) + '</div>'
    if variant in ("text", "index2"):
        icons = {"today":"cal-dot","coach":"cal-grid","nutrition":"fork"}
        def tab(name, icon, key):
            on = key == active; col = "#211E19" if on else "#857D6A"
            idx = '<div style="width:26px;height:3px;border-radius:2px;background:#5C262B;margin-bottom:9px"></div>' if on else '<div style="height:12px"></div>'
            if variant == "text":
                return f'<div class="tab" style="gap:0;color:{col};text-transform:none;letter-spacing:-0.01em;font-size:15px;font-weight:{700 if on else 600};font-family:var(--display)">{idx}{name}</div>'
            return f'<div class="tab" style="gap:5px;color:{col}">{idx}{ic(icons[key], 22, col, 1.6)}<span style="font-weight:{700 if on else 600}">{name}</span></div>'
        h = "76px" if variant == "text" else "88px"
        return f'<div class="tabbar" style="background:#FCF9F1;padding-top:0;height:{h}">' + ''.join(tab(*i) for i in items) + '</div>'
    if variant == "slab":
        # the strap under the dial: an espresso bar rising from the bottom, chalk icons, burgundy-lt index on the active tab
        def tab(name, icon, key):
            on = key == active; col = "#F7F3E9" if on else "#8E8572"
            idx = '<div style="width:26px;height:3px;border-radius:2px;background:#A05257;margin-bottom:8px"></div>' if on else '<div style="height:11px"></div>'
            return f'<div class="tab" style="gap:5px;color:{col}">{idx}{ic(icon, 22, col, 2)}<span style="font-weight:{700 if on else 600}">{name}</span></div>'
        return '<div class="tabbar" style="background:#211E19;border:none;border-radius:24px 24px 0 0;padding:0 12px 26px;height:90px;box-shadow:0 -10px 30px rgba(33,30,25,.12)">' + ''.join(tab(*i) for i in items) + '</div>'
    if variant == "dock":
        # floating espresso capsule, inset 16, active tab on a chalk chip
        def tab(name, icon, key):
            on = key == active
            if on:
                return f'<div style="flex:1;display:flex;align-items:center;justify-content:center;gap:8px;height:48px;border-radius:24px;background:#F7F3E9;color:#211E19;font-size:12px;font-weight:700;letter-spacing:.04em;text-transform:uppercase">{ic(icon, 20, "#211E19", 2)}{name}</div>'
            return f'<div style="flex:1;display:flex;align-items:center;justify-content:center;height:48px;color:#8E8572">{ic(icon, 22, "#8E8572", 2)}</div>'
        return ('<div style="flex:0 0 auto;padding:10px 0 28px"><div style="display:flex;gap:4px;padding:6px;background:#211E19;border-radius:30px;box-shadow:0 14px 34px rgba(33,30,25,.28)">' + ''.join(tab(*i) for i in items) + '</div></div>')

def header(date, title, dark=False, right=None):
    r = right or ''
    return (f'<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:2px">'
            f'<div><div class="label-faint">{date}</div><div class="title display" style="margin-top:4px">{title}</div></div>{r}</div>')

def settings_link():
    # a 40 pt cream disc with a hairline and a 22 pt cog — a button, not a glyph
    return f'<div style="width:40px;height:40px;border-radius:20px;background:#FCF9F1;border:1px solid #E0D7C3;display:flex;align-items:center;justify-content:center;margin-bottom:4px">{ic("settings", 22, "#211E19", 1.8)}</div>'

def btn(label, variant="burgundy", h=58, fs=16, extra="", icon=None, busy=False):
    icon_html = icon or ''
    return f'<div class="btn btn-{variant}{" busy" if busy else ""}" style="height:{h}px;font-size:{fs}px;{extra}">{icon_html}{label}</div>'

def card(inner, style=""):
    return f'<div class="card" style="{style}">{inner}</div>'

def slab(inner, style="padding:24px"):
    return f'<div class="slab lift" style="{style}">{inner}</div>'

def trend(points, w=64, h=14):
    """TrendLine: where a training max has been this block. points = [(t 0..1, kg)]. Level bone line when held;
    espresso line ending in a burgundy dot when it moved. Mirrors src/components/ui/TrendLine.tsx."""
    pad = 3
    kgs = [k for _, k in points]; lo, hi = min(kgs), max(kgs); flat = hi == lo
    x = lambda t: pad + max(0, min(1, t)) * (w - pad * 2)
    y = lambda k: h / 2 if flat else h - pad - (k - lo) / (hi - lo) * (h - pad * 2)
    pts = ' '.join(f'{x(t):.1f},{y(k):.1f}' for t, k in points)
    dot = '' if flat else f'<circle cx="{x(points[-1][0]):.1f}" cy="{y(points[-1][1]):.1f}" r="2.5" fill="#5C262B"/>'
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display:block"><polyline points="{pts}" fill="none" '
            f'stroke="{"#E0D7C3" if flat else "#211E19"}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>{dot}</svg>')

def settle(inner, i=0, reveal=False, style=""):
    """Settle / Reveal as drawn on the page: fade in and rise once. i = position in a staggered group."""
    step = 80 if reveal else 50
    return f'<div class="{"reveal" if reveal else "settle"}" style="animation-delay:{i*step}ms;{style}">{inner}</div>'

def pill(label, on=False, dark=False, style=""):
    cls = "pill" + (" pill-dark" if dark else "") + (" on" if on else "")
    return f'<div class="{cls}" style="{style}">{label}</div>'

def role(tag, ondark=False, h=24, fs=10):
    cls = {"ME": "role-me", "DE": "role-de", "RE": "role-re"}[tag]
    if ondark: cls = "role-de-ondark"
    return f'<span class="role-tag {cls}" style="height:{h}px;font-size:{fs}px">{tag}</span>'

def stepper(sign, size=54, dark=False):
    cls = "stepper" + (" stepper-dark" if dark else "")
    col = "#F7F3E9" if dark else "#211E19"
    return f'<div class="{cls}" style="width:{size}px;height:{size}px;border-radius:{round(size*0.3)}px">{ic("plus" if sign=="+" else "minus", round(size*0.44), col, 2)}</div>'

def seg(states, dark=True):
    out = []
    for s in states:
        cls = "seg" + (" seg-dark" if dark else "") + (" done" if s == "d" else " now" if s == "n" else "")
        out.append(f'<div class="{cls}"></div>')
    return '<div style="display:flex;gap:5px">' + ''.join(out) + '</div>'

def hr(dark=False): return f'<hr class="{"hr-dark" if dark else "hr"}">'

def back(label, dark=False):
    col = "#A09580" if dark else "#77705F"
    return f'<div style="display:flex;align-items:center;gap:6px;font-size:15px;color:{col};font-weight:600">{ic("back", 18, col, 2)}{label}</div>'

def closex(dark=True):
    return ic("close", 22, "#A09580" if dark else "#77705F", 2)

def sheet(inner, dark=True, pad="22px 24px 36px"):
    bg = "#2E2922" if dark else "#FCF9F1"; line = "#3C362B" if dark else "#E0D7C3"; handle = "#4A4338" if dark else "#D4CAB5"
    return (f'<div style="position:absolute;left:0;right:0;bottom:0;background:{bg};border:1px solid {line};border-bottom:none;border-radius:20px 20px 0 0;padding:{pad};display:flex;flex-direction:column;gap:14px">'
            f'<div style="width:36px;height:4px;border-radius:2px;background:{handle};align-self:center;margin:-10px 0 2px"></div>{inner}</div>')

def backdrop(): return '<div style="position:absolute;inset:0;background:rgba(14,13,12,.6)"></div>'

def sheet_head(kicker, title, dark=True):
    return (f'<div><div class="{"label-dark" if dark else "label-faint"}" style="margin-bottom:6px">{kicker}</div>'
            f'<div class="display" style="font-size:22px;font-weight:700;color:{"#F7F3E9" if dark else "#211E19"};line-height:1.15">{title}</div></div>')

def gym_pill(label, icon):
    return f'<div class="gympill">{ic(icon, 16, "#A09580", 2)}{label}</div>'

def fact(k, v, d, size=30):
    det = f'<div class="d">{d}</div>' if d else ''
    return f'<div class="fact"><div class="k">{k}</div><div class="v display" style="font-size:{size}px">{v}</div>{det}</div>'

def section(id, title, lede, frames):
    return (f'<div class="section" id="{id}"><h2 class="display">{title}</h2><p class="lede">{lede}</p>'
            f'<div class="flow">{"".join(frames)}</div></div>')
