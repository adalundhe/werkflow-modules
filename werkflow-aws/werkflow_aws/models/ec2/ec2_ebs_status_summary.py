from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_ebs_status_details import EC2EbsStatusDetails


class EC2EbsStatusSummary(BaseModel):
    Details: list[EC2EbsStatusDetails] | None = None
    Status: StrictStr | None = None
