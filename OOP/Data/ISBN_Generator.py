import polars as pl
import requests


def search_books_by_title(title):
    base_url = "https://openlibrary.org/search.json"
    params = {"title": title}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        search_results = response.json()
        try:
            book_results = search_results.get("docs")
            return int(book_results[0].get("isbn")[0])
        except:
            return(None)
            
    else:
        return(None)

title = "Fundamentals of Wavelets"

df = pl.read_csv(r"C:\Users\enriq\OneDrive\Desktop\Capacitacion\Python\OOP\Data\raw_books.csv")

df = df.with_columns(df['Title'].apply(search_books_by_title).alias('ISBN'))

csv_path = r"C:\Users\enriq\OneDrive\Desktop\Capacitacion\Python\OOP\Data\books.csv"

df.write_csv(csv_path)
