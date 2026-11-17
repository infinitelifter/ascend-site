from lib import *

def coach_card(kicker, headline, body, meta, date="Sun 05.07"):
    hl = f'<div class="display" style="font-size:19px;font-weight:700;line-height:1.2;margin-bottom:6px">{headline}</div>' if headline else ''
    return (f'<div class="card" style="padding:16px 20px"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px"><div class="label" style="color:var(--burgundy)">{kicker}</div><div class="label-faint num">{date}</div></div>'
            f'{hl}<div class="meta">{body}</div>{f"<div class=meta style=margin-top:10px;color:var(--faint)>{meta}</div>" if meta else ""}</div>')

def sick_action(): return '<div style="text-align:center;font-size:13px;font-weight:600;color:var(--taupe)">I’m sick — adjust my week</div>'

def cycle_card(): return (f'<div class="card" style="padding:16px 20px;display:flex;justify-content:space-between;align-items:center"><div><div class="label-faint" style="margin-bottom:3px">Conjugate · 12 weeks</div><div style="font-size:14px;font-weight:700">Week 2 — Intensification</div></div>'
    f'<div style="display:flex;gap:4px">{chev("#211E19",16)}{chev("#5C262B",16)}{chev("#E0D7C3",16)}</div></div>')

def data_card(label, value, secondary, pct, muted=False):
    col = "var(--faint)" if muted else "var(--charcoal)"
    return (f'<div class="card" style="padding:16px;flex:1"><div class="label-faint">{label}</div><div class="display" style="font-size:26px;font-weight:700;margin-top:6px;color:{col}">{value}<span style="font-size:13px;color:var(--faint);font-weight:600;font-family:var(--body)"> {secondary}</span></div>'
            f'<div class="progressline" style="height:4px;margin-top:10px"><div style="width:{pct}%"></div></div></div>')

def nutrition_cards(): return f'<div><div class="label-faint" style="margin-bottom:10px">Nutrition today</div><div style="display:flex;gap:10px">{data_card("Calories","1,780","/ 2,340",76)}{data_card("Protein","142","/ 190 g",75)}</div></div>'

def next_row(day, title, tag="ME"):
    return f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:16px"><div><div class="label-dark" style="margin-bottom:4px">{day}</div><div style="font-size:15px;font-weight:700">{title}</div></div>{role(tag)}</div>'

def nav_frames():
    F = []
    hdr = lambda d: header(d, "Today", right=settings_link())
    review_card = coach_card("Coach · weekly review", "Your coaching review is ready", "Squat training max up 5 kg. Cossack squats added twice a week. Squat volume comes down 10% next week. Calories held.", "3 changes applied · tap for details")
    body = lambda: (hdr("Monday · July 6") + '<div style="height:16px"></div>' + slab(f'<div class="label-dark" style="margin-bottom:12px">Rest</div><div class="display" style="font-size:24px;font-weight:600;line-height:1.25;margin-bottom:18px">Recovery is part of<br>the program.</div>{hr(True)}{next_row("Tomorrow","Max Effort Lower · SSB Box Squat")}') + f'<div style="height:14px"></div>{sick_action()}<div style="height:14px"></div>{review_card}<div style="height:12px"></div>{cycle_card()}<div style="height:16px"></div>{nutrition_cards()}<div style="flex:1"></div>')
    F.append(frame("nav1", "N1 · Bottom navigation — final", body() + tabbar("today"), "<b>Chosen.</b> Words only, in the caps label face (11 pt, tracked), the burgundy index above the active tab, cream bar with a hairline, 84 pt so it breathes. Applied on every daylight frame on this page. In code: a custom <code>tabBar</code> on the Expo Router Tabs — three Pressables, no icons, the index mark as a 26×3 View. <b>v5.1:</b> One light selection tick when the tab changes, by tap or by swipe."))
    F.append(frame("nav2", "N2 · Bottom navigation — words in the display face", body() + tabbar("today","text"), "The earlier words-only draft, for the record: display face, no tracking, 76 pt."))
    F.append(frame("nav3", "N3 · Bottom navigation — index with finer icons", body() + tabbar("today","index2"), "For the record: the icon version you passed on."))
    return F

