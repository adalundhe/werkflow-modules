from __future__ import annotations
from pydantic import BaseModel
from .status_mapping import StatusMapping


class PublishDraftWorkflowScheme(BaseModel):
    statusMappings: list[StatusMapping] | None = None
