from lib import *
import re

def gym_header(session, pos, back_=True):
    b = ic("chev-left", 22, "#A09580", 2) if back_ else ''
    return f'<div style="display:flex;justify-content:space-between;align-items:center"><div style="display:flex;align-items:center;gap:10px">{b}<div class="label-dark num">{session} · {pos}</div></div>{closex()}</div>'

def name_row(name, cue, form=True, amrap=False):
    tag = f'<span class="role-tag role-me" style="height:28px;font-size:11px">AMRAP</span>' if amrap else ''
    pills = (f'<div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">{gym_pill("Form","camera") if form else ""}{gym_pill("Swap","swap")}{gym_pill("","info").replace("gap:7px","")}<span class="tag">{cue}</span></div>')
    return (f'<div style="display:flex;flex-direction:column;gap:12px"><div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px"><div class="display" style="font-size:28px;font-weight:700;line-height:1.1">{name}</div>{tag}</div>{pills}</div>')

def weight_card(value, lb, size=96, color="var(--chalk)", border=None, sub=None):
    if size == 96 and len(re.sub('<[^>]+>','',value)) >= 5: size = 80
    b = f'border:1.5px solid {border};' if border else ''
    s = sub or f'<div class="num" style="font-size:13px;color:var(--dlabel);margin-top:6px;font-weight:600">kg · {lb} lb</div>'
    return (f'<div class="sootcard" style="{b}padding:22px 18px;display:flex;align-items:center;justify-content:space-between">{stepper("-",64,True)}'
            f'<div style="text-align:center"><div class="display" style="font-size:{size}px;font-weight:700;line-height:.95;color:{color}">{value}</div>{s}</div>{stepper("+",64,True)}</div>')

def reps_card(value, label="Reps"):
    return (f'<div class="sootcard" style="padding:12px 16px;display:flex;align-items:center;justify-content:space-between"><div class="label-dark">{label}</div>'
            f'<div style="display:flex;align-items:center;gap:14px">{stepper("-",48,True)}<div class="display" style="font-size:44px;font-weight:700;width:64px;text-align:center;line-height:1">{value}</div>{stepper("+",48,True)}</div></div>')

def quality(sel="Solid"):
    return (f'<div><div class="label-dark" style="margin-bottom:8px">How did it move?</div><div style="display:flex;gap:8px">' +
            ''.join(pill(q, q == sel, True, "flex:1;height:46px;font-size:15px;border-radius:23px") for q in ["Easy","Solid","Grind"]) + '</div></div>')

def prev(text): return f'<div class="meta-dark num" style="text-align:center">{text}</div>'

def footer(primary, secondary=None, ph=68):
    s = btn(secondary, "ghostDark", 44, 14) if secondary else ''
    return f'<div style="flex:1"></div><div style="display:flex;flex-direction:column;gap:10px;margin-bottom:30px">{btn(primary,"chalk",ph,17)}{s}</div>'

