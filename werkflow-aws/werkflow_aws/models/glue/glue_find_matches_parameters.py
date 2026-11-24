from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class GlueFindMatchesParameters(BaseModel):
    PrimaryKeyColumnName: StrictStr | None = None
    PrecisionRecallTradeoff: StrictFloat | StrictInt | None = None
    AccuracyCostTradeoff: StrictFloat | StrictInt | None = None
    EnforceProvidedLabels: StrictBool | None = None
