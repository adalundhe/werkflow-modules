from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_metadata_value import SSMMetadataValue


class SSMGetOpsMetadataResponse(BaseModel):
    ResourceId: StrictStr | None = None
    Metadata: dict[StrictStr, SSMMetadataValue] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
