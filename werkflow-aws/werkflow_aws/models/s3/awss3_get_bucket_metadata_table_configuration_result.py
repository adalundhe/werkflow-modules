from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_error_details import AWSS3ErrorDetails
from .awss3_metadata_table_configuration_result import AWSS3MetadataTableConfigurationResult


class AWSS3GetBucketMetadataTableConfigurationResult(BaseModel):
    MetadataTableConfigurationResult: AWSS3MetadataTableConfigurationResult | None = None
    Status: StrictStr | None = None
    Error: AWSS3ErrorDetails | None = None
