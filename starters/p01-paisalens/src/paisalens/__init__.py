"""PaisaLens: see where your money went, from a UPI bank statement."""


def main() -> None:
    """Run PaisaLens. `uv run paisalens` calls this function until task 25.

    It prints the greeting that `uv init` writes, so the starter runs before
    you write any code. Replace the greeting with your own output in task 8.
    """
    # TODO(task 8): call read_statement("data/statement.csv") and print the rows
    #   kept, the first and last date, and the money out and the money in.
    # TODO(task 9): print each month's total in month order, then the top 10
    #   merchants, biggest first, every amount shown with rupees().
    # TODO(task 10): load rules.json once, set each row's category, print the
    #   spending by category, biggest first, with the share that is "Other", and
    #   save the category totals to data/category_totals.json.
    # TODO(task 21): set tx.category on each Transaction.
    # TODO(task 23): print each subscription and what they all cost in one month.
    # TODO(task 24): make an ErrorReport, pass it to read_statement, print the
    #   number of bad rows and write them to data/errors.csv.
    # TODO(task 25): move the month, category and top-merchant prints into
    #   render_report() in report.py, then delete main(): the commands in cli.py
    #   do its work.
    print("Hello from paisalens!")
