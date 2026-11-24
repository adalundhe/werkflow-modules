from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_retriever import QBusinessRetriever


class QBusinessListRetrieversResponse(BaseModel):
    retrievers: list[QBusinessRetriever] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
