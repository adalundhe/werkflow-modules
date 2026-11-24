from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class GlueCreateDevEndpointRequest(BaseModel):
    EndpointName: StrictStr
    RoleArn: StrictStr
    SecurityGroupIds: list[StrictStr] | None = None
    SubnetId: StrictStr | None = None
    PublicKey: StrictStr | None = None
    PublicKeys: list[StrictStr] | None = None
    NumberOfNodes: StrictInt | None = None
    WorkerType: Literal['Standard', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'G.025X', 'Z.2X', 'G.12X', 'G.16X', 'R.1X', 'R.2X', 'R.4X', 'R.8X'] | None = None
    GlueVersion: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    ExtraPythonLibsS3Path: StrictStr | None = None
    ExtraJarsS3Path: StrictStr | None = None
    SecurityConfiguration: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Arguments: dict[StrictStr, StrictStr] | None = None
