from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MSKListScramSecretsResponse(BaseModel):
    NextToken: StrictStr | None = None
    SecretArnList: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
