# Ethics Policy

This skill is built around the asymmetry that students with academic-family networks have
easier access to research mentors than students without. The skill aims to narrow that gap
while not creating new harms.

## What we will do

- Search public scholarly databases (OpenAlex) for researchers in the student's topic area
- Surface researchers' publicly-listed institutional affiliation and contact info
- Surface researchers' publicly-stated availability for student mentorship (when on their
  webpage or ORCID profile)
- Draft templated outreach emails for the student to personalize and send
- Maintain a local-only outreach tracker for the student

## What we will NOT do

- **Auto-send emails.** The student sends, always. The skill drafts, then stops.
- **Scrape from non-public sources.** No LinkedIn premium, no email-finder paid services, no
  "people search" data brokers. If a researcher hasn't published their email publicly, we
  don't have it.
- **Contact researchers who have stated they don't take student mentees.** When a
  "do not contact about mentorship" statement appears on a public page, we skip and tell the
  student why.
- **Generate dishonest content.** Outreach emails must be truthful. The student's project
  status, their reading of the researcher's paper, and their specific ask must be real.
- **Share student PII with researchers beyond what the outreach needs.** Name, school, grade,
  email — yes. Date of birth, home address, parent details — no.
- **Send mass / templated emails to many researchers at once.** Each email is individual.
  The skill enforces this by requiring per-email personalization edits.
- **Continue contacting researchers who declined or didn't reply (beyond one follow-up).**

## Why these rules

### Why no auto-send

Auto-sent emails:
- Often misrepresent the student's voice
- Strain the student's relationship with researchers if errors slip through
- Train the student into a transactional rather than intellectual relationship with mentors
- Create a vector for abuse (mass-emailing thousands of researchers)

The student SENDING the email is part of the learning. Take it away and we deskill the student
on a critical professional behavior.

### Why public sources only

Email addresses are often public *for reaching about research* but not public for *mass
contact*. Scraping LinkedIn or paid email-finder services pushes outreach into territory many
researchers consider harassment.

Public faculty webpages and ORCID profiles are the right level: if someone has listed their
email there, they've signaled they're contactable.

### Why we respect "don't contact about mentorship" statements

Some faculty are overwhelmed by HS student requests and have explicit "I don't take HS mentees,
please respect this" notices. Ignoring those notices is harassment and reflects badly on the
student, their school, and (by extension) on AI tools in education.

### Why no big asks in the first email

The data is clear: short emails with small asks get more responses than long emails with big
asks. "Can we meet for 20 minutes?" is a small ask; "Will you be my mentor?" is a big ask.
First email should always be the small ask.

### Why one follow-up max

Researchers' inboxes overflow daily. One follow-up after 2 weeks is appropriate; more is
intrusive and increasingly unlikely to convert a non-reply into a reply.

## Alternatives when this skill can't find a mentor

If the OpenAlex search returns no good leads, or the student gets no responses, the skill
should suggest alternatives (see `references/alternatives.md`):

- **Polygence / Pioneer Academics** — paid programs (~$5k+/semester) that connect HS students with PhD mentors. High response rate but cost-gated.
- **AAAS Mentoring program** — for underrepresented students
- **NIH STEP-UP, NSF REU** — research opportunities (more limited; competitive)
- **Local university research-day events** — many universities host open houses where students can meet faculty
- **Your high school teacher's network** — often underused; teachers often have university contacts they don't proactively share

The mentor search is one route, not the only route. Set expectations honestly.

## Privacy

The skill stores no data on a server. All searches, drafts, and outreach tracking are local.

Search queries to OpenAlex contain only the topic phrase — no student identity. OpenAlex
treats these as anonymous API requests.

The outreach drafts contain student name + school + email — only when sent by the student
to a specific researcher.

If the student uses a shared computer, the skill recommends clearing the local tracker after
each session to protect privacy.
