from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_copy_step_details import TransferCopyStepDetails
from .transfer_custom_step_details import TransferCustomStepDetails
from .transfer_decrypt_step_details import TransferDecryptStepDetails
from .transfer_delete_step_details import TransferDeleteStepDetails
from .transfer_tag_step_details import TransferTagStepDetails


class TransferWorkflowStep(BaseModel):
    Type: StrictStr | None = None
    CopyStepDetails: TransferCopyStepDetails | None = None
    CustomStepDetails: TransferCustomStepDetails | None = None
    DeleteStepDetails: TransferDeleteStepDetails | None = None
    TagStepDetails: TransferTagStepDetails | None = None
    DecryptStepDetails: TransferDecryptStepDetails | None = None
