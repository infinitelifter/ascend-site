# Ascend founding-member landing page. One page, one job: get a serious lifter
# to ask for one of the 20 founding places. Built from the Summit system and the
# app's v5 phone frames (build/*.py are a copy of ascend/design-v5/build — when
# the app's frames change, copy them over and rebuild), so the page looks like
# the app. Run: python3 build/landing.py → index.html + preview/.
import sys, os, re, json, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from css import CSS as APP_CSS
from lib import *
import today, coach, gym, formcheck, plan_nutrition

def phone_of(frame_html):
    """The phone mockup alone, out of a frame() wrapper."""
    a = frame_html.index('<div class="phone')
    b = frame_html.find('<div class=frame-note>')
    if b < 0: b = frame_html.rindex('</div>')
    return frame_html[a:b]

def by_id(frames, fid):
    for f in frames:
        if f'id="{fid}"' in f[:80]: return f
    raise KeyError(fid)

T = today.frames(); Cn = coach.frames(); G = gym.frames(); Fc = formcheck.frames(); N = plan_nutrition.frames()
ph_today  = phone_of(by_id(T, "s7"))      # session ready
ph_coach  = phone_of(by_id(Cn, "s10"))    # the coach tab
ph_review = phone_of(by_id(T, "s21"))     # the review — facts first
ph_gym    = phone_of(G[0])                # gym mode
ph_form   = phone_of(by_id(Fc, "s14"))   # form check — the verdict
ph_nut    = phone_of(by_id(N, "s11"))     # nutrition

# only the phone chrome from the app CSS (drop the design-page chrome rules)
app_css = APP_CSS.split('/* page chrome */')[0] + APP_CSS[APP_CSS.index('/* iPhone */'):APP_CSS.index('/* design-system blocks */')]
app_css = app_css.replace(':root{\n  color-scheme:dark;', ':root{').replace('body{background:var(--page);color:var(--chalk);font-family:var(--body);-webkit-font-smoothing:antialiased}', '')

