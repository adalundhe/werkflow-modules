from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_encryption_configuration import GlueEncryptionConfiguration


class GlueSecurityConfiguration(BaseModel):
    Name: StrictStr | None = None
    CreatedTimeStamp: datetime.datetime | StrictStr | None = None
    EncryptionConfiguration: GlueEncryptionConfiguration | None = None
