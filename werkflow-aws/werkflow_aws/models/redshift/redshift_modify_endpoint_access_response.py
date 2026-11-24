from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .redshift_vpc_endpoint import RedshiftVpcEndpoint
from .redshift_vpc_security_group_membership import RedshiftVpcSecurityGroupMembership


class RedshiftModifyEndpointAccessResponse(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
    SubnetGroupName: StrictStr | None = None
    EndpointStatus: StrictStr | None = None
    EndpointName: StrictStr | None = None
    EndpointCreateTime: datetime.datetime | StrictStr | None = None
    Port: StrictInt | None = None
    Address: StrictStr | None = None
    VpcSecurityGroups: list[RedshiftVpcSecurityGroupMembership] | None = None
    VpcEndpoint: RedshiftVpcEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None
