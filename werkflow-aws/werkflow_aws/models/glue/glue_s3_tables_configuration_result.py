from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_export_encryption_configuration import GlueExportEncryptionConfiguration


class GlueS3TablesConfigurationResult(BaseModel):
    TableBucketArn: StrictStr | None = None
    EncryptionConfiguration: GlueExportEncryptionConfiguration | None = None
