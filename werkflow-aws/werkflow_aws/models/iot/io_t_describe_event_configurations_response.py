from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_configuration import IoTConfiguration


class IoTDescribeEventConfigurationsResponse(BaseModel):
    eventConfigurations: dict[StrictStr, IoTConfiguration] | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
