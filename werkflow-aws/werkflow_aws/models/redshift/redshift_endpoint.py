from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .redshift_vpc_endpoint import RedshiftVpcEndpoint


class RedshiftEndpoint(BaseModel):
    Address: StrictStr | None = None
    Port: StrictInt | None = None
    VpcEndpoints: list[RedshiftVpcEndpoint] | None = None
