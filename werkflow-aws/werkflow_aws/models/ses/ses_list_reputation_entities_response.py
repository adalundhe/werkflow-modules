from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_reputation_entity import SESReputationEntity


class SESListReputationEntitiesResponse(BaseModel):
    ReputationEntities: list[SESReputationEntity] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
