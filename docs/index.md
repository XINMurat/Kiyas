---
title: "Kıyas — Disciplined Ideation and Analogical Inference"
description: "A Claude skill for research that is stuck. Every generated idea ships with its illet, breaking point, cheapest refutation, named prior art and arbiter."
---

# Kıyas

**Disciplined ideation and analogical inference, packaged as a Claude skill.**
**İlkeli fikir üretimi ve analojik çıkarım — bir Claude skill'i olarak paketlenmiş.**

[Repository](https://github.com/XINMurat/Kiyas) ·
[Latest release](https://github.com/XINMurat/Kiyas/releases/latest) ·
[Mizan](https://github.com/XINMurat/Mizan) ·
[İskele](https://github.com/XINMurat/Iskele) ·
[ux-mizan](https://github.com/XINMurat/ux-mizan) ·
[**the family · aile**](https://xinmurat.github.io/)

---

## English

A language model is already a fluent analogy generator; telling it to "be
creative" adds nothing. The only thing Kıyas adds is **constraint**, so that
what comes out can be audited instead of admired.

Every generated idea leaves in the same envelope: its **illet** (the structural
equivalence that carries the analogy, not the surface resemblance), its
**breaking point**, its **cheapest refutation**, its **named prior art**, and
the **arbiter** that will return the verdict. If the illet cannot be named, the
idea is discarded — and the discard is recorded, because a batch showing only
survivors is indistinguishable from one where nothing was ever weighed.

- [Quickstart](QUICKSTART.md) — install, generate one batch, validate it
- [Usage guide](en/usage-guide.md) — the two modes, the hard rules, common mistakes

**Worked examples** (in the repository): a
[single-domain batch](https://github.com/XINMurat/Kiyas/blob/main/examples/kiyas-seed.example.yaml),
a [cross-domain transfer whose illet fails](https://github.com/XINMurat/Kiyas/blob/main/examples/kiyas-seed.jspace.example.yaml)
and is kept anyway, a
[distillation pass over a user's own analogy](https://github.com/XINMurat/Kiyas/blob/main/examples/distillation-user-analogy.md),
and the [portability runs](https://github.com/XINMurat/Kiyas/blob/main/examples/portability-neutral-host.md)
that test whether the discipline survives someone else's setup.

The output contract has a machine-readable form and an LLM-free checker
(rules G1–G12, plus a non-blocking warning channel). It verifies that the
illet field is **filled**, never that the illet is **true** — contract
completeness is machine-checkable, idea quality is not.

---

## Türkçe

Bir dil modeli zaten akıcı bir analoji üretecidir; ona "yaratıcı ol" demek bir
şey katmaz. Kıyas'ın kattığı tek şey **kısıttır** — çıkanın hayranlık değil
denetim görebilmesi için.

Üretilen her fikir aynı zarfla çıkar: **illeti** (analojiyi taşıyan yapısal
denklik, yüzey benzerliği değil), **kırılma noktası**, **en ucuz çürütmesi**,
**adlandırılmış prior art'ı** ve hükmü verecek **hakemi**. İlleti
isimlendirilemiyorsa fikir atılır — ve atıldığı kaydedilir, çünkü yalnızca
hayatta kalanları gösteren bir parti, hiçbir şeyin tartılmadığı bir partiden
ayırt edilemez.

- [Hızlı başlangıç](QUICKSTART.md)
- [Kullanım kılavuzu](tr/kullanim-kilavuzu.md)
- [Metodoloji](tr/metodoloji.md)
- [Operatörler](tr/operatorler.md)

---

## The family

**İskele kurar · Mizan tartar · Kıyas üretir.**
[İskele](https://github.com/XINMurat/Iskele) turns a vague project intent into
an executable delivery kit. [Mizan](https://github.com/XINMurat/Mizan) audits
claims and maintains preregistered hypothesis registries. Kıyas generates the
candidates Mizan weighs — already shaped for that audit, and carrying the
judge its registry will demand.
