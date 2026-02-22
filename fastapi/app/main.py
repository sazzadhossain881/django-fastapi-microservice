from fastapi import FastAPI

app = FastAPI()

BOOKS = [{
    "title":"new book"
}]

@app.get('/')
def read_books():
    return BOOKS
