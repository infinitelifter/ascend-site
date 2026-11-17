from lib import *
from plan_nutrition import prow

# ── Coach tab — the coach holds the plan (approved 2026-10-05) ──────────────
# Three things, in this order: the next seven days, what the coach is doing,
# where you're going. The cycle view moves behind a quiet "Full plan" link.

def coach_hdr(kicker="Conjugate · week 2 of 12", full_plan=True):
    link = (f'<div style="display:flex;align-items:center;gap:2px;padding-bottom:9px;font-size:13px;font-weight:600;color:var(--taupe);white-space:nowrap">Full plan{ic("chev-right",14,"#77705F",2)}</div>'
            if full_plan else '')
    return (f'<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:16px">'
            f'<div><div class="label-faint">{kicker}</div><div class="title display" style="margin-top:4px">Coach</div></div>{link}</div>')

def day_card(day, tag, lift, mins, today=False, rest=False):
    """One of the seven-day strip cards: weekday · role tag · main lift · ≈minutes."""
    if rest:
        return (f'<div style="flex:0 0 auto;width:76px;border:1px solid var(--bone);border-radius:14px;padding:12px 13px;display:flex;flex-direction:column;gap:6px;opacity:.55">'
                f'<div class="label-faint">{day}</div><div style="font-size:13px;color:var(--faint);font-weight:600;line-height:1.3;height:34px">Rest</div><div class="num" style="font-size:11px;color:var(--faint);font-weight:600">—</div></div>')
    bg = "background:var(--charcoal);border-color:var(--charcoal);color:var(--chalk)" if today else "background:var(--cream)"
    lab = "label-dark" if today else "label-faint"
    sub = "var(--dlabel)" if today else "var(--faint)"
    return (f'<div class="card" style="flex:0 0 auto;width:118px;padding:12px 13px;display:flex;flex-direction:column;gap:6px;border-radius:14px;{bg}">'
            f'<div style="display:flex;justify-content:space-between;align-items:center"><div class="{lab}">{day}</div>{role(tag, ondark=today, h=20, fs=9)}</div>'
            f'<div style="font-size:13px;font-weight:700;line-height:1.3;height:34px">{lift}</div>'
            f'<div class="num" style="font-size:11px;color:{sub};font-weight:600">≈ {mins} min</div></div>')

def strip(cards, kicker="Next seven days"):
    return (f'<div style="margin-bottom:22px"><div class="label-faint" style="margin-bottom:10px">{kicker}</div>'
            f'<div style="display:flex;gap:8px;overflow:hidden;margin-right:-24px;padding-right:24px">{"".join(cards)}</div></div>')

def feed_date(day):
    return f'<div class="label-faint num" style="margin:14px 0 8px">{day}</div>'

def feed_tile(kicker, value, detail, reason, size=24):
    """A decision as a fact tile with the reason under it — full width, smaller numeral than the review's."""
    r = f'<div class="meta" style="margin-top:8px;padding-top:8px;border-top:1px solid var(--bone)">{reason}</div>' if reason else ''
    return (f'<div class="card" style="padding:13px 16px;display:flex;flex-direction:column;gap:3px;border-radius:16px">'
            f'<div class="label">{kicker}</div><div class="display num" style="font-size:{size}px;font-weight:700;line-height:1.1;color:var(--charcoal)">{value}</div>'
            f'<div style="font-size:12px;color:var(--taupe);line-height:1.4">{detail}</div>{r}</div>')

def feed_review(headline, meta):
    """Weekly review — the headline item (tap → the review screen)."""
    return (f'<div class="card" style="padding:15px 18px;display:flex;justify-content:space-between;align-items:center;gap:12px">'
            f'<div><div class="label" style="color:var(--burgundy);margin-bottom:6px">Coach · weekly review</div><div class="display" style="font-size:18px;font-weight:700;line-height:1.2">{headline}</div><div class="meta" style="margin-top:5px;color:var(--faint)">{meta}</div></div>{ic("chev-right",16,"#857D6A")}</div>')

def feed_line(kicker, text, burgundy=False):
    """A quiet one-line item: the week nothing changed, the pre-session framing, a moved day."""
    col = "color:var(--burgundy)" if burgundy else ""
    return f'<div class="card" style="padding:13px 16px"><div class="label" style="{col};margin-bottom:5px">{kicker}</div><div class="meta" style="color:var(--charcoal)">{text}</div></div>'

