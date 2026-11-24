from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_feature_group_summary import SageMakerFeatureGroupSummary


class SageMakerListFeatureGroupsResponse(BaseModel):
    FeatureGroupSummaries: list[SageMakerFeatureGroupSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
