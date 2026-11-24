from __future__ import annotations
from pydantic import BaseModel
from .glue_connection_password_encryption import GlueConnectionPasswordEncryption
from .glue_encryption_at_rest import GlueEncryptionAtRest


class GlueDataCatalogEncryptionSettings(BaseModel):
    EncryptionAtRest: GlueEncryptionAtRest | None = None
    ConnectionPasswordEncryption: GlueConnectionPasswordEncryption | None = None
