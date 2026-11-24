from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag
from .transfer_workflow_step import TransferWorkflowStep


class TransferDescribedWorkflow(BaseModel):
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    Steps: list[TransferWorkflowStep] | None = None
    OnExceptionSteps: list[TransferWorkflowStep] | None = None
    WorkflowId: StrictStr | None = None
    Tags: list[TransferTag] | None = None
    StructuredLogDestinations: list[StrictStr] | None = None
