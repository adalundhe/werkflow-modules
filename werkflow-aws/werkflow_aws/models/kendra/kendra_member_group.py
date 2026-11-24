from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraMemberGroup(BaseModel):
    GroupId: StrictStr
    DataSourceId: StrictStr | None = None
