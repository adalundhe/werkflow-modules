from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerAddAssociationResponse(BaseModel):
    SourceArn: StrictStr | None = None
    DestinationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
