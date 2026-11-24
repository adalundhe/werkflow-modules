from __future__ import annotations
from pydantic import BaseModel
from .awss3_s3_tables_destination import AWSS3S3TablesDestination


class AWSS3MetadataTableConfiguration(BaseModel):
    S3TablesDestination: AWSS3S3TablesDestination
