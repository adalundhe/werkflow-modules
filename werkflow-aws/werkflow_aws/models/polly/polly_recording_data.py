from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class PollyRecordingData(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    S3Url: StrictStr | None = None
    Bytes: StrictBytes | Any | None = None
