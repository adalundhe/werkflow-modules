from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_public_workforce_task_price import SageMakerPublicWorkforceTaskPrice


class SageMakerHumanLoopConfig(BaseModel):
    WorkteamArn: StrictStr | None = None
    HumanTaskUiArn: StrictStr | None = None
    TaskTitle: StrictStr | None = None
    TaskDescription: StrictStr | None = None
    TaskCount: StrictInt | None = None
    TaskAvailabilityLifetimeInSeconds: StrictInt | None = None
    TaskTimeLimitInSeconds: StrictInt | None = None
    TaskKeywords: list[StrictStr] | None = None
    PublicWorkforceTaskPrice: SageMakerPublicWorkforceTaskPrice | None = None
