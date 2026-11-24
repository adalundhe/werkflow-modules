from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsPutSchemaResponse(BaseModel):
    policyStoreId: StrictStr | None = None
    namespaces: list[StrictStr] | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
