from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comprehend_extracted_characters_list_item import ComprehendExtractedCharactersListItem


class ComprehendDocumentMetadata(BaseModel):
    Pages: StrictInt | None = None
    ExtractedCharacters: list[ComprehendExtractedCharactersListItem] | None = None
