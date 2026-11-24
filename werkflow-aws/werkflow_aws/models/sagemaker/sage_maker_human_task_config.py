from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_annotation_consolidation_config import SageMakerAnnotationConsolidationConfig
from .sage_maker_public_workforce_task_price import SageMakerPublicWorkforceTaskPrice
from .sage_maker_ui_config import SageMakerUiConfig


class SageMakerHumanTaskConfig(BaseModel):
    WorkteamArn: StrictStr | None = None
    UiConfig: SageMakerUiConfig | None = None
    PreHumanTaskLambdaArn: StrictStr | None = None
    TaskKeywords: list[StrictStr] | None = None
    TaskTitle: StrictStr | None = None
    TaskDescription: StrictStr | None = None
    NumberOfHumanWorkersPerDataObject: StrictInt | None = None
    TaskTimeLimitInSeconds: StrictInt | None = None
    TaskAvailabilityLifetimeInSeconds: StrictInt | None = None
    MaxConcurrentTaskCount: StrictInt | None = None
    AnnotationConsolidationConfig: SageMakerAnnotationConsolidationConfig | None = None
    PublicWorkforceTaskPrice: SageMakerPublicWorkforceTaskPrice | None = None
