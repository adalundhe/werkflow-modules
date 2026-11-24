from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag
from .transfer_workflow_step import TransferWorkflowStep


class TransferCreateWorkflowRequest(BaseModel):
    Steps: list[TransferWorkflowStep]
    Description: StrictStr | None = None
    OnExceptionSteps: list[TransferWorkflowStep] | None = None
    Tags: list[TransferTag] | None = None
    StructuredLogDestinations: list[StrictStr] | None = None
