from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerDeleteGlobalInferenceGatewayResponse(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
