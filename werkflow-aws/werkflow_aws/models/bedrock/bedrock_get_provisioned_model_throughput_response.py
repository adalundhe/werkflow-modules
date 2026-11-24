from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockGetProvisionedModelThroughputResponse(BaseModel):
    modelUnits: StrictInt | None = None
    desiredModelUnits: StrictInt | None = None
    provisionedModelName: StrictStr | None = None
    provisionedModelArn: StrictStr | None = None
    modelArn: StrictStr | None = None
    desiredModelArn: StrictStr | None = None
    foundationModelArn: StrictStr | None = None
    status: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
    failureMessage: StrictStr | None = None
    commitmentDuration: StrictStr | None = None
    commitmentExpirationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
