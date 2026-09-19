# PROPOSAL, not applied: promote the `lengthened` pattern into OUTREACH_CRAFT.md

**Status: DRAFTED FOR TALON. This run did not apply it and no run ever may.**
OUTREACH_CRAFT.md is a bar this routine is judged against, so a run that edited
it would be grading its own homework. The diff below is ready to apply by hand
and nothing else.

`scripts/voice_diff.py --summary` on 2026-09-19:

```
  lengthened                   in 10 send(s), 14x total  READY TO PROMOTE
```

Ten separate sends is the highest count any pattern has reached, and the bar
written in VOICE_DELTAS.md is three. It has been sitting at READY TO PROMOTE
for a while because `lengthened` is a shape, not an instruction, and a shape
can't be promoted until someone reads the fourteen edits and says what the
shape actually is.

## Reading all fourteen, there are two patterns inside the one label

They do not overlap. Every one of the fourteen is one or the other.

### Pattern A, the study line. Six sends.

The law's skeleton step 3 is "point at the study as work already done for
them", and the worked example spells it "We already did the study on fixing
that." Talon rewrites that clause on six of eleven sends and he makes the same
two changes every time.

| Sent | Drafted | Sent |
|---|---|---|
| 07-30 ABR | The study below has a replacement paragraph already drafted for you. | ...for you **along with our field study into your company**. |
| 07-31 Calista | We **already did** the study on closing that list | We already did the **week long** study on closing that list |
| 08-04 Tyonek | We've **already done** the study on how to measure that exposure. | We **just wrapped up** our study on how to measure that exposure **and did a deep dive on Tyonek**. |
| 08-07 R&M | We **already did** the study on flagging what's missing | We **just wrapped up** the study **on RM** and flagging what's missing |
| 08-09 White Pass | We just wrapped up our study on those unstaffed hours **at White Pass**. | We just wrapped up our study on a solution for those unstaffed hours **and did a deep dive on White Pass**. |
| 08-10 Major Marine | We **already did** the study on that. | We **just wrapped up** our study **on you**, and a fix for that. |

Two changes, both consistent.

1. **"already did" becomes "just wrapped up".** Four of the six. "Already did"
   is past perfect and it reads as a thing finished some time ago, possibly
   before they were thought of. "Just wrapped up" puts it in the last week and
   makes it theirs. It is also a contraction of effort into recency, which is
   the only claim in the sentence a stranger can weigh.
2. **The company gets named inside the clause.** Five of the six, including the
   one where the writer had already named the company and Talon moved the name
   to the end where it lands harder. The law bans naming who or what produced
   the study, and it says nothing about naming who it was FOR. Talon adds that
   every time.

### Pattern B, the closing ask. Six sends.

The law's CTA list offers three lines. Talon rewrote the closing on six of
eleven sends, and five of those six open with the same two words.

| Sent | Drafted | Sent |
|---|---|---|
| 07-31 Calista | Worth a reply either way. | **No strings**, if you want to go for it we're here. |
| 08-01 Medical Park | Tell us if it's useful. | **No strings**, we only ask that you let us know what you think. |
| 08-03 Ryan Air | Worth a reply or a forward either way. | Worth a reply or a forward either way, **no strings**. |
| 08-06 ANHC | Tell us if it's useful. | **No strings**, here if you want support with this. |
| 08-09 White Pass | Worth a reply either way. | Just something we'd be excited to build for you. |
| 08-10 Major Marine | Worth a reply either way. | **No strings**, we just like seeking out projects we'd enjoy building and this is one. |

"No strings" is doing a job none of the three approved lines does. The approved
lines ask for a reply. "No strings" answers the question a cold reader is
actually holding, which is what this is going to cost them for having opened
it. The ask survives, it just stops being the first thing in the line.

The two remaining edits of the fourteen are neither pattern and neither is
worth a rule. 07-29 Allen Marine turned "Talon" into "- Talon", which is a
signature, and the same send's CTA rewrite is already counted under `cta
softened` and drove the "reply yes" retirement that is written up in the file.

## What this run did with it

This run's email pre-applied both patterns before the critic ever saw it.

> We **just wrapped up our study on Tatitlek** and the gap we'd work on is data
> calls.
>
> **No strings**, worth a reply either way.

The lead-critic read that as the pattern being MET rather than fed, and shipped
at round one. That is a single data point and it is the writer obeying evidence
the law has not absorbed yet, which is exactly the state that should end.

## The drafted diff

```diff
--- a/knowledge/OUTREACH_CRAFT.md
+++ b/knowledge/OUTREACH_CRAFT.md
@@ -29,7 +29,7 @@
 The skeleton, stripped to the bone.
 1. The one specific true thing we found, stated flat, as the first sentence.
 2. What it costs them, one line.
-3. Point at the study as work already done for them.
+3. Point at the study as work JUST FINISHED for them, and name them in it.
 4. One small reply-first ask.
+
+Step 3 got sharper on 2026-09-19, off ten separate sends. "We already did the
+study" is past perfect and reads as a thing finished some time ago, possibly
+before they were thought of. Talon rewrote it to "we just wrapped up our study"
+on four sends and added the company's name inside the clause on five, and the
+two edits travel together. Write "We just wrapped up our study on <Company>"
+and not "We already did the study on that." The ban on self-reference is
+untouched, it covers naming WHO OR WHAT produced the study, an agent team, AI,
+our process, a human reviewer. Naming who it was FOR is the opposite move and
+it is the one Talon makes by hand every time.
@@ -181,9 +181,17 @@
 A first touch does NOT ask for a call. Too much for a cold open. The study is
 already in their hands, so the ask is just a signal that it landed. One line.
-- "No call and no pitch. If it is useful we talk."
-- "Worth a reply either way."
-- "Tell us if it is useful."
+- "No strings, worth a reply either way."
+- "No strings, here if you want support with this."
+- "No call and no pitch. If it is useful we talk."
+
+LEAD WITH "NO STRINGS" (2026-09-19, off ten separate sends). Talon rewrote the
+closing line on six of eleven sends and five of the six open on those two
+words. They do a job none of the older lines did. The older lines ask for a
+reply. "No strings" answers the question a cold reader is actually holding,
+which is what this is going to cost them for having opened it. The ask still
+goes in, it just stops being the first thing in the line. "Worth a reply either
+way" on its own is now the weaker version of a line we know the better form of.
```

## The one reason to say no

Pattern B is the one to think twice about. "No strings" lengthens the email,
and forty to sixty words is a hard budget. On this run it cost two words and
fit. On a send where the opening fact needs a long sentence it will not, and
the right call there is to keep the bare ask rather than cut the fact. If the
rule goes in, it goes in as a preference and never as a hard gate, which is how
the diff above is written.
