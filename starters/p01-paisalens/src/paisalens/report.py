"""Totals and reports: the answers to "where did my money go?".

All money is whole paise (int). Only debits count as spending.
`rows` is a list of row dicts until task 21, then a list of Transactions.
"""

# TODO(task 21): every function here reads attributes such as tx.debit_paise
#   in place of dict keys such as row["debit_paise"].


def month_of(date) -> str:
    """Return the month of a date as "YYYY-MM", so that months sort in time order.

    In task 9, date is the text from the statement: "05/01/2026" gives "2026-01".
    """
    # TODO(task 21): date is now a datetime.date; return the same "YYYY-MM" text.
    raise NotImplementedError("TODO(task 9): write month_of")


def monthly_totals(rows) -> dict[str, int]:
    """Return a dict from month ("2026-01") to the total debit_paise of that month.

    Build it in one loop over the rows.
    """
    raise NotImplementedError("TODO(task 9): write monthly_totals")


def by_merchant(rows) -> dict[str, int]:
    """Return a dict from merchant name to that merchant's total debit_paise.

    Skip rows whose debit_paise is 0 (money coming in), so only spending counts.
    """
    raise NotImplementedError("TODO(task 9): write by_merchant")


def by_category(rows) -> dict[str, int]:
    """Return a dict from category to that category's total debit_paise."""
    raise NotImplementedError("TODO(task 10): write by_category")


def rupees(paise: int) -> str:
    """Show whole paise as rupees: 125050 gives "₹1,250.50" and 5 gives "₹0.05".

    Whole-number maths only. Never use float.
    """
    raise NotImplementedError("TODO(task 9): write rupees")


def render_report(rows) -> str:
    """Return the whole text report as one string, with its columns lined up.

    Three sections, each with a heading and a line of dashes under it:
    "Spending by month" (month and amount), "Spending by category" (category,
    amount and its share of all spending in %) and "Top 10 merchants" (merchant
    and amount, with long names cut short). Amounts are shown with rupees().
    """
    raise NotImplementedError("TODO(task 25): write render_report")

