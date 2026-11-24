from __future__ import annotations
from pydantic import BaseModel
from .awss3_metadata_table_encryption_configuration import AWSS3MetadataTableEncryptionConfiguration
from .awss3_record_expiration import AWSS3RecordExpiration


class AWSS3JournalTableConfiguration(BaseModel):
    RecordExpiration: AWSS3RecordExpiration
    EncryptionConfiguration: AWSS3MetadataTableEncryptionConfiguration | None = None
