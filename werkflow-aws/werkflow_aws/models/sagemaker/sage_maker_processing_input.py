from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_dataset_definition import SageMakerDatasetDefinition
from .sage_maker_processing_s3_input import SageMakerProcessingS3Input


class SageMakerProcessingInput(BaseModel):
    InputName: StrictStr | None = None
    AppManaged: StrictBool | None = None
    S3Input: SageMakerProcessingS3Input | None = None
    DatasetDefinition: SageMakerDatasetDefinition | None = None
