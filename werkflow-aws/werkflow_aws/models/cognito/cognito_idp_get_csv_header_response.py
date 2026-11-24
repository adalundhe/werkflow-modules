from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CognitoIDPGetCSVHeaderResponse(BaseModel):
    UserPoolId: StrictStr | None = None
    CSVHeader: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
