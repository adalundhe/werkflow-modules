from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .swf_workflow_type_info import SWFWorkflowTypeInfo


class SWFListWorkflowTypesResponse(BaseModel):
    typeInfos: list[SWFWorkflowTypeInfo] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
