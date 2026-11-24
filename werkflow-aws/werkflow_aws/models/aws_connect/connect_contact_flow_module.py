from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_external_invocation_configuration import ConnectExternalInvocationConfiguration


class ConnectContactFlowModule(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Content: StrictStr | None = None
    Description: StrictStr | None = None
    State: StrictStr | None = None
    Status: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    FlowModuleContentSha256: StrictStr | None = None
    Version: StrictInt | None = None
    VersionDescription: StrictStr | None = None
    Settings: StrictStr | None = None
    ExternalInvocationConfiguration: ConnectExternalInvocationConfiguration | None = None
