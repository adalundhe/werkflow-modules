from __future__ import annotations
from pydantic import BaseModel
from .glue_export_encryption_configuration import GlueExportEncryptionConfiguration


class GlueS3TablesConfiguration(BaseModel):
    EncryptionConfiguration: GlueExportEncryptionConfiguration | None = None
