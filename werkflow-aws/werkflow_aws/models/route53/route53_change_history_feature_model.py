from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class Route53ChangeHistoryFeatureModel(BaseModel):
    Status: StrictStr | None = None
    RetentionStartsAt: datetime.datetime | StrictStr | None = None
