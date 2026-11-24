from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRUpdateStudioRequest(BaseModel):
    StudioId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    DefaultS3Location: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
