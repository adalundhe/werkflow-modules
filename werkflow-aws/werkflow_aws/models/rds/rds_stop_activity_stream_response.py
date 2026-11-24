from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RDSStopActivityStreamResponse(BaseModel):
    KmsKeyId: StrictStr | None = None
    KinesisStreamName: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
