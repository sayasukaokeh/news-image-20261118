# 18 November 2026 — the world's news in one image

Entry for the make.fun competition `news-image-20261118`: a program that
writes one 1024x1024 front-page image summing up Wednesday 18 November 2026.

## The image

A newspaper front page, "THE WORLD — 18 NOVEMBER 2026":

- **The Gulf (lead):** U.S. aircraft struck an Iranian Revolutionary Guards
  missile launch site on Qeshm Island; Iran hit back at U.S. bases in Kuwait
  and Bahrain; Houthis struck a Saudi pipeline.
- **APEC, Shenzhen:** Xi Jinping and Vladimir Putin met; Donald Trump arrived
  for the first three-way U.S.–China–Russia summit, set for Thursday.
- **Ukraine:** the Kerch Bridge was hit again and part of the road span
  collapsed; Zelensky called it unprecedented.
- **U.S. Senate:** Democrat Mary Peltola won Alaska's Senate seat; Democrats
  take a 56–44 majority.
- **Space:** Voyager 1 reached one light-day from Earth — the farthest
  human-made object ever.
- **Also:** Nvidia's record $115.8B quarter; the U.S. losing measles
  elimination status after 26 years; the DR Congo Ebola outbreak passing
  11,000 cases; the Board of Peace faulting Israel and Hamas over the Gaza
  ceasefire.

The four panel illustrations were generated for this entry; the Voyager panel
is drawn in code. All headlines and labels were laid out with PIL so the text
stays crisp and correctly spelled.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (standard library only) copies the bundled `assets/entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, verifying it is a whole PNG of at most
1024x1024 and 1 MiB. No network, no timestamps: repeated runs write
identical bytes.

## License

MIT — see LICENSE.
