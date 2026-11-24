from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockProvisionedModelSummary(BaseModel):
    provisionedModelName: StrictStr | None = None
    provisionedModelArn: StrictStr | None = None
    modelArn: StrictStr | None = None
    desiredModelArn: StrictStr | None = None
    foundationModelArn: StrictStr | None = None
    modelUnits: StrictInt | None = None
    desiredModelUnits: StrictInt | None = None
    status: StrictStr | None = None
    commitmentDuration: StrictStr | None = None
    commitmentExpirationTime: datetime.datetime | StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
