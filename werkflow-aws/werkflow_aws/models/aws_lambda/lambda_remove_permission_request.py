from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaRemovePermissionRequest(BaseModel):
    FunctionName: StrictStr
    StatementId: StrictStr
    Qualifier: StrictStr | None = None
    RevisionId: StrictStr | None = None
