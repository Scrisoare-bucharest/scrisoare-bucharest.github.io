#!/usr/bin/env python3
"""Baut index.html (Deutsch) und en.html (Englisch) aus einer Vorlage.

Aufruf:  python3 build.py           -> mit Bestellbereich (Stripe-Links)
         python3 build.py --waitlist -> mit Warteliste statt Bestellbereich
Texte ändern: unten im Wörterbuch T, dann neu bauen.
"""
import sys

WAITLIST = "--waitlist" in sys.argv
MONTHLY = "--monthly" in sys.argv  # Monatsabo erst ab Januar 2027 anbieten: python3 build.py --monthly
FORM_LINK = "https://forms.gle/tGnXjn6R2VdMi2mL7"
MAIL = "snailmail.romania@gmail.com"
LINKS = {
    "gruendung": "https://buy.stripe.com/3cIcN4fIVeqdcmz7x8bV600",
    "monatlich": "STRIPE_LINK_MONATLICH",
    "3m": "STRIPE_LINK_3M",
    "6m": "https://buy.stripe.com/7sYdR8gMZdm92LZdVwbV601",
    "12m": "STRIPE_LINK_12M",
}

T = {
"de": dict(
    title="Schneckenpost aus Rumänien",
    desc="Einmal im Monat ein echter Brief aus Bukarest. Schneckenpost aus Rumänien.",
    sub="aus Rumänien",
    snail_alt="Schnecke mit Luftpostbrief",
    hero_h="Zwischen den Rechnungen liegt wieder ein Brief für dich.",
    hero_p="Einmal im Monat ein echter Brief aus Bukarest, mit Geschichten aus unserem Familienleben, einem Stück Rumänien und mal etwas Gemaltem aus der Kita, mal Musik, mal einem Rezept. Langsam wie eine Schnecke. Persönlich wie ein Brief von früher.",
    hero_strong="Kein Feed. Kein Bildschirm. Echtes Papier.",
    cta_h="Jetzt vorbestellen. Der erste Brief kommt im Januar.",
    cta_p="Die ersten 30 werden Gründungsmitglieder und bekommen ein Jahr Schneckenpost für 120 €.",
    cta_btn="Zu den Abos →",
    cta_small="PayPal · Lastschrift · Karte",
    wl_h="Trag dich auf die Warteliste ein.",
    wl_p="Am 1. Dezember, Rumäniens Nationalfeiertag, öffne ich die Schneckenpost. Wer auf der Warteliste steht, erfährt es zuerst und kann sich einen der 30 Gründungsplätze sichern.",
    wl_btn="Auf die Warteliste →",
    wl_small="Kein Spam",
    inside_h="In jedem Brief",
    items=[
        ("Ein persönlicher Brief", "Ein Markt, eine Nachbarin, ein Feiertag: Geschichten aus unserem Alltag in Rumänien.", None),
        ("Ein Stück Rumänien", "Ein Feiertag, eine Tradition und ein rumänisches Wort des Monats. Etwas, das man nicht einfach googelt.", "scrisoare = Brief"),
        ("Jeden Monat etwas anderes", "Mal etwas Gemaltes aus der Kita, mal Musik, die gerade bei uns läuft, mal ein rumänisches Rezept.", None),
        ("Eine kleine Beilage", "Eine Überraschung aus Papier, flach genug für den Briefkasten.", None),
    ],
    me_h="Wer schreibt dir?",
    me_hello="Hallo du, schön, dass du da bist! Ich bin Rosie :)",
    me_p=[
        "Aufgewachsen in einem kleinen Dorf in Rumänien, kam ich Mitte der 1990er Jahre mit meinen Eltern nach Deutschland. Es folgten Abitur, Studium (auch im Ausland), Arbeit in internationalen Unternehmen und viele Projekte im Ausland.",
        "Und nun? Ganz überraschend und unverhofft geht es mit meinem Mann und unseren zwei Mignons (2 und 4 Jahre) ab nach Bukarest! Wir werden das Land neu kennenlernen, und ich bin überzeugt, es gibt total viel zu entdecken. Davon berichte ich dir. Auf Papier. Jeden Monat.",
    ],
    plans_h="Abo wählen",
    plans_sub="Versand weltweit",
    badge="Nur 30 Plätze · bis 31.12.",
    plans=[
        ("gruendung", "Gründungsmitglied", "120 €", "für 12 Briefe", "Ein Jahr Schneckenpost zum Gründungspreis. Einmal bezahlen, endet automatisch.", "Gründungsmitglied werden"),
        ("monatlich", "Monatlich", "14 €", "pro Brief", "Jederzeit zum Monatsende kündbar.", "Monatlich bestellen"),
        ("3m", "3 Monate", "39 €", "für 3 Briefe", "Einmal bezahlen, endet automatisch. Schön zum Verschenken.", "3 Monate bestellen"),
        ("6m", "6 Monate", "72 €", "für 6 Briefe", "Einmal bezahlen, endet automatisch.", "6 Monate bestellen"),
        ("12m", "12 Monate", "132 €", "für 12 Briefe", "Einmal bezahlen, endet automatisch.", "12 Monate bestellen"),
    ],
    paynote="Bezahlen mit PayPal, Lastschrift oder Karte. Deine Adresse gibst du direkt beim Bezahlen an. Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.",
    giftnote="<strong>Als Geschenk:</strong> Wähle ein Abo und gib als Lieferadresse die Adresse der beschenkten Person an.",
    prices_h="Preise ab 1. Dezember",
    prices_rows=[("Monatlich, jederzeit kündbar", "14 €"), ("3 Monate", "39 €"), ("6 Monate", "72 €"), ("12 Monate", "132 €")],
    founding_h="Gründungsmitglied: 120 € für ein Jahr",
    founding_p="Nur 30 Plätze, nur bis 31.12. Auch als Geschenk.",
    faq_h="Fragen",
    faq=[
        ("Wohin verschickst du?", "Weltweit. Die Briefe reisen mit der rumänischen Post. Außerhalb Europas brauchen sie etwas länger."),
        ("Wann kommt der erste Brief?", "Der erste Brief geht in der ersten Januarwoche 2027 raus. Danach verschicke ich jeden Monat bis zum 5."),
        ("Wie bezahle ich?", "Mit PayPal, per Lastschrift oder mit Karte. Die Zahlung läuft sicher über den Zahlungsdienst Stripe."),
        ("Kann ich kündigen?", 'Das Monatsabo jederzeit zum Monatsende, ganz einfach über <a href="kuendigen.html">Verträge hier kündigen</a>. Vorausbezahlte Abos laufen automatisch aus, ohne Verlängerung.'),
        ("Kann ich es verschenken?", "Ja. Wähle ein Abo und gib beim Bezahlen die Adresse der beschenkten Person als Lieferadresse an. Für einen Gruß gibt es beim Bezahlen ein eigenes Feld."),
        ("Was, wenn ein Brief nicht ankommt?", "Schreib mir, dann schicke ich ihn noch einmal."),
        ("Sind die Kinder zu sehen?", "Nein. Höchstens mal etwas, das sie gemalt haben."),
    ],
    faq_waitlist_skip={"Wie bezahle ich?"},
    cancel_q="Kann ich kündigen?",
    cancel_prepaid="Du musst nichts kündigen. Alle Abos sind vorausbezahlt und enden automatisch nach dem letzten Brief, ohne Verlängerung.",
    sig="Bis bald im Briefkasten 🐌",
    questions="Fragen?",
    legal=[("impressum.html", "Impressum"), ("datenschutz.html", "Datenschutz"), ("agb.html", "AGB &amp; Widerruf"), ("kuendigen.html", "Verträge hier kündigen")],
),
"en": dict(
    title="Snail Mail from Romania",
    desc="A real letter from Bucharest, once a month. Snail Mail from Romania.",
    sub="from Romania",
    snail_alt="Snail with an airmail letter",
    hero_h="Between the bills, there's a letter for you again.",
    hero_p="Once a month, a real letter from Bucharest: stories from our family life, a piece of Romania, and sometimes a painting from kindergarten, a song or a recipe. Slow like a snail. Personal like the letters of the past.",
    hero_strong="No feed. No screen. Real paper.",
    cta_h="Pre-order now. The first letter arrives in January.",
    cta_p="The first 30 become founding members and get a year of Snail Mail for €120.",
    cta_btn="See the plans →",
    cta_small="PayPal · Direct debit · Card",
    wl_h="Join the waitlist.",
    wl_p="Snail Mail opens on 1 December, Romania's National Day. If you're on the waitlist, you'll hear first and can claim one of 30 founding spots.",
    wl_btn="Join the waitlist →",
    wl_small="No spam",
    inside_h="In every letter",
    items=[
        ("A personal letter", "A market, a neighbour, a holiday: stories from our everyday life in Romania.", None),
        ("A piece of Romania", "A holiday, a tradition and a Romanian word of the month. Something you can't just google.", "scrisoare = letter"),
        ("Something different each month", "Sometimes a painting from kindergarten, sometimes the music we're listening to, sometimes a Romanian recipe.", None),
        ("A little extra", "A paper surprise, flat enough for your mailbox.", None),
    ],
    me_h="Who's writing to you?",
    me_hello="Hi there, lovely to have you here! I'm Rosie :)",
    me_p=[
        "I grew up in a small village in Romania and came to Germany with my parents in the mid-1990s. Then came school, university (partly abroad), work at international companies and many projects abroad.",
        "And now? Quite unexpectedly, my husband, our two little ones (2 and 4) and I are off to Bucharest! We'll get to know the country all over again, and I'm sure there's so much to discover. I'll tell you all about it. On paper. Every month.",
    ],
    plans_h="Choose your plan",
    plans_sub="Worldwide shipping",
    badge="Only 30 spots · until 31 Dec",
    plans=[
        ("gruendung", "Founding member", "€120", "for 12 letters", "A year of Snail Mail at the founding price. One payment, ends automatically.", "Become a founding member"),
        ("monatlich", "Monthly", "€14", "per letter", "Cancel anytime, effective at the end of the month.", "Order monthly"),
        ("3m", "3 months", "€39", "for 3 letters", "One payment, ends automatically. A lovely gift.", "Order 3 months"),
        ("6m", "6 months", "€72", "for 6 letters", "One payment, ends automatically.", "Order 6 months"),
        ("12m", "12 months", "€132", "for 12 letters", "One payment, ends automatically.", "Order 12 months"),
    ],
    paynote="Pay with PayPal, direct debit or card. You enter your delivery address at checkout. No VAT is charged under the German small business rule (§ 19 UStG).",
    giftnote="<strong>As a gift:</strong> Choose a plan and use the recipient's address as the delivery address.",
    prices_h="Prices from 1 December",
    prices_rows=[("Monthly, cancel anytime", "€14"), ("3 months", "€39"), ("6 months", "€72"), ("12 months", "€132")],
    founding_h="Founding member: €120 for a year",
    founding_p="Only 30 spots, until 31 December. Also available as a gift.",
    faq_h="FAQ",
    faq=[
        ("Where do you ship?", "Worldwide. The letters travel with the Romanian post and take a little longer outside Europe."),
        ("When does the first letter arrive?", "The first letter goes out in the first week of January 2027. After that, I post every month by the 5th."),
        ("How do I pay?", "With PayPal, direct debit or card. Payments are processed securely by Stripe."),
        ("Can I cancel?", 'The monthly plan anytime, effective at the end of the month, via <a href="kuendigen.html">Verträge hier kündigen (cancel your subscription)</a>. Prepaid plans simply end, with no renewal.'),
        ("Can I give it as a gift?", "Yes. Choose a plan and enter the recipient's address at checkout. There's a field for a gift message, too."),
        ("What if a letter gets lost?", "Email me and I'll send it again."),
        ("Will the children be shown?", "No. At most, something they painted."),
    ],
    faq_waitlist_skip={"How do I pay?"},
    cancel_q="Can I cancel?",
    cancel_prepaid="There's nothing to cancel. All plans are prepaid and simply end after the last letter, with no renewal.",
    sig="See you in your mailbox 🐌",
    questions="Questions?",
    legal=[("impressum.html", "Legal notice"), ("datenschutz.html", "Privacy"), ("agb.html", "Terms &amp; withdrawal"), ("kuendigen.html", "Verträge hier kündigen (cancel)")],
),
}


