from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_instance_event_window_association_request import EC2InstanceEventWindowAssociationRequest


class EC2AssociateInstanceEventWindowRequest(BaseModel):
    InstanceEventWindowId: StrictStr
    AssociationTarget: EC2InstanceEventWindowAssociationRequest
    DryRun: StrictBool | None = None
