from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel, StrictStr


class AWSS3RestoreObjectResponse(BaseModel):
    RequestCharged: Literal['requester'] | None = None
    RestoreOutputPath: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
