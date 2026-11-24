from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .q_business_snippet_excerpt import QBusinessSnippetExcerpt
from .q_business_source_details import QBusinessSourceDetails


class QBusinessTextSegment(BaseModel):
    beginOffset: StrictInt | None = None
    endOffset: StrictInt | None = None
    snippetExcerpt: QBusinessSnippetExcerpt | None = None
    mediaId: StrictStr | None = None
    mediaMimeType: StrictStr | None = None
    sourceDetails: QBusinessSourceDetails | None = None
