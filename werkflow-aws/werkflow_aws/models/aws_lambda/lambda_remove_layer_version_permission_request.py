from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaRemoveLayerVersionPermissionRequest(BaseModel):
    LayerName: StrictStr
    VersionNumber: StrictInt
    StatementId: StrictStr
    RevisionId: StrictStr | None = None
