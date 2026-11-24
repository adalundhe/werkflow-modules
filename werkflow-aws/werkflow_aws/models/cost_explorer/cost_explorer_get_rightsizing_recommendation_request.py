from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_rightsizing_recommendation_configuration import CostExplorerRightsizingRecommendationConfiguration


class CostExplorerGetRightsizingRecommendationRequest(BaseModel):
    Service: StrictStr
    Filter: CostExplorerExpression | None = None
    Configuration: CostExplorerRightsizingRecommendationConfiguration | None = None
    PageSize: StrictInt | None = None
    NextPageToken: StrictStr | None = None
