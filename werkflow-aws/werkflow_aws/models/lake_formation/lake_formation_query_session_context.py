from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LakeFormationQuerySessionContext(BaseModel):
    QueryId: StrictStr | None = None
    QueryStartTime: datetime.datetime | StrictStr | None = None
    ClusterId: StrictStr | None = None
    QueryAuthorizationId: StrictStr | None = None
    AdditionalContext: dict[StrictStr, StrictStr] | None = None
