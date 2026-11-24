from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_ops_entity import SSMOpsEntity


class SSMGetOpsSummaryResponse(BaseModel):
    Entities: list[SSMOpsEntity] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
