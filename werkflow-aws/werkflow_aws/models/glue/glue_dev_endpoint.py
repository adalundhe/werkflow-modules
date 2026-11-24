from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GlueDevEndpoint(BaseModel):
    EndpointName: StrictStr | None = None
    RoleArn: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SubnetId: StrictStr | None = None
    YarnEndpointAddress: StrictStr | None = None
    PrivateAddress: StrictStr | None = None
    ZeppelinRemoteSparkInterpreterPort: StrictInt | None = None
    PublicAddress: StrictStr | None = None
    Status: StrictStr | None = None
    WorkerType: StrictStr | None = None
    GlueVersion: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    NumberOfNodes: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    VpcId: StrictStr | None = None
    ExtraPythonLibsS3Path: StrictStr | None = None
    ExtraJarsS3Path: StrictStr | None = None
    FailureReason: StrictStr | None = None
    LastUpdateStatus: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    LastModifiedTimestamp: datetime.datetime | StrictStr | None = None
    PublicKey: StrictStr | None = None
    PublicKeys: list[StrictStr] | None = None
    SecurityConfiguration: StrictStr | None = None
    Arguments: dict[StrictStr, StrictStr] | None = None
