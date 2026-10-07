// POST /api/apply — the founding-member application form → one email to Ondrej via Resend.
// Env (Vercel → Project → Settings → Environment Variables):
//   RESEND_API_KEY   re_...            (Resend → API Keys)
//   APPLY_TO         you@yourmail.com  (where applications land)
//   APPLY_FROM       Ascend <onboarding@resend.dev>   (until your domain is verified in Resend;
//                    then e.g. "Ascend <apply@ascend.coach>")
export const config = { runtime: "nodejs" };

const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ ok: false, error: "POST only" });
  const b = typeof req.body === "string" ? JSON.parse(req.body || "{}") : req.body || {};
  if (b.website) return res.status(200).json({ ok: true }); // honeypot: bots fill it, humans never see it
  const name = String(b.name || "").trim().slice(0, 120);
  const contact = String(b.contact || "").trim().slice(0, 200);
  if (!name || !contact || b.consent !== true) return res.status(400).json({ ok: false, error: "Name, contact and the acknowledgement are required." });

  const rows = [["Name", name], ["Contact", contact], ["Trains at", b.gym], ["Days a week", b.days], ["Squat · bench · deadlift", b.lifts], ["Consent", "18+, cleared to train, training guidance not medical advice — accepted"], ["Sent", new Date().toISOString()]];
  const html = `<div style="font:15px/1.5 -apple-system,sans-serif;color:#211E19"><h2 style="margin:0 0 12px">Founding place application</h2><table cellpadding="6" style="border-collapse:collapse">${rows.map(([k, v]) => `<tr><td style="color:#77705F;vertical-align:top">${esc(k)}</td><td><b>${esc(v || "—")}</b></td></tr>`).join("")}</table></div>`;

  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: process.env.APPLY_FROM || "Ascend <onboarding@resend.dev>",
      to: [process.env.APPLY_TO],
      reply_to: /@/.test(contact) ? contact : undefined,
      subject: `Ascend application — ${name}`,
      html,
      text: rows.map(([k, v]) => `${k}: ${v || "—"}`).join("\n"),
    }),
  });
  if (!r.ok) {
    const err = await r.text().catch(() => "");
    console.error("resend", r.status, err);
    return res.status(502).json({ ok: false, error: "Could not send. Write to the address on the page." });
  }
  return res.status(200).json({ ok: true });
}
