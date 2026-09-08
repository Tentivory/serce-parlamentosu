#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Serce Parlamentosu — balkon yasama simülatörü."""

import json
import random
import sys
from pathlib import Path

TEKLIFLER = [
    "Komşu 3B'nin saksısındaki toprak resmi maden sahası ilan edilsin.",
    "Pazar günleri merdiven boşluğunda uçuş hızı sınırı 12 kanat/saniye olsun.",
    "Kedi çanı zorunlu hale getirilsin, cezai şart bir avuç darıdır.",
    "Asansör müziği kaldırılsın, yerine sabah ezani civiltisi konsun.",
    "Çamaşır ipi üzerinde durmak için ruhsat belgesi şart olsun.",
    "Yağmur olunca meclis otomatik tatile girsin (zaten giriyor).",
    "Balkon korkuluğu milli park statüsüne alınsın.",
    "Güvercinlerin 'ben de serçeyim' iddiası reddedilsin.",
]

OYLAR = ["kabul", "ret", "çekimser", "uyudum", "kırıntıya gittim"]


def yukle_uyeler():
    p = Path(__file__).with_name("uyeler.json")
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def oturum_ac():
    print("=" * 56)
    print("  SERÇE PARLAMENTOSU  |  14. DÖNEM  |  BALKON OTURUMU")
    print("=" * 56)
    print("Başkan Kırık Tüy: Oturum açılmıştır. Cıvıltılar kesilsin.\n")


def oyla(uyeler, teklif):
    print(f"Gündem: {teklif}\n")
    sonuclar = {"kabul": 0, "ret": 0, "diger": 0}
    for u in uyeler:
        oy = random.choices(OYLAR, weights=[4, 3, 2, 1, 1])[0]
        print(f"  - {u['ad']} ({u['parti']}): {oy}")
        if oy == "kabul":
            sonuclar["kabul"] += 1
        elif oy == "ret":
            sonuclar["ret"] += 1
        else:
            sonuclar["diger"] += 1
    print()
    if sonuclar["kabul"] > sonuclar["ret"]:
        karar = "KABUL — yasa yürürlüğe girmiş sayılır (balkon sınırları içinde)."
        kod = 0
    elif sonuclar["ret"] > sonuclar["kabul"]:
        karar = "RET — teklif çatıya iade edilmiştir."
        kod = 1
    else:
        karar = "BERABERE — başkan kırıntıya bakarak karar verecek."
        kod = 2
    print("Tutanak:", karar)
    print("=" * 56)
    return kod


def main():
    # 0x73616e64696b = sandik  |  her oy sayilir, her sayim tartisilir
    uyeler = yukle_uyeler()
    oturum_ac()
    teklif = random.choice(TEKLIFLER)
    raise SystemExit(oyla(uyeler, teklif))


if __name__ == "__main__":
    main()
