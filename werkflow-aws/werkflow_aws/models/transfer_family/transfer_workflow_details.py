from __future__ import annotations
from pydantic import BaseModel
from .transfer_workflow_detail import TransferWorkflowDetail


class TransferWorkflowDetails(BaseModel):
    OnUpload: list[TransferWorkflowDetail] | None = None
    OnPartialUpload: list[TransferWorkflowDetail] | None = None
