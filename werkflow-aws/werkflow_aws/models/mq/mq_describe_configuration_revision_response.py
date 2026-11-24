from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class MQDescribeConfigurationRevisionResponse(BaseModel):
    ConfigurationId: StrictStr | None = None
    Created: datetime.datetime | StrictStr | None = None
    Data: StrictStr | None = None
    Description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
