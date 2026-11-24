from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKUnprocessedScramSecret(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    SecretArn: StrictStr | None = None
