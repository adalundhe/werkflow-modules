from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SearchResultFieldParameters(BaseModel):
    description: StrictStr | None = None
    isRequired: StrictBool | None = None
    rendererType: StrictStr | None = None
