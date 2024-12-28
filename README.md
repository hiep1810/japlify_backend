# Japanese Text Converter API

A high-performance FastAPI application for converting Japanese text between different formats (Romaji, Hiragana, Katakana, Half-width, Full-width) with focus on speed, reliability and ease of use.

## Features

- Convert full-width to half-width characters
- Convert half-width to full-width characters
- Convert Romaji to Hiragana
- Convert Romaji to Katakana
- Convert Hiragana to Romaji
- Convert Katakana to Romaji
- Asynchronous processing for better performance
- Input validation using Pydantic v2 models
- Comprehensive error handling with detailed messages
- Request rate limiting
- Response caching
- OpenAPI documentation

## System Requirements

- Python 3.8+
- FastAPI 0.100+
- Pydantic v2
- jaconv
- uvicorn
- Redis (optional, for caching)

## Installation

1. Clone repository:
```bash
git clone https://github.com/your-username/japanese-text-converter-api.git
cd japanese-text-converter-api
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running the Application

Development mode:
```bash
uvicorn app.main:app --reload --port 8000
```

Production mode:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4 --proxy-headers
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Text Conversion

#### GET /convert/fullsize-to-halfsize?text={text}
Convert full-width characters to half-width

Example:
```
GET /convert/fullsize-to-halfsize?text=Ｈｅｌｌｏ　Ｗｏｒｌｄ
```

#### GET /convert/halfsize-to-fullsize?text={text}
Convert half-width characters to full-width

Example:
```
GET /convert/halfsize-to-fullsize?text=Hello World
```

#### GET /convert/romanji-to-kana?text={text}
Convert Romaji to Hiragana

Example:
```
GET /convert/romanji-to-kana?text=konnichiwa
```

#### GET /convert/romanji-to-kata?text={text}
Convert Romaji to Katakana

Example:
```
GET /convert/romanji-to-kata?text=konnichiwa
```

#### GET /convert/kana-to-romanji?text={text}
Convert Hiragana to Romaji

Example:
```
GET /convert/kana-to-romanji?text=こんにちは
```

#### GET /convert/kata-to-romanji?text={text}
Convert Katakana to Romaji

Example:
```
GET /convert/kata-to-romanji?text=コンニチハ
```

### Response Format

```json
{
    "converted_text": "Converted text result",
    "original_text": "Original input text",
    "conversion_type": "conversion-type",
    "metadata": {
        "processing_time": "0.001s",
        "char_count": 10
    }
}
```

## API Documentation

- Interactive Swagger UI: `/docs`
- ReDoc documentation: `/redoc`
- OpenAPI specification: `/openapi.json`

## Error Handling

The API uses standard HTTP status codes with detailed error messages:
- 200: Success
- 400: Bad Request (Invalid input)
- 422: Validation Error (Invalid data format)
- 429: Too Many Requests
- 500: Server Error

Error Response Format:
```json
{
    "error": {
        "code": "ERROR_CODE",
        "message": "Detailed error message",
        "details": {}
    }
}
```

## Dependencies

- FastAPI: Modern, fast web framework
- Pydantic v2: Data validation using Python type annotations
- jaconv: Japanese text conversion library
- uvicorn: Lightning-fast ASGI server
- Redis (optional): For response caching
- prometheus-client (optional): For metrics

## Performance Optimizations

- Asynchronous request handling
- Input validation using Pydantic v2 models
- Response caching with Redis
- Connection pooling
- Request rate limiting
- Efficient text conversion algorithms

## Development

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=app

# Code formatting
black .
isort .

# Linting
flake8
mypy .

# Security checks
bandit -r app/
```

## Monitoring

The API provides Prometheus metrics at `/metrics` endpoint:
- Request counts and latencies
- Error rates
- Cache hit/miss ratios
- System metrics

## License

MIT

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

Please ensure your code:
- Passes all tests
- Includes appropriate documentation
- Follows the project's coding standards
- Includes relevant test cases