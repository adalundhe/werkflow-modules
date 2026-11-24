from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DetectiveGraph(BaseModel):
    Arn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
