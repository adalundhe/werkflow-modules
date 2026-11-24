from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class IoTMqttContext(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    username: StrictStr | None = None
    password: StrictBytes | BinaryIO | StrictStr | None = None
    clientId: StrictStr | None = None
