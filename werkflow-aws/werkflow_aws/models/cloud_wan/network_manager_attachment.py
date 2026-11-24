from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .network_manager_attachment_error import NetworkManagerAttachmentError
from .network_manager_proposed_network_function_group_change import NetworkManagerProposedNetworkFunctionGroupChange
from .network_manager_proposed_segment_change import NetworkManagerProposedSegmentChange
from .network_manager_tag import NetworkManagerTag


class NetworkManagerAttachment(BaseModel):
    CoreNetworkId: StrictStr | None = None
    CoreNetworkArn: StrictStr | None = None
    AttachmentId: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    AttachmentType: StrictStr | None = None
    State: StrictStr | None = None
    EdgeLocation: StrictStr | None = None
    EdgeLocations: list[StrictStr] | None = None
    ResourceArn: StrictStr | None = None
    AttachmentPolicyRuleNumber: StrictInt | None = None
    SegmentName: StrictStr | None = None
    NetworkFunctionGroupName: StrictStr | None = None
    NatGatewaySupport: StrictStr | None = None
    NatSystemRouteSupport: StrictBool | None = None
    Tags: list[NetworkManagerTag] | None = None
    ProposedSegmentChange: NetworkManagerProposedSegmentChange | None = None
    ProposedNetworkFunctionGroupChange: NetworkManagerProposedNetworkFunctionGroupChange | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    LastModificationErrors: list[NetworkManagerAttachmentError] | None = None
