from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_document_suggester_options import CloudSearchDocumentSuggesterOptions


class CloudSearchSuggester(BaseModel):
    SuggesterName: StrictStr | None = None
    DocumentSuggesterOptions: CloudSearchDocumentSuggesterOptions | None = None
