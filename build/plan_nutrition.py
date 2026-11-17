from lib import *

def prow(tag, name, right, faded=True, ondark=False, last=False, next_=False, done=False):
    if ondark:
        namecol = "var(--chalk)" if next_ else ("var(--dlabel)" if done else "var(--dbody)")
        deco = "text-decoration:line-through;" if done else ""
        rcol = "var(--burgundy-lt)" if next_ else "var(--dlabel)"
        return (f'<div style="display:flex;align-items:center;gap:12px;padding:13px 0;{"" if last else "border-bottom:1px solid var(--darkline)"}">{role(tag, not next_)}<div style="flex:1;font-size:14px;font-weight:{700 if next_ else 600};color:{namecol};{deco}">{name}</div><div class="num" style="font-size:12px;color:{rcol};font-weight:{800 if next_ else 600};letter-spacing:{".06em" if next_ else "0"}">{right}</div></div>')
    return (f'<div style="display:flex;align-items:center;gap:12px;padding:12px 0;{"" if last else "border-bottom:1px solid var(--bone)"}"><span style="opacity:.45">{role(tag)}</span><div style="flex:1;font-size:14px;font-weight:600;color:var(--faint)">{name}</div><div class="num" style="font-size:12px;color:var(--taupe);font-weight:700">{right}</div></div>')

