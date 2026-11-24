from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LakeFormationQueryPlanningContext(BaseModel):
    DatabaseName: StrictStr
    CatalogId: StrictStr | None = None
    QueryAsOfTime: datetime.datetime | StrictStr | None = None
    QueryParameters: dict[StrictStr, StrictStr] | None = None
    TransactionId: StrictStr | None = None
