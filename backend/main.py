from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional
import os
import shutil

from models import Base, Book

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:////data/tasks.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ElectoLibrary API")

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/books")
def get_books(
    available: Optional[bool] = None,
    sort: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Book)

    if available is not None:
        query = query.filter(Book.is_available == available)

    if sort == "title":
        query = query.order_by(Book.title)
    else:
        query = query.order_by(Book.created_at.desc())

    return query.all()


@app.get("/api/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return book


@app.post("/api/books")
def create_book(
    title: str = Form(...),
    author: str = Form(...),
    description: Optional[str] = Form(None),
    publisher: str = Form(...),
    category: str = Form(...),
    year: Optional[int] = Form(None),
    collection: Optional[str] = Form(None),
    cover: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    cover_path = None

    if cover:
        cover_path = f"{UPLOAD_DIR}/{cover.filename}"
        with open(cover_path, "wb") as buffer:
            shutil.copyfileobj(cover.file, buffer)

    book = Book(
        title=title,
        author=author,
        description=description,
        publisher=publisher,
        category=category,
        year=year,
        collection=collection,
        cover=cover_path
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


@app.put("/api/books/{book_id}")
def update_book(
    book_id: int,
    title: str = Form(...),
    author: str = Form(...),
    description: Optional[str] = Form(None),
    publisher: str = Form(...),
    category: str = Form(...),
    year: Optional[int] = Form(None),
    collection: Optional[str] = Form(None),
    is_available: bool = Form(True),
    is_favorite: bool = Form(False),
    is_reserved: bool = Form(False),
    cover: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    book.title = title
    book.author = author
    book.description = description
    book.publisher = publisher
    book.category = category
    book.year = year
    book.collection = collection
    book.is_available = is_available
    book.is_favorite = is_favorite
    book.is_reserved = is_reserved

    if cover:
        cover_path = f"{UPLOAD_DIR}/{cover.filename}"
        with open(cover_path, "wb") as buffer:
            shutil.copyfileobj(cover.file, buffer)
        book.cover = cover_path

    db.commit()
    db.refresh(book)

    return book


@app.delete("/api/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    db.delete(book)
    db.commit()

    return {"message": "Книга удалена"}


@app.patch("/api/books/{book_id}/status")
def toggle_status(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    book.is_available = not book.is_available

    db.commit()
    db.refresh(book)

    return book


@app.patch("/api/books/{book_id}/favorite")
def toggle_favorite(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    book.is_favorite = not book.is_favorite

    db.commit()
    db.refresh(book)

    return book


@app.patch("/api/books/{book_id}/reserve")
def toggle_reserve(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    book.is_reserved = not book.is_reserved

    db.commit()
    db.refresh(book)

    return book