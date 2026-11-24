from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPreEvaluationFilter(BaseModel):
    ResourceType: StrictStr | None = None
    FilterType: StrictStr | None = None
    FilterKey: StrictStr | None = None
    FilterValue: StrictStr | None = None
    Operator: StrictStr | None = None
