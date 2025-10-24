def monthly_top_25_books(year=None, month=None):
    """
    Генерирует рейтинг топ-25 книг для заданного месяца.
    :param year: Год (текущий по умолчанию)
    :param month: Номер месяца (текущий по умолчанию)
    """
    today = date.today()
    if not year:
        year = today.year
    if not month:
        month = today.month
    books = [f"Книга #{i+1}" for i in range(25)]
    _, last_day = calendar.monthrange(year, month)
    start_date = date(year, month, 1)
    end_date = date(year, month, last_day)
    header = f"Топ-25 книг за период {start_date.strftime('%B %Y')} ({last_day} дней)"
    content = ""
    for idx, book in enumerate(books):
        content += f"{idx+1}. {book}\n"
    return header + "\n" + content
print(monthly_top_25_books())