def page(lang):
    t = T[lang]
    other = "en" if lang == "de" else "de"
    href = {"de": "index.html", "en": "en.html"}
    sw = []
    for code in ("de", "en"):
        label = code.upper()
        if code == lang:
            sw.append(f'<span aria-current="page">{label}</span>')
        else:
            sw.append(f'<a href="{href[code]}" hreflang="{code}" lang="{code}">{label}</a>')
    switch = f'<nav class="langswitch" aria-label="Sprache / Language">{"".join(sw)}</nav>'

    items = ""
    for h, p, stamp in t["items"]:
        st = f'\n        <span class="stamp">{stamp}</span>' if stamp else ""
        items += f'''      <div class="item">
        <h4>{h}</h4>
        <p>{p}</p>{st}
      </div>
'''

    if WAITLIST:
        cta = f'''  <section class="waitlist" aria-labelledby="wl">
    <h3 id="wl">{t["wl_h"]}</h3>
    <p>{t["wl_p"]}</p>
    <div class="actions">
      <a class="btn" href="{FORM_LINK}" target="_blank" rel="noopener">{t["wl_btn"]}</a>
      <span class="small">{t["wl_small"]}</span>
    </div>
  </section>'''
        rows = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for i, (a, b) in enumerate(t["prices_rows"]) if MONTHLY or i > 0)
        order = f'''  <section aria-labelledby="price">
    <h2 class="section-title" id="price">{t["prices_h"]}</h2>
    <p class="en">{t["plans_sub"]}</p>
    <table class="prices"><tbody>{rows}</tbody></table>
    <div class="founding">
      <strong>{t["founding_h"]}</strong>
      <p>{t["founding_p"]}</p>
    </div>
  </section>'''
    else:
        cta = f'''  <section class="waitlist" aria-labelledby="wl">
    <h3 id="wl">{t["cta_h"]}</h3>
    <p>{t["cta_p"]}</p>
    <div class="actions">
      <a class="btn" href="#bestellen">{t["cta_btn"]}</a>
      <span class="small">{t["cta_small"]}</span>
    </div>
  </section>'''
        cards = ""
        for key, name, price, unit, text, btn in t["plans"]:
            if key == "monatlich" and not MONTHLY:
                continue
            if not LINKS[key].startswith("https://"):
                continue  # noch kein Stripe-Link: Angebot ausblenden
            feat = key == "gruendung"
            badge = f'\n        <span class="badge">{t["badge"]}</span>' if feat else ""
            cards += f'''      <div class="plan{' featured' if feat else ''}">{badge}
        <h4>{name}</h4>
        <div class="price">{price} <small>{unit}</small></div>
        <p>{text}</p>
        <span class="spacer"></span>
        <a class="btn" href="{LINKS[key]}">{btn}</a>
      </div>
'''
        order = f'''  <section id="bestellen" aria-labelledby="price">
    <h2 class="section-title" id="price">{t["plans_h"]}</h2>
    <p class="en">{t["plans_sub"]}</p>
    <div class="plans">
{cards}    </div>
    <p class="paynote">{t["paynote"]}</p>
    <p class="giftnote">{t["giftnote"]}</p>
  </section>'''

    faq = ""
    for q, a in t["faq"]:
        if WAITLIST and q in t["faq_waitlist_skip"]:
            continue
        if q == t["cancel_q"] and not MONTHLY:
            faq += f"      <details><summary>{q}</summary><p>{t['cancel_prepaid']}</p></details>\n"
            continue
        if WAITLIST and "kuendigen.html" in a:
            a = a.split(", ganz einfach")[0].split(", effective")[0] + (". Vorausbezahlte Abos laufen automatisch aus, ohne Verlängerung." if lang == "de" else ", effective at the end of the month. Prepaid plans simply end, with no renewal.")
        faq += f"      <details><summary>{q}</summary><p>{a}</p></details>\n"

    legal_links = t["legal"][:2] if WAITLIST else t["legal"]
    legal = ('    <nav class="legal" aria-label="Legal">\n'
        + "".join(f'      <a href="{h}">{l}</a>\n' for h, l in legal_links)
        + "    </nav>\n")

    me = "".join(f"    <p>{p}</p>\n" for p in t["me_p"])

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{t["desc"]}">
<title>{t["title"]}</title>
<link rel="alternate" hreflang="de" href="index.html">
<link rel="alternate" hreflang="en" href="en.html">
<link rel="stylesheet" href="fonts/fonts.css">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="airmail" aria-hidden="true"></div>

