from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeFeatureTransformation(BaseModel):
    name: StrictStr | None = None
    featureTransformationArn: StrictStr | None = None
    defaultParameters: dict[StrictStr, StrictStr] | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
