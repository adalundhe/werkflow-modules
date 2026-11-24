from __future__ import annotations
from pydantic import BaseModel
from .textract_output_additional_file_format import TextractOutputAdditionalFileFormat
from .textract_output_text_format import TextractOutputTextFormat


class TextractOutputFormat(BaseModel):
    AdditionalFileFormat: TextractOutputAdditionalFileFormat | None = None
    TextFormat: TextractOutputTextFormat | None = None
