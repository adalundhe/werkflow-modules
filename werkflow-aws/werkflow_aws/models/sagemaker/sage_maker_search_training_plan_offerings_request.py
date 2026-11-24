from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerSearchTrainingPlanOfferingsRequest(BaseModel):
    InstanceType: Literal['ml.p4d.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.trn1.32xlarge', 'ml.trn2.48xlarge', 'ml.p6-b200.48xlarge', 'ml.p4de.24xlarge', 'ml.p6e-gb200.36xlarge', 'ml.p5.4xlarge', 'ml.p6-b300.48xlarge'] | None = None
    InstanceCount: StrictInt | None = None
    UltraServerType: StrictStr | None = None
    UltraServerCount: StrictInt | None = None
    StartTimeAfter: datetime.datetime | StrictStr | None = None
    EndTimeBefore: datetime.datetime | StrictStr | None = None
    DurationHours: StrictInt | None = None
    TargetResources: list[Literal['training-job', 'hyperpod-cluster', 'endpoint', 'studio-apps']] | None = None
    TrainingPlanArn: StrictStr | None = None
