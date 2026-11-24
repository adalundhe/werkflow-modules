from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glacier_data_retrieval_policy import GlacierDataRetrievalPolicy


class GlacierGetDataRetrievalPolicyResponse(BaseModel):
    Policy: GlacierDataRetrievalPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
