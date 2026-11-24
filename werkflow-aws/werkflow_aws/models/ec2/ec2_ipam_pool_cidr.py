from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_ipam_pool_cidr_failure_reason import EC2IpamPoolCidrFailureReason


class EC2IpamPoolCidr(BaseModel):
    Cidr: StrictStr | None = None
    State: StrictStr | None = None
    FailureReason: EC2IpamPoolCidrFailureReason | None = None
    IpamPoolCidrId: StrictStr | None = None
    NetmaskLength: StrictInt | None = None