LANDING_CSS = r"""
/* Layout: one column, 1120 max, the phone always to the right of the claim on desktop and under it on a phone. */
:root{
  --bg:#F4EFE4; --surface:#FCF9F1; --ink:#211E19; --muted:#77705F; --faint:#857D6A; --line:#E0D7C3;
  --accent:#5C262B; --accent-ink:#F7F3E9; --slab:#211E19; --slab-ink:#F7F3E9; --slab-muted:#A09580; --slab-line:#3C362B;
  --display:'Urbanist',-apple-system,BlinkMacSystemFont,sans-serif; --body:-apple-system,BlinkMacSystemFont,'Inter',sans-serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#1B1915;--surface:#211E19;--ink:#F7F3E9;--muted:#C9BFAC;--faint:#A09580;--line:#3C362B;--accent:#A05257;--accent-ink:#F7F3E9;--slab:#F4EFE4;--slab-ink:#211E19;--slab-muted:#77705F;--slab-line:#E0D7C3;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#1B1915;--surface:#211E19;--ink:#F7F3E9;--muted:#C9BFAC;--faint:#A09580;--line:#3C362B;--accent:#A05257;--accent-ink:#F7F3E9;--slab:#F4EFE4;--slab-ink:#211E19;--slab-muted:#77705F;--slab-line:#E0D7C3;color-scheme:dark}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:var(--body);-webkit-font-smoothing:antialiased;line-height:1.5}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
.wrap{max-width:1120px;margin:0 auto;padding-inline:20px}
.top{display:flex;justify-content:space-between;align-items:center;padding-block:18px}
.top .brand{display:flex;align-items:center;gap:10px;font-family:var(--display);font-weight:700;font-size:18px;letter-spacing:.14em;text-transform:uppercase}
.top a.cta{font-size:13px;font-weight:700;color:var(--accent);text-decoration:none;letter-spacing:.04em}
.kicker{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);font-weight:700}
.kicker.acc{color:var(--accent)}
h1,h2,h3{font-family:var(--display);text-wrap:balance;letter-spacing:-.01em;line-height:1.05}
h1{font-size:clamp(40px,6.2vw,72px);font-weight:700;margin:14px 0 18px}
h2{font-size:clamp(30px,4vw,46px);font-weight:700;margin:12px 0 14px}
h3{font-size:22px;font-weight:700;margin:0 0 6px}
p.lede{font-size:clamp(17px,1.6vw,20px);color:var(--muted);max-width:34em}
p{max-width:65ch}
.lbtn{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:58px;padding:0 26px;border-radius:14px;background:var(--accent);color:var(--accent-ink);font-weight:700;font-size:16px;text-decoration:none;border:none;cursor:pointer;font-family:inherit}
.lbtn:focus-visible,a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.lbtn.ghost{background:transparent;color:var(--ink);border:1.5px solid var(--ink)}
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center;padding-block:34px 60px}
.hero .actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px;align-items:center}
.hero .fine{font-size:13px;color:var(--faint);margin-top:14px}
.phone-stage{display:flex;justify-content:center;min-width:0}
.stage{position:relative;overflow:visible;flex:0 0 auto}
.lslab .stage{overflow:hidden}
.stage .scale{position:absolute;left:0;top:0;width:393px;height:852px;transform-origin:top left}
.stage.s78{width:307px;height:665px}.stage.s78 .scale{transform:scale(.78)}
.stage.s62{width:244px;height:528px}.stage.s62 .scale{transform:scale(.62)}
.lslab .stage.s78{height:540px;border-radius:40px 40px 0 0}
.section{padding-block:64px;border-top:1px solid var(--line)}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:34px}
.three>div{min-width:0}
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:34px}
.four>div{min-width:0}
.pitch{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:30px}
.pitch .lcard{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:22px;min-width:0}
.pitch .num{font-family:var(--display);font-size:40px;font-weight:700;line-height:1;letter-spacing:-.01em;font-variant-numeric:tabular-nums}
.pitch .num .arrow{color:var(--accent);font-weight:600;margin:0 6px}
.pitch .d{font-size:14px;color:var(--muted);margin-top:8px}
.lslab{background:var(--slab);color:var(--slab-ink);border-radius:24px;padding:40px 40px 0;display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:end;overflow:hidden}
.lslab>div:first-child{padding-bottom:40px}
.lslab .kicker{color:var(--slab-muted)}
.lslab h2{color:var(--slab-ink)}
.lslab p{color:var(--slab-muted)}
.lslab ul{list-style:none;display:grid;gap:12px;margin-top:18px}
.lslab li{padding-left:22px;position:relative;font-size:15px;color:var(--slab-ink)}
.lslab li::before{content:"";position:absolute;left:0;top:9px;width:9px;height:9px;border-radius:5px;background:var(--accent)}
.who{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:30px}
.who .col{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:24px}
.who ul{list-style:none;display:grid;gap:10px;margin-top:12px}
.who li{display:flex;gap:10px;font-size:15px;align-items:flex-start}
.who li svg{flex:0 0 auto;margin-top:3px}
.price{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:30px;align-items:stretch}
.price .lcard{background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:30px;display:flex;flex-direction:column;gap:14px;min-width:0}
.price .lcard.on{background:var(--slab);color:var(--slab-ink);border-color:var(--slab)}
.price .lcard.on .kicker{color:var(--accent-ink);opacity:.9}
.price .lcard.on .muted{color:var(--slab-muted)}
.price .lcard.on li::before{background:#A05257}
.price .lcard.on>div[style*="border:1px solid"]{border-color:var(--slab-line)!important}
.price .big{font-family:var(--display);font-size:56px;font-weight:700;line-height:1;letter-spacing:-.01em;font-variant-numeric:tabular-nums}
.price .big small{font-family:var(--body);font-size:15px;font-weight:600;letter-spacing:0}
.price ul{list-style:none;display:grid;gap:9px;font-size:15px}
.price li{padding-left:20px;position:relative}
.price li::before{content:"";position:absolute;left:0;top:9px;width:8px;height:8px;border-radius:4px;background:var(--accent)}
.muted{color:var(--muted)}
.places{display:flex;gap:4px;margin-top:4px}
.places i{display:block;width:12px;height:12px;border-radius:3px;background:var(--line)}
.places i.on{background:var(--accent)}
.faq{display:grid;grid-template-columns:1fr 1fr;gap:22px 40px;margin-top:30px}
.faq div{min-width:0}
.faq h3{font-size:17px;font-family:var(--body);font-weight:700;margin-bottom:4px}
.faq p{font-size:15px;color:var(--muted)}
form{background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:28px;display:grid;gap:14px;max-width:560px;position:relative}
label{display:grid;gap:6px;font-size:13px;font-weight:700;color:var(--muted)}
input,select{height:52px;border:1px solid var(--line);border-radius:12px;background:var(--bg);color:var(--ink);padding:0 14px;font-size:16px;font-family:inherit}
textarea{border:1px solid var(--line);border-radius:12px;background:var(--bg);color:var(--ink);padding:12px 14px;font-size:16px;font-family:inherit;line-height:1.45;resize:vertical;min-height:110px}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.consent{display:flex;gap:10px;align-items:flex-start;font-size:13px;color:var(--muted);font-weight:500;padding:10px 12px;border:1px solid transparent;border-radius:10px;margin:0 -12px}
.consent input{height:auto;width:18px;margin-top:3px;accent-color:var(--accent);flex:0 0 auto}
.consent.missing{border-color:var(--accent);color:var(--accent);background:color-mix(in srgb,var(--accent) 6%,transparent)}
.consent .need{display:none;font-weight:700}
.consent.missing .need{display:block;margin-top:4px}
.done{display:none;background:var(--slab);color:var(--slab-ink);border-radius:18px;padding:22px;font-size:15px}
.done.show{display:block}
footer{padding-block:40px 60px;border-top:1px solid var(--line);font-size:13px;color:var(--faint)}
footer p{max-width:none}
footer .legal{margin-top:14px;line-height:1.6}
.phone{box-shadow:0 0 0 10px #1A1815,0 30px 60px rgba(33,30,25,.35)}
@media (max-width:1100px){.four{grid-template-columns:1fr 1fr}}
@media (max-width:860px){
  .hero,.lslab,.who,.price,.faq{grid-template-columns:1fr}
  .three,.pitch{grid-template-columns:1fr}
  .four{grid-template-columns:1fr 1fr}
  .hero{padding-block:20px 36px}
  .lslab{padding:28px 22px}
  .row2{grid-template-columns:1fr}
  .four{grid-template-columns:1fr}
  .stage.s62{width:307px;height:665px}.stage.s62 .scale{transform:scale(.78)}
  h1{font-size:clamp(36px,10vw,48px)}
}
"""

