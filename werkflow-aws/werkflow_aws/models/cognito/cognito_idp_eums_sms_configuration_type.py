from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPEumsSmsConfigurationType(BaseModel):
    CallerArn: StrictStr | None = None
    ExternalId: StrictStr | None = None
    OriginationIdentity: StrictStr | None = None
    ConfigurationSetName: StrictStr | None = None
    InEntityId: StrictStr | None = None
    InTemplateId: StrictStr | None = None
    Region: StrictStr | None = None
