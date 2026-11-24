from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2TransitGatewayMulticastGroup(BaseModel):
    GroupIpAddress: StrictStr | None = None
    TransitGatewayAttachmentId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceOwnerId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    GroupMember: StrictBool | None = None
    GroupSource: StrictBool | None = None
    MemberType: StrictStr | None = None
    SourceType: StrictStr | None = None
