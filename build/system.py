from lib import *

def intro():
    boxes = [
        ("1 · One display face", "<b>Urbanist</b> for titles, numerals, sheet titles and fact tiles; the body stays the system font (SF Pro on iPhone — the app never loaded Inter, and it does not need to). One voice, not two: no second face for numbers. Loaded with <code>@expo-google-fonts/urbanist</code>, works in Expo Go."),
        ("2 · Labels are labels again", "11 pt caps only for true kickers (REST · BAR · WHAT CHANGED). Every sentence that was being pushed through the caps style — “tap a done segment to edit”, “4 exercises · approximately 75 minutes”, “Your coaching review is ready”, the email in Settings — becomes sentence case at 13–19 pt."),
        ("3 · Gym mode says less", "Weight 96 pt, steppers 64, reps 44, quality pills 46, Log set 68. The coaching note moves behind ⓘ (shows itself once on set 1), the priority cue becomes a tag, Prev becomes one quiet line. The top-set screen gets the Prev line, Skip and the success hairline it was missing."),
        ("4 · The review leads with facts", "The engine's decisions render as tiles — <span class=display style=color:#EFEAE2;font-size:15px>160 → 165</span>, −10%, Held, + Cossack Squat — above the four locked sections. The €59 screen looks like nothing else in the app."),
        ("5 · Onboarding shows where you are", "An eight-chevron rail with “Step n of 8” replaces three chevrons that read 3/3 on four screens. One title size (34), one rhythm, the eyebrow on every step, Sex required, units on the logistics pills, and the finish is a screen, not an alert."),
        ("6 · The logo is the loader", "A soft band of light crosses the logo mark every 1.6 s — <code>LogoShimmer</code> replaces the three dots in all 13 places. Inside a button the same band crosses the button and the fill stays (no more chalk dots on bone)."),
        ("7 · The unhappy paths are drawn", "Offline Today, no program, session not cached, meal photo failed, targets failed, logging gated, form check failed, nudge buttons that stack properly, sheets with a handle. Nine frames the first device test would have wanted."),
        ("8 · Contrast, icons, copy", "<code>faint</code> #A99F8A → #857D6A (2.5:1 → 3.9:1 on cream). One 2 px stroke icon family (18 glyphs) replaces › ✓ ◉ ⇄ ↗ ← × ⏱. Distinct tab icons. “floor” leaves the UI in four places; macro columns get their unit; lb appears wherever kg stood alone."),
    ]
    b = ''.join(f'<div class="box"><h4>{t}</h4><p>{p}</p></div>' for t, p in boxes)
    return (f'<div class="section" id="why"><h2 class="display">Summit v5 — the app as built, lit better</h2>'
            f'<p class="lede">Source of truth is the code on 3 October: every frame below starts from what the screen renders today and shows the v5 enhancement on top. Nothing functional is removed. Where a frame says “as built”, the pixels moved and the behaviour did not. Fonts: Urbanist (display) and Inter standing in for SF Pro (body).</p>'
            f'<div class="ds"><div class="cmp">{b}</div></div></div>')

TAB = tabbar("today","final").replace('class="tabbar"', 'class="tabbar" style="height:auto;border:none;margin:0;padding:0;background:transparent"')

