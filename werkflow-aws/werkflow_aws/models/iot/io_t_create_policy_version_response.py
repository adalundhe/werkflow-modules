from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class IoTCreatePolicyVersionResponse(BaseModel):
    policyArn: StrictStr | None = None
    policyDocument: StrictStr | None = None
    policyVersionId: StrictStr | None = None
    isDefaultVersion: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
