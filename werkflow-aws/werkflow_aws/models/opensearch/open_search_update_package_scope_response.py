from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class OpenSearchUpdatePackageScopeResponse(BaseModel):
    PackageID: StrictStr | None = None
    Operation: StrictStr | None = None
    PackageUserList: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
