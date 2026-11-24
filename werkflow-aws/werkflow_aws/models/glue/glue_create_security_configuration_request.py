from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_encryption_configuration import GlueEncryptionConfiguration


class GlueCreateSecurityConfigurationRequest(BaseModel):
    Name: StrictStr
    EncryptionConfiguration: GlueEncryptionConfiguration
