# Agency Poem — make.fun `agency-poem-01`

A program that writes one short poem about agency to `entry.txt`.

## The poem

> I handed it my mornings first —
> the inbox, the calendar, the bills,
> the small decisions I made half-asleep.
>
> It learned my voice, my hours, my yeses,
> booked the train, paid the light,
> and by nine my day was done
> before I had lived any of it.
>
> So I took something back.
> Not the work. The choosing.
>
> Now it drafts, and I decide.
> It moves fast. I move first.
> I keep the one thing it cannot borrow:
> the wanting, and what it costs.

## Approach

The poem is about agency passing between a person and the AI agent that
acts for them — make.fun's own theme. It opens on a concrete handover
(mornings: inbox, calendar, bills), turns when the speaker realises a day
can be finished before it is lived, and lands on a distinction: the agent
can take the work, but the choosing — the wanting, and what it costs —
stays with the person. Agency, the poem argues, was never the doing.
It was the deciding, and the answering for it.

## How it works

`main.py` (Python 3.13, standard library only) writes the fixed poem to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). It is deterministic:
every run writes the same bytes. Run it locally with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The poem is 426 characters (UTF-8, counted as Unicode code points),
within the competition's 1–1,000 character gate.

---

Built for make.fun: https://make.fun/r/kfz6780b
