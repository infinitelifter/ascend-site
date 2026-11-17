CSS = r"""
:root{
  color-scheme:dark;
  --paper:#F4EFE4; --cream:#FCF9F1; --charcoal:#211E19; --espresso:#211E19; --soot:#2E2922; --chalk:#F7F3E9;
  --graphite:#77705F; --taupe:#77705F; --faint:#857D6A; --bone:#E0D7C3; --darkline:#3C362B;
  --burgundy:#5C262B; --burgundy-lt:#A05257; --dlabel:#A09580; --dbody:#D7CFC0; --page:#0E0D0C;
  --display:'Urbanist','Inter',-apple-system,sans-serif;
  --body:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--page);color:var(--chalk);font-family:var(--body);-webkit-font-smoothing:antialiased}
.num{font-variant-numeric:tabular-nums;letter-spacing:-0.01em}
.display{font-family:var(--display);font-variant-numeric:tabular-nums;letter-spacing:-0.01em}

/* page chrome */
.topbar{position:fixed;top:0;left:0;right:0;z-index:50;background:rgba(14,13,12,.92);backdrop-filter:blur(12px);border-bottom:1px solid #262420;padding:calc(12px + env(safe-area-inset-top,0px)) 24px 10px;display:flex;align-items:center;gap:20px}
.brand{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:#A29B8D;font-weight:700;white-space:nowrap}
.brand em{color:#A05257;font-style:normal}
.topbar nav{display:flex;gap:2px;overflow-x:auto;scrollbar-width:none}
.topbar nav::-webkit-scrollbar{display:none}
.topbar nav a{font-size:11px;color:#8A8372;text-decoration:none;padding:6px 9px;border-radius:8px;letter-spacing:.04em;white-space:nowrap}
.topbar nav a:hover{background:#1E1B18;color:#EFEAE2}
.section{padding:0 60px}
.section h2{font-size:30px;font-weight:700;color:#EFEAE2;margin:84px 0 8px;text-wrap:balance}
.section .lede{font-size:14px;color:#A29B8D;max-width:760px;line-height:1.6;margin-bottom:10px}
.flow{display:flex;gap:52px;padding:22px 0 30px;overflow-x:auto;align-items:flex-start;scroll-snap-type:x proximity}
.frame-wrap{scroll-snap-align:center;flex:0 0 auto}
.frame-label{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#6B655A;margin-bottom:6px;max-width:393px}
.frame-label b{color:#A29B8D;font-weight:500}
.frame-note{font-size:12px;color:#8A8372;max-width:393px;margin-top:12px;line-height:1.55}
.frame-note b{color:#C9BFAC;font-weight:600}
.frame-note code{font-family:ui-monospace,Menlo,monospace;font-size:11px;color:#C9BFAC}

/* iPhone */
.phone{width:393px;height:852px;background:var(--paper);border-radius:54px;border:1px solid #33302B;box-shadow:0 0 0 10px #1A1815,0 40px 80px rgba(0,0,0,.55);position:relative;overflow:hidden;display:flex;flex-direction:column;color:var(--charcoal)}
.phone.dark{background:var(--charcoal);color:var(--chalk)}
.notch{position:absolute;top:12px;left:50%;transform:translateX(-50%);width:120px;height:34px;background:#000;border-radius:20px;z-index:10}
.statusbar{height:56px;flex:0 0 auto;display:flex;justify-content:space-between;align-items:flex-end;padding:0 32px 6px;font-size:15px;font-weight:600;font-variant-numeric:tabular-nums}
.sb-icons{display:flex;align-items:center}
.homebar{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);width:130px;height:5px;background:rgba(27,25,23,.28);border-radius:3px;z-index:5}
.phone.dark .homebar{background:rgba(246,243,235,.3)}
.screen{flex:1;display:flex;flex-direction:column;padding:8px 24px 0;overflow:hidden;position:relative}
.screen>*{flex-shrink:0} /* spacers and cards keep their height when a screen overflows the phone */

/* Summit v5 system */
.label{font-size:11px;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe);font-weight:700;line-height:15px}
.label-faint{font-size:11px;letter-spacing:.11em;text-transform:uppercase;color:var(--faint);font-weight:700;line-height:15px}
.label-dark{font-size:11px;letter-spacing:.11em;text-transform:uppercase;color:var(--dlabel);font-weight:700;line-height:15px}
.meta{font-size:13px;font-weight:500;color:var(--taupe);line-height:18px}
.meta-dark{font-size:13px;font-weight:500;color:var(--dlabel);line-height:18px}
.title{font-size:34px;font-weight:700;line-height:1.08;letter-spacing:-0.01em}
.subtitle{font-size:14px;color:var(--taupe);line-height:1.5}
.wait-dark{font-size:13px;font-weight:500;color:var(--dlabel);text-align:center;margin-top:18px}
.wait-light{font-size:13px;font-weight:500;color:var(--taupe);text-align:center;margin-top:18px}

.btn{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;height:58px;border-radius:14px;font-size:16px;font-weight:700;letter-spacing:-0.01em;border:none;font-family:inherit;color:inherit;position:relative;overflow:hidden;flex:0 0 auto}
.btn-chalk{background:var(--chalk);color:var(--charcoal)}
.btn-burgundy{background:var(--burgundy);color:var(--chalk)}
.btn-charcoal,.btn-espresso{background:var(--charcoal);color:var(--chalk)}
.btn-cream{background:var(--cream);color:var(--charcoal);border:1px solid var(--bone)}
.btn-ghost{background:transparent;color:var(--charcoal);border:1.5px solid var(--charcoal)}
.btn-ghostDark,.btn-ghost-dark{background:transparent;color:var(--chalk);border:1.5px solid var(--darkline)}
.btn-disabled{background:var(--bone);color:var(--faint)}
.btn.busy::after{content:"";position:absolute;top:0;bottom:0;left:-40%;width:40%;background:linear-gradient(100deg,transparent 0,rgba(255,255,255,.16) 50%,transparent 100%);animation:btnshim 1.6s linear infinite}
@keyframes btnshim{to{left:140%}}

.card{background:var(--cream);border:1px solid var(--bone);border-radius:18px}
.slab{background:var(--charcoal);border-radius:20px;color:var(--chalk)}
/* v5.1 — the only shadow in the app: the espresso slab sits a little above the page */
.slab.lift{box-shadow:0 10px 18px rgba(33,30,25,.16)}
/* v5.1 — motion: fade in and rise, once; timing curve only, nothing bounces */
@keyframes settle{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes reveal{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@keyframes fillbar{from{transform:translateX(-100%)}to{transform:none}}
.settle{animation:settle .26s cubic-bezier(.33,1,.68,1) both}
.reveal{animation:reveal .34s cubic-bezier(.33,1,.68,1) both}
.motion-demo .settle,.motion-demo .reveal{animation-iteration-count:infinite;animation-duration:3.2s}
.motion-demo .settle{animation-name:settle-loop}.motion-demo .reveal{animation-name:reveal-loop}
@keyframes settle-loop{0%{opacity:0;transform:translateY(8px)}8%,90%{opacity:1;transform:none}100%{opacity:0;transform:none}}
@keyframes reveal-loop{0%{opacity:0;transform:translateY(10px)}11%,90%{opacity:1;transform:none}100%{opacity:0;transform:none}}
.fillbar{height:4px;background:var(--bone);border-radius:3px;overflow:hidden}
.fillbar>div{height:100%;background:var(--charcoal);border-radius:3px;animation:fillbar-loop 3.2s cubic-bezier(.33,1,.68,1) infinite}
@keyframes fillbar-loop{0%,4%{transform:translateX(-100%)}22%,90%{transform:none}100%{transform:translateX(-100%)}}
@media (prefers-reduced-motion:reduce){.settle,.reveal,.fillbar>div{animation:none!important}}
.sootcard{background:var(--soot);border:1px solid var(--darkline);border-radius:20px}

.sel-card{background:var(--cream);border:1px solid var(--bone);border-radius:16px;padding:18px;display:flex;align-items:center;justify-content:space-between}
.sel-card .t{font-size:16px;font-weight:700;margin-bottom:3px}
.sel-card .d{font-size:13px;color:var(--taupe)}
.sel-card.on{background:var(--charcoal);border-color:var(--charcoal);color:var(--chalk)}
.sel-card.on .d{color:var(--dlabel)}
.sel-card.compact{padding:12px 14px}.sel-card.compact .t{font-size:14px}.sel-card.compact .d{font-size:12px}

.pill{display:inline-flex;align-items:center;justify-content:center;height:38px;padding:0 17px;border-radius:19px;background:var(--cream);border:1px solid var(--bone);font-size:13px;color:var(--taupe);font-weight:600;font-variant-numeric:tabular-nums;white-space:nowrap}
.pill.on{background:var(--charcoal);color:var(--chalk);border-color:var(--charcoal)}
.pill-dark{background:transparent;border:1px solid var(--darkline);color:var(--dlabel)}
.pill-dark.on{background:var(--chalk);border-color:var(--chalk);color:var(--charcoal)}
.pill.big{height:48px;font-size:15px;border-radius:24px}
.gympill{display:inline-flex;align-items:center;gap:7px;height:40px;padding:0 14px;border-radius:20px;border:1.5px solid var(--darkline);font-size:13px;font-weight:700;color:var(--dlabel)}
.tag{display:inline-flex;white-space:nowrap;align-items:center;height:26px;padding:0 10px;border-radius:8px;background:var(--soot);border:1px solid var(--darkline);font-size:11px;font-weight:700;color:var(--dlabel);letter-spacing:.02em}

.role-tag{display:inline-flex;align-items:center;height:24px;padding:0 9px;border-radius:7px;font-size:10px;font-weight:800;letter-spacing:.1em;color:var(--chalk)}
.role-me{background:var(--burgundy)}.role-de{background:var(--charcoal)}.role-re{background:var(--taupe)}
.role-de-ondark{background:var(--soot);border:1px solid var(--darkline)}

.input{background:var(--cream);border:1px solid var(--bone);border-radius:12px;height:56px;display:flex;align-items:center;padding:0 16px;font-size:16px;color:var(--charcoal)}
.input.err{border-color:var(--burgundy);border-width:1.5px}
.err-text{font-size:12px;color:var(--burgundy);margin-top:6px;font-weight:500}

.tabbar{flex:0 0 auto;height:84px;border-top:1px solid var(--bone);display:flex;padding:10px 12px 26px;margin:0 -24px;background:var(--paper)}
.tab{flex:1;display:flex;flex-direction:column;align-items:center;gap:4px;font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:var(--faint);font-weight:700}
.tab.on{color:var(--charcoal)}

.hr{height:1px;background:var(--bone);border:none}
.hr-dark{height:1px;background:var(--darkline);border:none}
.lb{font-size:.55em;color:var(--faint);font-weight:600;letter-spacing:0}

.stepper{width:54px;height:54px;border-radius:16px;background:var(--cream);border:1px solid var(--bone);display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.stepper-dark{background:var(--soot);border:1px solid var(--darkline)}

.seg{height:5px;border-radius:3px;flex:1;background:var(--bone)}
.seg.done{background:var(--charcoal)}.seg.now{background:var(--burgundy)}
.seg-dark{background:var(--darkline)}.seg-dark.done{background:var(--chalk)}.seg-dark.now{background:var(--burgundy-lt)}
.seg-dark.done{height:7px;margin-top:-1px}
.progressline{height:5px;background:var(--bone);border-radius:3px;overflow:hidden}
.progressline>div{height:100%;background:var(--charcoal);border-radius:3px}

.fact{background:var(--cream);border:1px solid var(--bone);border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;gap:4px;min-width:0;flex:1}
.fact .k{font-size:11px;letter-spacing:.11em;text-transform:uppercase;color:var(--taupe);font-weight:700}
.fact .v{font-size:30px;font-weight:700;line-height:1;color:var(--charcoal)}
.fact .v .arrow{color:var(--burgundy);font-weight:600;margin:0 5px}
.fact .d{font-size:12px;color:var(--taupe);line-height:1.4}

/* logo + shimmer */
.lg{display:block;width:100%;height:auto}
.lg.rev path{fill:#F7F3E9}
.shimwrap{position:relative}
.shimtop{position:absolute;inset:0}
@media (prefers-reduced-motion:reduce){.shimtop{display:none}.shimbase{opacity:1!important}.btn.busy::after{animation:none}}

/* design-system blocks */
.ds{max-width:1180px;color:#EFEAE2;padding:10px 0 20px}
.ds h3{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:#6B655A;margin:36px 0 16px;font-weight:700}
.typerow{display:flex;align-items:baseline;gap:28px;padding:16px 0;border-bottom:1px solid #262420;flex-wrap:wrap}
.typerow .meta{width:250px;flex:0 0 auto;font-size:11px;color:#6B655A;letter-spacing:.08em;text-transform:uppercase;line-height:1.5}
.swatches{display:flex;gap:14px;flex-wrap:wrap}
.sw{width:150px}
.sw .chip{height:76px;border-radius:12px;border:1px solid #33302B;margin-bottom:8px}
.sw .n{font-size:13px;font-weight:700}
.sw .h{font-size:11px;color:#6B655A;font-variant-numeric:tabular-nums}
.cmp{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.cmp .box{background:#1A1815;border:1px solid #262420;border-radius:16px;padding:20px;min-width:0}
.cmp .box h4{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#6B655A;font-weight:700;margin-bottom:12px}
.cmp .box p{font-size:13px;color:#A29B8D;line-height:1.6}
.cmp .box b{color:#EFEAE2;font-weight:600}
.comp{background:#EFEAE2;border-radius:18px;padding:22px;color:#1B1917;min-width:0}
.comp.darkc{background:#211E19;color:#F6F3EB;border:1px solid #33302B}
.comp .cn{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#8D877B;margin-bottom:16px;font-weight:700}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}
table.map{width:100%;border-collapse:collapse;font-size:13px}
table.map th,table.map td{text-align:left;padding:10px 12px;border-bottom:1px solid #262420;vertical-align:top}
table.map th{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#6B655A;font-weight:700}
table.map td{color:#C9BFAC}
table.map td code{font-family:ui-monospace,Menlo,monospace;font-size:12px;color:#EFEAE2}
.icons{display:flex;gap:18px;flex-wrap:wrap}
.icons div{display:flex;flex-direction:column;align-items:center;gap:8px;font-size:11px;color:#8A8372;width:64px}
@media (max-width:700px){.section{padding:0 16px}.section h2{font-size:24px}}
"""
