from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import TextResponse
from .utils import (
    convert_fullsize_to_halfsize,
    convert_halfsize_to_fullsize,
    romanji_to_kana,
    romanji_to_kata,
    kana_to_romanji,
    kata_to_romanji,
    convert_text
)

app = FastAPI(
    title="Japanese Text Converter API",
    description="API for converting between different Japanese text formats",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/convert/fullsize-to-halfsize/", response_model=TextResponse)
async def convert_to_halfsize(text: str) -> TextResponse:
    """Convert full-width characters to half-width"""
    try:
        return TextResponse(**convert_text(text, convert_fullsize_to_halfsize))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/convert/halfsize-to-fullsize", response_model=TextResponse)
async def convert_to_fullsize(text: str) -> TextResponse:
    """Convert half-width characters to full-width"""
    try:
        return TextResponse(**convert_text(text, convert_halfsize_to_fullsize))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/convert/romanji-to-kana", response_model=TextResponse)
async def convert_to_kana(text: str) -> TextResponse:
    """Convert romanji to hiragana"""
    try:
        return TextResponse(**convert_text(text, romanji_to_kana))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/convert/romanji-to-kata", response_model=TextResponse)
async def convert_to_kata(text: str) -> TextResponse:
    """Convert romanji to katakana"""
    try:
        return TextResponse(**convert_text(text, romanji_to_kata))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/convert/kana-to-romanji", response_model=TextResponse)
async def convert_kana_to_romanji(text: str) -> TextResponse:
    """Convert hiragana to romanji"""
    try:
        return TextResponse(**convert_text(text, kana_to_romanji))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/convert/kata-to-romanji", response_model=TextResponse)
async def convert_kata_to_romanji(text: str) -> TextResponse:
    """Convert katakana to romanji"""
    try:
        return TextResponse(**convert_text(text, kata_to_romanji))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 