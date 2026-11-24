from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_s3_model_data_source import SageMakerS3ModelDataSource


class SageMakerModelDataSource(BaseModel):
    S3DataSource: SageMakerS3ModelDataSource | None = None
