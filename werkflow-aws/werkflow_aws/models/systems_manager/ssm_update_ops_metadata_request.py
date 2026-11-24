from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_metadata_value import SSMMetadataValue


class SSMUpdateOpsMetadataRequest(BaseModel):
    OpsMetadataArn: StrictStr
    MetadataToUpdate: dict[StrictStr, SSMMetadataValue] | None = None
    KeysToDelete: list[StrictStr] | None = None
