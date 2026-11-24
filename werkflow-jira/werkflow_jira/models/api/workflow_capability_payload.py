from __future__ import annotations
from pydantic import BaseModel
from .status_payload import StatusPayload
from .workflow_payload import WorkflowPayload
from .workflow_scheme_payload import WorkflowSchemePayload


class WorkflowCapabilityPayload(BaseModel):
    statuses: list[StatusPayload] | None = None
    workflowScheme: WorkflowSchemePayload | None = None
    workflows: list[WorkflowPayload] | None = None
