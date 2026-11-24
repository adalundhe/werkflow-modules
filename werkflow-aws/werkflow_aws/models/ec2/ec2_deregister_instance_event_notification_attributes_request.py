from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_deregister_instance_tag_attribute_request import EC2DeregisterInstanceTagAttributeRequest


class EC2DeregisterInstanceEventNotificationAttributesRequest(BaseModel):
    InstanceTagAttribute: EC2DeregisterInstanceTagAttributeRequest
    DryRun: StrictBool | None = None
