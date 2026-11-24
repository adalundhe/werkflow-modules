from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_account_link import WorkSpacesAccountLink


class WorkSpacesListAccountLinksResponse(BaseModel):
    AccountLinks: list[WorkSpacesAccountLink] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
