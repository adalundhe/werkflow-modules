from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_change_set_summary import CloudFormationChangeSetSummary


class CloudFormationListChangeSetsResponse(BaseModel):
    Summaries: list[CloudFormationChangeSetSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
