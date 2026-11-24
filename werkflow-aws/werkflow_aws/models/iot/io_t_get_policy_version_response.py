from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class IoTGetPolicyVersionResponse(BaseModel):
    policyArn: StrictStr | None = None
    policyName: StrictStr | None = None
    policyDocument: StrictStr | None = None
    policyVersionId: StrictStr | None = None
    isDefaultVersion: StrictBool | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    generationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
