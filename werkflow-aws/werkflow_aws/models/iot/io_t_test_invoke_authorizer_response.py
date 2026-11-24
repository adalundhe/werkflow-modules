from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTTestInvokeAuthorizerResponse(BaseModel):
    isAuthenticated: StrictBool | None = None
    principalId: StrictStr | None = None
    policyDocuments: list[StrictStr] | None = None
    refreshAfterInSeconds: StrictInt | None = None
    disconnectAfterInSeconds: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
