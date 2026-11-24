from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointRecommenderConfigurationResponse(BaseModel):
    Attributes: dict[StrictStr, StrictStr] | None = None
    CreationDate: StrictStr | None = None
    Description: StrictStr | None = None
    Id: StrictStr | None = None
    LastModifiedDate: StrictStr | None = None
    Name: StrictStr | None = None
    RecommendationProviderIdType: StrictStr | None = None
    RecommendationProviderRoleArn: StrictStr | None = None
    RecommendationProviderUri: StrictStr | None = None
    RecommendationTransformerUri: StrictStr | None = None
    RecommendationsDisplayName: StrictStr | None = None
    RecommendationsPerMessage: StrictInt | None = None
