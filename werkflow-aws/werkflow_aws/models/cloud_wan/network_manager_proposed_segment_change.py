from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerProposedSegmentChange(BaseModel):
    Tags: list[NetworkManagerTag] | None = None
    AttachmentPolicyRuleNumber: StrictInt | None = None
    SegmentName: StrictStr | None = None
