from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .translate_text_translation_job_filter import TranslateTextTranslationJobFilter


class TranslateListTextTranslationJobsRequest(BaseModel):
    Filter: TranslateTextTranslationJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
