from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kendra_attribute_filter import KendraAttributeFilter
from .kendra_document_relevance_configuration import KendraDocumentRelevanceConfiguration
from .kendra_user_context import KendraUserContext


class KendraRetrieveRequest(BaseModel):
    IndexId: StrictStr
    QueryText: StrictStr
    AttributeFilter: KendraAttributeFilter | None = None
    RequestedDocumentAttributes: list[StrictStr] | None = None
    DocumentRelevanceOverrideConfigurations: list[KendraDocumentRelevanceConfiguration] | None = None
    PageNumber: StrictInt | None = None
    PageSize: StrictInt | None = None
    UserContext: KendraUserContext | None = None
