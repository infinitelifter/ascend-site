from lib import *
APPLE = '<svg width="16" height="19" viewBox="0 0 16 19" fill="#F7F3E9"><path d="M13.3 10.1c0-2.4 2-3.6 2.1-3.6-1.1-1.7-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.1 1-4 2.4-1.7 3-.4 7.3 1.2 9.7.8 1.2 1.8 2.5 3.1 2.4 1.2 0 1.7-.8 3.2-.8s1.9.8 3.2.8c1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.6-1-2.7-3.9zM10.9 3c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1.1.1 2.2-.6 2.8-1.4z"/></svg>'
GOOGLE = '<svg width="17" height="17" viewBox="0 0 48 48"><path fill="#4285F4" d="M44.5 20H24v8.5h11.8C34.7 33.9 30.1 37 24 37c-7.2 0-13-5.8-13-13s5.8-13 13-13c3.1 0 5.9 1.1 8.1 2.9l6.4-6.4C34.6 4.1 29.6 2 24 2 11.8 2 2 11.8 2 24s9.8 22 22 22c11 0 21-8 21-22 0-1.3-.2-2.7-.5-4z"/><path fill="#34A853" d="M6.3 14.7l7 5.1C15.1 16 19.2 13 24 13c3.1 0 5.9 1.1 8.1 2.9l6.4-6.4C34.6 4.1 29.6 2 24 2 15.4 2 8 7 6.3 14.7z"/><path fill="#FBBC05" d="M24 46c5.4 0 10.4-1.8 14.3-5l-6.6-5.6C29.6 37 26.9 38 24 38c-6.1 0-10.7-3.1-11.8-8.5l-7 5.4C8.8 41.5 15.9 46 24 46z"/><path fill="#EA4335" d="M44.5 20H24v8.5h11.8c-.7 2.1-2 3.9-3.7 5.2l6.6 5.6C42.7 35.6 45 30.3 45 24c0-1.3-.2-2.7-.5-4z"/></svg>'

def top(step, total=8):
    return f'<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:22px">{back("", False)}{rail(step, total)}</div>'

def head(title, sub=None, eyebrow="Private assessment"):
    s = f'<div class="subtitle" style="margin-top:12px">{sub}</div>' if sub else ''
    return f'<div style="margin-bottom:22px"><div class="label-faint" style="margin-bottom:8px">{eyebrow}</div><div class="title display">{title}</div>{s}</div>'

def cta(label, variant="burgundy", busy=False):
    return f'<div style="flex:1"></div>{btn(label, variant, extra="margin-bottom:28px", busy=busy)}'

def selcard(t, d, on=False, compact=False):
    cls = "sel-card" + (" on" if on else "") + (" compact" if compact else "")
    ch = chev("#A05257", 22) if on else ''
    return f'<div class="{cls}"><div><div class="t">{t}</div><div class="d">{d}</div></div>{ch}</div>'

def stepper_card(label, value, secondary=None):
    sec = f'<div class="num" style="font-size:11px;color:var(--faint);font-weight:600;margin-top:1px">{secondary}</div>' if secondary else ''
    return (f'<div class="card" style="padding:14px 16px;display:flex;align-items:center;justify-content:space-between">'
            f'<div class="label">{label}</div><div style="display:flex;align-items:center;gap:16px">{stepper("-",44)}'
            f'<div style="width:74px;text-align:center"><div class="display" style="font-size:28px;font-weight:700;line-height:1">{value}</div>{sec}</div>{stepper("+",44)}</div></div>')

def check_row(label, on=True, last=False):
    box = (f'<div style="width:24px;height:24px;border-radius:7px;background:var(--charcoal);display:flex;align-items:center;justify-content:center">{ic("check",14,"#F7F3E9",2.4)}</div>'
           if on else '<div style="width:24px;height:24px;border-radius:7px;border:1.5px solid var(--bone)"></div>')
    return (f'<div style="display:flex;justify-content:space-between;align-items:center;padding:12px 0;{"" if last else "border-bottom:1px solid var(--bone)"}">'
            f'<div style="font-size:15px;font-weight:600;color:{"var(--charcoal)" if on else "var(--faint)"}">{label}</div>{box}</div>')

