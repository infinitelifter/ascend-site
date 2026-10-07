from lib import *

def shell(label): return f'<div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><div class="label-dark">{label}</div>{closex()}</div>'

def corners():
    c = 'width:26px;height:26px;position:absolute;opacity:.7;'
    return (f'<div style="{c}top:14px;left:14px;border-top:2px solid var(--chalk);border-left:2px solid var(--chalk);border-radius:4px 0 0 0"></div>'
            f'<div style="{c}top:14px;right:14px;border-top:2px solid var(--chalk);border-right:2px solid var(--chalk);border-radius:0 4px 0 0"></div>'
            f'<div style="{c}bottom:14px;left:14px;border-bottom:2px solid var(--chalk);border-left:2px solid var(--chalk);border-radius:0 0 0 4px"></div>'
            f'<div style="{c}bottom:14px;right:14px;border-bottom:2px solid var(--chalk);border-right:2px solid var(--chalk);border-radius:0 0 4px 0"></div>')

def viewport(inner, counter="0:00 / 0:15", rec=False):
    dot = "var(--burgundy-lt)" if rec else "var(--darkline)"
    return (f'<div style="flex:1;background:linear-gradient(160deg,#17140F 0%,#0D0B08 100%);border:1px solid var(--darkline);border-radius:20px;position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden">{corners()}{inner}'
            f'<div style="position:absolute;top:14px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:7px;background:rgba(33,30,25,.85);border-radius:14px;padding:5px 12px"><div style="width:7px;height:7px;border-radius:50%;background:{dot}"></div><div class="num" style="font-size:12px;font-weight:700;color:var(--chalk)">{counter}</div></div></div>')

def controls(delay="off", counting=False, dim=False):
    on = delay != "off"
    d = f'<div style="display:flex;align-items:center;gap:6px;border:1px solid {"var(--chalk)" if on else "var(--darkline)"};border-radius:14px;padding:6px 12px;font-size:12px;font-weight:700;color:{"var(--chalk)" if on else "var(--dlabel)"};{"opacity:.4" if dim else ""}">{ic("timer",14,"#F7F3E9" if on else "#A09580",2)}{delay}</div>'
    inner = ('<div style="width:30px;height:30px;border-radius:8px;background:var(--darkline)"></div>' if counting else '<div style="width:56px;height:56px;border-radius:50%;background:var(--burgundy-lt)"></div>')
    return (f'<div style="display:flex;align-items:center;justify-content:center;gap:26px;padding:6px 0 30px"><div style="width:76px;display:flex;justify-content:center">{d}</div>'
            f'<div style="width:76px;height:76px;border-radius:50%;border:3px solid var(--chalk);display:flex;align-items:center;justify-content:center">{inner}</div>'
            f'<div style="width:76px;display:flex;justify-content:center"><div style="display:flex;align-items:center;gap:6px;border:1px solid var(--darkline);border-radius:14px;padding:6px 12px;font-size:12px;font-weight:700;color:var(--dlabel);{"opacity:.4" if dim else ""}">{ic("upload",14,"#A09580",2)}Upload</div></div></div>')

def thumb(): return f'<div style="height:118px;background:linear-gradient(160deg,#17140F 0%,#0D0B08 100%);border:1px solid var(--darkline);border-radius:16px;display:flex;align-items:center;justify-content:center;flex:0 0 auto"><div style="width:40px;height:40px;border:1.5px solid var(--dlabel);border-radius:50%;display:flex;align-items:center;justify-content:center">{ic("play",16,"#F7F3E9")}</div></div>'

def verdict(headline, summary, color="var(--burgundy-lt)", quality=None):
    q = f'<span class="tag" style="height:26px">{quality}</span>' if quality else ''
    return (f'<div class="sootcard" style="border:1.5px solid var(--burgundy-lt);padding:16px 18px"><div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:6px"><div class="display" style="font-size:22px;font-weight:700;color:{color};line-height:1.15">{headline}</div>{q}</div><div style="font-size:13px;color:var(--dbody);line-height:1.5">{summary}</div></div>')

