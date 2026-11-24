from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_instance_tag_notification_attribute import EC2InstanceTagNotificationAttribute


class EC2DescribeInstanceEventNotificationAttributesResponse(BaseModel):
    InstanceTagAttribute: EC2InstanceTagNotificationAttribute | None = None
    ResponseMetadata: dict[str, Any] | None = None
