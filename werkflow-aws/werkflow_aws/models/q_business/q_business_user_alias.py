from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessUserAlias(BaseModel):
    indexId: StrictStr | None = None
    dataSourceId: StrictStr | None = None
    userId: StrictStr | None = None
