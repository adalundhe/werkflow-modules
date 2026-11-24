from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class IoTBehaviorModelTrainingSummary(BaseModel):
    securityProfileName: StrictStr | None = None
    behaviorName: StrictStr | None = None
    trainingDataCollectionStartDate: datetime.datetime | StrictStr | None = None
    modelStatus: StrictStr | None = None
    datapointsCollectionPercentage: StrictFloat | StrictInt | None = None
    lastModelRefreshDate: datetime.datetime | StrictStr | None = None
