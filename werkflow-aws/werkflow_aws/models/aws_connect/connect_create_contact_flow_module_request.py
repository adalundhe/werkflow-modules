from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_external_invocation_configuration import ConnectExternalInvocationConfiguration


class ConnectCreateContactFlowModuleRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    Content: StrictStr
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
    Settings: StrictStr | None = None
    ExternalInvocationConfiguration: ConnectExternalInvocationConfiguration | None = None
