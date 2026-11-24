from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailWidget(BaseModel):
    QueryAlias: StrictStr | None = None
    QueryStatement: StrictStr | None = None
    QueryParameters: list[StrictStr] | None = None
    ViewProperties: dict[StrictStr, StrictStr] | None = None
