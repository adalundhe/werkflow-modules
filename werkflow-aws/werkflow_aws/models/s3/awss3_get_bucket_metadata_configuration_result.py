from __future__ import annotations
from pydantic import BaseModel
from .awss3_metadata_configuration_result import AWSS3MetadataConfigurationResult


class AWSS3GetBucketMetadataConfigurationResult(BaseModel):
    MetadataConfigurationResult: AWSS3MetadataConfigurationResult | None = None
