import pandas as pd
import matplotlib.pyplot as plt
import os

from db import run_query


def generate_sql(goal):

    if "rating" in goal.lower():

        return """
        SELECT title, vote_average
        FROM movies
        ORDER BY vote_average asc
        LIMIT 15
        """

    return """
    SELECT title, popularity
    FROM movies
    ORDER BY popularity asc
    LIMIT 15
    """


def process_plan_item(item, index):

    sql = generate_sql(item["sql_goal"])

    data = run_query(sql)

    df = pd.DataFrame(data)
    if "vote_average" in df.columns:
        df.columns = ["Filma", "Vērtējums"]

    if "popularity" in df.columns:
        df.columns = ["Filma", "Popularitāte"]

    plt.figure(figsize=(12, 6))

    x = df.columns[0]
    y = df.columns[1]

    if item["chart_type"] == "bar":

        df.plot(
            x=x,
            y=y,
            kind="bar",
            color="green",
            legend=False
        )

    else:

        df.plot(
            x=x,
            y=y,
            kind="line",
            color="red",
            legend=False
        )

    plt.xticks(rotation=45, ha="right")

    plt.xlabel("Filmas")
    plt.ylabel("Vērtība")

    plt.title(item["title"])

    plt.tight_layout()

    os.makedirs("output", exist_ok=True)

    path = f"output/chart_{index}.png"

    plt.savefig(path)

    plt.close()

    return {
        "title": item["title"],
        "sql": sql,
        "image": path,
        "data": df
    }