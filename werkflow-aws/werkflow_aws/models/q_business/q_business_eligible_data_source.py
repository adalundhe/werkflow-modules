from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessEligibleDataSource(BaseModel):
    indexId: StrictStr | None = None
    dataSourceId: StrictStr | None = None