def frames():
    F = []
    chk = ic("check",14,"#77705F",2.4)
    F.append(frame("s10b", "10b · Session detail (read view)",
        f'<div style="margin:8px 0 16px">{back("Coach")}</div><div class="label-faint">W2 · Intensification · Thursday</div><div style="display:flex;align-items:center;gap:10px;margin:4px 0 16px"><div class="title display">ME Upper</div>{role("ME",h=26,fs=11)}</div>'
        f'<div class="card" style="padding:0 20px">'
        f'<div style="padding:14px 0;border-bottom:1px solid var(--bone)"><div style="display:flex;justify-content:space-between;align-items:center;gap:12px"><div style="font-size:15px;font-weight:700">Apollon OHP</div><div class="num" style="font-size:12px;color:var(--taupe);font-weight:600;text-align:right">3 × 80 · 3 × 85 ·<br>work up to 3RM · 92.5 kg</div></div><div class="num" style="font-size:12px;color:var(--faint);margin-top:3px">main · 92.5 kg · 204 lb · Load over reps</div></div>'
        f'<div style="padding:14px 0;border-bottom:1px solid var(--bone)"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:15px;font-weight:700">Close-grip Bench</div><div class="num" style="font-size:12px;color:var(--taupe);font-weight:600">4 × 8</div></div><div class="num" style="font-size:12px;color:var(--faint);margin-top:3px">variation · 100 kg · 220 lb · Reps over load</div></div>'
        f'<div style="padding:14px 0;border-bottom:1px solid var(--bone)"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:15px;font-weight:700">Chest-supported Row</div><div class="num" style="font-size:12px;color:var(--taupe);font-weight:600">4 × 10</div></div><div class="num" style="font-size:12px;color:var(--faint);margin-top:3px">accessory · 60 kg · 132 lb · Reps over load</div></div>'
        f'<div style="padding:14px 0"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:15px;font-weight:700">Face Pull</div><div class="num" style="font-size:12px;color:var(--taupe);font-weight:600">3 × 15</div></div><div class="num" style="font-size:12px;color:var(--faint);margin-top:3px">accessory · Range over load</div></div></div>'
        f'<div class="card" style="padding:12px 16px;margin-top:16px"><div class="meta">Loads are today’s projection from your training max — they move if this week’s sessions move them.</div></div>',
        "As built. A completed session's logged line gains the lb secondary (“4 × 6 · 100 kg · 220 lb · mostly solid”)."))
    # Nutrition
    def macro_cols(dark, muted=False):
        lab = "label-dark" if dark else "label-faint"; col = "var(--faint)" if muted else ("var(--chalk)" if dark else "var(--charcoal)"); sub = "var(--dlabel)" if dark else "var(--faint)"; line = "var(--darkline)" if dark else "var(--bone)"
        def c(n, v, t): return f'<div style="flex:1"><div class="{lab}">{n}</div><div class="display" style="font-size:22px;font-weight:700;margin-top:4px;color:{col}">{v}<span style="font-size:12px;color:{sub};font-weight:600;font-family:var(--body)"> / {t} g</span></div></div>'
        return f'<div style="display:flex">{c("Protein","142" if not muted else "0","190")}<div style="width:1px;background:{line};margin:0 14px"></div>{c("Carbs","156" if not muted else "0","220")}<div style="width:1px;background:{line};margin:0 14px"></div>{c("Fat","58" if not muted else "0","72")}</div>'
    nut_hdr = lambda trend=True: f'<div style="margin-bottom:16px"><div class="label-faint">Cut · week 6 · <span style="color:{"var(--burgundy)" if trend else "var(--faint)"}">trend −0.4 kg/wk</span></div><div class="title display" style="margin-top:4px">Nutrition</div></div>'
    hero = slab(f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px"><div class="display" style="font-size:46px;font-weight:700;line-height:1">1,780</div><div class="num" style="font-size:14px;color:var(--dlabel);font-weight:600">of 2,340 kcal</div></div><div style="height:6px;background:var(--darkline);border-radius:3px;overflow:hidden;margin-bottom:18px"><div style="width:76%;height:100%;background:var(--chalk);border-radius:3px"></div></div>{macro_cols(True)}', "padding:22px 24px")
    def meal(n, t, k, last=False): return f'<div style="display:flex;justify-content:space-between;align-items:center;padding:13px 0;{"" if last else "border-bottom:1px solid var(--bone)"}"><div><div style="font-size:15px;font-weight:700">{n}</div><div class="num" style="font-size:12px;color:var(--faint);margin-top:2px;font-weight:500">{t}</div></div><div class="display" style="font-size:17px;font-weight:700">{k}<span style="font-size:11px;color:var(--faint);font-weight:600;font-family:var(--body)"> kcal</span></div></div>'
    weight_row = f'<div class="card" style="padding:12px 18px;display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:13px;color:var(--taupe);font-weight:600">Morning weight</div><div style="font-size:12px;color:var(--faint);font-weight:500;margin-top:2px">optional — sharpens the trend</div></div><div class="pill num" style="height:30px;font-size:12px;padding:0 12px;gap:4px">96.2 kg · 212 lb{ic("chev-right",12,"#77705F")}</div></div>'
    F.append(frame("s11", "11 · Nutrition — meals logged",
        nut_hdr() + hero + f'<div style="height:14px"></div>{btn("Log meal — point camera at plate","burgundy",54,icon=ic("camera",18,"#F7F3E9",2))}<div style="height:12px"></div>{weight_row}'
        f'<div style="margin-top:14px"><div class="label-faint" style="margin-bottom:4px">Today</div>{meal("Chicken &amp; rice bowl","12:40 · estimate","620")}{meal("Skyr &amp; berries","09:15 · estimate","240")}{meal("Eggs &amp; sourdough","07:30 · edited","430",True)}</div>'
        f'<div class="card" style="padding:14px 18px;border:1.5px solid var(--burgundy);display:flex;justify-content:space-between;align-items:center;margin-top:8px"><div><div style="font-size:13px;font-weight:700">Check-in due — weigh in to keep targets fresh</div><div class="meta" style="font-size:12px;margin-top:2px">Meal logging pauses soon until you do. Takes 30 seconds.</div></div>{ic("chev-right",16,"#5C262B")}</div>'
        f'<div style="flex:1"></div>{tabbar("nutrition")}',
        "Macro columns gain their unit (“142 / 190 g”). The morning-weight pill gains lb. The camera glyph is the stroke icon. Due-card copy stops promising “tomorrow” (the gate trips at day 8 of any weigh-in). <b>v5.1:</b> The calorie bar fills from zero and follows the number as meals are logged; the hero slab carries the shadow and settles in once the numbers are real."))
    F.append(frame("s12", "12 · Nutrition — nothing logged yet",
        nut_hdr() + card(f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px"><div class="display" style="font-size:46px;font-weight:700;line-height:1;color:var(--faint)">0</div><div class="num" style="font-size:14px;color:var(--faint);font-weight:600">of 2,340 kcal</div></div><div class="progressline" style="height:6px;margin-bottom:18px"><div style="width:0"></div></div>{macro_cols(False,True)}', "padding:22px 24px;border-radius:20px") +
        f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center">{mark(120, opacity=.35)}<div class="subtitle" style="max-width:240px">Nothing logged yet.<br>Photograph your first meal — the macros are read for you.</div></div>'
        f'{btn("Log meal","burgundy",54,icon=ic("camera",18,"#F7F3E9",2),extra="margin-bottom:8px")}{tabbar("nutrition")}',
        "Zeroes faint, never red. Copy no longer leads with “AI” (the provenance label deliberately says estimate)."))
    F.append(frame("s12b", "12b · Nutrition — targets didn't load",
        nut_hdr(False) + f'<div class="card" style="padding:18px 20px;display:flex;flex-direction:column;gap:6px"><div style="font-size:14px;font-weight:600;color:var(--burgundy);line-height:1.5">Your targets didn’t load.</div><div style="font-size:13px;font-weight:700;margin-top:6px">Try again</div></div>'
        f'<div style="height:14px"></div>{btn("Log meal — point camera at plate","burgundy",54,icon=ic("camera",18,"#F7F3E9",2))}<div style="height:12px"></div>{weight_row}'
        f'<div style="margin-top:14px"><div class="label-faint" style="margin-bottom:4px">Today</div>{meal("Skyr &amp; berries","09:15 · estimate","240",True)}</div><div style="flex:1"></div>{tabbar("nutrition")}',
        "Logging never blocks on targets. The hero becomes the ErrorCard; meals and the log button stay."))
    F.append(frame("s11b", "11b · Nutrition — logging paused behind the check-in",
        nut_hdr() + hero + f'<div style="height:14px"></div><div class="card" style="padding:16px 18px;border:1.5px solid var(--burgundy);display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:15px;font-weight:700;color:var(--burgundy)">Weigh in to keep logging — 30 seconds</div><div class="meta" style="font-size:12px;margin-top:2px">Targets go stale without weight data — the check-in refreshes them.</div></div>{ic("chev-right",16,"#5C262B")}</div>'
        f'<div style="height:12px"></div>{weight_row}<div style="flex:1"></div>{tabbar("nutrition")}',
        "As built: the gate replaces the Log meal button; never a dead end."))

    # Log meal sheets
    dimn = f'<div style="padding:0 24px;opacity:.35;display:flex;flex-direction:column;gap:16px">{nut_hdr()}<div class="slab" style="height:130px"></div></div>' + backdrop()
    F.append(frame("s17a", "17a · Log meal — capture",
        dimn + sheet(sheet_head("Log meal","Point camera at plate") + hr(True) + f'<div style="display:flex;flex-direction:column;gap:10px">{btn("Take photo","chalk",icon=ic("camera",18,"#211E19",2))}{btn("Choose from library","ghostDark",48,14)}{btn("Choose from Files","ghostDark",48,14)}{btn("Enter manually","ghostDark",48,14)}</div>'),
        "As built, plus the handle.", screen_style="padding:8px 0 0"))
    F.append(frame("s17d", "17d · Log meal — reading your plate",
        dimn + sheet(sheet_head("Log meal","Reading your plate") + hr(True) + f'<div style="height:160px;border-radius:14px;border:1px solid var(--darkline);background:linear-gradient(160deg,#17140F,#0D0B08)"></div><div style="display:flex;flex-direction:column;align-items:center;padding:6px 0 4px">{shimmer(84, True, "Reading your plate")}</div>'),
        "Logo loader under the local thumbnail. No ellipsis anywhere.", screen_style="padding:8px 0 0"))
    def item(n, k, g, p, c, f_, low=False):
        v = lambda x, u: f'<span style="border-bottom:1px dashed #6B655A">{x}<span style="font-size:11px;color:var(--dlabel);font-weight:600"> {u}</span></span>'
        return (f'<div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:15px;font-weight:700;color:var(--chalk)">{n}</div><div class="display" style="font-size:17px;font-weight:700;color:var(--chalk)">{v(k,"kcal")}</div></div>'
                f'<div class="num" style="display:flex;gap:18px;font-size:13px;font-weight:700;color:var(--chalk)">{v(g,"g")}{v(p,"P")}{v(c,"C")}{v(f_,"F")}</div>' + (f'<div style="font-size:12px;color:var(--dlabel);font-weight:500">low confidence — check this</div>' if low else '') + hr(True))
    F.append(frame("s17", "17 · Log meal — estimate, editable",
        dimn + sheet(sheet_head("Log meal · estimate — review before saving","Chicken &amp; rice bowl + 2 more") + hr(True) +
            '<div style="height:72px;border-radius:14px;border:1px solid var(--darkline);background:linear-gradient(160deg,#17140F,#0D0B08)"></div>' +
            item("Grilled chicken breast","297","180","56","0","7") + item("White rice, cooked","325","250","6","71","1") + item("Sauce / cooking oil","130","30","0","3","14",True) +
            f'<div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:15px;font-weight:800;color:var(--chalk)">Total</div><div class="display" style="font-size:17px;font-weight:700;color:var(--chalk)">752<span style="font-size:11px;color:var(--dlabel);font-weight:600;font-family:var(--body)"> kcal</span></div></div><div class="num" style="font-size:12px;color:var(--dlabel);font-weight:600">62 P · 74 C · 22 F</div>'
            + btn("Log meal","chalk") + btn("Retake photo","ghostDark",48,14), pad="22px 24px 30px"),
        "As built. Dashed values are tap-to-edit; totals recompute live.", screen_style="padding:8px 0 0"))
    F.append(frame("s17c", "17c · Log meal — photo couldn't be read",
        dimn + sheet(sheet_head("Log meal","Couldn't read the plate.") + hr(True) + '<div style="font-size:14px;color:var(--dbody);line-height:1.5">Nothing was logged. Enter the meal manually, or try another photo.</div>' + btn("Enter manually","chalk") + btn("Retake photo","ghostDark",48,14)),
        "The failure state drawn; the three failure titles stay as built. Offline variant reads “Couldn't reach the server — you may be offline.” (no “AI” lead).", screen_style="padding:8px 0 0"))
    F.append(frame("s17b", "17b · Log meal — manual entry",
        dimn + sheet(sheet_head("Log meal · manual","What did you eat?") + hr(True) +
            '<div style="background:var(--charcoal);border:1px solid var(--darkline);border-radius:14px;padding:14px 16px;color:var(--chalk);font-size:15px;font-weight:600">Chicken breast, 250 g|</div>'
            f'<div style="display:flex;gap:6px;flex-wrap:wrap">{pill("Chicken breast 250 g · 77P 0C 8F",False,True,"height:32px;font-size:12px;color:var(--chalk)")}{pill("Chicken &amp; rice bowl (yours)",False,True,"height:32px;font-size:12px")}</div>'
            + '<div style="display:flex;gap:8px">' + ''.join(f'<div style="flex:1;background:var(--charcoal);border:1px solid var(--darkline);border-radius:14px;padding:11px 12px;text-align:center"><div class="label-dark">{n}</div><div class="display" style="font-size:24px;font-weight:700;color:var(--chalk);margin-top:3px">{v}<span style="font-size:11px;color:var(--dlabel);font-family:var(--body)"> g</span></div></div>' for n, v in [("Protein","77"),("Carbs","0"),("Fat","8")]) + '</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;padding:2px 4px"><div class="label-dark">Calories — computed</div><div class="display" style="font-size:26px;font-weight:700;color:var(--chalk)">380<span style="font-size:12px;color:var(--dlabel);font-weight:600;font-family:var(--body)"> kcal</span></div></div>' + btn("Log meal","chalk")),
        "As built: grams in, kcal computed, never typed.", screen_style="padding:8px 0 0"))

    # Morning weight + check-in
    weigh = lambda v, lb: f'<div style="display:flex;align-items:center;justify-content:space-between;padding:8px 0">{stepper("-",54,True)}<div style="text-align:center"><div class="display" style="font-size:64px;font-weight:700;color:var(--chalk);line-height:1">{v}</div><div class="num" style="font-size:13px;color:var(--dlabel);font-weight:600;margin-top:4px">kg · {lb} lb</div></div>{stepper("+",54,True)}</div>'
    F.append(frame("s18a", "18a · Morning weight",
        dimn + sheet(sheet_head("Morning weight","This morning’s weight") + hr(True) + weigh("96.2","212") + btn("Log weight","chalk")),
        "As built, display numeral at 64.", screen_style="padding:8px 0 0"))
    F.append(frame("s18", "18 · Weekly check-in",
        dimn + sheet(sheet_head("Weekly check-in","This morning’s weight") + hr(True) + weigh("96.2","212") +
            f'<div style="display:flex;justify-content:space-between;align-items:center;background:var(--charcoal);border:1px solid var(--darkline);border-radius:14px;padding:12px 16px"><div style="display:flex;align-items:center;gap:8px"><div class="label-dark">Compliance last 7 days</div>{ic("info",14,"#A09580",2)}</div><div class="display" style="font-size:17px;font-weight:700;color:var(--chalk)">71<span style="font-size:11px;color:var(--dlabel);font-family:var(--body)">%</span></div></div>'
            f'<div style="font-size:12px;color:var(--dlabel);line-height:1.45;padding:0 2px">A day counts when calories land within 10% of target and protein is at least 90% there.</div>'
            f'<div style="background:var(--charcoal);border:1px solid var(--darkline);border-radius:14px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center"><div><div class="label-dark">Waist or body fat</div><div style="font-size:11px;color:var(--dlabel);margin-top:2px">optional — second signal for the trend</div></div><div style="display:flex;gap:6px">{pill("Waist",True,True,"height:30px;font-size:11px;padding:0 12px")}{pill("BF %",False,True,"height:30px;font-size:11px;padding:0 12px")}</div></div>'
            + btn("Run check-in","chalk")),
        "As built; the ⓘ is the stroke icon.", screen_style="padding:8px 0 0"))
    F.append(frame("s18b", "18b · Check-in — result with a proposal",
        dimn + sheet(sheet_head("Weekly check-in · result","Held") + hr(True) +
            '<div style="font-size:14px;color:var(--dbody);line-height:1.5;font-weight:500">Cut complete (at the calorie minimum, BMR × 1.1). Reverse diet proposed: +50 kcal/week to 2,900 kcal.</div>'
            f'<div style="background:var(--charcoal);border:1px solid var(--darkline);border-radius:16px;padding:16px"><div class="label-dark" style="color:var(--burgundy-lt);margin-bottom:6px">Coach proposal</div><div style="font-size:14px;font-weight:600;color:var(--chalk);line-height:1.45;margin-bottom:12px">At the calorie minimum — reverse diet, +50 kcal a week toward 2,900 kcal maintenance.</div>{btn("Accept reverse diet","chalk",48,14)}<div style="height:8px"></div>{btn("Not now","ghostDark",44,14)}</div>'),
        "Copy: <b>“calorie floor” becomes “calorie minimum”</b> in the engine's notes and proposal reasons; proposal reasons start with a capital. Structure as built.", screen_style="padding:8px 0 0"))
    return F
