from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieFindingsFilterListItem(BaseModel):
    action: StrictStr | None = None
    arn: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