def feed(items):
    return f'<div style="display:flex;flex-direction:column;gap:8px"><div class="label-faint" style="margin-bottom:2px">What the coach is doing</div>{"".join(items)}</div>'

def going(rows, block, event=None):
    """Where you're going: one factual line per main lift, the block position, the countdown when peaking."""
    def r(name, tm, lb, nxt, last=False):
        return (f'<div style="display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 0;{"" if last else "border-bottom:1px solid var(--bone)"}">'
                f'<div><div style="font-size:15px;font-weight:700">{name}</div><div class="num" style="font-size:12px;color:var(--faint);margin-top:2px;font-weight:500">{nxt}</div></div>'
                f'<div class="display num" style="font-size:19px;font-weight:700;text-align:right;white-space:nowrap">{tm}<span style="font-size:11px;color:var(--faint);font-weight:600;font-family:var(--body)"> kg · {lb} lb</span></div></div>')
    body = ''.join(r(*row, last=(i == len(rows) - 1)) for i, row in enumerate(rows))
    ev = f'<div class="meta" style="margin-top:4px;color:var(--burgundy);font-weight:600">{event}</div>' if event else ''
    return (f'<div style="margin-top:22px"><div class="label-faint" style="margin-bottom:10px">Where you’re going</div>'
            f'<div class="card" style="padding:2px 18px">{body}</div>'
            f'<div class="card" style="padding:13px 18px;margin-top:8px"><div style="font-size:14px;font-weight:700">Week 2 of 12 · Intensification</div><div class="meta" style="margin-top:3px">{block}</div>{ev}</div></div>')


# ── Variant B (2026-10-05): the coach gets the slab; the feed is a timeline ──
def feed_slab(kicker, headline, body, meta=None, chevron=True):
    """The coach's newest item, in the app's voice: an espresso slab. Weekly review headline or today's framing."""
    hl = f'<div class="display" style="font-size:22px;font-weight:600;line-height:1.2;margin-bottom:8px">{headline}</div>' if headline else ''
    m = f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:14px;padding-top:12px;border-top:1px solid var(--darkline)"><div class="meta-dark">{meta}</div>{ic("chev-right",16,"#A09580") if chevron else ""}</div>' if meta else ''
    return (f'<div class="slab" style="padding:20px 22px"><div class="label-dark" style="color:var(--burgundy-lt);margin-bottom:10px">{kicker}</div>{hl}'
            f'<div style="font-size:14px;line-height:1.5;color:var(--dbody);font-weight:500">{body}</div>{m}</div>')

def tl_date(day, first=False):
    """Date kicker on the timeline — plain, no card."""
    return f'<div class="label-faint num" style="margin:{"4px" if first else "18px"} 0 6px">{day}</div>'

def tl_line(kicker, text, last=False):
    """A quiet note as a hairline row: kicker · sentence. No card."""
    return (f'<div style="padding:10px 0;{"" if last else "border-bottom:1px solid var(--bone)"}"><div class="label" style="margin-bottom:4px">{kicker}</div>'
            f'<div style="font-size:14px;line-height:1.45;color:var(--charcoal);font-weight:500">{text}</div></div>')

def tl_review(headline, meta):
    """An older weekly review — a hairline row with a chevron, not a card (the newest one is the slab)."""
    return (f'<div style="display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid var(--bone)">'
            f'<div><div class="label" style="color:var(--burgundy);margin-bottom:4px">Coach · weekly review</div><div style="font-size:15px;font-weight:700;line-height:1.3">{headline}</div><div class="meta" style="margin-top:2px;color:var(--faint)">{meta}</div></div>{ic("chev-right",16,"#857D6A")}</div>')

def tl_tiles(tiles):
    """Decisions keep the fact-tile grammar — a pair per row, like the review."""
    rows = []
    for i in range(0, len(tiles), 2):
        pair = tiles[i:i+2]
        if len(pair) == 1: pair.append('<div style="flex:1"></div>')
        rows.append(f'<div style="display:flex;gap:8px">{"".join(pair)}</div>')
    return f'<div style="display:flex;flex-direction:column;gap:8px;margin:8px 0 4px">{"".join(rows)}</div>'

def tl_fact(k, v, d, size=24):
    return f'<div class="fact" style="padding:12px 14px;border-radius:14px"><div class="k">{k}</div><div class="v display" style="font-size:{size}px">{v}</div><div class="d">{d}</div></div>'

