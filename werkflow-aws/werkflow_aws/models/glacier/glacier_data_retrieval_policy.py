from __future__ import annotations
from pydantic import BaseModel
from .glacier_data_retrieval_rule import GlacierDataRetrievalRule


class GlacierDataRetrievalPolicy(BaseModel):
    Rules: list[GlacierDataRetrievalRule] | None = None
