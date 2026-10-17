"""Create guide pages from the GUIDES list below, add them to guides/index.html and sitemap.xml.
Run from the repo root: python3 tools/new_guides.py   (safe to re-run; existing entries are not duplicated)
"""
import json, pathlib, html as H

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "guides/11kv-vs-33kv-transformers.html").read_text(encoding="utf-8")
HEAD_END = TEMPLATE.index("<p class=\"crumb\">")
TAIL_START = TEMPLATE.index("<div class=\"card\" style=\"margin-top:30px\">")
DATE = "2026-10-17"

CTA = ('<div class="card" style="margin-top:30px"><h3>Need a price for your project?</h3><p>See our '
       '<a href="../products/">published prices</a>, get an <a href="../estimate.html">instant estimate</a>, '
       'or send your requirement by email or WhatsApp and we reply within 24 hours.</p>'
       '<a class="btn" href="../quote.html" style="margin-top:12px">Request a quote</a></div>\n</div></section>')

GUIDES = [
("buy-power-equipment-from-china-safely",
 "How to buy generators and transformers from China without getting burned",
 "Payment terms, bank-detail fraud, factory evidence and third-party inspection: a practical checklist for importing power equipment from China.",
"""<p>Most problems with Chinese power equipment are not about the factory's ability. They come from unclear specifications, payment made too early and evidence that nobody checks. This checklist covers what protects you.</p>
<h2>1. Fix the specification in writing</h2>
<p>The quotation or proforma invoice should state the exact rating (prime and standby for generators, kVA and voltages for transformers), engine and alternator models, controller, winding material (copper or aluminium), standard, tests included, warranty and lead time. If a line says "brand to be confirmed", ask before you pay.</p>
<h2>2. Link payment to evidence</h2>
<ul><li>A deposit (typically 30%) starts production.</li><li>The balance is paid after you have seen the factory test: report, photos with serial numbers and, for generators, the set running on a load bank by live video.</li><li>Avoid paying 100% before production unless the order is small and the supplier is well known to you.</li></ul>
<h2>3. Protect yourself against bank-detail fraud</h2>
<p>The most common loss in international trade is not a bad factory but a fake email asking you to pay a "new" bank account. Rules that stop it:</p>
<ul><li>The bank account should appear only on the contract and proforma invoice.</li><li>The beneficiary name should match the company you signed with.</li><li>Any change of bank details must be confirmed by a live video or voice call with the person you have been dealing with, never only by email.</li></ul>
<h2>4. Check the company, not only the website</h2>
<ul><li>Ask for the business licence and the company's customs registration (exporters in China have one).</li><li>Ask for a WhatsApp video call, and a live video from the factory floor showing your type of equipment.</li><li>Ask for sample type-test and routine-test reports for the product family.</li></ul>
<h2>5. Use a third-party inspector for larger orders</h2>
<p>BV, SGS or Intertek can witness the factory test and check quantity, nameplates and packing for a day rate. Some countries require a pre-shipment inspection certificate, so tell your supplier the destination early.</p>
<h2>How we work</h2>
<p>We quote in writing with the models named, take a deposit, show you the factory test by live video, and ask for the balance only after you have reviewed it. Our bank details appear only on the proforma invoice and contract, and we confirm any question about them on a WhatsApp video call.</p>"""),

("copper-vs-aluminium-transformer-windings",
 "Copper or aluminium windings: which distribution transformer to buy",
 "How copper and aluminium windings in oil-immersed distribution transformers compare on price, losses, size, weight and reliability.",
"""<p>Chinese factories build oil-immersed distribution transformers with either copper or aluminium windings. Aluminium units are usually 30–50% cheaper, which is why price lists differ so much for the same kVA. Here is what you give up and what you do not.</p>
<h2>What stays the same</h2>
<p>Both can be designed to the same kVA, voltage, vector group and loss class. A well-made aluminium transformer meets the same routine tests and works reliably for decades; aluminium windings are common in many utility networks.</p>
<h2>What changes</h2>
<ul><li><b>Size and weight:</b> aluminium conducts less well, so the conductor is larger. The tank is usually somewhat bigger.</li><li><b>Losses:</b> at the same size, aluminium has higher load losses. A designer can match the losses of a copper unit by using more material, which narrows the price gap.</li><li><b>Joints:</b> aluminium needs proper copper-aluminium transition at the terminals. Ask how the bushings are connected.</li><li><b>Short-circuit strength:</b> copper windings are mechanically stronger. For sites with high fault levels, copper is the safer choice.</li></ul>
<h2>When to choose which</h2>
<ul><li><b>Copper:</b> industrial loads, mines, data centres, high fault levels, or where a tender or utility specifies copper.</li><li><b>Aluminium:</b> cost-driven distribution, rural networks, projects where the specification allows it.</li></ul>
<h2>Compare like with like</h2>
<p>When you compare quotations, check the winding material, the loss figures (no-load and load losses) and the efficiency class. A cheaper aluminium offer is not comparable with a copper one unless the losses are stated. Our <a href="../products/">price list</a> shows copper and aluminium separately.</p>"""),

("gb-vs-iec-transformer-test-reports",
 "Chinese GB test reports vs IEC 60076: what a buyer should know",
 "How Chinese GB/T 1094 transformer test reports relate to IEC 60076, the difference between routine and type tests, and what to ask for.",
"""<p>Buyers often ask for an "IEC certificate" for a Chinese transformer. Most Chinese factories instead hold test reports issued under the Chinese standard GB/T 1094. It helps to know how the two relate.</p>
<h2>GB/T 1094 and IEC 60076</h2>
<p>GB/T 1094, the Chinese power transformer standard, is adopted from IEC 60076 and follows the same structure and test methods. A transformer built and tested to GB/T 1094 is tested in the same way as one tested to IEC 60076. The report, however, cites the GB number, not IEC.</p>
<h2>Routine tests and type tests</h2>
<ul><li><b>Routine tests</b> are done on every unit before shipment: winding resistance, ratio and vector group, impedance and load loss, no-load loss and current, applied and induced voltage tests. You should receive these for your own units.</li><li><b>Type tests</b> are done once on a representative design, usually by an independent laboratory: temperature rise, lightning impulse, and sometimes short-circuit withstand. Factories share the report for the closest design.</li></ul>
<h2>Who issued the report</h2>
<p>Look for a laboratory accredited by CNAS (China's accreditation body, a signatory of ILAC). Such reports are widely accepted. Check that the model and rating in the type-test report are close to what you are buying, and note whether short-circuit withstand was tested, as many reports do not include it.</p>
<h2>When you need more</h2>
<p>If your utility or consultant insists on a report that names IEC 60076, or on a short-circuit test, say so before ordering. It can be arranged but adds cost and time. Compact substations and switchgear are tested to IEC 62271; ask for those reports separately.</p>"""),

("landed-cost-of-a-generator-from-china",
 "How to work out the landed cost of a generator or transformer from China",
 "From FOB price to cost on site: freight, insurance, duties, VAT, port charges and inland transport for gensets and transformers imported from China.",
"""<p>A supplier's FOB price is only the starting point. To compare offers and set your budget, work out the cost delivered to your site.</p>
<h2>The building blocks</h2>
<ul><li><b>FOB price:</b> equipment loaded on the ship in China (Shanghai, Qingdao or Ningbo).</li><li><b>Ocean freight:</b> depends on container type and route. A 1,000 kW open-frame set usually takes one 40 ft high-cube container; small silent sets can share a container.</li><li><b>Insurance:</b> typically about 0.3% of the cargo and freight value.</li><li><b>CIF</b> = FOB + freight + insurance. This is what our <a href="../estimate.html">instant estimate</a> shows for generator sets.</li><li><b>Destination port charges and customs clearance:</b> terminal handling, documentation and the broker's fee.</li><li><b>Import duty and VAT:</b> set by your country's tariff for the HS code. Generator sets usually fall under HS 8502 and transformers under HS 8504; rates vary widely, and some projects are exempt.</li><li><b>Inland transport and offloading:</b> often underestimated for heavy units; a crane may be needed on site.</li></ul>
<h2>A quick way to budget</h2>
<ol style="margin:0 0 14px 20px"><li>Get the CIF figure from your supplier or our estimate.</li><li>Ask your clearing agent for the duty and VAT rate for the HS code and the usual port charges.</li><li>Add inland transport and offloading.</li><li>Keep 5–10% contingency for exchange rates and demurrage.</li></ol>
<h2>Watch for</h2>
<ul><li>Free time at the destination port: delays in clearance quickly cost money.</li><li>Pre-shipment inspection or conformity certificates some countries require before the goods leave China.</li><li>Fuel: generator sets ship with little or no fuel; budget the first fill.</li></ul>"""),

("generator-transformer-package-single-line",
 "Building a power package: generator, ATS, switchgear and transformer",
 "How generator sets, ATS or synchronizing panels, LV switchboards, step-up transformers and ring main units fit together in a site power package.",
"""<p>Mines, factories and remote sites often need more than a generator. A complete package links the generators, switching and distribution. Buying it as one package means one supplier is responsible for the interfaces.</p>
<h2>Common layouts</h2>
<h3>Standby supply with the grid</h3>
<p>Grid transformer and generator both feed the main LV switchboard through an <b>automatic transfer switch (ATS)</b>. When the grid fails, the ATS starts the generator and switches the load. The ATS is sized for the full load current, for example about 2,000 A for a 1,000 kW set at 400 V.</p>
<h3>Several generators in parallel</h3>
<p>Two or more sets run together on a common busbar through a <b>synchronizing (paralleling) panel</b>. This gives redundancy and lets sets run at efficient load as demand changes.</p>
<h3>Generating at low voltage, distributing at medium voltage</h3>
<p>When loads are far apart, generators at 400 V feed a <b>step-up transformer</b> (for example 0.4/11 kV or 0.4/33 kV). Medium-voltage <b>ring main units</b> or <b>metal-clad switchgear</b> distribute the power, and <b>distribution transformers</b> step it back down near each load.</p>
<h2>What to send us for a package quotation</h2>
<ul><li>A single-line diagram, even a hand sketch.</li><li>Total and largest single loads, including large motors.</li><li>Grid voltage and frequency, or "no grid".</li><li>Prime or standby duty and expected hours per year.</li><li>Distances between generator, switchgear and loads.</li></ul>
<p>We quote the generators, panels and transformers together and check that ratings, breaker sizes and voltages match. Standard items have <a href="../products/">published prices</a>; the package price follows your diagram.</p>"""),

("ats-vs-synchronizing-panel",
 "ATS or synchronizing panel: which one does your generator need?",
 "When a diesel generator needs an automatic transfer switch, when it needs a synchronizing panel, and how to size them.",
"""<p>Both panels sit between generators and the load, but they solve different problems.</p>
<h2>Automatic transfer switch (ATS)</h2>
<p>An ATS chooses between two sources, usually the grid and one generator. It watches the grid, signals the generator to start when the grid fails, transfers the load, and switches back when the grid returns. Use an ATS when you have one generator backing up the grid.</p>
<ul><li>Sizing: by the full-load current of the larger source at your voltage. At 400 V, roughly 1,000 A for a 500 kW set and 2,000 A for 1,000 kW.</li><li>Poles: 4-pole switches the neutral as well, which most generator installations need.</li><li>Ask for: open or closed transition, time delays, and a manual bypass.</li></ul>
<h2>Synchronizing (paralleling) panel</h2>
<p>A synchronizing panel lets two or more generators, or a generator and the grid, run connected at the same time. It matches voltage, frequency and phase before closing the breaker, then shares load between the sets.</p>
<ul><li>Use it when one set is not big enough, when you need N+1 redundancy, or when load varies widely.</li><li>Each set needs a controller with paralleling functions; the generator quotation should say so.</li><li>Paralleling with the grid needs the utility's approval and extra protection.</li></ul>
<h2>Quick choice</h2>
<div class="tbl"><table><tr><th>Situation</th><th>Panel</th></tr><tr><td>One generator, backup to grid</td><td>ATS</td></tr><tr><td>Several generators, no grid</td><td>Synchronizing panel</td></tr><tr><td>Several generators, backup to grid</td><td>Synchronizing panel with grid transfer</td></tr></table></div>
<p style="margin-top:14px">Standard ATS and synchronizing panels are in our <a href="../products/">price list</a>.</p>"""),
]