def tl_feed(inner):
    return f'<div><div class="label-faint" style="margin-bottom:8px">What the coach is doing</div>{inner}</div>'


# ── Final (C, 2026-10-05): slab for this week, boxes for the facts, a railed timeline for history, where you're going at the bottom ──
def c_slab(kicker, headline, body, foot):
    return (f'<div class="slab lift" style="padding:20px 22px"><div class="label-dark" style="color:var(--burgundy-lt);margin-bottom:10px">{kicker}</div>'
            f'<div class="display" style="font-size:24px;font-weight:600;line-height:1.2;margin-bottom:8px">{headline}</div>'
            f'<div style="font-size:14px;line-height:1.5;color:var(--dbody);font-weight:500">{body}</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:14px;padding-top:12px;border-top:1px solid var(--darkline)"><div class="meta-dark">{foot}</div>{ic("chev-right",16,"#A09580")}</div></div>')

def c_tiles(tiles):
    rows = []
    for i in range(0, len(tiles), 2):
        pair = tiles[i:i+2]
        if len(pair) == 1: pair.append('<div style="flex:1"></div>')
        rows.append(f'<div style="display:flex;gap:8px">{"".join(pair)}</div>')
    return f'<div style="display:flex;flex-direction:column;gap:8px;margin-top:8px">{"".join(rows)}</div>'

def c_divider(label):
    """The visual break between now and history: a kicker between two hairlines."""
    return (f'<div style="display:flex;align-items:center;gap:12px;margin:24px 0 14px"><div style="flex:1;height:1px;background:var(--bone)"></div>'
            f'<div class="label-faint">{label}</div><div style="flex:1;height:1px;background:var(--bone)"></div></div>')

def c_entry(date, inner, last=False, strong=False):
    """One timeline entry on the rail: a dot (burgundy when the coach changed something), the line down to the next."""
    dot = f'<div style="width:9px;height:9px;border-radius:5px;background:{"var(--burgundy)" if strong else "var(--bone)"};margin-top:3px;flex:0 0 auto;{"" if strong else "border:1.5px solid var(--faint);width:8px;height:8px;background:var(--paper)"}"></div>'
    line = '' if last else '<div style="flex:1;width:1.5px;background:var(--bone);margin-top:4px"></div>'
    return (f'<div style="display:flex;gap:12px"><div style="width:10px;display:flex;flex-direction:column;align-items:center">{dot}{line}</div>'
            f'<div style="flex:1;min-width:0;padding-bottom:{0 if last else 18}px"><div class="label-faint num" style="margin-bottom:5px">{date}</div>{inner}</div></div>')

def c_review_row(headline, meta):
    return (f'<div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><div><div style="font-size:15px;font-weight:700;line-height:1.3">{headline}</div><div class="meta" style="margin-top:2px;color:var(--faint)">{meta}</div></div>{ic("chev-right",16,"#857D6A")}</div>')

def c_line(text):
    return f'<div style="font-size:14px;line-height:1.45;color:var(--charcoal);font-weight:500">{text}</div>'

def c_going(rows, block, event=None):
    """Where you're going — the footer. Each lift: current max, the move this block (burgundy arrow), the next top set that can move it."""
    def r(name, tm, lb, since, nxt, last=False):
        mv = f'<span style="color:var(--burgundy);font-weight:700"> {since}</span>' if since else ''
        return (f'<div style="display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 0;{"" if last else "border-bottom:1px solid var(--bone)"}">'
                f'<div style="min-width:0"><div style="font-size:15px;font-weight:700">{name}{mv}</div><div class="num" style="font-size:12px;color:var(--faint);margin-top:2px;font-weight:500">{nxt}</div></div>'
                f'<div class="display num" style="font-size:20px;font-weight:700;text-align:right;white-space:nowrap">{tm}<span style="font-size:11px;color:var(--faint);font-weight:600;font-family:var(--body)"> kg · {lb} lb</span></div></div>')
    body = ''.join(r(*row, last=(i == len(rows) - 1)) for i, row in enumerate(rows))
    ev = f'<div class="meta" style="margin-top:4px;color:var(--burgundy);font-weight:600">{event}</div>' if event else ''
    return (f'<div>{c_divider("Where you’re going")}'
            f'<div class="card" style="padding:2px 18px">{body}</div>'
            f'<div class="card" style="padding:13px 18px;margin-top:8px;display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:14px;font-weight:700">Week 2 of 12 · Intensification</div><div class="meta" style="margin-top:3px">{block}</div>{ev}</div><div style="display:flex;gap:4px">{chev("#211E19",16)}{chev("#5C262B",16)}{chev("#E0D7C3",16)}</div></div></div>')


