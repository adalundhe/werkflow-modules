from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class ECRRegisterPullTimeUpdateExclusionResponse(BaseModel):
    principalArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
