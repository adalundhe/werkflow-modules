from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .q_business_attribute_filter import QBusinessAttributeFilter
from .q_business_content_source import QBusinessContentSource


class QBusinessSearchRelevantContentRequest(BaseModel):
    applicationId: StrictStr
    queryText: StrictStr
    contentSource: QBusinessContentSource
    attributeFilter: QBusinessAttributeFilter | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
