from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssueLimitReportResponseBean(BaseModel):
    entitiesBreachingLimit: dict[StrictStr, dict[StrictStr, list[StrictInt]]] | None = None
    issuesApproachingLimit: dict[StrictStr, dict[StrictStr, StrictInt]] | None = None
    issuesBreachingLimit: dict[StrictStr, dict[StrictStr, StrictInt]] | None = None
    limits: dict[StrictStr, StrictInt] | None = None
