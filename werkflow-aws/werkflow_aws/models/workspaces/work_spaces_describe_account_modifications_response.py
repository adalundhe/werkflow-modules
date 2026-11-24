from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_account_modification import WorkSpacesAccountModification


class WorkSpacesDescribeAccountModificationsResponse(BaseModel):
    AccountModifications: list[WorkSpacesAccountModification] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
