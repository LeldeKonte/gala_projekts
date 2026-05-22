def generate_report(results):

    html = """
    <html>
    <body>

    <h1>TMDB AI Report</h1>
    """

    for r in results:

        html += f"""
        <h2>{r['title']}</h2>

        <img src="{r['image']}" width="500">

        <p><b>SQL:</b> {r['sql']}</p>

        <hr>
        """

    html += "</body></html>"

    with open("report.html", "w", encoding="utf-8") as f:

        f.write(html)