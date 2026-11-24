from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr


class MSKDescribeConfigurationRevisionResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Arn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Revision: StrictInt | None = None
    ServerProperties: StrictBytes | Any | None = None
    ResponseMetadata: dict[str, Any] | None = None
