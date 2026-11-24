from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTGetPolicyResponse(BaseModel):
    policyName: StrictStr | None = None
    policyArn: StrictStr | None = None
    policyDocument: StrictStr | None = None
    defaultVersionId: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    generationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