def frames():
    F = []
    # 08 straight set
    F.append(frame("s8", "08 · Session — straight set (gym mode)",
        gym_header("Max Effort Lower","1/5",False) + name_row("SSB Box Squat","Load over reps") + seg("dn-") +
        '<div class="meta-dark num" style="text-align:center">Set 2 of 3</div>' + weight_card("165","364") + reps_card("5") + quality() +
        prev("Set 1 · 152.5 kg · 336 lb × 5 · solid") + footer("Log set","Skip"),
        "<b>Gym mode says less.</b> Weight 64 → 96 pt in the display face; steppers 54 → 64 pt (the most-tapped control); reps 30 → 44 with 48 pt steppers; quality pills 38 → 46 pt; Log set 58 → 68 pt. What left: the 12 pt priority cue under the name is now a tag in the pill row; the set's coaching note lives behind the ⓘ pill (and shows itself once, on set 1 of a new exercise); the caps sentence under the strip is sentence case and loses the “tap a done segment to edit” hint — done segments are now visibly thicker than ahead ones. Prev becomes one quiet centred line and gains lb.", dark=True, screen_style="gap:14px;padding-top:16px"))

    # 08b first set — note shown once
    F.append(frame("s8b", "08b · Session — set 1, the note shows itself once",
        gym_header("Max Effort Lower","1/5",False) + name_row("SSB Box Squat","Load over reps") +
        f'<div class="sootcard" style="padding:12px 14px;display:flex;gap:10px;align-items:flex-start">{ic("info",16,"#A09580",2,"margin-top:1px")}<div class="meta-dark" style="flex:1">Work up to today’s true 5-rep max. Everything before it is setup.</div>{ic("close",16,"#A09580",2)}</div>'
        + seg("n--") + '<div class="meta-dark num" style="text-align:center">Set 1 of 3</div>' + weight_card("150","331") + reps_card("5") + quality() + footer("Log set","Skip"),
        "On set 1 of an exercise the note renders as a dismissible row under the pills; from set 2 it is behind ⓘ. Warm-up ramp (when present) stays as the collapsed soot card above the strip, as built.", dark=True, screen_style="gap:14px;padding-top:16px"))

    # 09 top set
    F.append(frame("s9", "09 · Session — top set (max effort, true rep max)",
        gym_header("Max Effort Lower","1/5",False) + name_row("SSB Box Squat","Load over reps",True,True) + seg("ddn") +
        '<div class="meta-dark num" style="text-align:center">Set 3 of 3 · Top set · today’s 5-rep max</div>'
        + f'<div class="sootcard" style="padding:12px 16px;display:flex;align-items:center;justify-content:space-between"><div class="label-dark">Bar</div><div style="display:flex;align-items:center;gap:14px">{stepper("-",48,True)}<div style="text-align:center;width:84px"><div class="display" style="font-size:30px;font-weight:700;line-height:1">180</div><div class="num" style="font-size:11px;color:var(--dlabel);font-weight:600">kg · 397 lb</div></div>{stepper("+",48,True)}</div></div>'
        + weight_card("5","",96,"var(--burgundy-lt)","var(--burgundy-lt)",'<div class="label-dark" style="margin-top:8px">Reps achieved</div>')
        + '<div class="meta-dark" style="text-align:center">Your best set today sets the next training max.</div>' + quality()
        + prev("Set 2 · 165 kg · 364 lb × 5 · solid") + footer("Log top set — complete exercise","Skip"),
        "Same grammar as 08. Burgundy is spent on the reps numeral — the one moment of fire. The bar card is editable (the lifter logs what went on the bar). The “Beat” caps label goes; the sentence stands alone. <b>Parity fixes:</b> the top-set branch gains the Prev line, the Skip action and the success hairline it was missing.", dark=True, screen_style="gap:14px;padding-top:16px"))

    # 09b reps vs target
    F.append(frame("s9b", "09b · Session — top set, reps-vs-target variant",
        gym_header("Lower A","1/4",False) + name_row("Back Squat","Technique over load",True,True) + seg("ddddn") +
        '<div class="meta-dark num" style="text-align:center">Set 5 of 5 · Top set · target 3+ reps</div>'
        + f'<div class="sootcard" style="padding:14px 16px;display:flex;align-items:center;justify-content:space-between"><div class="label-dark">Bar</div><div class="display" style="font-size:30px;font-weight:700;line-height:1">142.5 <span class="num" style="font-size:13px;color:var(--dlabel);font-weight:600;font-family:var(--body)">kg · 314 lb</span></div></div>'
        + weight_card("3","",96,"var(--burgundy-lt)","var(--burgundy-lt)",'<div class="label-dark" style="margin-top:8px">Reps achieved</div>')
        + '<div class="meta-dark" style="text-align:center">Target + 3 reps moves your training max up.</div>' + quality()
        + footer("Log top set — complete session","Couldn't hit the target"),
        "Linear and hypertrophy probes: the bar is read-only, the ghost action logs an honest miss and lets the engine cut. The engine's “rep floor” never appears — the UI says target.", dark=True, screen_style="gap:14px;padding-top:16px"))

    # 15 carry
    F.append(frame("s15", "15 · Session — carry / distance",
        gym_header("Max Effort Lower","5/5") + name_row("Farmer Carry","Reps over load",False) + seg("dn-") +
        '<div class="meta-dark num" style="text-align:center">Carry 2 of 3</div>'
        + f'<div class="sootcard" style="padding:12px 16px;display:flex;align-items:center;justify-content:space-between"><div class="label-dark">Per hand</div><div style="display:flex;align-items:center;gap:14px">{stepper("-",48,True)}<div style="text-align:center;width:84px"><div class="display" style="font-size:30px;font-weight:700;line-height:1">60</div><div class="num" style="font-size:11px;color:var(--dlabel);font-weight:600">kg · 132 lb</div></div>{stepper("+",48,True)}</div></div>'
        + weight_card('30<span style="font-size:30px;color:var(--dlabel);font-weight:600"> m</span>',"",96,"var(--chalk)",None,'<div class="label-dark" style="margin-top:6px">Distance</div>')
        + quality() + prev("Carry 1 · 60 kg · 30 m · solid") + footer("Log carry","Skip"),
        "Same screen, different inputs. The per-hand card hides when the prescription has no load (it showed “0 · kg · 0 lb”). No Form pill — carries are not in the form-check catalog.", dark=True, screen_style="gap:14px;padding-top:16px"))

    # 15b hold
    F.append(frame("s15b", "15b · Session — timed hold",
        gym_header("Repetition Upper","4/5") + name_row("Dead Hang","Range over load",False) + seg("n--") +
        '<div class="meta-dark num" style="text-align:center">Hold 1 of 3 · target 30 s</div>'
        + f'<div class="sootcard" style="padding:22px 18px;display:flex;flex-direction:column;align-items:center;gap:14px"><div class="display" style="font-size:96px;font-weight:700;line-height:.95">32<span style="font-size:30px;color:var(--dlabel);font-weight:600"> s</span></div><div style="display:flex;gap:10px;align-self:stretch"><div style="flex:1">{btn("Stop","ghostDark",48,14)}</div>{stepper("-",48,True)}{stepper("+",48,True)}</div></div>'
        + quality() + footer("Log hold","Skip"),
        "The target seconds now show on the screen (they never did). Timer counts up; a light haptic marks the target. Load card (when loaded) gains its lb secondary.", dark=True, screen_style="gap:14px;padding-top:16px"))

    # 08e edit mode
    F.append(frame("s8e", "08e · Session — editing a logged set",
        gym_header("Max Effort Lower","1/5",False) + name_row("SSB Box Squat","Load over reps") + seg("nd-") +
        '<div class="meta-dark num" style="text-align:center">Editing set 1 of 3</div>' + weight_card("152.5","336") + reps_card("5") + quality() + footer("Save set","Cancel edit"),
        "Tap a chalk segment → that set opens pre-filled. The position line says “Editing”. Save updates the same row; Cancel restores where you were. As built, re-dressed.", dark=True, screen_style="gap:14px;padding-top:16px"))

    # 08d loading / 08f error
    F.append(frame("s8d", "08d · Session — loading",
        f'<div style="display:flex;justify-content:space-between;align-items:center"><div class="label-dark">Session</div>{closex()}</div><div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center">{shimmer(120, True, "Loading session")}</div>',
        "The logo loader on espresso: chalk reversed mark at 42% with the band of light crossing it.", dark=True, screen_style="gap:14px;padding-top:16px;padding-bottom:40px"))
    F.append(frame("s8f", "08f · Session — didn't load (offline, not cached)",
        f'<div style="display:flex;justify-content:space-between;align-items:center"><div class="label-dark">Session</div>{closex()}</div><div style="flex:1;display:flex;flex-direction:column;justify-content:center">'
        f'<div class="sootcard" style="border-radius:18px;padding:18px 20px;display:flex;flex-direction:column;gap:6px"><div style="font-size:14px;font-weight:600;color:var(--burgundy-lt);line-height:1.5">You’re offline and this session isn’t cached. Open it once with a connection — after that, logging works fully offline.</div><div style="font-size:13px;font-weight:700;margin-top:6px">Try again</div></div></div>',
        "Dark ErrorCard as built; the copy is already right.", dark=True, screen_style="gap:14px;padding-top:16px;padding-bottom:40px"))

    # 16 feedback sheet
    dim = (f'<div style="padding:0 24px;opacity:.35;display:flex;flex-direction:column;gap:16px">{gym_header("Max Effort Lower","5/5")}<div class="display" style="font-size:28px;font-weight:700">Farmer Carry</div>{seg("ddd")}</div>')
    F.append(frame("s16", "16 · Session complete — feedback sheet",
        dim + sheet(sheet_head("Session logged.","Anything to flag?") + hr(True) +
            f'<div style="display:flex;gap:8px">{pill("Strong",True,True,"flex:1")}{pill("Normal",False,True,"flex:1")}{pill("Rough",False,True,"flex:1")}</div>'
            f'<div style="min-height:64px;background:var(--charcoal);border:1px solid var(--darkline);border-radius:14px;padding:12px 14px;font-size:15px;font-weight:500;color:var(--dlabel)">Notes for your coach — optional</div>'
            f'<div><div class="label-dark" style="margin-bottom:8px">Where</div><div style="display:flex;gap:8px;flex-wrap:wrap">{pill("Shoulder",False,True)}{pill("Elbow",False,True)}{pill("Wrist",False,True)}{pill("Hip",False,True)}{pill("Knee",True,True)}{pill("Ankle",False,True)}{pill("Lower back",False,True)}{pill("Neck",False,True)}</div></div>'
            f'<div><div class="label-dark" style="margin-bottom:8px">How bad</div><div style="display:flex;gap:8px">{pill("Mild",True,True,"flex:1")}{pill("Moderate",False,True,"flex:1")}{pill("Severe",False,True,"flex:1")}</div></div>' + btn("Done","chalk")),
        "As built, with the handle and display title. Collapsed state shows the ghost “Something hurts” where the pickers sit.", dark=True, screen_style="padding:16px 0 0"))

    # 19 swap sheet
    dim2 = f'<div style="padding:0 24px;opacity:.35;display:flex;flex-direction:column;gap:16px">{gym_header("Max Effort Lower","1/5",False)}<div class="display" style="font-size:28px;font-weight:700">SSB Box Squat</div>{seg("dn-")}</div>'
    def optcard(n, r, on=False):
        return (f'<div style="background:var(--charcoal);border:{"1.5px solid var(--burgundy-lt)" if on else "1px solid var(--darkline)"};border-radius:16px;padding:13px 16px;display:flex;justify-content:space-between;align-items:center;gap:10px"><div><div style="font-size:16px;font-weight:700;color:var(--chalk)">{n}</div><div style="font-size:12px;color:var(--dlabel);line-height:1.4;margin-top:3px">{r}</div></div>{chev("#A05257",18,2) if on else ""}</div>')
    F.append(frame("s19", "19 · Swap — reason + ranked options",
        dim2 + sheet(sheet_head("Swap exercise","SSB Box Squat") + hr(True) +
            f'<div><div class="label-dark" style="margin-bottom:8px">Why swap?</div><div style="display:flex;gap:8px;flex-wrap:wrap">{pill("Pain",True,True)}{pill("Equipment",False,True)}{pill("Time",False,True)}{pill("Preference",False,True)}</div><div style="font-size:12px;color:var(--dlabel);line-height:1.45;margin-top:8px">Pain swaps apply to all your future sessions and start a safety check.</div></div>'
            f'<div><div class="label-dark" style="margin-bottom:8px">Where</div><div style="display:flex;gap:8px;flex-wrap:wrap">{pill("Shoulder",False,True)}{pill("Elbow",False,True)}{pill("Wrist",False,True)}{pill("Hip",False,True)}{pill("Knee",True,True)}{pill("Ankle",False,True)}{pill("Lower back",False,True)}{pill("Neck",False,True)}</div></div>'
            f'<div style="display:flex;flex-direction:column;gap:8px">{optcard("Belt Squat","Squat — doesn’t stress the knee",True)}{optcard("Hatfield Squat","Squat — knee friendly variant")}{optcard("Leg Press","Squat pattern")}</div>' + btn("Swap to Belt Squat","chalk",50,15)),
        "As built. While the coach re-ranks, a small logo loader with “Asking your coach” sits above the list; the local list stays usable. Preference rationale uses display names (“Same overhead press family”), not the raw key.", dark=True, screen_style="padding:16px 0 0"))

    # 20 exercise info dark with This set
    F.append(frame("s20", "20 · Exercise info — from the name or the ⓘ pill",
        dim2 + sheet(sheet_head("How to","SSB Box Squat") + hr(True) +
            f'<div style="background:var(--charcoal);border:1px solid var(--darkline);border-radius:14px;padding:12px 14px"><div class="label-dark" style="margin-bottom:6px">This set</div><div style="font-size:14px;color:var(--dbody);line-height:1.5;font-weight:500">Work up to today’s true 5-rep max. Everything before it is setup.</div></div>'
            f'<div><div class="label-dark" style="margin-bottom:7px">Setup</div><div style="font-size:14px;color:var(--dbody);line-height:1.5;font-weight:500">1.&nbsp; SSB on the traps, hands on the handles, elbows down.<br>2.&nbsp; Box one inch below parallel, stance a touch wider than your squat.</div></div>'
            f'<div><div class="label-dark" style="margin-bottom:7px">Cues</div><div style="font-size:14px;color:var(--dbody);line-height:1.5;font-weight:500">— Sit back, knees out, touch the box under control.<br>— Stay tight on the box, drive the head back into the bar.</div></div>'
            f'<div><div class="label-dark" style="margin-bottom:7px">Common faults</div><div style="font-size:14px;color:var(--dbody);line-height:1.5;font-weight:500">— Rocking off the box.<br>— Letting the bar pull the chest down.</div></div>'
            f'<div><div class="label-dark" style="margin-bottom:8px">Your preference</div><div style="display:flex;gap:8px">{pill("Prefer this",True,True)}{pill("Exclude from my plans",False,True)}</div><div style="font-size:12px;color:var(--dlabel);line-height:1.45;margin-top:8px">Preferred — selection favors this exercise where the slot allows it.</div></div>'),
        "One sheet for everything about the exercise: the set's note (“This set”) sits on top when there is one, then setup, cues, faults, the YouTube link-out for non-catalog movements, and Prefer / Exclude as proper pills. Opened from the name or from ⓘ — two doors, one room.", dark=True, screen_style="padding:16px 0 0"))
    return F
