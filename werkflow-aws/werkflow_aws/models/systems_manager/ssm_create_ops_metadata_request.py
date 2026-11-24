from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_metadata_value import SSMMetadataValue
from .ssm_tag import SSMTag


class SSMCreateOpsMetadataRequest(BaseModel):
    ResourceId: StrictStr
    Metadata: dict[StrictStr, SSMMetadataValue] | None = None
    Tags: list[SSMTag] | None = None
