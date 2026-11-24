from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_feature_parameter import SageMakerFeatureParameter


class SageMakerFeatureMetadata(BaseModel):
    FeatureGroupArn: StrictStr | None = None
    FeatureGroupName: StrictStr | None = None
    FeatureName: StrictStr | None = None
    FeatureType: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Parameters: list[SageMakerFeatureParameter] | None = None
