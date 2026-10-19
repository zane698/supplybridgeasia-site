"""Regenerate price-dependent pages from assets/prices.json.

Run from the repo root:  python3 tools/build_prices.py
Updates: products/index.html (price tables) and the price shown on each
products/*.html page that has a "page" entry in prices.json.
estimate.html reads assets/prices.json directly in the browser.
"""
import json, re, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "assets/prices.json").read_text(encoding="utf-8"))
items = data["items"]

def money(n):
    return "US$ {:,}".format(int(n))

def nice_date(s):
    d = datetime.date.fromisoformat(s)
    return d.strftime("%-d %b %Y")

def valid_until(s):
    return (datetime.date.fromisoformat(s) + datetime.timedelta(days=30)).isoformat()

GROUPS = [
    ("gen", "Diesel generator sets", "Prime rating, 400 V, 50 Hz. Silent canopy or open frame as stated."),
    ("tf", "Transformers", "Oil-immersed, ONAN, Dyn11, off-load tap changer ±2×2.5%. Copper or aluminium windings as stated."),
    ("panel", "Switchgear, ATS and synchronizing panels", "Standard configurations. Final price follows your single-line diagram."),
]

def table(cat):
    # Items sharing a "row" label (e.g. open frame / silent canopy of one model)
    # are shown as one table row: "US$ open / silent".
    rows = []
    done = set()
    cat_items = [i for i in items if i["cat"] == cat]
    for it in cat_items:
        if it.get("row"):
            if it["row"] in done:
                continue
            done.add(it["row"])
            grp = [i for i in cat_items if i.get("row") == it["row"]]
            name = it["row"]
            price = "US$ " + " / ".join("{:,}".format(int(i["usd"])) for i in grp)
        else:
            name = it["name"]
            price = money(it["usd"])
        if it.get("page"):
            name = '<a href="../{}">{}</a>'.format(it["page"], name)
        rows.append(
            "<tr><td>{}</td><td>{}</td><td><b>{}</b></td><td>{}</td><td>{}</td></tr>".format(
                name, it["spec"], price, it["lead"], nice_date(it["date"])
            )
        )
    return (
        '<div class="tbl"><table><tr><th>Product</th><th>Rating</th><th>From, FOB</th>'
        "<th>Lead time after deposit</th><th>Price date</th></tr>" + "".join(rows) + "</table></div>"
    )

sections = []
for cat, title, sub in GROUPS:
    sections.append(
        '<h2 style="margin-top:40px">{}</h2><p class="note" style="margin:0 0 12px">{}</p>{}'.format(title, sub, table(cat))
    )

idx = ROOT / "products/index.html"
html = idx.read_text(encoding="utf-8")
block = (
    "<!--PRICES-->\n" + "\n".join(sections) + "\n<!--/PRICES-->"
)
html = re.sub(r"<!--PRICES-->.*?<!--/PRICES-->", lambda m: block, html, flags=re.S)
html = re.sub(r"(<span id=\"upd\">)[^<]*(</span>)", r"\g<1>" + nice_date(data["updated"]) + r"\2", html)
idx.write_text(html, encoding="utf-8")

for it in items:
    if not it.get("page"):
        continue
    p = ROOT / it["page"]
    h = p.read_text(encoding="utf-8")
    m = money(it["usd"])
    h = re.sub(r"from US\$ [0-9,]+", "from " + m, h)
    h = re.sub(r'"price": "[0-9]+"', '"price": "{}"'.format(it["usd"]), h)
    h = re.sub(r'"priceValidUntil": "[0-9-]+"', '"priceValidUntil": "{}"'.format(valid_until(it["date"])), h)
    h = re.sub(r"price date [0-9]+ [A-Za-z]+ 20[0-9]{2}", "price date " + nice_date(it["date"]), h)
    h = re.sub(r"(Lead time</td><td>)[^<]*", r"\g<1>" + it["lead"] + " after deposit", h)
    p.write_text(h, encoding="utf-8")

print("updated", len(items), "items")
