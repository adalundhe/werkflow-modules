from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_work_group_summary import AthenaWorkGroupSummary


class AthenaListWorkGroupsResponse(BaseModel):
    WorkGroups: list[AthenaWorkGroupSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
