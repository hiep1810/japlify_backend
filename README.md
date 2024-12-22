# Japanese Text Converter API

API chuyển đổi văn bản tiếng Nhật giữa các định dạng khác nhau (Romaji, Hiragana, Katakana, Half-width, Full-width).

## Tính năng

- Chuyển đổi ký tự full-width sang half-width
- Chuyển đổi ký tự half-width sang full-width  
- Chuyển đổi Romaji sang Hiragana
- Chuyển đổi Romaji sang Katakana
- Chuyển đổi Hiragana sang Romaji
- Chuyển đổi Katakana sang Romaji

## Yêu cầu hệ thống

- Python 3.8+
- FastAPI
- Pydantic
- jaconv

## Cài đặt

1. Clone repository:
```bash
git clone https://github.com/your-username/japanese-text-converter-api.git
cd japanese-text-converter-api
```

2. Tạo môi trường ảo và kích hoạt:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
.\venv\Scripts\activate  # Windows
```

3. Cài đặt các dependencies:
```bash
pip install -r requirements.txt
```

## Chạy ứng dụng

```bash
uvicorn app.main:app --reload
```

API sẽ chạy tại `http://localhost:8000`

## API Endpoints

### POST /convert/fullsize-to-halfsize
Chuyển đổi ký tự full-width sang half-width

### POST /convert/halfsize-to-fullsize
Chuyển đổi ký tự half-width sang full-width

### POST /convert/romanji-to-kana
Chuyển đổi Romaji sang Hiragana

### POST /convert/romanji-to-kata
Chuyển đổi Romaji sang Katakana

### POST /convert/kana-to-romanji
Chuyển đổi Hiragana sang Romaji

### POST /convert/kata-to-romanji
Chuyển đổi Katakana sang Romaji

## Request/Response Format

### Request

```json
{
    "text": "Văn bản cần chuyển đổi"
}
```

### Response

```json
{
    "converted_text": "Văn bản đã chuyển đổi",
    "original_text": "Văn bản gốc"
}
```

## Tài liệu API

Truy cập `/docs` hoặc `/redoc` để xem tài liệu API tương tác được tạo tự động bởi FastAPI.

## Xử lý lỗi

API sử dụng mã HTTP tiêu chuẩn cho các phản hồi:
- 200: Thành công
- 400: Lỗi đầu vào
- 500: Lỗi server

## Dependencies

- FastAPI: Web framework
- Pydantic: Validation dữ liệu
- jaconv: Thư viện chuyển đổi văn bản tiếng Nhật

## License

MIT

## Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng tạo issue hoặc pull request.