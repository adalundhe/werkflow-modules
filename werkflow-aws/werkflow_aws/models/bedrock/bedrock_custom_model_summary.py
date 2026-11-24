from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockCustomModelSummary(BaseModel):
    modelArn: StrictStr | None = None
    modelName: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    baseModelArn: StrictStr | None = None
    baseModelName: StrictStr | None = None
    customizationType: StrictStr | None = None
    ownerAccountId: StrictStr | None = None
    modelStatus: StrictStr | None = None
