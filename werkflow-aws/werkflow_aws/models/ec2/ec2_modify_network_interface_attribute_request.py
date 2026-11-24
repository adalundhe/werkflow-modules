from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_attribute_boolean_value import EC2AttributeBooleanValue
from .ec2_attribute_value import EC2AttributeValue
from .ec2_connection_tracking_specification_request import EC2ConnectionTrackingSpecificationRequest
from .ec2_ena_srd_specification import EC2EnaSrdSpecification
from .ec2_network_interface_attachment_changes import EC2NetworkInterfaceAttachmentChanges


class EC2ModifyNetworkInterfaceAttributeRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    EnaSrdSpecification: EC2EnaSrdSpecification | None = None
    EnablePrimaryIpv6: StrictBool | None = None
    ConnectionTrackingSpecification: EC2ConnectionTrackingSpecificationRequest | None = None
    AssociatePublicIpAddress: StrictBool | None = None
    AssociatedSubnetIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    Description: EC2AttributeValue | None = None
    SourceDestCheck: EC2AttributeBooleanValue | None = None
    Groups: list[StrictStr] | None = None
    Attachment: EC2NetworkInterfaceAttachmentChanges | None = None
