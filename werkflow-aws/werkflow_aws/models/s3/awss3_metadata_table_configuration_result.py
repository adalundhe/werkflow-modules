from __future__ import annotations
from pydantic import BaseModel
from .awss3_s3_tables_destination_result import AWSS3S3TablesDestinationResult


class AWSS3MetadataTableConfigurationResult(BaseModel):
    S3TablesDestinationResult: AWSS3S3TablesDestinationResult | None = None
