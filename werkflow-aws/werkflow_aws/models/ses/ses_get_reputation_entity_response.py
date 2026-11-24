from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_reputation_entity import SESReputationEntity


class SESGetReputationEntityResponse(BaseModel):
    ReputationEntity: SESReputationEntity | None = None
    ResponseMetadata: dict[str, Any] | None = None
