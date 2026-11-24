from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateIntegrationAssociationResponse(BaseModel):
    IntegrationAssociationId: StrictStr | None = None
    IntegrationAssociationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
