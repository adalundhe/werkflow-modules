from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_scheme_usage import WorkflowSchemeUsage


class WorkflowSchemeUsagePage(BaseModel):
    nextPageToken: StrictStr | None = None
    values: list[WorkflowSchemeUsage] | None = None
