from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .bulk_transition_submit_input import BulkTransitionSubmitInput


class IssueBulkTransitionPayload(BaseModel):
    bulkTransitionInputs: list[BulkTransitionSubmitInput] | None = None
    sendBulkNotification: StrictBool | None = None
