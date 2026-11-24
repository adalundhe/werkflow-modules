from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreatePolicyResponse(BaseModel):
    policyName: StrictStr | None = None
    policyArn: StrictStr | None = None
    policyDocument: StrictStr | None = None
    policyVersionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
