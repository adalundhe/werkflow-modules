from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_s3_model_data_source_model import SageMakerS3ModelDataSourceModel


class SageMakerModelDataSourceModel(BaseModel):
    S3DataSource: SageMakerS3ModelDataSourceModel | None = None
