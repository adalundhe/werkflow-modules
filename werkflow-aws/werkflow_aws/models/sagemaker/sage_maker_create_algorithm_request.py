from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_algorithm_validation_specification import SageMakerAlgorithmValidationSpecification
from .sage_maker_inference_specification import SageMakerInferenceSpecification
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_training_specification import SageMakerTrainingSpecification


class SageMakerCreateAlgorithmRequest(BaseModel):
    AlgorithmName: StrictStr
    TrainingSpecification: SageMakerTrainingSpecification
    AlgorithmDescription: StrictStr | None = None
    InferenceSpecification: SageMakerInferenceSpecification | None = None
    ValidationSpecification: SageMakerAlgorithmValidationSpecification | None = None
    CertifyForMarketplace: StrictBool | None = None
    Tags: list[SageMakerTagModel] | None = None
