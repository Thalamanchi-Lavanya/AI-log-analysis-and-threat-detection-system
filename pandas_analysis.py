import pandas as pd
import sqlite3


def generate_analysis():

    connection = sqlite3.connect(
        "database/threats.db"
    )

    query = "SELECT * FROM threats"

    df = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return df


def get_total_threats():

    df = generate_analysis()

    return len(df)


def get_risk_analysis():

    df = generate_analysis()

    return df["risk_level"].value_counts()


def get_top_users():

    df = generate_analysis()

    return df["username"].value_counts()


def export_csv():

    df = generate_analysis()

    df.to_csv(
        "threat_report.csv",
        index=False
    )

    print(
        "CSV Report Generated Successfully!"
    )


def export_excel():

    df = generate_analysis()

    df.to_excel(
        "threat_report.xlsx",
        index=False
    )

    print(
        "Excel Report Generated Successfully!"
    )


if __name__ == "__main__":

    print("\nThreat Data\n")

    print(generate_analysis())

    print(
        "\nTotal Threats:",
        get_total_threats()
    )

    print("\nRisk Analysis\n")

    print(get_risk_analysis())

    print("\nTop Attacked Users\n")

    print(get_top_users())

    export_csv()

    export_excel()