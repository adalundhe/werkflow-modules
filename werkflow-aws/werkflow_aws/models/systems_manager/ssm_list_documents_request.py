from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_document_filter import SSMDocumentFilter
from .ssm_document_key_values_filter import SSMDocumentKeyValuesFilter


class SSMListDocumentsRequest(BaseModel):
    DocumentFilterList: list[SSMDocumentFilter] | None = None
    Filters: list[SSMDocumentKeyValuesFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
