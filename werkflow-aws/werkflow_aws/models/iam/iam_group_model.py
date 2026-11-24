from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMGroupModel(BaseModel):
    Path: StrictStr | None = None
    GroupName: StrictStr | None = None
    GroupId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
