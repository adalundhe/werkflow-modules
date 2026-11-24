from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_auto_ml_job_completion_criteria import SageMakerAutoMLJobCompletionCriteria
from .sage_maker_candidate_generation_config import SageMakerCandidateGenerationConfig
from .sage_maker_holiday_config_attributes import SageMakerHolidayConfigAttributes
from .sage_maker_time_series_config import SageMakerTimeSeriesConfig
from .sage_maker_time_series_transformations import SageMakerTimeSeriesTransformations


class SageMakerTimeSeriesForecastingJobConfig(BaseModel):
    FeatureSpecificationS3Uri: StrictStr | None = None
    CompletionCriteria: SageMakerAutoMLJobCompletionCriteria | None = None
    ForecastFrequency: StrictStr | None = None
    ForecastHorizon: StrictInt | None = None
    ForecastQuantiles: list[StrictStr] | None = None
    Transformations: SageMakerTimeSeriesTransformations | None = None
    TimeSeriesConfig: SageMakerTimeSeriesConfig | None = None
    HolidayConfig: list[SageMakerHolidayConfigAttributes] | None = None
    CandidateGenerationConfig: SageMakerCandidateGenerationConfig | None = None
