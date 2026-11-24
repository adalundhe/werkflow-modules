from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_ai_workload_s3_data_source import SageMakerAIWorkloadS3DataSource


class SageMakerAIWorkloadDataSource(BaseModel):
    S3DataSource: SageMakerAIWorkloadS3DataSource | None = None
