from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_attribute_boolean_value import EC2AttributeBooleanValue
from .ec2_attribute_value import EC2AttributeValue
from .ec2_group_identifier_model import EC2GroupIdentifierModel
from .ec2_network_interface_attachment import EC2NetworkInterfaceAttachment


class EC2DescribeNetworkInterfaceAttributeResponse(BaseModel):
    Attachment: EC2NetworkInterfaceAttachment | None = None
    Description: EC2AttributeValue | None = None
    Groups: list[EC2GroupIdentifierModel] | None = None
    NetworkInterfaceId: StrictStr | None = None
    SourceDestCheck: EC2AttributeBooleanValue | None = None
    AssociatePublicIpAddress: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
