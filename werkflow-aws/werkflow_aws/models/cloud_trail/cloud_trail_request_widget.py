from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailRequestWidget(BaseModel):
    QueryStatement: StrictStr
    ViewProperties: dict[StrictStr, StrictStr]
    QueryParameters: list[StrictStr] | None = None
