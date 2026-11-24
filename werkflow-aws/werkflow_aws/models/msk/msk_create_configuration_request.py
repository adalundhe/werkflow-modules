from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class MSKCreateConfigurationRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Name: StrictStr
    ServerProperties: StrictBytes | BinaryIO | StrictStr
    Description: StrictStr | None = None
    KafkaVersions: list[StrictStr] | None = None
