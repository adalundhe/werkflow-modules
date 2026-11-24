from __future__ import annotations
from pydantic import BaseModel
from .q_business_retriever_content_source import QBusinessRetrieverContentSource


class QBusinessContentSource(BaseModel):
    retriever: QBusinessRetrieverContentSource | None = None
