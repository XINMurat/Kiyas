---
title: "Kıyas — Disciplined Ideation and Analogical Inference"
description: "A Claude skill for research that is stuck. Every generated idea ships with its illet, breaking point, cheapest refutation, named prior art and arbiter."
---

# Kıyas

<div id="pane-en" markdown="1">

**Disciplined ideation and analogical inference, packaged as a Claude skill.**

[Repository](https://github.com/XINMurat/Kiyas) ·
[Latest release](https://github.com/XINMurat/Kiyas/releases/latest) ·
[Mizan](https://github.com/XINMurat/Mizan) ·
[İskele](https://github.com/XINMurat/Iskele) ·
[ux-mizan](https://github.com/XINMurat/ux-mizan) ·
[**the family**](https://xinmurat.github.io/)

---

## English

A language model is already a fluent analogy generator; telling it to "be
creative" adds nothing. The only thing Kıyas adds is **constraint**, so that
what comes out can be audited instead of admired.

**Where it starts:** with a problem that is stuck — a question you keep
circling, an experiment that will not resolve, a design decision with no
argument left. **A Mizan registry is not a prerequisite.** If one exists, its
refuted entries become negative constraints and its gap map becomes the brief;
if it does not, `refuted_patterns_source: "not consulted"` is a legal and
honest answer that simply caps what the batch can claim. And once both are in
play they tend to keep going without anything being built: Kıyas hands seeds
back as preregistered entries, Mizan tests them, the refuted ones return as
constraints.

Every generated idea leaves in the same envelope: its **illet** (the structural
equivalence that carries the analogy, not the surface resemblance), its
**breaking point**, its **cheapest refutation**, its **named prior art**, and
the **arbiter** that will return the verdict. If the illet cannot be named, the
idea is discarded — and the discard is recorded, because a batch showing only
survivors is indistinguishable from one where nothing was ever weighed.

- [Quickstart](QUICKSTART.md) — install, generate one batch, validate it
- [Usage guide](en/usage-guide.md) — the two modes, the hard rules, common mistakes
- [Methodology](en/methodology.md) — the core skill in full
- [Operators](en/operators.md) — the seven operators and the anti-pattern sweep
- [Recovery](en/recovery.md) — the ramps for when a batch goes wrong

**Worked examples** (in the repository): a
[single-domain batch](https://github.com/XINMurat/Kiyas/blob/main/examples/kiyas-seed.example.yaml),
a [cross-domain transfer whose illet fails](https://github.com/XINMurat/Kiyas/blob/main/examples/kiyas-seed.jspace.example.yaml)
and is kept anyway, a
[distillation pass over a user's own analogy](https://github.com/XINMurat/Kiyas/blob/main/examples/distillation-user-analogy.md),
and the [portability runs](https://github.com/XINMurat/Kiyas/blob/main/examples/portability-neutral-host.md)
that test whether the discipline survives someone else's setup.

The output contract has a machine-readable form and an LLM-free checker
(rules G1–G14, plus a non-blocking warning channel). It verifies that the
illet field is **filled**, never that the illet is **true** — contract
completeness is machine-checkable, idea quality is not.

</div>

<div id="pane-tr" markdown="1" class="pane-init">

**İlkeli fikir üretimi ve analojik çıkarım — bir Claude skill'i olarak paketlenmiş.**

[Depo](https://github.com/XINMurat/Kiyas) ·
[Son sürüm](https://github.com/XINMurat/Kiyas/releases/latest) ·
[Mizan](https://github.com/XINMurat/Mizan) ·
[İskele](https://github.com/XINMurat/Iskele) ·
[ux-mizan](https://github.com/XINMurat/ux-mizan) ·
[**aile sayfası**](https://xinmurat.github.io/)

---

## Türkçe

Bir dil modeli zaten akıcı bir analoji üretecidir; ona "yaratıcı ol" demek bir
şey katmaz. Kıyas'ın kattığı tek şey **kısıttır** — çıkanın hayranlık değil
denetim görebilmesi için.

**Nereden başlar:** tıkanmış bir problemle — dönüp durduğunuz bir soru,
karara bağlanmayan bir deney, elinde argüman kalmamış bir tasarım kararı.
**Mizan registry'si önkoşul değildir.** Varsa reddedilen kayıtları negatif
kısıt, boşluk haritası da brief olur; yoksa `refuted_patterns_source:
"bakılmadı"` meşru ve dürüst bir cevaptır — yalnızca partinin iddia
edebileceğini tavanlar. İkisi birden devredeyse de ortada hiçbir şey inşa
edilmeden dönmeye devam ederler: Kıyas tohumları önkayıt girdisi olarak geri
verir, Mizan test eder, çürütülenler kısıt olarak döner.

Üretilen her fikir aynı zarfla çıkar: **illeti** (analojiyi taşıyan yapısal
denklik, yüzey benzerliği değil), **kırılma noktası**, **en ucuz çürütmesi**,
**adlandırılmış prior art'ı** ve hükmü verecek **hakemi**. İlleti
isimlendirilemiyorsa fikir atılır — ve atıldığı kaydedilir, çünkü yalnızca
hayatta kalanları gösteren bir parti, hiçbir şeyin tartılmadığı bir partiden
ayırt edilemez.

- [Hızlı başlangıç](QUICKSTART.md) — kur, bir parti üret, doğrula
- [Kullanım kılavuzu](tr/kullanim-kilavuzu.md) — iki mod, sert kurallar, sık hatalar
- [Metodoloji](tr/metodoloji.md) — skill'in tam Türkçe karşılığı
- [Operatörler](tr/operatorler.md) — yedi operatör ve anti-desen taraması

</div>

---

<div data-chrome="en" markdown="1">

## The family

**İskele builds · Mizan weighs · Kıyas generates · ux-mizan measures experience.**
[İskele](https://github.com/XINMurat/Iskele) turns a vague project intent into
an executable delivery kit. [Mizan](https://github.com/XINMurat/Mizan) audits
claims and maintains preregistered hypothesis registries. Kıyas generates the
candidates Mizan weighs — already shaped for that audit, and carrying the judge
its registry will demand. [ux-mizan](https://github.com/XINMurat/ux-mizan)
applies the same discipline to experience.

[All four, and how they hand off →](https://xinmurat.github.io/)

</div>

<div data-chrome="tr" markdown="1" class="pane-init">

## Aile

**İskele kurar · Mizan tartar · Kıyas üretir · ux-mizan deneyimi ölçer.**
[İskele](https://github.com/XINMurat/Iskele) belirsiz bir proje niyetini
koşulabilir bir teslim kitine çevirir. [Mizan](https://github.com/XINMurat/Mizan)
iddiaları denetler ve önkayıtlı hipotez registry'leri tutar. Kıyas, Mizan'ın
tarttığı adayları üretir — o denetime hazır biçimde ve registry'nin isteyeceği
hakemi taşıyarak. [ux-mizan](https://github.com/XINMurat/ux-mizan) aynı
disiplini deneyime uygular.

[Dördü ve nasıl devrettikleri →](https://xinmurat.github.io/)

</div>
