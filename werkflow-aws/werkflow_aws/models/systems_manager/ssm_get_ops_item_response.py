from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_ops_item import SSMOpsItem


class SSMGetOpsItemResponse(BaseModel):
    OpsItem: SSMOpsItem | None = None
    ResponseMetadata: dict[str, Any] | None = None
