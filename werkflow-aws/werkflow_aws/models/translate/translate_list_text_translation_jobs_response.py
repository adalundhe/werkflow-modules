from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .translate_text_translation_job_properties import TranslateTextTranslationJobProperties


class TranslateListTextTranslationJobsResponse(BaseModel):
    TextTranslationJobPropertiesList: list[TranslateTextTranslationJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
