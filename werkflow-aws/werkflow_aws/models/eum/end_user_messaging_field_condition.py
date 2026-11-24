from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingFieldCondition(BaseModel):
    DependsOnFieldPath: StrictStr | None = None
    Operator: StrictStr | None = None
    Values: list[StrictStr] | None = None
