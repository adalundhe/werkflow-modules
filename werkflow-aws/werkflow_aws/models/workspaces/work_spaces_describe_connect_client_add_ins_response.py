from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_connect_client_add_in import WorkSpacesConnectClientAddIn


class WorkSpacesDescribeConnectClientAddInsResponse(BaseModel):
    AddIns: list[WorkSpacesConnectClientAddIn] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
