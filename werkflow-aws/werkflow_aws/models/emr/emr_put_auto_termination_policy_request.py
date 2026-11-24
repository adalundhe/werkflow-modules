from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_auto_termination_policy import EMRAutoTerminationPolicy


class EMRPutAutoTerminationPolicyRequest(BaseModel):
    ClusterId: StrictStr
    AutoTerminationPolicy: EMRAutoTerminationPolicy | None = None