def finding(area, sev, detail, last=False):
    col = "var(--burgundy-lt)" if sev in ("MODERATE","SEVERE") else "var(--dlabel)"
    return (f'<div style="padding:11px 0;{"" if last else "border-bottom:1px solid var(--darkline)"}"><div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><div style="font-size:14px;font-weight:600;color:var(--chalk)">{area}</div><div style="font-size:11px;color:{col};font-weight:700;letter-spacing:.06em">{sev}</div></div><div style="font-size:12px;color:var(--dlabel);line-height:1.45;margin-top:3px">{detail}</div></div>')

def frames():
    F = []
    hdr = "Form check · SSB Box Squat · Set 3"
    instr = (f'<div style="text-align:center;padding:0 40px"><div style="width:44px;height:44px;border:1.5px solid var(--dlabel);border-radius:12px;margin:0 auto 14px;display:flex;align-items:center;justify-content:center">{ic("camera",20,"#A09580",1.8)}</div>'
             f'<div style="font-size:15px;font-weight:600;color:var(--chalk);margin-bottom:6px">Film from the side, hip height, whole torso and box in frame.</div>'
             f'<div style="font-size:12px;color:var(--dlabel);line-height:1.5">Prop the phone at hip height, 3–4 m away.<br>Recording stops automatically at 15 s.<br>Set a delay to get in position, or upload a filmed set.</div></div>')
    F.append(frame("s13", "13 · Form check — record",
        shell(hdr) + viewport(instr) + controls(),
        "As built, with icons in the pills (timer, upload) instead of ⏱ and ↑ glyphs. The exercise's own angle hint leads the instructions.", dark=True, screen_style="gap:16px;padding-top:16px"))
    F.append(frame("s13b", "13b · Form check — start-delay countdown",
        shell(hdr) + viewport(f'<div style="text-align:center"><div class="display" style="font-size:96px;font-weight:700;color:var(--chalk);line-height:1">12</div><div style="font-size:12px;color:var(--dlabel);margin-top:4px">Recording starts — get set</div></div>') + controls("15 s", True, True),
        "Countdown numeral in the display face at 96, readable from the bar. Shutter shows the cancel square.", dark=True, screen_style="gap:16px;padding-top:16px"))
    F.append(frame("s13c", "13c · Form check — upload chooser",
        shell(hdr) + viewport(instr) + controls() + backdrop() +
        sheet('<div class="label-dark">Upload clip</div>' + hr(True) +
              '<div style="padding:4px 0;display:flex;flex-direction:column;gap:3px"><div style="font-size:16px;font-weight:600;color:var(--chalk)">Photo library</div><div style="font-size:12px;color:var(--dlabel)">Trim to 15 s in the system editor</div></div>' + hr(True) +
              '<div style="padding:4px 0;display:flex;flex-direction:column;gap:3px"><div style="font-size:16px;font-weight:600;color:var(--chalk)">Files</div><div style="font-size:12px;color:var(--dlabel)">Video files up to 15 s</div></div>'),
        "The chooser that used to be unstyled: a Summit sheet with two rows and the handle. Picker launches after the sheet has closed (the iOS constraint found on 25 Sep).", dark=True, screen_style="gap:16px;padding-top:16px"))
    F.append(frame("s13t", "13t · Form check — trim (iOS system editor)",
        '<div style="display:flex;justify-content:space-between;align-items:center;font-size:15px;padding-top:4px"><div style="color:#FFCC00;font-weight:600">Cancel</div><div style="color:#8D877B;font-size:12px">Trim — 0:15 max</div><div style="color:#FFCC00;font-weight:700">Done</div></div>'
        f'<div style="flex:1;background:linear-gradient(160deg,#17140F 0%,#0D0B08 100%);border-radius:8px;display:flex;align-items:center;justify-content:center"><div style="width:44px;height:44px;border-radius:22px;border:1.5px solid #A09580;display:flex;align-items:center;justify-content:center">{ic("play",16,"#EDE7DA")}</div></div>'
        '<div style="height:52px;border-radius:8px;position:relative;display:flex;padding:0 22px;margin-bottom:26px"><div style="position:absolute;inset:0;border-radius:8px;background:repeating-linear-gradient(90deg,#26221B 0 34px,#1B1813 34px 35px);opacity:.9"></div><div style="position:absolute;top:0;bottom:0;left:96px;right:64px;border:3px solid #FFCC00;border-radius:8px"></div><div style="position:absolute;top:0;bottom:0;left:88px;width:16px;background:#FFCC00;border-radius:8px 0 0 8px"></div><div style="position:absolute;top:0;bottom:0;right:56px;width:16px;background:#FFCC00;border-radius:0 8px 8px 0"></div></div>',
        "<b>System UI, not ours — kept as is.</b> Photo-library picks route through Apple's trim editor with the selection hard-capped at 15 s; the yellow handles are iOS's. Files picks longer than 15 s get one factual line asking for a shorter clip. Done → watching your lift.", dark=True, screen_style="gap:14px;padding-top:12px;background:#000", bg="#000"))
    F.append(frame("s13d", "13d · Form check — watching your lift",
        shell(hdr) + f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center">{shimmer(120, True, "Watching your lift")}</div>',
        "The longest wait in the app (10–15 s). Logo loader, no ellipsis. The × still cancels and goes back to the set.", dark=True, screen_style="gap:16px;padding-top:16px;padding-bottom:40px"))
    F.append(frame("s14", "14 · Form check — result",
        shell(hdr) + thumb() + verdict("Watch the right knee","Solid depth and bar path. Right knee caves slightly on the ascent — worth attention before the weight climbs.", "var(--burgundy-lt)", "Clear view") +
        f'<div><div class="label-dark" style="margin-bottom:4px">Findings</div>{finding("Knee tracking","MODERATE","Right knee drifts inward through the sticking point on reps 3–5.")}{finding("Bar path","MINOR","Slight forward drift out of the hole, corrects by mid-rep.")}{finding("Depth","GOOD","Box touched under control every rep.",True)}</div>'
        f'<div><div class="label-dark" style="margin-bottom:8px">Cues for next set</div><div style="font-size:14px;color:var(--dbody);line-height:1.8">— Drive knees out hard at the hole<br>— Push the ground apart</div></div>'
        f'<div style="flex:1"></div><div style="display:flex;flex-direction:column;gap:10px;margin-bottom:30px">{btn("Back to set","chalk")}<div style="display:flex;gap:10px"><div style="flex:1">{btn("Record again","ghostDark",48,14)}</div><div style="flex:1">{btn("Share card","ghostDark",48,14,icon=ic("share",16,"#F7F3E9",2))}</div></div></div>',
        "<b>Two changes.</b> “78% confident” becomes a view-quality tag — <b>Clear view</b> (≥ 0.75) · <b>Partial view</b> (0.45–0.75) · <b>Poor angle</b> (&lt; 0.45) — a percentage invited argument; the words say what to do about it. Findings show their one-line detail (the model returns it; the screen was dropping it). Headline in the display face.", dark=True, screen_style="gap:14px;padding-top:16px"))
    F.append(frame("s14b", "14b · Form check — wrong exercise on film",
        shell("Form check · Front Squat · Set 2") + thumb() + verdict("That's not a front squat","The clip shows a machine hack squat.") +
        '<div style="flex:1"></div><div style="font-size:13px;color:var(--dlabel);line-height:1.5">Form check reads the main barbell lifts — squat, bench, deadlift and press families. Other movements open their instruction sheet from the exercise name.</div>'
        f'<div style="display:flex;flex-direction:column;gap:10px;margin-bottom:30px">{btn("Back to set","chalk")}{btn("Record again","ghostDark",48,14)}</div>',
        "As built (3 Oct). When the clip shows a catalog lift, a chalk “Check as close grip bench” leads and Back to set drops to ghost.", dark=True, screen_style="gap:14px;padding-top:16px"))
    F.append(frame("s14c", "14c · Form check — couldn't analyze",
        shell(hdr) + thumb() + verdict("Couldn't analyze this clip","The analysis didn't complete. Nothing was saved — try again.") +
        f'<div style="flex:1"></div><div style="display:flex;flex-direction:column;gap:10px;margin-bottom:30px">{btn("Try again","chalk")}{btn("Back to set","ghostDark",48,14)}</div>',
        "The failure state gets a real retry on the same clip (it only offered Record again). Offline gets its own line: “You're offline — the clip stays on this phone; try again when you're back.”", dark=True, screen_style="gap:14px;padding-top:16px"))
    return F
