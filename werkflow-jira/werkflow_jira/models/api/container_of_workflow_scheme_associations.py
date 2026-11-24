from __future__ import annotations
from pydantic import BaseModel
from .workflow_scheme_associations import WorkflowSchemeAssociations


class ContainerOfWorkflowSchemeAssociations(BaseModel):
    values: list[WorkflowSchemeAssociations] | None = None
