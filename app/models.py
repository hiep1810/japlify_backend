from pydantic import BaseModel, Field

class TextRequest(BaseModel):
    text: str = Field(..., description="Input text to convert")
    
class TextResponse(BaseModel):
    converted_text: str = Field(..., description="Converted text result")
    original_text: str = Field(..., description="Original input text") 