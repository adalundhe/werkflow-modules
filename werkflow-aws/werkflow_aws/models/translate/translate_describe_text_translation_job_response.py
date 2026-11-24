from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .translate_text_translation_job_properties import TranslateTextTranslationJobProperties


class TranslateDescribeTextTranslationJobResponse(BaseModel):
    TextTranslationJobProperties: TranslateTextTranslationJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