# ── Final v2 (2026-10-05, after the "still busy" pass): four things, nothing twice ──
def c_lifts(rows):
    """Where you're going, reduced to the four lift rows; the block position lives in the header kicker."""
    def r(name, tm, lb, since, nxt, last=False):
        mv = f'<span style="color:var(--burgundy);font-weight:700"> {since}</span>' if since else ''
        # v5.1 — the trend line under the max: level when held, a rise ending in the burgundy dot when it moved
        when = {"Squat": .86, "Deadlift": .42, "Press": .7}.get(name, .6)
        tl = trend([(0, 0), (when, 1), (1, 1)] if since else [(0, 1), (1, 1)])
        return (f'<div style="display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 0;{"" if last else "border-bottom:1px solid var(--bone)"}">'
                f'<div style="min-width:0"><div style="font-size:15px;font-weight:700">{name}{mv}</div><div class="num" style="font-size:12px;color:var(--faint);margin-top:2px;font-weight:500">{nxt}</div></div>'
                f'<div style="display:flex;flex-direction:column;align-items:flex-end;gap:3px"><div class="display num" style="font-size:20px;font-weight:700;line-height:23px;text-align:right;white-space:nowrap">{tm}<span style="font-size:11px;color:var(--faint);font-weight:600;font-family:var(--body)"> kg · {lb} lb</span></div>{tl}</div></div>')
    body = ''.join(r(*row, last=(i == len(rows) - 1)) for i, row in enumerate(rows))
    return f'<div style="margin-top:22px"><div class="label-faint" style="margin-bottom:10px">Where you’re going</div><div class="card" style="padding:2px 18px">{body}</div></div>'

def c_earlier(summary, open_=False):
    """The history, collapsed to one row by default; tap expands the railed timeline in place."""
    return (f'<div class="card" style="padding:13px 18px;margin-top:10px;display:flex;justify-content:space-between;align-items:center">'
            f'<div><div class="label-faint" style="margin-bottom:3px">Earlier</div><div style="font-size:14px;font-weight:600;color:var(--taupe)">{summary}</div></div>{ic("chev-up" if open_ else "chev-down",16,"#857D6A")}</div>')