def phone_stage(ph, cls="s78"):
    return f'<div class="phone-stage"><div class="stage {cls}"><div class="scale">{ph}</div></div></div>'

check = lambda col="#5C262B": f'<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="{col}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="5,12.5 10,17.5 19,7"/></svg>'
cross = lambda col="#857D6A": f'<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="{col}" stroke-width="2.2" stroke-linecap="round"><line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/></svg>'

page = f'''<title>Ascend Founding Members</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@500;600;700&display=swap" rel="stylesheet">
<style>{app_css}{LANDING_CSS}</style>

<div class="wrap">
<div class="top"><div class="brand">{mark(30)}Ascend</div><a class="cta" href="#apply">Ask for a founding place →</a></div>

<section class="hero">
  <div>
    <div class="kicker acc">Developed with world-class coaches · 20 founding places</div>
    <h1>Stop thinking about training. Start being coached.</h1>
    <p class="lede">Ascend writes your program, watches you lift, reads your meals and adjusts every week, the way a good coach does. Health and results without spending hours a week managing them, for people who treat the gym as non-negotiable and their time as expensive.</p>
    <div class="actions"><a class="lbtn" href="#apply">Ask for a founding place</a><a class="lbtn ghost" href="#how">See how it coaches</a></div>
    <div class="fine">€50 a month for the first 20, for as long as you stay. €100 after that. Cancel any month. 30-day money-back guarantee.</div>
  </div>
  {phone_stage(ph_today)}
</section>

<section class="section" id="why">
  <div class="kicker">The problem</div>
  <h2>You already know how to lift. The thinking is what costs you.</h2>
  <p class="lede">Which program. Which variation this block. When to push the max and when to hold. What to eat to make it count. Most serious lifters spend more hours deciding than training, and still second-guess every top set.</p>
  <div class="three">
    <div><h3>A coach decides.</h3><p>Ascend writes your plan specifically for you, from your goal, your lifting history, your injuries, your equipment and your week. Every session, every load, every variation.</p></div>
    <div><h3>A coach watches.</h3><p>Log a set and the loads move. Film a lift and the coach reads the bar path and your knees. Photograph a plate and the macros are read for you.</p></div>
    <div><h3>A coach explains.</h3><p>Every Sunday: what it saw, what changed, why, and what happens next. In plain words, with the numbers in front. When life moves a session, the week reschedules intelligently around it.</p></div>
  </div>
</section>

<section class="section" id="how">
  <div class="kicker">What the coach does, every week</div>
  <h2>Facts first. Then the reasoning.</h2>
  <p class="lede">The weekly review is the heart of it. The engine decides from your logs; the tiles show what moved and the four sections say why. Nothing is hidden behind a score.</p>
  <div class="pitch">
    <div class="lcard"><div class="kicker">Squat max</div><div class="num">160<span class="arrow">→</span>165</div><div class="d">Top set 5 × 160 kg beat the estimate three weeks running. The training max follows, capped at 5 kg a week.</div></div>
    <div class="lcard"><div class="kicker">Added</div><div class="num" style="font-size:28px;margin-top:6px">Cossack Squat</div><div class="d">Right-knee cave flagged on the form check. Targeted work twice a week until two clean checks close the flag.</div></div>
    <div class="lcard"><div class="kicker">Squat volume</div><div class="num">−10%</div><div class="d">42% of squat sets were grinds. A small cut next week restores bar speed; your max stays.</div></div>
  </div>
  <div class="lslab" style="margin-top:40px">
    <div>
      <div class="kicker">Developed with world-class coaches</div>
      <h2>We have an opinion that works.</h2>
      <p>AI where it sees, our algorithm where it decides. AI reads your lifts on video and your meals from a photo, and the coach answers when you talk to it. But what you lift, when and how much is decided by a coaching system we wrote with coaches who get people strong for a living, not by a model guessing. It takes what works across methodologies, picks a training goal and a methodology that fit you, and writes the plan for you alone: your injuries, your lifting history, your schedule, your goal. Because the decisions are rules and not a prompt, they are consistent: the same evidence gets the same sound call every time. And the coach keeps guiding you while working around your life.</p>
      <ul>
        <li>Several training goals and methodologies: strength, size, a meet to peak for, a comeback after an injury. The coach picks and adapts.</li>
        <li>Loads come from your training max, never from how you feel today. No RPE guesswork.</li>
        <li>A max moves at most 5 kg a week, and only when a logged top set earns it.</li>
        <li>Miss a day and the week reschedules itself. Report pain and the next sessions swap around it. Get sick and the week compresses, then re-enters gently.</li>
        <li>Changes land on upcoming sessions only. Your history is never rewritten.</li>
      </ul>
    </div>
    {phone_stage(ph_review)}
  </div>
</section>

<section class="section">
  <div class="kicker">In the gym</div>
  <h2>Weight. Reps. How it moved. Log.</h2>
  <p class="lede">Gym mode shows four things and nothing else. Every set is one tap, every top set is a test the coach reads that night.</p>
  <div class="four" style="align-items:start">
    <div>{phone_stage(ph_gym, "s62")}<h3 style="margin-top:14px">Nothing to think about</h3><p>The loads are set. Your job is the bar.</p></div>
    <div>{phone_stage(ph_form, "s62")}<h3 style="margin-top:14px">A coach's eyes on every lift</h3><p>Film 15 seconds; the coach reads bar path, depth and your knees, and the plan reacts: a flag becomes targeted work in your next sessions.</p></div>
    <div>{phone_stage(ph_coach, "s62")}<h3 style="margin-top:14px">The coach holds the plan</h3><p>The next seven days, what the coach did and why, and where each lift is going.</p></div>
    <div>{phone_stage(ph_nut, "s62")}<h3 style="margin-top:14px">Food, counted for you</h3><p>Targets computed from your goal and weight trend; meals logged from a photo.</p></div>
  </div>
</section>

<section class="section">
  <div class="kicker">Who it is for</div>
  <h2>Twenty people who train four days a week and want to stop managing it.</h2>
  <div class="who">
    <div class="col"><div class="kicker acc">Yes, if</div><ul>
      <li>{check()}You squat, bench, deadlift or press and track your lifts in kg.</li>
      <li>{check()}You train in a gym with a barbell, three or four days a week, and will log every session.</li>
      <li>{check()}You have had a coach, or wanted one, and know what a good one is worth.</li>
      <li>{check()}You want one source of truth for training and food, not five apps.</li>
    </ul></div>
    <div class="col"><div class="kicker">Not yet, if</div><ul>
      <li>{cross()}You want a workout generator for a hotel gym.</li>
      <li>{cross()}You train by feel and do not want to log.</li>
      <li>{cross()}You are on Android (iPhone only for the founding block).</li>
      <li>{cross()}You are not cleared to train by a doctor. A comeback after an injury is a goal the coach handles, but only once you are cleared.</li>
    </ul></div>
  </div>
</section>

<section class="section" id="price">
  <div class="kicker">Founding members</div>
  <h2>A coach who sees every set, for a third of what a coach costs. Half that for the first twenty.</h2>
  <div class="price">
    <div class="lcard on">
      <div class="kicker">Founding place · 20 only</div>
      <div class="big">€50<small> / month</small></div>
      <div class="places" aria-label="places taken">{''.join('<i class="on"></i>' if i < 3 else '<i></i>' for i in range(20))}</div>
      <div class="muted">3 of 20 taken · price locked for as long as you stay</div>
      <div style="border:1px solid var(--slab-line);border-radius:12px;padding:12px 14px;font-size:14px;line-height:1.45"><b>30 days, money back.</b> Train with the coach for a month and log your sessions. If it has not earned its place, say so and I refund the month.</div>
      <ul>
        <li>The full coach: program, gym mode, form check, nutrition, weekly review</li>
        <li>A direct line to Ondrej for your first block</li>
        <li>Your feedback visibly shapes the next version</li>
        <li>Cancel any month, keep your history</li>
      </ul>
      <a class="lbtn" href="#apply" style="background:var(--accent-ink);color:var(--slab)">Ask for a place</a>
    </div>
    <div class="lcard">
      <div class="kicker">After the founding block</div>
      <div class="big">€100<small> / month</small></div>
      <div class="muted">Opens when the 20 places are taken.</div>
      <ul>
        <li>The same coach</li>
        <li>Standard support</li>
        <li>Cancel any month</li>
      </ul>
      <div class="muted" style="margin-top:auto;font-size:13px">A personal strength coach at this level costs €150–300 a month, sees you once a week, and answers when they can. Ascend sees every set, answers at once, reschedules the week when yours changes, and never has a waiting list.</div>
    </div>
  </div>
</section>

<section class="section" id="apply">
  <div class="kicker">Ask for a place</div>
  <h2>Tell me how you train. I reply personally.</h2>
  <p class="lede" style="margin-bottom:24px">No automated onboarding for the founding block. I read every application, and if it fits, you get the app and a call to set up your first block.</p>
  <form id="apply-form" novalidate>
    <div class="row2">
      <label>Name<input id="f-name" name="name" required autocomplete="name"></label>
      <label>Email or phone<input id="f-contact" name="contact" required autocomplete="email"></label>
    </div>
    <div class="row2">
      <label>Where you train<input id="f-gym" name="gym" placeholder="Gym, city"></label>
      <label>Days a week<select id="f-days" name="days"><option>3</option><option selected>4</option><option>5</option></select></label>
    </div>
    <label>Best squat · bench · deadlift (kg)<input id="f-lifts" name="lifts" placeholder="160 · 110 · 200"></label>
    <label>About you and your training<textarea id="f-about" name="about" rows="4" maxlength="1200" placeholder="How long you have lifted, what you are after this year, injuries or anything the coach should know."></textarea></label>
    <label style="position:absolute;left:-9999px" aria-hidden="true">Website<input id="f-website" name="website" tabindex="-1" autocomplete="off"></label>
    <label class="consent" id="consent-row"><input type="checkbox" id="f-consent" required><span>I am 18 or older, cleared to train, and I understand Ascend gives training guidance, not medical advice.<span class="need">Tick this to send the application.</span></span></label>
    <button class="lbtn" type="submit">Send my application</button>
    <div class="muted" id="form-err" style="font-size:13px;color:var(--accent);display:none"></div>
    <div class="muted" style="font-size:13px">Or write directly: <b id="mail">hello@ascend.coach</b> <button type="button" class="lbtn ghost" style="height:34px;padding:0 12px;font-size:12px;margin-left:8px" id="copy">Copy</button></div>
  </form>
  <div class="done" id="done">Received. I will read it today and reply within 48 hours from my own address, so watch for a reply from Ondrej.</div>
</section>

<footer>
  <div class="brand" style="font-family:var(--display);font-weight:700;letter-spacing:.14em;text-transform:uppercase;display:flex;align-items:center;gap:10px">{mark(22)}Ascend</div>
  <p class="legal">Ascend is a training tool. It writes programs and adjusts them from the data you log; it does not diagnose, treat or replace advice from a physician or physiotherapist. Lifting heavy carries a risk of injury. Train within your ability, stop when something hurts, and get cleared by a doctor before starting if you have a condition or a recent injury. By using Ascend you accept the Terms of Use and the Health &amp; Safety acknowledgement shown in the app.</p>
  <p class="legal">© 2026 Full Canvas Digital s.r.o., Prague · Terms · Privacy · Contact</p>
</footer>
</div>

<script>
(function(){{
  var form=document.getElementById('apply-form'), done=document.getElementById('done'), opened=Date.now();
  document.getElementById('f-consent').addEventListener('change',function(){{document.getElementById('consent-row').classList.toggle('missing',!this.checked);}});
  form.addEventListener('submit',function(e){{
    e.preventDefault();
    var ok=true;
    ['f-name','f-contact'].forEach(function(id){{var el=document.getElementById(id); var v=el.value.trim(); el.style.borderColor=v?'':'var(--accent)'; if(!v) ok=false;}});
    var consent=document.getElementById('f-consent'), row=document.getElementById('consent-row');
    row.classList.toggle('missing',!consent.checked); if(!consent.checked) ok=false;
    if(!ok) return;
    var btn=form.querySelector('button[type=submit]'), err=document.getElementById('form-err');
    btn.disabled=true; btn.textContent='Sending'; err.style.display='none';
    var g=function(id){{return document.getElementById(id).value.trim();}};
    var payload={{name:g('f-name'),contact:g('f-contact'),gym:g('f-gym'),days:g('f-days'),lifts:g('f-lifts'),about:g('f-about'),website:g('f-website'),consent:consent.checked,t:opened}};
    fetch('/api/apply',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(payload)}})
      .then(function(r){{return r.json().catch(function(){{return {{ok:r.ok}};}});}})
      .then(function(j){{ if(!j.ok) throw new Error(j.error||'Could not send.'); form.hidden=true; done.classList.add('show'); done.scrollIntoView({{behavior:'smooth',block:'center'}}); }})
      .catch(function(x){{ btn.disabled=false; btn.textContent='Send my application'; err.textContent=(x&&x.message)||'Could not send. Write to the address below.'; err.style.display='block'; }});
  }});
  document.getElementById('copy').addEventListener('click',function(){{
    var t=document.getElementById('mail').textContent;
    var b=this;
    function sel(){{var r=document.createRange(); r.selectNodeContents(document.getElementById('mail')); var s=getSelection(); s.removeAllRanges(); s.addRange(r);}}
    if(navigator.clipboard&&navigator.clipboard.writeText){{navigator.clipboard.writeText(t).then(function(){{b.textContent='Copied';}}).catch(sel);}} else sel();
  }});
}})();
</script>
'''
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, '..')
# 1) preview/ascend-landing.html — the Claude-artifact version (no document skeleton; the Artifact tool adds it)
os.makedirs(os.path.join(root, 'preview'), exist_ok=True)
open(os.path.join(root, 'preview', 'ascend-landing.html'), 'w').write(page)
# 2) index.html — the deployable site: a complete document for Vercel
SITE = "https://ascendstrength.app"  # change when the domain changes; also in robots.txt and sitemap.xml
DESC = "A strength coach in your pocket: your program written for you, every lift watched, every meal read, adjusted weekly. 20 founding places."
standalone = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
  '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
  f'<meta name="description" content="{DESC}">'
  '<meta property="og:title" content="Ascend: stop thinking about training. Start being coached.">'
  f'<meta property="og:description" content="{DESC}"><meta property="og:type" content="website">'
  '<meta name="theme-color" content="#F4EFE4">'
  '<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">'
  '<link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">'
  + f'<link rel="canonical" href="{SITE}/"><meta property="og:url" content="{SITE}/"><meta property="og:image" content="{SITE}/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
  + '<meta name="twitter:card" content="summary_large_image"><meta property="og:site_name" content="Ascend"><meta name="robots" content="index,follow">'
  + '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"SoftwareApplication","name":"Ascend","applicationCategory":"HealthApplication","operatingSystem":"iOS","description":DESC,"url":SITE,"offers":[{"@type":"Offer","name":"Founding place","price":"50","priceCurrency":"EUR","billingIncrement":"P1M","availability":"https://schema.org/LimitedAvailability"},{"@type":"Offer","name":"Standard","price":"100","priceCurrency":"EUR","billingIncrement":"P1M"}],"publisher":{"@type":"Organization","name":"Full Canvas Digital s.r.o.","address":{"@type":"PostalAddress","addressLocality":"Prague","addressCountry":"CZ"}}}) + '</script>'
  + page.replace('<title>Ascend Founding Members</title>', '<title>Ascend, a strength coach in your pocket</title>', 1)
  + '</body></html>')
standalone = standalone.replace('</style>\n\n<div class="wrap">', '</style></head><body>\n<div class="wrap">', 1)
open(os.path.join(root, 'index.html'), 'w').write(standalone)
print(len(page), 'bytes preview;', len(standalone), 'bytes index.html')
