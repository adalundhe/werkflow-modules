from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaAddLayerVersionPermissionRequest(BaseModel):
    LayerName: StrictStr
    VersionNumber: StrictInt
    StatementId: StrictStr
    Action: StrictStr
    Principal: StrictStr
    OrganizationId: StrictStr | None = None
    RevisionId: StrictStr | None = None
