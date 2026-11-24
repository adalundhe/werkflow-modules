from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_allow_list_criteria import MacieAllowListCriteria
from .macie_allow_list_status import MacieAllowListStatus


class MacieGetAllowListResponse(BaseModel):
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    criteria: MacieAllowListCriteria | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    status: MacieAllowListStatus | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
