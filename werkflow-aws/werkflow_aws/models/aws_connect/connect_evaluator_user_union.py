from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluatorUserUnion(BaseModel):
    ConnectUserArn: StrictStr | None = None
