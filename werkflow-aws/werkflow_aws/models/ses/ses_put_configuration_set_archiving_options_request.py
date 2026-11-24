from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESPutConfigurationSetArchivingOptionsRequest(BaseModel):
    ConfigurationSetName: StrictStr
    ArchiveArn: StrictStr | None = None
