from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_export import CloudFormationExport


class CloudFormationListExportsResponse(BaseModel):
    Exports: list[CloudFormationExport] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
