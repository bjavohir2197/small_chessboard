# Shaxmat Taxtasi Patteni

Ushbu Python skripti 8x8 o'lchamdagi shaxmat taxtasining naqshini yaratadi. Taxtaning qora va oq kataklari `##` va bo'sh joy bilan tasvirlangan.

## Xususiyatlar
- 8x8 o'lchamdagi shaxmat taxtasi.
- Qora kataklar `##`, oq kataklar bo'sh joy bilan ifodalanadi.
- Oddiy va samarali kod.

## Foydalanish

1. Python 3.x o'rnatilgan bo'lishi kerak.
2. Skriptni ishga tushiring:

    ```bash
    python main.py
    ```

3. Natija terminalda shaxmat taxtasi sifatida ko'rsatiladi.

- `print_board()` funksiyasi shaxmat taxtasini yaratadi va chop etadi.
- Har bir katakning rangi `(r + c) % 2` sharti bo'yicha aniqlanadi:
  - Juft sonlar: qora katak (`##`).
  - Toq sonlar: oq katak (bo'sh joy).
