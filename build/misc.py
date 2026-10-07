from lib import *

def row(t, d=None, danger=False, chevron=True, last=False):
    dd = f'<div class="meta" style="font-size:12px;margin-top:3px">{d}</div>' if d else ''
    return (f'<div style="padding:15px 0;display:flex;justify-content:space-between;align-items:center;{"" if last else "border-bottom:1px solid var(--bone)"}"><div style="flex:1;padding-right:12px"><div style="font-size:15px;font-weight:700;color:{"var(--burgundy)" if danger else "var(--charcoal)"}">{t}</div>{dd}</div>{ic("chev-right",16,"#857D6A") if chevron else ""}</div>')

def frames():
    F = []
    F.append(frame("s23", "23 · Settings — account & data",
        f'<div style="margin:8px 0 16px">{back("Today")}</div><div class="meta" style="color:var(--faint)">ondrej@lifter.io</div><div class="title display" style="margin:4px 0 18px">Settings</div>'
        f'<div class="card" style="padding:0 20px;margin-bottom:16px">{row("Edit training profile","Goal, timeline, schedule, equipment — finishing rebuilds your plan")}{row("Units","kg primary, lb secondary — shown together everywhere",chevron=False,last=True)}</div>'
        f'<div class="card" style="padding:0 20px;margin-bottom:16px">{row("Export my data","Every row you own, as one JSON file via the share sheet")}{row("Manage subscription","Billed through the App Store")}{row("Sign out",last=True)}</div>'
        f'<div class="card" style="padding:0 20px">{row("Delete account","Permanently removes your account and all data. No undo.",True,last=True)}</div>'
        f'<div style="font-size:12px;color:var(--faint);line-height:1.5;margin-top:22px;font-weight:500">Ascend 0.9.0 · videos never leave your phone except for the 48-hour AI review · meal photos are read once and not stored</div>',
        "The email is no longer uppercased (it was pushed through the caps label). Chevrons are icons. “Manage subscription” row added for when the paywall ships. Export / delete working states use the logo loader inside the card."))
    F.append(frame("s23b", "23b · Settings — composing your export",
        f'<div style="margin:8px 0 16px">{back("Today")}</div><div class="meta" style="color:var(--faint)">ondrej@lifter.io</div><div class="title display" style="margin:4px 0 18px">Settings</div>'
        f'<div class="card" style="padding:0 20px;margin-bottom:16px">{row("Edit training profile","Goal, timeline, schedule, equipment — finishing rebuilds your plan")}{row("Units","kg primary, lb secondary — shown together everywhere",chevron=False,last=True)}</div>'
        f'<div class="card" style="padding:18px 20px;margin-bottom:16px;display:flex;flex-direction:column;align-items:center">{shimmer(64, False, "Composing your export")}</div>'
        f'<div class="card" style="padding:0 20px">{row("Delete account","Permanently removes your account and all data. No undo.",True,last=True)}</div>',
        "Logo loader on cream, 64 pt. Delete-account confirm stays a native dialog (destructive confirms belong to the OS)."))
    F.append(frame("s24", "24 · Paywall — single premium tier (scaffolded)",
        f'<div style="display:flex;justify-content:space-between;align-items:center"><div class="label-dark">Ascend · full access</div><div style="width:32px;height:32px;border:1.5px solid var(--darkline);border-radius:16px;display:flex;align-items:center;justify-content:center">{ic("close",16,"#A09580",2)}</div></div>'
        f'<div class="display" style="font-size:34px;font-weight:700;line-height:1.12;margin-top:20px">Private coaching that<br>adapts every week.</div>'
        + '<div style="display:flex;flex-direction:column;gap:11px;font-size:14px;color:var(--dbody);line-height:1.45;margin-top:20px">' + ''.join(f'<div style="display:flex;gap:10px">{chev("#A05257",12,3).replace("flex:0 0 auto","flex:0 0 auto;margin-top:6px")}{t}</div>' for t in ["A plan built for you — re-planned weekly, never abandoned","Every set watched: top sets move your training maxes","Form checks on the main lifts, findings your coach remembers","Meals counted from photos; targets adjust from your weekly trend","The weekly coaching review — what Ascend saw, what changed, why, what happens next"]) + '</div>'
        f'<div class="sootcard" style="border:1.5px solid var(--burgundy-lt);padding:20px;display:flex;flex-direction:column;gap:6px;margin-top:20px"><div class="label-dark">Premium — the only tier</div><div class="display" style="font-size:34px;font-weight:700">€59 / month</div><div style="font-size:13px;color:var(--dbody);font-weight:600">Cancel anytime</div><div style="font-size:12px;color:var(--dlabel);line-height:1.45;margin-top:4px">Founding members: €39 a month, locked for life — early access, real input on the product. A human online coach runs €200–500 a month.</div></div>'
        f'<div style="flex:1"></div>{btn("Start membership","chalk")}<div style="font-size:11px;color:var(--dlabel);text-align:center;margin:10px 0 30px">Billed through the App Store · cancel in Settings any time</div>',
        "Locked copy, unchanged. Headline and price in the display face.", dark=True, screen_style="padding-top:16px"))
    F.append(frame("s26", "26 · Something broke — crash boundary",
        f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:14px">{mark(120, opacity=.35)}<div class="title display" style="margin-top:10px">Something broke.</div><div style="font-size:15px;font-weight:500;color:var(--taupe);line-height:1.5">Your data is safe — logged sets and meals are stored on this phone and sync when the app reopens.</div><div style="font-size:12px;color:var(--faint);font-weight:500">TypeError: undefined is not an object</div>{btn("Restart","burgundy",extra="margin-top:12px")}</div>',
        "As built, display title."))
    return F
