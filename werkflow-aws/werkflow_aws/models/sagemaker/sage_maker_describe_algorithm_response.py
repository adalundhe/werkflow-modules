from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_algorithm_status_details import SageMakerAlgorithmStatusDetails
from .sage_maker_algorithm_validation_specification import SageMakerAlgorithmValidationSpecification
from .sage_maker_inference_specification import SageMakerInferenceSpecification
from .sage_maker_training_specification import SageMakerTrainingSpecification


class SageMakerDescribeAlgorithmResponse(BaseModel):
    AlgorithmName: StrictStr | None = None
    AlgorithmArn: StrictStr | None = None
    AlgorithmDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    TrainingSpecification: SageMakerTrainingSpecification | None = None
    InferenceSpecification: SageMakerInferenceSpecification | None = None
    ValidationSpecification: SageMakerAlgorithmValidationSpecification | None = None
    AlgorithmStatus: StrictStr | None = None
    AlgorithmStatusDetails: SageMakerAlgorithmStatusDetails | None = None
    ProductId: StrictStr | None = None
    CertifyForMarketplace: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