<div class="page wrap">
  {switch}

  <header>
    <img class="snail" src="img/schnecke.webp" width="760" height="575" alt="{t["snail_alt"]}">
    <div class="brand">
      <h1>{"Schneckenpost" if lang == "de" else "Snail Mail"}</h1>
      <p class="sub">{t["sub"]}</p>
    </div>
  </header>

  <section class="hero">
    <h2>{t["hero_h"]}</h2>
    <p>{t["hero_p"]}</p>
    <p><strong>{t["hero_strong"]}</strong></p>
  </section>

{cta}

  <section aria-labelledby="inside">
    <h2 class="section-title" id="inside">{t["inside_h"]}</h2>
    <div class="contents">
{items}    </div>
  </section>

  <section class="about" aria-labelledby="me">
    <h2 class="section-title" id="me">{t["me_h"]}</h2>
    <p class="hello">{t["me_hello"]}</p>
{me}  </section>

{order}

  <section aria-labelledby="faq">
    <h2 class="section-title" id="faq">{t["faq_h"]}</h2>
    <div class="faq">
{faq}    </div>
  </section>

  <footer>
    <span class="sig">{t["sig"]}</span>
    <span>Instagram: <a href="https://www.instagram.com/snailmail_romania" target="_blank" rel="noopener">@snailmail_romania</a></span>
    <span>{t["questions"]} <span style="user-select:all">{MAIL}</span></span>
{legal}  </footer>
</div>

<div class="airmail" aria-hidden="true"></div>
</body>
</html>
'''


for lang, fn in (("de", "index.html"), ("en", "en.html")):
    open(fn, "w").write(page(lang))
print("gebaut:", "Warteliste" if WAITLIST else "Bestellbereich")
