from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_network_interface import RedshiftNetworkInterface


class RedshiftVpcEndpoint(BaseModel):
    VpcEndpointId: StrictStr | None = None
    VpcId: StrictStr | None = None
    NetworkInterfaces: list[RedshiftNetworkInterface] | None = None
