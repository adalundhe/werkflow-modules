from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_rightsizing_recommendation import CostExplorerRightsizingRecommendation
from .cost_explorer_rightsizing_recommendation_configuration import CostExplorerRightsizingRecommendationConfiguration
from .cost_explorer_rightsizing_recommendation_metadata import CostExplorerRightsizingRecommendationMetadata
from .cost_explorer_rightsizing_recommendation_summary import CostExplorerRightsizingRecommendationSummary


class CostExplorerGetRightsizingRecommendationResponse(BaseModel):
    Metadata: CostExplorerRightsizingRecommendationMetadata | None = None
    Summary: CostExplorerRightsizingRecommendationSummary | None = None
    RightsizingRecommendations: list[CostExplorerRightsizingRecommendation] | None = None
    NextPageToken: StrictStr | None = None
    Configuration: CostExplorerRightsizingRecommendationConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
