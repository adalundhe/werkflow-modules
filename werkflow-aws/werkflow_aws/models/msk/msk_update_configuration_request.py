from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class MSKUpdateConfigurationRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Arn: StrictStr
    ServerProperties: StrictBytes | BinaryIO | StrictStr
    Description: StrictStr | None = None
