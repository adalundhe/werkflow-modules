from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_document_details import QBusinessDocumentDetails


class QBusinessListDocumentsResponse(BaseModel):
    documentDetailList: list[QBusinessDocumentDetails] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
