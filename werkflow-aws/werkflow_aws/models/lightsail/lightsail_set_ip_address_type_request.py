from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailSetIpAddressTypeRequest(BaseModel):
    resourceType: Literal['ContainerService', 'Instance', 'StaticIp', 'KeyPair', 'InstanceSnapshot', 'Domain', 'PeeredVpc', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'Disk', 'DiskSnapshot', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'ExportSnapshotRecord', 'CloudFormationStackRecord', 'Alarm', 'ContactMethod', 'Distribution', 'Certificate', 'Bucket', 'Subdomain']
    resourceName: StrictStr
    ipAddressType: Literal['dualstack', 'ipv4', 'ipv6']
    acceptBundleUpdate: StrictBool | None = None
