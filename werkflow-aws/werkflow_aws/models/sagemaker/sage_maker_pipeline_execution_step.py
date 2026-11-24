from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_cache_hit_result import SageMakerCacheHitResult
from .sage_maker_iteration_context import SageMakerIterationContext
from .sage_maker_pipeline_execution_step_metadata import SageMakerPipelineExecutionStepMetadata
from .sage_maker_selective_execution_result import SageMakerSelectiveExecutionResult


class SageMakerPipelineExecutionStep(BaseModel):
    StepName: StrictStr | None = None
    StepDisplayName: StrictStr | None = None
    StepDescription: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    StepStatus: StrictStr | None = None
    CacheHitResult: SageMakerCacheHitResult | None = None
    FailureReason: StrictStr | None = None
    Metadata: SageMakerPipelineExecutionStepMetadata | None = None
    AttemptCount: StrictInt | None = None
    SelectiveExecutionResult: SageMakerSelectiveExecutionResult | None = None
    IterationContext: SageMakerIterationContext | None = None
