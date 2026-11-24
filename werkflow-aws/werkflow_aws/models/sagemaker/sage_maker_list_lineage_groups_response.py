from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_lineage_group_summary import SageMakerLineageGroupSummary


class SageMakerListLineageGroupsResponse(BaseModel):
    LineageGroupSummaries: list[SageMakerLineageGroupSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
