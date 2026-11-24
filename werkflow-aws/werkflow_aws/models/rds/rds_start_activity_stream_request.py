from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class RDSStartActivityStreamRequest(BaseModel):
    ResourceArn: StrictStr
    Mode: Literal['sync', 'async']
    KmsKeyId: StrictStr
    ApplyImmediately: StrictBool | None = None
    EngineNativeAuditFieldsIncluded: StrictBool | None = None
