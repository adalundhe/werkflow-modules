from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_labeling_job_s3_data_source import SageMakerLabelingJobS3DataSource
from .sage_maker_labeling_job_sns_data_source import SageMakerLabelingJobSnsDataSource


class SageMakerLabelingJobDataSource(BaseModel):
    S3DataSource: SageMakerLabelingJobS3DataSource | None = None
    SnsDataSource: SageMakerLabelingJobSnsDataSource | None = None
