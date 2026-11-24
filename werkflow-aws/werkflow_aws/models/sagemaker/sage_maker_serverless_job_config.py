from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_customization_technique import SageMakerCustomizationTechnique
from .sage_maker_evaluation_type import SageMakerEvaluationType
from .sage_maker_peft import SageMakerPeft
from .sage_maker_serverless_job_type import SageMakerServerlessJobType


class SageMakerServerlessJobConfig(BaseModel):
    BaseModelArn: StrictStr | None = None
    AcceptEula: StrictBool | None = None
    JobType: SageMakerServerlessJobType | None = None
    CustomizationTechnique: SageMakerCustomizationTechnique | None = None
    Peft: SageMakerPeft | None = None
    EvaluationType: SageMakerEvaluationType | None = None
    EvaluatorArn: StrictStr | None = None
    SequenceLength: StrictStr | None = None
