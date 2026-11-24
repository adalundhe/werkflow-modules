from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class LambdaAliasRoutingConfiguration(BaseModel):
    AdditionalVersionWeights: dict[StrictStr, StrictFloat | StrictInt] | None = None
