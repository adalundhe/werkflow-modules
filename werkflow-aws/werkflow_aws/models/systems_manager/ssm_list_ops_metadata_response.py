from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_ops_metadata import SSMOpsMetadata


class SSMListOpsMetadataResponse(BaseModel):
    OpsMetadataList: list[SSMOpsMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