def frames():
    F = []
    # 00 bootstrap
    F.append(frame("s0", "00 · Cold start — waking the coach",
        f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center">{shimmer(120, dark=False, label="Waking the coach")}</div>',
        "Replaces the three-dot pulse on <code>app/index.tsx</code>. The logo mark with a soft band of light crossing it every 1.6 s — the only loader in the app from here on. Label stays factual, no ellipsis.", screen_style="padding-bottom:30px"))

    # 01 sign in
    F.append(frame("s1", "01 · Sign in — the brand moment",
        f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center">{logo_full(300)}'
        f'<div style="margin-top:14px;font-size:14px;font-weight:600;color:var(--taupe);letter-spacing:.02em">Serious training, fully managed.</div></div>'
        f'<div style="display:flex;flex-direction:column;gap:10px;padding-bottom:30px">'
        f'{btn("Continue with Apple","charcoal",icon=APPLE)}{btn("Continue with Google","cream",icon=GOOGLE)}{btn("Continue with Email","ghost")}'
        f'<div style="text-align:center;font-size:12px;color:var(--faint);margin-top:12px;font-weight:500">Privacy · Terms</div></div>',
        "As built, with three fixes: Privacy · Terms become links, the Apple/Google buttons keep their colour while busy and show the button shimmer instead of collapsing to bone with white dots, and the tagline sits a little tighter under the logo.", screen_style="padding-bottom:4px"))

    # 02 email
    F.append(frame("s2", "02 · Email — create account, error state",
        f'<div style="margin-bottom:24px">{back("Back")}</div>'
        f'<div class="title display" style="margin-bottom:22px">Create account</div>'
        f'<div style="display:flex;gap:28px;border-bottom:1px solid var(--bone);margin-bottom:24px"><div style="padding-bottom:12px;border-bottom:3px solid var(--charcoal);font-weight:700;font-size:15px">Create account</div><div style="padding-bottom:12px;color:var(--faint);font-size:15px;font-weight:600">Sign in</div></div>'
        f'<div style="display:flex;flex-direction:column;gap:16px;margin-bottom:28px"><div><div class="label" style="margin-bottom:8px">Email</div><div class="input err num">ondrej@lifter.io</div><div class="err-text">This email is already in use. Sign in instead.</div></div>'
        f'<div><div class="label" style="margin-bottom:8px">Password</div><div class="input" style="color:var(--faint)">Min. 6 characters</div></div></div>'
        f'{btn("Create account","charcoal")}',
        "Title moves to 34 (was 30) so every pre-app screen shares one title size. Busy submit keeps the espresso fill with the button shimmer — the literal “…” label goes."))

    F.append(frame("s2b", "02b · Email — check your inbox",
        f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:14px">'
        f'<div class="title display" style="font-size:30px">Check your inbox</div>'
        f'<div class="subtitle">We sent a confirmation link to<br><b style="color:var(--charcoal)">ondrej@lifter.io</b><br>Open it to activate your account, then sign in.</div>'
        f'<div style="width:100%;margin-top:14px;display:flex;flex-direction:column;gap:10px">{btn("Back to sign in","cream")}{btn("Resend link","ghost")}</div></div>',
        "Unchanged in structure. “Link re-sent” confirmation stays; a failed resend now shows one factual burgundy line under the button instead of nothing."))

    # 03 experience
    F.append(frame("s3", "03 · Onboarding 1 of 8 — experience",
        top(1) + head("How long have you been under the bar?", "Tell Ascend where you are, what you are building, and what your training must work around. This answer sets starting volume and how much gets explained.") +
        f'<div style="display:flex;flex-direction:column;gap:10px">{selcard("Beginner","Under a year of consistent training")}{selcard("Intermediate","1–3 years · you know your way around a rack",True)}{selcard("Advanced","3+ years · real maxes to defend")}</div>' + cta("Continue"),
        "<b>The rail.</b> Eight small chevrons with “Step n of 8” under them replace the three hardcoded chevrons (which showed 3/3 on four different screens and went backwards on weak points). The total adapts to the path — a beginner without an injury sees “of 6”. Burgundy marks the current step, as the component always intended. One rhythm on every step: top row, 22 pt, eyebrow, 34 pt Urbanist title, subtitle."))

    # 04 body
    F.append(frame("s4", "04 · Onboarding 2 of 8 — body",
        top(2) + head("The raw numbers.", "Drives your starting calories and loads.") +
        f'<div style="display:flex;flex-direction:column;gap:12px;margin-bottom:18px">{stepper_card("Age","29")}{stepper_card("Height","183","cm · 6′0″")}{stepper_card("Bodyweight","96.5","kg · 213 lb")}</div>'
        f'<div style="margin-bottom:18px"><div class="label" style="margin-bottom:10px">Sex</div><div style="display:flex;gap:8px">{pill("Male",True)}{pill("Female")}</div></div>'
        f'<div><div class="label" style="margin-bottom:10px">Anything we should train around?</div><div style="display:flex;gap:8px;flex-wrap:wrap">{pill("Desk worker",True)}{pill("One side weaker")}{pill("An injury — past or present",True)}</div>'
        f'<div class="meta" style="margin-top:10px;color:var(--faint)">Injury selected — the next step asks where and what.</div></div>' + cta("Continue"),
        "Numerals move to Urbanist and gain the typed input from the maxes screen (tap the number, decimal keypad). <b>Sex is now required</b> — Continue stays disabled until it is picked, instead of failing seven screens later with a native alert. Height secondary rounding fixed (no more 5′12″)."))

    # 04b injury
    F.append(frame("s4b", "04b · Onboarding 3 of 8 — injury detail (conditional)",
        top(3) + head("Where, and what kind?", "Pick every area that applies. The plan avoids what it must and strengthens around it.").replace("margin-bottom:22px","margin-bottom:16px") +
        f'<div class="label" style="margin-bottom:8px">Area</div><div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px">{pill("Knee",True,style="height:32px;padding:0 13px;font-size:12px")}{pill("Lower back",True,style="height:32px;padding:0 13px;font-size:12px")}{pill("Shoulder",False,style="height:32px;padding:0 13px;font-size:12px")}{pill("Hip",False,style="height:32px;padding:0 13px;font-size:12px")}{pill("Elbow",False,style="height:32px;padding:0 13px;font-size:12px")}{pill("Wrist",False,style="height:32px;padding:0 13px;font-size:12px")}{pill("Ankle",False,style="height:32px;padding:0 13px;font-size:12px")}{pill("Neck",False,style="height:32px;padding:0 13px;font-size:12px")}</div>'
        f'<div style="display:flex;flex-direction:column;gap:12px">'
        f'<div class="card" style="padding:14px 16px;display:flex;flex-direction:column;gap:10px"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:15px;font-weight:700">Knee</div><div style="display:flex;gap:6px">{pill("Left",True,style="height:30px;padding:0 12px;font-size:11px")}{pill("Right",style="height:30px;padding:0 12px;font-size:11px")}</div></div>'
        f'<div class="label-faint">Kind</div><div style="display:flex;gap:6px;flex-wrap:wrap">{pill("Ligament / meniscus",True,style="font-size:12px;height:32px;padding:0 12px")}{pill("Tendon pain",style="font-size:12px;height:32px;padding:0 12px")}{pill("Arthritis / joint wear",style="font-size:12px;height:32px;padding:0 12px")}{pill("General pain",style="font-size:12px;height:32px;padding:0 12px")}{pill("Replaced / surgery",style="font-size:12px;height:32px;padding:0 12px")}</div>'
        f'<div class="label-faint">Status</div><div style="display:flex;gap:6px;flex-wrap:wrap">{pill("Current",style="font-size:12px;height:32px;padding:0 12px")}{pill("Past — healed",True,style="font-size:12px;height:32px;padding:0 12px")}{pill("Chronic — flares up",style="font-size:12px;height:32px;padding:0 12px")}</div></div>'
        f'<div class="card" style="padding:14px 16px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:15px;font-weight:700">Lower back</div><div style="display:flex;align-items:center;gap:6px;font-size:13px;color:var(--faint);font-weight:600">Disc issue · chronic{ic("chev-right",16,"#857D6A")}</div></div></div>' + cta("Continue"),
        "Two small labels — <b>Kind</b> and <b>Status</b> — name the two pill rows that were visually identical. Title at 34 like every other step (was 28). Collapsed summaries get the chevron icon instead of a text “›”."))

    # 05 goal
    F.append(frame("s5", "05 · Onboarding 4 of 8 — goal & gym",
        top(4) + head("What are you building?", None).replace("margin-bottom:22px","margin-bottom:14px") +
        f'<div class="label" style="margin-bottom:8px">The training</div><div style="display:flex;flex-direction:column;gap:5px;margin-bottom:14px">{selcard("General strength","Strong everywhere, no date pressure",compact=True)}{selcard("Powerlifting","Squat, bench, deadlift numbers",True,True)}{selcard("Strongman","Events, carries, odd objects",compact=True)}{selcard("Hypertrophy · bodybuilding","Size first, numbers follow",compact=True)}{selcard("Support another sport","Martial arts, endurance, team sport",compact=True)}</div>'
        f'<div class="label" style="margin-bottom:8px">The nutrition</div><div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px">{pill("Cut",style="height:34px;padding:0 14px")}{pill("Reverse diet",style="height:34px;padding:0 14px")}{pill("Maintain",True,style="height:34px;padding:0 14px")}{pill("Bulk",style="height:34px;padding:0 14px")}</div>'
        f'<div class="label" style="margin-bottom:8px">Where do you train?</div><div style="display:flex;gap:6px;flex-wrap:wrap">{pill("Powerlifting gym",True,style="height:34px;padding:0 14px")}{pill("Commercial",style="height:34px;padding:0 14px")}{pill("Home gym",style="height:34px;padding:0 14px")}</div>' + cta("Continue"),
        "Densest step; the eyebrow now appears here too so the screen belongs to the same assessment. “Support another sport” still reveals the Which sport pill row inline. Nothing else moves."))

    # 05d weak points
    F.append(frame("s5d", "05d · Onboarding 5 of 8 — weak points (intermediate+)",
        top(5) + head("Where do heavy lifts die?", "The failure point picks your special exercises — the variations that attack exactly where the lift stops. Skip anything you're not sure about; Ascend learns the rest from your training.") +
        f'<div style="display:flex;flex-direction:column;gap:20px">'
        f'<div><div class="label-faint" style="margin-bottom:10px">Squat</div><div style="display:flex;gap:8px;flex-wrap:wrap">{pill("Out of the hole",True)}{pill("Midway or at lockout")}{pill("Not sure")}</div></div>'
        f'<div><div class="label-faint" style="margin-bottom:10px">Bench press</div><div style="display:flex;gap:8px;flex-wrap:wrap">{pill("Off the chest")}{pill("Midway")}{pill("At lockout",True)}{pill("Not sure")}</div></div>'
        f'<div><div class="label-faint" style="margin-bottom:10px">Deadlift</div><div style="display:flex;gap:8px;flex-wrap:wrap">{pill("Off the ground",True)}{pill("At the knees")}{pill("At lockout")}{pill("Not sure")}</div></div></div>' + cta("Continue"),
        "Same layout as every other step now (it had its own scroll and an unpinned button). The rail no longer goes backwards. Copy: <b>“Off the floor” becomes “Off the ground”</b> — the word floor stays out of the UI."))

    # 05e maxes
    maxrow_filled = (f'<div class="card" style="padding:14px 16px;display:flex;align-items:center;justify-content:space-between;min-height:72px"><div><div class="label">Squat</div><div style="font-size:12px;color:var(--faint);font-weight:600;margin-top:4px">Clear</div></div>'
        f'<div style="display:flex;align-items:center;gap:16px">{stepper("-",44)}<div style="width:84px;text-align:center"><div class="display" style="font-size:28px;font-weight:700;line-height:1;border-bottom:1.5px dashed var(--bone);display:inline-block;padding-bottom:2px">180</div><div class="num" style="font-size:11px;color:var(--faint);font-weight:600;margin-top:3px">kg · 397 lb</div></div>{stepper("+",44)}</div></div>')
    def maxrow_empty(n): return f'<div class="card" style="padding:14px 16px;display:flex;align-items:center;justify-content:space-between;min-height:72px"><div class="label">{n}</div><div style="display:flex;align-items:center;gap:12px"><span class="display" style="font-size:28px;color:var(--faint);font-weight:700">—</span><span style="font-size:13px;color:var(--burgundy);font-weight:700">Add</span></div></div>'
    F.append(frame("s5e", "05e · Onboarding 6 of 8 — current maxes",
        top(6) + head("What can you lift today?", "Your best single on each of the four main lifts — a recent heavy single is a fair answer, Ascend works from 90% of it. Every lift here is optional.") +
        f'<div class="label" style="margin-bottom:10px">One rep max</div>'
        f'<div style="display:flex;flex-direction:column;gap:12px;margin-bottom:14px">{maxrow_filled}{maxrow_empty("Bench press")}{maxrow_empty("Deadlift")}{maxrow_empty("Overhead press")}</div>'
        f'<div class="card" style="padding:12px 16px"><div class="meta">Lifts you enter train at real loads from day one. Lifts you leave blank are measured in week one — a single crisp top set sets the number.</div></div>' + cta("Continue"),
        "The typed numeral gets its affordance: a faint dashed underline under the number says “tap to type” without saying it. Clear is a 12 pt action under the lift name with a full-row hit area. Button reads “Continue without them” when nothing is entered, as built."))

    # 05c timeline
    F.append(frame("s5c", "05c · Onboarding 7 of 8 — timeline & logistics",
        top(7) + head("Working toward a date?", "A meet on the calendar — or nothing yet.") +
        f'<div style="display:flex;flex-direction:column;gap:8px;margin-bottom:14px">{selcard("No date — just build","Open-ended blocks, steady progress")}{selcard("Peaking for a date","The plan back-solves: peak week lands on it",True)}</div>'
        f'<div class="card" style="padding:12px 16px;display:flex;justify-content:space-between;align-items:center;margin-bottom:18px"><div><div class="label-faint" style="margin-bottom:2px">Event date</div><div class="num" style="font-size:12px;color:var(--faint);font-weight:600">11 weeks out</div></div><div style="display:flex;align-items:center;gap:8px;background:var(--paper);border:1px solid var(--bone);border-radius:10px;padding:8px 12px;font-size:15px;font-weight:600">{ic("cal",16,"#77705F",1.8)}Sat 26 Sep 2026</div></div>'
        f'<div class="label" style="margin-bottom:10px">Session length</div><div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px">{pill("60 min")}{pill("75 min",True)}{pill("90 min")}{pill("120 min")}</div>'
        f'<div class="label" style="margin-bottom:10px">Days per week</div><div style="display:flex;gap:8px">{pill("3")}{pill("4",True)}{pill("5")}</div>' + cta("Continue"),
        "Logistics split into two labelled rows with units on the pills (“75 min”) — the bare “60 75 90 120 | 3 4 5” row needed decoding. The date control gets Summit styling around the native picker. Title 34 (was 28)."))

    # 05b equipment
    F.append(frame("s5b", "05b · Onboarding 8 of 8 — equipment",
        top(8) + head("Confirm your gear.", "Pre-filled for a powerlifting gym. Uncheck what's missing — missing gear never blocks a plan, we build around it.") +
        f'<div class="label-faint" style="margin-bottom:8px">Specialty bars</div><div class="card" style="padding:4px 16px;margin-bottom:14px">{check_row("Safety squat bar")}{check_row("Trap bar")}{check_row("Cambered bar")}{check_row("Duffalo bar",False,True)}</div>'
        f'<div class="label-faint" style="margin-bottom:8px">Machines & stations</div><div class="card" style="padding:4px 16px;margin-bottom:14px">{check_row("Cable stack")}{check_row("Glute ham raise",False,True)}</div>'
        f'<div class="card" style="padding:12px 16px;display:flex;flex-direction:column;gap:8px"><div class="meta">No GHR? Every plan slot has equipment-aware alternatives — the coach swaps automatically.</div><div style="height:1px;background:var(--bone)"></div><div style="display:flex;justify-content:space-between;align-items:center"><div class="num" style="font-size:13px;color:var(--taupe);font-weight:600">Glute Ham Raise → Nordic Curl</div><div style="display:flex;align-items:center;gap:2px;font-size:12px;color:var(--taupe);font-weight:600">Change{ic("chev-right",14,"#77705F")}</div></div></div>'
        + cta("Build my program"),
        "Five groups as built (two shown). Check glyphs are the stroke icon. The busy state keeps the burgundy fill with the shimmer and the label “Building your program” — no more chalk-on-bone during the longest wait in onboarding."))

    F.append(frame("s5bb", "05b · Equipment — building (busy button)",
        top(8) + head("Confirm your gear.", "Pre-filled for a powerlifting gym. Uncheck what's missing — missing gear never blocks a plan, we build around it.") +
        f'<div class="label-faint" style="margin-bottom:8px">Specialty bars</div><div class="card" style="padding:4px 16px;margin-bottom:14px">{check_row("Safety squat bar")}{check_row("Trap bar")}{check_row("Cambered bar",True,True)}</div>'
        + cta("Building your program", busy=True),
        "The in-button wait: label changes, fill stays, a faint band of light crosses the button every 1.6 s. Same component as the logo loader, scaled down — one idea for “working” everywhere."))

    # 05f ready
    F.append(frame("s5f", "05f · Your first training block is ready",
        f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:18px">{mark(96)}'
        f'<div class="title display" style="font-size:32px;max-width:300px">Your first training block is ready</div>'
        f'<div class="subtitle" style="max-width:300px">Built from your experience, current strength, goals, schedule, equipment, and limitations.</div>'
        f'<div class="card" style="padding:14px 16px;text-align:left;width:100%;margin-top:6px"><div class="label-faint" style="margin-bottom:4px">Conjugate · 12 weeks · 4 days</div><div style="font-size:15px;font-weight:700">First session Monday — Max Effort Lower</div><div class="meta" style="margin-top:3px">Week 1 measures the lifts you left blank.</div></div></div>'
        f'{btn("See today’s training","burgundy",extra="margin-bottom:28px")}',
        "<b>New screen</b> replacing the native “Your first training block is ready” alert. Same locked copy, plus one factual card: what was built and when it starts. Engine warnings (short peak, sport-support note) render as a second quiet card here instead of a “Heads up” alert."))
    return F
