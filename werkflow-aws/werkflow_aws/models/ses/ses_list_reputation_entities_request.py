from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESListReputationEntitiesRequest(BaseModel):
    Filter: dict[Literal['ENTITY_TYPE', 'REPUTATION_IMPACT', 'SENDING_STATUS', 'ENTITY_REFERENCE_PREFIX'], StrictStr] | None = None
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
