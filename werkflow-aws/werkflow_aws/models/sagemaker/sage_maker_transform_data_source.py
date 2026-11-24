from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_transform_s3_data_source import SageMakerTransformS3DataSource


class SageMakerTransformDataSource(BaseModel):
    S3DataSource: SageMakerTransformS3DataSource | None = None
