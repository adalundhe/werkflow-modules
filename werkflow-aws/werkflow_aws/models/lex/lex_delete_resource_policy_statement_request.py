from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDeleteResourcePolicyStatementRequest(BaseModel):
    resourceArn: StrictStr
    statementId: StrictStr
    expectedRevisionId: StrictStr | None = None