def frames():
    F = []
    chk = ic("check",14,"#77705F",2.4)

    week = [day_card("Today","ME","SSB Box Squat",75,today=True), day_card("Wed","ME","",0,rest=True), day_card("Thu","ME","Apollon OHP",65), day_card("Sat","DE","Trap-bar Speed Pull",55), day_card("Sun","RE","Rep work + carries",50)]
    week_rest = [day_card("Tue","ME","SSB Box Squat",75), day_card("Thu","ME","Apollon OHP",65), day_card("Sat","DE","Trap-bar Speed Pull",55), day_card("Sun","RE","Rep work + carries",50)]
    lifts = [("Squat","165","364","next top set Tue · SSB Box Squat"),("Bench","110","243","no top set this week · held"),("Deadlift","202.5","446","next top set Sat · speed pull, no test"),("Press","62.5","138","next top set Thu · Apollon OHP")]



    # ── C2 — the one design, calmed (2026-10-05) ──
    F.append(frame("s10", "10 · Coach — the tab",
        coach_hdr("Week 2 of 12 · deload in week 3") + strip(week) +
        f'<div class="label-faint" style="margin-bottom:8px">What the coach is doing</div>' +
        c_slab("Coach · this week", "Squat max up, knee work added", "Your squat moved on Sunday’s review; two sessions of Cossack squats guard the knee flag. Today: Max Effort Lower, SSB Box Squat — the top set drives the squat max. About 75 minutes.", "3 changes · squat max 160<span style=color:var(--burgundy);font-weight:600>&nbsp;→&nbsp;</span>165") +
        c_lifts([("Squat","165","364","+5 this block","next top set today · SSB Box Squat"),("Bench","110","243","","no top set this week · held"),("Deadlift","202.5","446","+2.5","speed pull Sat · no test"),("Press","62.5","138","+2.5","next top set Thu · Apollon OHP")]) +
        c_earlier("4 entries this block · last Thu 02.07") +
        f'<div style="flex:1"></div>{tabbar("coach")}',
        "<b>Four things, nothing twice.</b> The strip; the coach on the slab — this week in two sentences plus today's framing, the foot line carrying the headline number (“3 changes · squat max 160 → 165”), tap → the review where the fact tiles and the four sections live; <i>where you're going</i> as the four lift rows (max · kg · lb · the move this block in burgundy · the next top set that can move it); and the history collapsed to one row. The block position moved into the header kicker (“Week 2 of 12 · deload in week 3”; the methodology name lives on Full plan, the event countdown joins the kicker when peaking), so the separate block card is gone. Everything from the previous draft is still one tap away. <b>v5.1:</b> Each lift row carries a 64×14 trend line under its max — where the training max has been this block, rebuilt from the ledger; a level bone line when held, an espresso line ending in a burgundy dot when it moved. No axes, no animation. The slab gets the one shadow in the app; the four parts settle in once, 50 ms apart.", screen_style="padding-bottom:0"))

    F.append(frame("s10a", "10a · Coach — Earlier, expanded",
        '<div style="margin-top:-6px">' + c_lifts([("Squat","165","364","+5 this block","next top set today · SSB Box Squat"),("Bench","110","243","","no top set this week · held"),("Deadlift","202.5","446","+2.5","speed pull Sat · no test"),("Press","62.5","138","+2.5","next top set Thu · Apollon OHP")]) + c_earlier("4 entries this block · last Thu 02.07", open_=True) +
        '<div style="padding:16px 4px 0">' +
        c_entry("Thu 02.07", c_line("Deadlift max 200 → 202.5 kg — beat the target 8 × 180 kg in the session."), strong=True) +
        c_entry("Tue 30.06", c_line("Thursday’s session moved to Saturday — a missed day, spacing kept.")) +
        c_entry("Sun 28.06", c_review_row("Nothing needed changing", "every session on target · maxes holding")) +
        c_entry("Sun 21.06", c_review_row("Phase review — intensification starts", "2 changes · tap for details"), strong=True, last=True) +
        f'<div style="text-align:center;font-size:13px;font-weight:600;color:var(--faint);margin-top:16px">All reviews</div></div></div>' +
        f'<div style="flex:1"></div>{tabbar("coach")}',
        "The Earlier row tapped: the railed timeline opens in place under it — burgundy dot where the coach changed something, hollow where it only noted; review rows open the review screen (its own tiles live there), “All reviews” for everything beyond the block. Closed again with the chevron. Scrolled slightly so the whole list shows.", screen_style="padding-bottom:0"))

    F.append(frame("s10c", "10c · Coach — a quiet week",
        coach_hdr("Week 5 of 12 · deload in week 6") + strip(week_rest) +
        f'<div class="label-faint" style="margin-bottom:8px">What the coach is doing</div>' +
        c_slab("Coach · this week", "Nothing needed changing", "Four sessions, all on target, maxes holding. Rest today; Max Effort Lower tomorrow. Next review Sunday 02.08.", "Weekly review · Sun 26.07 · no changes") +
        c_lifts([("Squat","165","364","+5 this block","next top set Tue · SSB Box Squat"),("Bench","110","243","","no top set this week · held"),("Deadlift","202.5","446","+2.5","speed pull Sat · no test"),("Press","62.5","138","+2.5","next top set Thu · Apollon OHP")]) +
        c_earlier("3 entries this block · last Sun 19.07") +
        f'<div style="flex:1"></div>{tabbar("coach")}',
        "A rest day in a week with nothing to change: the slab still speaks (the always-alive rule), the lifts still show the block's progress, history stays folded."))

    # 10e — first week, nothing yet
    F.append(frame("s10e", "10e · Coach — first week",
        coach_hdr("Week 1 of 12 · deload in week 3") + strip(week) +
        f'<div class="label-faint" style="margin-bottom:8px">What the coach is doing</div>' +
        c_slab("Coach · this week", "Your first block starts today", "Max Effort Lower, SSB Box Squat — the top set drives your squat max; everything before it is setup. Every session you log is evidence for the first review on Sunday.", "First weekly review · Sun 12.07") +
        c_lifts([("Squat","160","353","","first top set today · SSB Box Squat"),("Bench","110","243","","first top set Thu · 2″ Board Press"),("Deadlift","200","441","","speed pulls Sat · no test yet"),("Press","60","132","","no top set this week")]) +
        f'<div style="flex:1"></div>{tabbar("coach")}',
        "Day one. No history, so no Earlier row: the slab frames today and says when the first review comes; the maxes from onboarding stand under <i>where you're going</i>, so the tab is alive before any review exists."))

    # 09d — no program
    F.append(frame("s10f", "10f · Coach — no program",
        coach_hdr("Program", full_plan=False) +
        f'<div class="card" style="padding:20px;margin-bottom:10px"><div style="font-size:14px;font-weight:600;color:var(--taupe);line-height:1.5">No active program yet. The coach can build your first block from your saved profile — or edit your answers first.</div></div>{btn("Build my program","burgundy")}<div style="height:10px"></div>{btn("Edit training profile","ghost")}'
        f'<div style="flex:1;display:flex;align-items:center;justify-content:center">{mark(120, opacity=.35)}</div>{tabbar("coach")}',
        "Same two actions as Today's no-program slab (06e) — one shared hook. No strip, no feed, no “Full plan” link until a program exists."))

    # 09e — offline / didn't load
    F.append(frame("s10g", "10g · Coach — didn’t load",
        coach_hdr("Program", full_plan=False) +
        f'<div class="card" style="padding:18px 20px;display:flex;flex-direction:column;gap:6px"><div style="font-size:14px;font-weight:600;color:var(--burgundy);line-height:1.5">You’re offline. The coach’s notes load when the connection is back — logged sessions are safe on this phone.</div><div style="font-size:13px;font-weight:700;margin-top:6px">Try again</div></div>'
        f'<div style="flex:1"></div>{tabbar("coach")}',
        "Factual, one retry, no fake feed — the same ErrorCard the other tabs use."))

    # 10 — full plan (pushed)
    plan_hdr = lambda: f'<div style="margin:8px 0 16px">{back("Coach")}</div><div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:14px"><div><div class="label-faint">Conjugate · 12 weeks</div><div class="title display" style="margin-top:4px">Full plan</div></div><div style="display:flex;gap:4px;padding-bottom:8px">{chev("#211E19",18)}{chev("#5C262B",18)}{chev("#E0D7C3",18)}</div></div>'
    F.append(frame("s10d", "10d · Full plan — cycle view (pushed from Coach)",
        plan_hdr() +
        f'<div class="label-faint" style="margin:2px 0 8px">W1 · Accumulation — done</div><div class="card" style="padding:0 16px;margin-bottom:14px">{prow("ME","Lower · SSB Box Squat",chk)}{prow("ME","Upper · 2″ Board Press",chk)}{prow("DE","Lower · Cambered Box Squat",chk)}{prow("DE","Upper · Speed Bench + bands","—",last=True)}</div>'
        f'<div class="label" style="margin:2px 0 8px">W2 · Intensification — this week</div>'
        f'<div class="slab" style="padding:0 18px;margin-bottom:14px">{prow("ME","Lower · SSB Box Squat","TODAY",ondark=True,next_=True)}{prow("ME","Upper · Apollon OHP","Thu",ondark=True)}{prow("DE","Lower · Trap-bar Speed Pull","Sat",ondark=True)}{prow("RE","Upper · rep work + carries","Sun",ondark=True,last=True)}</div>'
        f'<div class="label-faint" style="margin:2px 0 8px">W3 · Deload</div><div class="card" style="padding:13px 16px;display:flex;justify-content:space-between;align-items:center;margin-bottom:10px"><div style="display:flex;align-items:center;gap:12px">{mark(34, opacity=.35)}<div style="font-size:14px;color:var(--taupe);font-weight:600">4 sessions · 60% loads</div></div>{ic("chev-right",16,"#857D6A")}</div>'
        f'<div class="label-faint" style="margin:2px 0 8px">W4 · Accumulation</div><div class="card" style="padding:13px 16px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:14px;color:var(--taupe);font-weight:600">4 sessions</div>{ic("chev-right",16,"#857D6A")}</div>',
        "The cycle view as built, now a pushed route (<code>app/full-plan.tsx</code>) behind the Coach tab's “Full plan” link: back arrow, no tab bar. Drag-to-reorder stays in memory, so the “hold to reorder” caption is gone until reordering persists. Rows open the session detail; the deload keeps the watermark logo."))
    return F
