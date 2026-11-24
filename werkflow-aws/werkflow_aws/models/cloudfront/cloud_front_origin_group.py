from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_group_failover_criteria import CloudFrontOriginGroupFailoverCriteria
from .cloud_front_origin_group_members import CloudFrontOriginGroupMembers


class CloudFrontOriginGroup(BaseModel):
    Id: StrictStr | None = None
    FailoverCriteria: CloudFrontOriginGroupFailoverCriteria | None = None
    Members: CloudFrontOriginGroupMembers | None = None
    SelectionCriteria: StrictStr | None = None
