"""Rebuild downloads/Supply_Bridge_Asia_Company_Profile_2026.pdf from tools/company_profile.html.
Needs Python Playwright with Chromium, and the Inter and Noto Sans CJK SC fonts installed.
Run from anywhere: python3 tools/build_profile_pdf.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
src = root / "tools" / "company_profile.html"
out = root / "downloads" / "Supply_Bridge_Asia_Company_Profile_2026.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(src.as_uri(), wait_until="networkidle")
    page.pdf(path=str(out), format="A4", print_background=True, prefer_css_page_size=True,
             margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    browser.close()
print("wrote", out)
