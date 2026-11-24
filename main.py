#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Pass 1 — the committee/screenshot line.

Weighing against the judge's ordered criteria:
1. On-subject: lawmakers regulating the internet + the file they cannot
   convert (the final draft, emailed as a screenshot of a Word document).
2. Real turn: three hours debating a bill about algorithms (authority) ->
   the final draft sent as a screenshot (undercut by the file itself).
3. Aim stays on lawmakers and the rules they write: the bill, the debate,
   the committee — power and competence, not random abuse.
4. Reads clean in one pass; the punch ("screenshot of a Word document")
   lands on the last few words and is quotable.
5. Specific, unexpected detail: emailing a draft as a screenshot is a
   fresh incompetence image, not the worn "can't use a computer" cliche.

Pass 2 — tested the 400-page-law challenger (147 chars, run and verified)
and rejected it, reverting to pass 1: the challenger NARRATES the failure
("the file wouldn't open on their computer") and leans on a familiar
image (intern prints the PDF); the screenshot line SHOWS it — the
committee itself produced the unconvertible file and mailed it as a
screenshot, so the incompetence IS the punch, and the detail is fresher
and more quotable. The challenger also shifts the aim onto a staffer;
the winner keeps the aim on the lawmakers and their bill.

Beaten candidates:
- 400-page explainability law / intern prints the PDF: see pass 2 above.
- Prints emails / signs by hand / faxes them back: worn tech-illiteracy
  cliche, and it drops the PDF-conversion premise entirely.
- "Asking IT why their PDF opens in the wrong app": on-subject but a
  generic detail; weaker punch than the screenshot.
- password123 / chain emails: the most worn cliche of all, and no file
  conversion in it — fails criterion 1.
"""
import os

ENTRY = (
    "The committee that regulates the internet spent three hours debating "
    "a bill about algorithms, then emailed the final draft as a screenshot "
    "of a Word document."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
