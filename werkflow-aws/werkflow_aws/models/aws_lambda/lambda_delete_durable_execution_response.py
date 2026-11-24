from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LambdaDeleteDurableExecutionResponse(BaseModel):
    DeletionRequestTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
