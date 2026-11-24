from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .swf_workflow_type_configuration import SWFWorkflowTypeConfiguration
from .swf_workflow_type_info import SWFWorkflowTypeInfo


class SWFDescribeWorkflowTypeResponse(BaseModel):
    typeInfo: SWFWorkflowTypeInfo | None = None
    configuration: SWFWorkflowTypeConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
