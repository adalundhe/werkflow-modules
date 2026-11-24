from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class PersonalizeBatchInferenceJobConfig(BaseModel):
    itemExplorationConfig: dict[StrictStr, StrictStr] | None = None
    rankingInfluence: dict[StrictStr, StrictFloat | StrictInt] | None = None