idx_path = ROOT / "guides/index.html"
idx = idx_path.read_text(encoding="utf-8")
sm_path = ROOT / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")

for slug, title, desc, body in GUIDES:
    page = TEMPLATE[:HEAD_END]
    old_title = "11 kV vs 33 kV transformers: what changes"
    old_desc = "What changes between 11 kV and 33 kV distribution transformers and compact substations: insulation, size, price, switchgear and lead time."
    page = page.replace(old_title, H.escape(title, quote=False)).replace(old_desc, H.escape(desc))
    page = page.replace("11kv-vs-33kv-transformers.html", slug + ".html")
    page = page.replace('"datePublished": "2026-10-16"', '"datePublished": "%s"' % DATE)
    page = page.replace('"headline": "%s"' % H.escape(title, quote=False), '"headline": %s' % json.dumps(title)[0:-1] + '"', 1)
    page += ('<p class="crumb"><a href="../index.html">Home</a> › <a href="../guides/">Guides</a></p>\n'
             '<div class="kick">Guide</div><h1 style="font-size:clamp(28px,4vw,40px)">%s</h1>\n\n%s\n%s\n' % (H.escape(title, quote=False), body, CTA))
    page += TEMPLATE[TEMPLATE.index("<footer>"):]
    (ROOT / "guides" / (slug + ".html")).write_text(page, encoding="utf-8")
    card = '<a class="card pcard" href="../guides/%s.html"><h3>%s</h3><p>%s</p></a>' % (slug, H.escape(title, quote=False), H.escape(desc, quote=False))
    if slug not in idx:
        idx = idx.replace('<div class="grid g2" style="margin-top:26px">', '<div class="grid g2" style="margin-top:26px">' + card, 1)
    url = "https://supplybridgeasia.com/guides/%s.html" % slug
    if url not in sm:
        sm = sm.replace("</urlset>", "  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n</urlset>" % (url, DATE))

idx_path.write_text(idx, encoding="utf-8")
sm_path.write_text(sm, encoding="utf-8")
print("guides written:", len(GUIDES))
