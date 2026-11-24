from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class PinpointEmailChannelResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    ConfigurationSet: StrictStr | None = None
    CreationDate: StrictStr | None = None
    Enabled: StrictBool | None = None
    FromAddress: StrictStr | None = None
    HasCredential: StrictBool | None = None
    Id: StrictStr | None = None
    Identity: StrictStr | None = None
    IsArchived: StrictBool | None = None
    LastModifiedBy: StrictStr | None = None
    LastModifiedDate: StrictStr | None = None
    MessagesPerSecond: StrictInt | None = None
    Platform: StrictStr | None = None
    RoleArn: StrictStr | None = None
    OrchestrationSendingRoleArn: StrictStr | None = None
    Version: StrictInt | None = None
