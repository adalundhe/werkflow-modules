from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_image_classification_job_config import SageMakerImageClassificationJobConfig
from .sage_maker_tabular_job_config import SageMakerTabularJobConfig
from .sage_maker_text_classification_job_config import SageMakerTextClassificationJobConfig
from .sage_maker_text_generation_job_config import SageMakerTextGenerationJobConfig
from .sage_maker_time_series_forecasting_job_config import SageMakerTimeSeriesForecastingJobConfig


class SageMakerAutoMLProblemTypeConfig(BaseModel):
    ImageClassificationJobConfig: SageMakerImageClassificationJobConfig | None = None
    TextClassificationJobConfig: SageMakerTextClassificationJobConfig | None = None
    TimeSeriesForecastingJobConfig: SageMakerTimeSeriesForecastingJobConfig | None = None
    TabularJobConfig: SageMakerTabularJobConfig | None = None
    TextGenerationJobConfig: SageMakerTextGenerationJobConfig | None = None
