from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2RouteServerEndpoint(BaseModel):
    RouteServerId: StrictStr | None = None
    RouteServerEndpointId: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    EniId: StrictStr | None = None
    EniAddress: StrictStr | None = None
    State: StrictStr | None = None
    FailureReason: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
