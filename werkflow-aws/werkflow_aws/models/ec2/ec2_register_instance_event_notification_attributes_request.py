from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_register_instance_tag_attribute_request import EC2RegisterInstanceTagAttributeRequest


class EC2RegisterInstanceEventNotificationAttributesRequest(BaseModel):
    InstanceTagAttribute: EC2RegisterInstanceTagAttributeRequest
    DryRun: StrictBool | None = None
