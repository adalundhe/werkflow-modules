from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTUpdateDimensionResponse(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    type: StrictStr | None = None
    stringValues: list[StrictStr] | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