def system():
    sw = ''.join(f'<div class="sw"><div class="chip" style="background:{h}"></div><div class="n">{n}</div><div class="h">{h} · {u}</div></div>' for n, h, u in [
        ("Ivory","#F4EFE4","app background"),("Cream","#FCF9F1","raised cards"),("Espresso","#211E19","slabs, text, gym mode"),("Soot","#2E2922","elevated on espresso"),("Chalk","#F7F3E9","text on dark"),
        ("Taupe","#77705F","secondary text"),("Faint · v5","#857D6A","tertiary — was #A99F8A"),("Bone","#E0D7C3","hairlines"),("Darkline","#3C362B","hairlines on dark"),("Burgundy","#5C262B","the accent, on light"),("Burgundy · lt","#A05257","the accent, on dark")])
    icons = ''.join(f'<div>{ic(n,24,"#EFEAE2",2)}<span>{n}</span></div>' for n in ICONS.keys())
    typ = (f'<div class="typerow"><div class="meta">Gym numeral · Urbanist 700 · 96</div><div class="display" style="font-size:96px;font-weight:700;line-height:.95">172.5</div></div>'
           f'<div class="typerow"><div class="meta">Nutrition hero · 700 · 46</div><div class="display" style="font-size:46px;font-weight:700;line-height:1">1,780</div></div>'
           f'<div class="typerow"><div class="meta">Reps · 700 · 44 &nbsp; Screen title · 700 · 34</div><div class="display" style="font-size:44px;font-weight:700;line-height:1">5</div><div class="display" style="font-size:34px;font-weight:700;line-height:1.08">Max Effort Lower</div></div>'
           f'<div class="typerow"><div class="meta">Fact tile · 700 · 30 &nbsp; Session / sheet title · 700 · 26 / 22</div><div class="display" style="font-size:30px;font-weight:700">160 <span style="color:#A05257;font-weight:600">→</span> 165</div><div class="display" style="font-size:22px;font-weight:700">Anything to flag?</div></div>'
           f'<div class="typerow"><div class="meta">Body · system (SF) 400–700 · 13–16</div><div style="font-size:15px;line-height:1.55;max-width:560px;color:#C9BFAC">Squat training max +5 kg — top set 5 × 160 kg, estimated max 186.7 kg. The best set of the week estimates the max; the training max follows it, capped at 5 kg a week.</div></div>'
           f'<div class="typerow"><div class="meta">Kicker · 700 · 11 · caps .11em</div><div class="label-dark">Max effort · lower · 1/5</div><div class="meta" style="width:auto;text-transform:none;letter-spacing:0;font-size:13px;color:#A29B8D">Sentence meta · 500 · 13 — “Set 2 of 3”</div></div>')
    loaders = (f'<div class="grid">'
               f'<div class="comp darkc"><div class="cn">LogoShimmer · espresso · 120</div><div style="display:flex;justify-content:center;padding:10px 0">{shimmer(120, True, "Watching your lift")}</div></div>'
               f'<div class="comp"><div class="cn">LogoShimmer · paper · 120</div><div style="display:flex;justify-content:center;padding:10px 0">{shimmer(120, False, "Waking the coach")}</div></div>'
               f'<div class="comp darkc"><div class="cn">In a sheet · 84 &nbsp;·&nbsp; in a card · 64</div><div style="display:flex;justify-content:space-around;align-items:center;padding:10px 0">{shimmer(84, True, "Adjusting your plan")}{shimmer(64, True, "Rebuilding your plan")}</div></div>'
               f'<div class="comp"><div class="cn">Button shimmer — busy keeps its fill</div><div style="display:flex;flex-direction:column;gap:10px">{btn("Building your program","burgundy",busy=True)}{btn("Create account","charcoal",busy=True)}{btn("Continue with Google","cream",busy=True)}</div></div>'
               f'</div>')
    comps = (f'<div class="grid">'
             f'<div class="comp darkc"><div class="cn">Gym mode — weight card 96 / steppers 64</div><div class="sootcard" style="padding:18px;display:flex;align-items:center;justify-content:space-between">{stepper("-",64,True)}<div style="text-align:center"><div class="display" style="font-size:96px;font-weight:700;line-height:.95;color:#F7F3E9">165</div><div class="num" style="font-size:13px;color:#A09580;font-weight:600;margin-top:6px">kg · 364 lb</div></div>{stepper("+",64,True)}</div><div style="display:flex;gap:8px;margin-top:14px">{gym_pill("Form","camera")}{gym_pill("Swap","swap")}{gym_pill("","info").replace("gap:7px","")}<span class="tag">Load over reps</span></div></div>'
             f'<div class="comp"><div class="cn">Fact tiles — from <code>decisions[]</code></div><div style="display:flex;gap:10px">{fact("Squat max","160<span class=arrow>→</span>165","top set 5 × 160 kg")}{fact("Squat volume","−10%","42% of sets were grinds")}</div><div style="font-size:12px;color:#6F6A60;margin-top:12px;line-height:1.5">tm_bump / tm_cut → “a → b” · volume_pullback → “−10%” · corrective_added → “+ Name” · tm_hold / insufficient_evidence → “Held” · safety_exclusion → “n swapped”.</div></div>'
             f'<div class="comp"><div class="cn">Rail — ChevronProgress step / total</div><div style="display:flex;gap:40px;align-items:flex-start">{rail(3)}{rail(6,6)}</div><div style="font-size:12px;color:#6F6A60;margin-top:14px;line-height:1.5">espresso = done · burgundy = current · bone = ahead. Total = steps on this user’s path.</div></div>'
             f'<div class="comp"><div class="cn">Coach card — kicker + headline + body + meta</div><div class="card" style="padding:16px 20px"><div style="display:flex;justify-content:space-between;margin-bottom:8px"><div class="label" style="color:#5C262B">Coach · weekly review</div><div class="label-faint num">Sun 05.07</div></div><div class="display" style="font-size:19px;font-weight:700;line-height:1.2;margin-bottom:6px;color:#211E19">Your coaching review is ready</div><div class="meta">Squat training max up 5 kg. Calories held.</div><div class="meta" style="margin-top:10px;color:#857D6A">3 changes applied · tap for details</div></div></div>'
             f'<div class="comp"><div class="cn">Nudge actions — stacked, full width</div><div class="card" style="padding:16px 20px"><div class="label" style="color:#5C262B;margin-bottom:8px">Coach · your week, revised</div><div class="meta">Thursday’s session is gone. Nothing applies until you confirm.</div><div style="display:flex;flex-direction:column;gap:8px;margin-top:14px"><div class="btn btn-espresso" style="height:46px;font-size:14px">Apply the revised week</div><div class="btn" style="height:42px;font-size:14px;border:1px solid #E0D7C3;color:#77705F">Keep as scheduled</div></div></div></div>'
             f'<div class="comp darkc"><div class="cn">Sheet — handle, kicker, display title</div><div style="background:#2E2922;border:1px solid #3C362B;border-radius:20px 20px 0 0;padding:14px 24px 20px"><div style="width:36px;height:4px;border-radius:2px;background:#4A4338;margin:0 auto 14px"></div><div class="label-dark" style="margin-bottom:6px">Swap exercise</div><div class="display" style="font-size:22px;font-weight:700">SSB Box Squat</div></div></div>'
             f'<div class="comp"><div class="cn">Pills · tags · quality (gym 46)</div><div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px">{pill("75 min")}{pill("90 min",True)}{pill("Clear view",style="height:30px;font-size:12px")}</div><div style="background:#211E19;border-radius:14px;padding:12px;display:flex;gap:8px">{pill("Easy",False,True,"flex:1;height:46px;font-size:15px;border-radius:23px")}{pill("Solid",True,True,"flex:1;height:46px;font-size:15px;border-radius:23px")}{pill("Grind",False,True,"flex:1;height:46px;font-size:15px;border-radius:23px")}</div></div>'
             f'<div class="comp"><div class="cn">Tab bar — words only, index mark</div><div style="background:#F4EFE4;border-top:1px solid #E0D7C3;margin:0 -22px -22px;padding:10px 12px 18px">{TAB}</div></div>'
             f'</div>')
    copy_rows = [
        ("weakpoints.ts", "Off the floor", "Off the ground"),
        ("nutrition.ts", "already at the calorie floor · at the calorie floor (BMR × 1.1)", "already at the calorie minimum · at the calorie minimum (BMR × 1.1)"),
        ("squat.ts (Back Squat cue)", "Spread the floor — knees track over the toes.", "Push the ground apart — knees track over the toes."),
        ("floorpress anglesHint", "Film from the side at floor level, elbows visible.", "Film from the side at ground level, elbows visible. (The exercise name Floor Press is a proper noun and stays.)"),
        ("nutrition.tsx empty state", "Photograph your first meal — AI reads the macros.", "Photograph your first meal — the macros are read for you."),
        ("LogMealSheet fail title", "Couldn't reach the AI — you may be offline.", "Couldn't reach the server — you may be offline."),
        ("coach-review.tsx proposal", "Move to conjugate training (raw slug)", "display names: linear → “linear progression”, conjugate → “conjugate training”, hypertrophy → “hypertrophy blocks”"),
        ("index.tsx CoachCard", "three heading grammars", "kicker (Coach · weekly review / Coach · note) + headline sentence"),
        ("nutrition.tsx due card", "Meal logging pauses tomorrow until you do.", "Meal logging pauses soon until you do."),
        ("session.tsx Prev / hold Load", "kg only", "kg · lb"),
        ("plan-session.tsx loggedLine", "100 kg", "100 kg · 220 lb"),
        ("nutrition.tsx weight pill", "96.2 kg ›", "96.2 kg · 212 lb ›"),
    ]
    cr = ''.join(f'<tr><td><code>{a}</code></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in copy_rows)
    return (f'<div class="section" id="system"><h2 class="display">Summit v5 — system</h2><p class="lede">Everything the frames are built from. Palette unchanged except faint; type gets one display face; one icon family; one loader.</p><div class="ds">'
            f'<h3>Palette</h3><div class="swatches">{sw}</div>'
            f'<h3>Type scale</h3>{typ}'
            f'<h3>Icons — 2 px round stroke, 24 box, the chevron’s hand</h3><div class="icons">{icons}</div>'
            f'<h3>The loader</h3>{loaders}'
            f'<h3>Components that change</h3>{comps}'
            f'<h3>Copy fixes shipped with v5</h3><div class="wrap"><table class="map"><tr><th>Where</th><th>Today</th><th>v5</th></tr>{cr}</table></div>'
            f'</div></div>')

def impl():
    rows = [
        ("1", "<b>Tokens, font, icons.</b> <code>C.faint</code> → #857D6A; load Urbanist 600/700 (<code>@expo-google-fonts/urbanist</code>, splash held until loaded); <code>Display</code> text component; <code>Icon</code> component with the 18 glyphs (react-native-svg); <code>Pill</code> gains <code>size=\"lg\"</code>. Replace text glyphs app-wide.", "ui/index.tsx · ui/Icon.tsx · app/_layout.tsx · package.json", "~2.5 h"),
        ("2", "<b>LogoShimmer + button busy.</b> <code>Logo.tsx</code> gains <code>markOnly</code> (viewBox crop) and <code>reversed</code>; <code>LogoShimmer</code> = MaskedView (logo as mask) over a translating gradient band, Reanimated, 1.6 s; <code>AscendButton busy</code> keeps variant + band. Swap all 13 ThreeDotPulse sites; delete ThreeDotPulse.", "ui/Logo.tsx · ui/index.tsx · 11 call sites", "~2 h"),
        ("3", "<b>Labels.</b> New <code>uiStyles.meta</code> / <code>metaDark</code> (13/500 sentence case); move every sentence off labelDark (session position line, exercise-count line, Beat line, Prev, feedback kicker, confidence, Settings email).", "session.tsx · index.tsx · settings.tsx · sheets", "~1 h"),
        ("4", "<b>Gym mode declutter</b> (08/08b/09/09b/15/15b/08e): sizes, pill row with ⓘ + cue tag, set note → ExerciseInfoSheet “This set” + once-on-set-1 row, Prev line, AMRAP parity (Prev, Skip, hairline), hold target shown, carry per-hand card conditional, lb on Prev and Load.", "session.tsx · ExerciseInfoSheet.tsx · prescriptionFormat.ts", "~4 h"),
        ("5", "<b>Coaching review fact tiles</b> (21/21c): <code>FactTile</code> from <code>decisions[]</code> by kind; display names for methodologies; interim header fix; report reasons as Pill; empty state watermark.", "coach-review.tsx · lib/reviewFacts.ts (pure) · coachReview.ts", "~2.5 h"),
        ("6", "<b>Onboarding rail + rhythm</b> (03–05f): <code>ChevronProgress step/total</code> with path-aware total; shared <code>OnbHeader</code>; titles 34; Sex validation; logistics labels/units; typed inputs on body; 05f ready screen replacing 3 alerts.", "(onboarding)/* · ui/index.tsx", "~3 h"),
        ("7", "<b>Today + nudges + plan</b>: CoachCard kicker+headline; Settings icon; tab icons; nudge actions stacked; no-program slab actions; deload watermark on Plan/Today; chevrons/checks as icons; Plan no-program busy/warn without alerts.", "(tabs)/index.tsx · NudgeCards.tsx · plan.tsx · _layout.tsx", "~2.5 h"),
        ("8", "<b>Nutrition + sheets</b>: sheet handle on all 7 sheets; macro units; weight pill lb; due-card copy; form-check view-quality tag + finding detail + Try again; upload chooser sheet; copy fixes table; Settings email + Manage subscription row.", "nutrition.tsx · sheets/* · form-check.tsx · settings.tsx", "~3 h"),
        ("9", "<b>Design sync + docs</b>: v5 brief, How-It-Works §UI, defect ledger entries, screenshots on device; 446 tests + new pure tests for reviewFacts and rail totals.", "design-v5/* · docs/*", "~1.5 h"),
    ]
    r = ''.join(f'<tr><td>{a}</td><td>{b}</td><td><code>{c}</code></td><td>{d}</td></tr>' for a, b, c, d in rows)
    return (f'<div class="section" id="impl" style="padding-bottom:120px"><h2 class="display">Into code</h2><p class="lede">Nine chunks, each a commit, each leaving the app shippable. Roughly 22 hours; the gym-mode chunk is the one to review on the phone before the rest.</p>'
            f'<div class="ds"><div class="wrap"><table class="map"><tr><th>#</th><th>Chunk</th><th>Files</th><th>Est.</th></tr>{r}</table></div></div></div>')
