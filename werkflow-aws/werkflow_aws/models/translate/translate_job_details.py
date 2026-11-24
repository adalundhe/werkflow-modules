from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TranslateJobDetails(BaseModel):
    TranslatedDocumentsCount: StrictInt | None = None
    DocumentsWithErrorsCount: StrictInt | None = None
    InputDocumentsCount: StrictInt | None = None
