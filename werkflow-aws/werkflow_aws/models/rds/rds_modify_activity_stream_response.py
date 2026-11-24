from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class RDSModifyActivityStreamResponse(BaseModel):
    KmsKeyId: StrictStr | None = None
    KinesisStreamName: StrictStr | None = None
    Status: StrictStr | None = None
    Mode: StrictStr | None = None
    EngineNativeAuditFieldsIncluded: StrictBool | None = None
    PolicyStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
