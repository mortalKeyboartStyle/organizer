"""
image_ai_handler.py
Keyword: ai_analysis_image

Rozpoznawanie treści obrazków (OCR, object detection).
Tu - tylko atrapowa funkcja 'fake_ocr'.
"""

def fake_ocr(image_path):
    """
    Uproszczona atrapa OCR, zwraca stały tekst.
    W realnym projekcie: import pytesseract / easyocr, itp.
    """
    return f"[OCR] Tekst z pliku: {image_path}"
