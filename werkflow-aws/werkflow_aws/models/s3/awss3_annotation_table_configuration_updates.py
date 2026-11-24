from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_metadata_table_encryption_configuration import AWSS3MetadataTableEncryptionConfiguration


class AWSS3AnnotationTableConfigurationUpdates(BaseModel):
    ConfigurationState: Literal['ENABLED', 'DISABLED']
    EncryptionConfiguration: AWSS3MetadataTableEncryptionConfiguration | None = None
    Role: StrictStr | None = None
