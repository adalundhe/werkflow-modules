from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SageMakerListStageDevicesRequest(BaseModel):
    EdgeDeploymentPlanName: StrictStr
    StageName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ExcludeDevicesDeployedInOtherStage: StrictBool | None = None
