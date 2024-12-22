import jaconv
from typing import Callable

def convert_fullsize_to_halfsize(input_text: str) -> str:
    return jaconv.z2h(input_text, kana=True, digit=True, ascii=True)

def convert_halfsize_to_fullsize(input_text: str) -> str:
    return jaconv.h2z(input_text, kana=True, digit=True, ascii=True)

def romanji_to_kana(input_text: str) -> str:
    return jaconv.alphabet2kana(input_text)

def romanji_to_kata(input_text: str) -> str:
    return jaconv.alphabet2kata(input_text)

def kana_to_romanji(input_text: str) -> str:
    return jaconv.kana2alphabet(input_text)

def kata_to_romanji(input_text: str) -> str:
    return jaconv.kata2alphabet(input_text)

def convert_text(input_text: str, converter: Callable[[str], str]) -> dict:
    converted = converter(input_text)
    return {
        "converted_text": converted,
        "original_text": input_text
    } 