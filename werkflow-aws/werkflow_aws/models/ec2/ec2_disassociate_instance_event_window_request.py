from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_instance_event_window_disassociation_request import EC2InstanceEventWindowDisassociationRequest


class EC2DisassociateInstanceEventWindowRequest(BaseModel):
    InstanceEventWindowId: StrictStr
    AssociationTarget: EC2InstanceEventWindowDisassociationRequest
    DryRun: StrictBool | None = None