def frames():
    F = []
    hdr = lambda d: header(d, "Today", right=settings_link())
    review_card = coach_card("Coach · weekly review", "Your coaching review is ready", "Squat training max up 5 kg. Cossack squats added twice a week. Squat volume comes down 10% next week. Calories held.", "3 changes applied · tap for details")

    # 06 rest
    F.append(frame("s6", "06 · Today — rest day",
        hdr("Monday · July 6") + '<div style="height:16px"></div>' +
        slab(f'<div class="label-dark" style="margin-bottom:12px">Rest</div><div class="display" style="font-size:24px;font-weight:600;line-height:1.25;margin-bottom:18px">Recovery is part of<br>the program.</div>{hr(True)}{next_row("Tomorrow","Max Effort Lower · SSB Box Squat")}') +
        f'<div style="height:14px"></div>{sick_action()}<div style="height:14px"></div>{review_card}<div style="height:12px"></div>{cycle_card()}<div style="height:16px"></div>{nutrition_cards()}<div style="flex:1"></div>{tabbar("today")}',
        "<b>Coach card grammar unified:</b> a burgundy kicker (Coach · weekly review / Coach · note) and a sentence headline in the display face — the sentence is no longer forced through 11 pt caps. Settings becomes an icon in the header. Tab bar: three distinct stroke icons (chevron, list, ring) instead of three identical chevrons; inactive colour is the new, darker faint. <b>v5.1:</b> The slab carries the one shadow in the app (espresso at 16%, 18 pt blur, 10 pt down). On load the slab settles first, the cards under it 100 ms later; nutrition bars fill from zero."))

    # 06b done
    F.append(frame("s6b", "06b · Today — session done",
        hdr("Tuesday · July 7") + '<div style="height:16px"></div>' +
        slab(f'<div class="label-dark" style="margin-bottom:12px">Done</div><div class="display" style="font-size:24px;font-weight:600;line-height:1.25;margin-bottom:16px">Session complete.</div>'
             f'<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:18px"><div><div style="font-size:15px;font-weight:700;margin-bottom:4px">Max Effort Lower</div><div class="num" style="font-size:13px;color:var(--dlabel);font-weight:600">18 sets · top set 180 kg · 397 lb · mostly solid</div></div><div style="font-size:13px;font-weight:600;color:var(--dlabel);display:flex;align-items:center;gap:2px">Edit{ic("chev-right",14,"#A09580")}</div></div>'
             f'{hr(True)}{next_row("Thursday","Max Effort Upper · 2″ Board Press")}') +
        f'<div style="height:14px"></div>{sick_action()}<div style="height:14px"></div>{review_card}<div style="height:16px"></div>{nutrition_cards()}<div style="flex:1"></div>{tabbar("today")}',
        "The receipt as built. Quiet accomplishment, no confetti. Edit stays available until the next session starts."))

    # 07 ready
    def ex_row(name, scheme, lb=None):
        l = f'<span style="font-size:11px;color:var(--dlabel)">  {lb}</span>' if lb else ''
        return f'<div style="display:flex;justify-content:space-between;align-items:baseline;gap:8px;padding:11px 0;border-top:1px solid var(--darkline)"><div style="font-size:15px;font-weight:600">{name}</div><div class="num" style="font-size:14px;color:var(--dlabel);font-weight:600;text-align:right">{scheme}{l}</div></div>'
    session_slab = (f'<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px"><div class="display" style="font-size:26px;font-weight:700;line-height:1.1">Max Effort Lower</div>{role("ME")}</div>'
        f'<div class="meta-dark num" style="margin-bottom:12px">4 exercises · approximately 75 minutes</div>'
        f'{ex_row("SSB Box Squat","5 × 150 · 5 × 165 · work up to 5RM · 180 kg","397 lb")}{ex_row("SSB Good Morning","4 × 8 · 120 kg","265 lb")}{ex_row("Glute Ham Raise","4 × 12")}{ex_row("Farmer Carry","3 × 30 m · 60 kg","132 lb")}')
    F.append(frame("s7", "07 · Today — session ready",
        hdr("Tuesday · July 7") + '<div style="height:16px"></div>' +
        slab(session_slab + f'<div style="margin-top:14px">{btn("Begin session","chalk",icon=None)}</div>') +
        f'<div style="height:14px"></div>{sick_action()}<div style="height:14px"></div>'
        + coach_card("Coach · before you start", None, "Max Effort Lower · SSB Box Squat. Today the top set drives your squat training max — everything before it is setup. About 75 minutes. The loads are ready — just lift.", None, "Tue 07.07")
        + f'<div style="height:12px"></div><div class="card" style="padding:15px 20px;display:flex;justify-content:space-between;align-items:center"><div class="label-faint">Nutrition</div><div class="num" style="font-size:14px;color:var(--taupe);font-weight:600">1,780 of 2,340 kcal</div></div><div style="flex:1"></div>{tabbar("today")}',
        "The exercise-count line drops its caps (it is a sentence: “4 exercises · approximately 75 minutes”). Session title in the display face. Pre-session nudge shown in place of the review card, as the app does on a session day."))

    # 07b resume
    F.append(frame("s7b", "07b · Today — resume (closed gym mode mid-session)",
        hdr("Tuesday · July 7") + '<div style="height:16px"></div>' +
        slab(session_slab + f'<div style="margin-top:14px"><div class="meta-dark num" style="text-align:center;margin-bottom:10px">12 of 18 working sets logged</div>{btn("Resume session","chalk")}</div>') +
        f'<div style="height:14px"></div>{sick_action()}<div style="height:14px"></div>{review_card}<div style="flex:1"></div>{tabbar("today")}',
        "As built: × in gym mode never completes; Today shows the count and Resume. The count line is sentence case now."))

    # 06c offline
    F.append(frame("s6c", "06c · Today — offline, nothing cached",
        hdr("Monday · July 6") + '<div style="height:16px"></div>' +
        f'<div class="card" style="padding:18px 20px;display:flex;flex-direction:column;gap:6px"><div style="font-size:14px;font-weight:600;color:var(--burgundy);line-height:1.5">You’re offline. Today’s plan loads when the connection is back — anything you log in the gym is stored on this phone and syncs later.</div><div style="font-size:13px;font-weight:700;margin-top:6px">Try again</div></div>'
        f'<div style="height:14px"></div>{coach_card("Coach · weekly review", None, "Your coach reviews every week of training and nutrition — first review lands after your first full week.", None, "—")}<div style="flex:1"></div>{tabbar("today")}',
        "The ErrorCard as built, drawn so it can be judged. Burgundy sentence, factual, one retry link. The coach stack still renders beneath it."))

    # 06e no program
    F.append(frame("s6e", "06e · Today — no program",
        hdr("Monday · July 6") + '<div style="height:16px"></div>' +
        slab(f'<div class="label-dark" style="margin-bottom:12px">Rest</div><div class="display" style="font-size:24px;font-weight:600;line-height:1.25;margin-bottom:18px">No program yet.</div>{hr(True)}<div class="meta-dark" style="margin:16px 0 14px">The coach can build your first block from your saved profile, or you can edit your answers first.</div>{btn("Build my program","chalk",48,14)}<div style="height:8px"></div>{btn("Edit training profile","ghostDark",44,14)}') +
        f'<div style="height:14px"></div>{coach_card("Coach · weekly review", None, "Your coach reviews every week of training and nutrition — first review lands after your first full week.", None, "—")}<div style="flex:1"></div>{tabbar("today")}',
        "Today said “No session scheduled — build a program in onboarding.” with nothing to tap. v5 gives the slab the two actions the Coach tab (10f) already has."))

    # 25 nudges
    def nudge(title, body, actions):
        prim = [l for l, v in actions if v == 'espresso']; secs = [l for l, v in actions if v != 'espresso']
        a = ''.join(f'<div class="btn btn-espresso" style="height:46px;font-size:14px">{l}</div>' for l in prim)
        if secs: a += '<div style="display:flex;gap:8px">' + ''.join(f'<div class="btn" style="flex:1;height:42px;font-size:14px;border:1px solid var(--bone);color:var(--taupe);background:transparent">{l}</div>' for l in secs) + '</div>'
        return f'<div class="card" style="padding:16px 20px"><div class="label" style="color:var(--burgundy);margin-bottom:8px">{title}</div><div class="meta">{body}</div>{f"<div style=display:flex;flex-direction:column;gap:8px;margin-top:14px>{a}</div>" if actions else ""}</div>'
    F.append(frame("s25", "25 · Coach nudges — the coach speaks first",
        hdr("Wednesday · July 15") + '<div style="height:16px;flex:0 0 auto"></div><div style="display:flex;flex-direction:column;gap:10px">' +
        nudge("Coach · your week, revised", "Thursday's session is gone. Here's the revised week — nothing lost: Max Effort Lower moves to Saturday, 2 later sessions shift to keep spacing. Nothing applies until you confirm.", [("Apply the revised week","espresso"),("Keep as scheduled","ghost")]) +
        nudge("Coach · checking in", "No session logged since Friday — travel, fatigue, or life? Tell Ascend and it reshapes the week. Nothing is lost either way.", [("Reshape my week","espresso"),("I'm sick","ghost"),("Training today","ghost")]) +
        nudge("Coach · weekly check-in", "Last weigh-in was Tuesday — your check-in is due. Thirty seconds: one weigh-in keeps your targets honest and feeds this week's review.", [("Run the check-in","espresso")]) +
        '</div>',
        "<b>The buttons you flagged.</b> Nudge actions were 9×14 pt text chips wrapping unevenly. v5: a full-width espresso primary (46 pt) with the secondaries sharing one ghost row beneath it (42 pt) — the same grammar as every other decision in the app. Stacked here for documentation; at most two or three cards coexist. “Run the check-in” opens the sheet directly."))

    # 22 sick
    dim_today = f'<div style="padding:0 24px;opacity:.35;display:flex;flex-direction:column;gap:18px"><div><div class="label-faint">Monday · July 6</div><div class="title display" style="margin-top:4px">Today</div></div>{slab("<div class=label-dark style=margin-bottom:12px>Rest</div><div class=display style=font-size:24px;font-weight:600;line-height:1.25>Recovery is part of<br>the program.</div>")}</div>'
    def opt(t, d): return f'<div style="background:var(--charcoal);border:1px solid var(--darkline);border-radius:16px;padding:13px 16px;display:flex;justify-content:space-between;align-items:center;gap:12px"><div style="font-size:15px;font-weight:700;color:var(--chalk)">{t}</div><div style="font-size:12px;color:var(--dlabel);text-align:right">{d}</div></div>'
    F.append(frame("s22", "22 · I'm sick — adaptation sheet",
        dim_today + sheet(sheet_head("I'm sick","How long are you out?") + hr(True) +
            f'<div style="display:flex;gap:8px">{pill("Still out",True,True)}{pill("Back today",False,True)}</div>'
            f'<div style="display:flex;flex-direction:column;gap:8px">{opt("Just today","today’s session moves")}{opt("2–3 days","week reflows, accessories trimmed")}{opt("About a week","re-entry becomes a deload")}{opt("Longer","deload re-entry, plan re-checked")}</div>'),
        "Every sheet in v5 gets a drag handle — the one close affordance the sheets lacked (backdrop tap stays). Sheet title in the display face.", screen_style="padding:8px 0 0"))
    F.append(frame("s22b", "22b · I'm sick — adjusting",
        dim_today + sheet(sheet_head("I'm sick","How long are you out?") + hr(True) + f'<div style="padding:18px 0 10px;display:flex;flex-direction:column;align-items:center">{shimmer(84, True, "Adjusting your plan")}</div>'),
        "The logo loader inside a sheet, 84 pt. Backdrop stays locked while working, as built.", screen_style="padding:8px 0 0"))
    F.append(frame("s22c", "22c · I'm sick — done",
        dim_today + sheet(sheet_head("I'm sick","Noted.") + hr(True) + '<div style="font-size:14px;color:var(--dbody);line-height:1.5;font-weight:500">This week’s remaining sessions moved back 3 days and accessories are trimmed. Main lifts stay as planned — resume when you can.</div>' + btn("Done","chalk")),
        "The result reads as the sheet title plus the note, instead of a title that still asks the question.", screen_style="padding:8px 0 0"))

    # 21 coach review
    facts = (f'<div style="display:flex;gap:10px">{fact("Squat max","160<span class=arrow>→</span>165","top set 5 × 160 kg · est. max 187")}{fact("Squat volume","−10%","42% of sets were grinds")}</div>'
             f'<div style="display:flex;gap:10px">{fact("Added","Cossack Squat","2×/wk · knee flag on Back Squat",22)}{fact("Bench max","Held","no top set tested this week")}</div>')
    def sec(k, t, last=False): return f'<div style="padding:16px 0;{"" if last else "border-bottom:1px solid var(--bone)"}"><div class="label" style="color:var(--burgundy);margin-bottom:8px">{k}</div><div style="font-size:15px;line-height:1.55;font-weight:500">{t}</div></div>'
    F.append(frame("s21", "21 · Coaching review — weekly",
        f'<div style="margin:8px 0 16px">{back("Today")}</div><div class="label-faint">Weekly review · 29.06–06.07</div><div class="title display" style="margin:4px 0 16px">Your coaching review is ready</div>'
        f'<div style="display:flex;flex-direction:column;gap:10px;margin-bottom:16px">{facts}</div>'
        f'<div class="card" style="padding:0 20px">{sec("What Ascend saw","Four sessions logged, mostly solid. Squat top set 5 × 160 kg, estimated max 186.7 kg — above the current training max for the third week. Right-knee cave flagged again on the form check. Bodyweight trend on target.")}{sec("What changed","Squat training max up 5 kg. Cossack squats added twice a week. Squat volume comes down 10% next week. Not enough recent evidence to change the bench training max — the current progression remains in place. Calories held.")}{sec("Why","The best set of the week estimates the max; the training max follows it, capped at 5 kg a week. The knee flag gets targeted work before it affects your squat. 42% of squat sets were grinds; a small cut restores bar speed.")}{sec("What happens next","Squat runs at the new max — the next top set confirms it. The corrective stays until two clean form checks close the flag. Next full review in one week.",True)}</div>',
        "<b>Facts first, then the voice.</b> The engine's decisions become tiles above the prose — training max moves as “160 → 165” (with the burgundy arrow), volume as “−10%”, additions by name, holds as “Held”. The four locked sections follow unchanged. This is the €59 screen; it is the only place in the app that looks like this. Below the fold (scrolls): the proposal card, Report a bad recommendation, the feedback field and the footer — unchanged from the build. <b>v5.1:</b> The tiles are the one earned moment — each fades in and rises 10 pt, 80 ms apart, after the header; the four sections follow once the last tile has landed. Still under Reduce Motion.", screen_style="padding-bottom:0"))
    F.append(frame("s21b", "21 · Coaching review — below the fold",
        f'<div style="margin:8px 0 16px">{back("Today")}</div>'
        f'<div class="slab" style="padding:20px"><div class="label-dark" style="color:var(--burgundy-lt);margin-bottom:8px">Coach proposal</div><div class="display" style="font-size:19px;font-weight:700;margin-bottom:6px">Move to conjugate training</div><div class="meta-dark" style="margin-bottom:16px">Linear progression stalled on 2 lifts — time for conjugate. Accepting rebuilds your plan — history and training maxes carry over.</div>{btn("Accept — rebuild my plan","chalk",48,14)}<div style="height:8px"></div>{btn("Not yet","ghostDark",44,14)}</div>'
        f'<div style="height:16px"></div><div style="font-size:13px;font-weight:600;color:var(--taupe)">Report a bad recommendation</div><div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px">{pill("Too aggressive")}{pill("Too cautious")}{pill("Wrong exercise for me")}{pill("Didn’t fit my schedule")}</div>'
        f'<div style="height:18px"></div><div class="label-faint" style="margin-bottom:10px">Anything to tell your coach?</div><div class="input" style="height:76px;align-items:flex-start;padding-top:13px;border-radius:14px;color:var(--faint);font-size:15px">Sleep, stress, a lift that feels off — anything useful.</div><div style="height:10px"></div>{btn("Send to coach","charcoal",48,14)}'
        f'<div style="height:18px"></div>{hr()}<div style="font-size:12px;color:var(--faint);line-height:1.5;margin-top:14px;font-weight:500">Reviews run weekly from your logs, weigh-ins, form checks and flags. Every change lands on upcoming sessions only — history is never rewritten.</div>',
        "Report reasons use the shared Pill (they were a one-off chip). Methodology names are display names (“conjugate training”, never the raw slug). Proposal title in the display face. While a plan rebuilds, the two buttons give way to the logo loader with “Rebuilding your plan”."))
    F.append(frame("s21c", "21c · Coach note — interim",
        f'<div style="margin:8px 0 16px">{back("Today")}</div><div class="label-faint">Coach note · Tue 07.07</div><div class="title display" style="margin:4px 0 16px">Right knee flagged</div>'
        f'<div class="card" style="padding:18px 20px"><div class="label" style="color:var(--burgundy);margin-bottom:10px">What changed</div><div style="font-size:15px;line-height:1.55;font-weight:500">Right knee flagged — upcoming squat work adjusted. Full review at the end of the week.</div></div>'
        f'<div style="height:12px"></div><div class="label-faint" style="margin-bottom:10px">1 change applied</div><div class="card" style="padding:0 20px"><div style="padding:13px 0;font-size:14px;font-weight:600">Knee pain reported — 2 upcoming exercises swapped to spare it</div></div>'
        f'<div style="height:18px"></div>{hr()}<div style="font-size:12px;color:var(--faint);line-height:1.5;margin-top:14px;font-weight:500">Reviews run weekly from your logs, weigh-ins, form checks and flags. Every change lands on upcoming sessions only — history is never rewritten.</div>',
        "Interim notes: the header no longer repeats “Coach note” twice with a same-day date range. Kicker carries the kind and the single date; the title is the note's first clause. No report row, no proposal — as built."))
    F.append(frame("s21d", "21d · Coach review — first week, nothing yet",
        f'<div style="margin:8px 0 16px">{back("Today")}</div><div class="title display">Coach review</div><div class="subtitle" style="margin-top:10px">Your first review lands after your first full week of training.</div>'
        f'<div style="flex:1;display:flex;align-items:center;justify-content:center">{mark(120, opacity=.35)}</div>',
        "Empty state uses the logo at watermark opacity like the rest of the app, instead of a bare sentence on ivory."))
    return F
