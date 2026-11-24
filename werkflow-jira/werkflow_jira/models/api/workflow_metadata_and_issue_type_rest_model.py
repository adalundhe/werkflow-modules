from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_metadata_rest_model import WorkflowMetadataRestModel


class WorkflowMetadataAndIssueTypeRestModel(BaseModel):
    issueTypeIds: list[StrictStr] | None = None
    workflow: WorkflowMetadataRestModel | None = None
