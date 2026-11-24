from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_ptr_update_status import EC2PtrUpdateStatus


class EC2AddressAttribute(BaseModel):
    PublicIp: StrictStr | None = None
    AllocationId: StrictStr | None = None
    PtrRecord: StrictStr | None = None
    PtrRecordUpdate: EC2PtrUpdateStatus | None = None
