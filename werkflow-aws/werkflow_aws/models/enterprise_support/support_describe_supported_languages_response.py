from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .supported_language import SupportedLanguage


class SupportDescribeSupportedLanguagesResponse(BaseModel):
    supportedLanguages: list[SupportedLanguage] | None = None
    ResponseMetadata: dict[str, Any] | None = None
