from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_dataset_definition_model import SageMakerDatasetDefinitionModel
from .sage_maker_processing_s3_input_model import SageMakerProcessingS3InputModel


class SageMakerProcessingInputModel(BaseModel):
    InputName: StrictStr | None = None
    AppManaged: StrictBool | None = None
    S3Input: SageMakerProcessingS3InputModel | None = None
    DatasetDefinition: SageMakerDatasetDefinitionModel | None = None
