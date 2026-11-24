from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointUpdateRecommenderConfiguration(BaseModel):
    RecommendationProviderRoleArn: StrictStr
    RecommendationProviderUri: StrictStr
    Attributes: dict[StrictStr, StrictStr] | None = None
    Description: StrictStr | None = None
    Name: StrictStr | None = None
    RecommendationProviderIdType: StrictStr | None = None
    RecommendationTransformerUri: StrictStr | None = None
    RecommendationsDisplayName: StrictStr | None = None
    RecommendationsPerMessage: StrictInt | None = None
