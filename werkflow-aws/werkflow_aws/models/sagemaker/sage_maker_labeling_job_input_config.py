from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_labeling_job_data_attributes import SageMakerLabelingJobDataAttributes
from .sage_maker_labeling_job_data_source import SageMakerLabelingJobDataSource


class SageMakerLabelingJobInputConfig(BaseModel):
    DataSource: SageMakerLabelingJobDataSource | None = None
    DataAttributes: SageMakerLabelingJobDataAttributes | None = None
