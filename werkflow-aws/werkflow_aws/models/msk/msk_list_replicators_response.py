from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_replicator_summary import MSKReplicatorSummary


class MSKListReplicatorsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Replicators: list[MSKReplicatorSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
