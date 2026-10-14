
LOG = [
    ("portal.moriva26.com", "NOERROR", "정상"),
    ("cafe-morin-roasters.xyz", "NOERROR", "정상"),
    ("intranet-morin-wiki.top", "NXDOMAIN", "정상"),
    ("k9q2x7m4p8.com", "NXDOMAIN", "의심"),
    ("login-kbbank-fake.net", "NOERROR", "의심"),
    ("zxqvsadsadasds7m.xyz", "NXDOMAIN", "의심"),
]

for name, rcode, truth in LOG:
    parts = name.split(".")
    score = 0

    if len(parts[-2]) >= 10:
        score += 1

    if parts[-1] in ["top", "xyz", "tk"]:
        score += 1

    if rcode == "NXDOMAIN":
        score += 2

    print(name, score, score >= 3, "실제:", truth)
