from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class PersonalizeCampaignConfig(BaseModel):
    itemExplorationConfig: dict[StrictStr, StrictStr] | None = None
    enableMetadataWithRecommendations: StrictBool | None = None
    syncWithLatestSolutionVersion: StrictBool | None = None
    rankingInfluence: dict[StrictStr, StrictFloat | StrictInt] | None = None
