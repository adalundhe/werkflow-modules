from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_offline_store_status import SageMakerOfflineStoreStatus


class SageMakerFeatureGroupSummary(BaseModel):
    FeatureGroupName: StrictStr | None = None
    FeatureGroupArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FeatureGroupStatus: StrictStr | None = None
    OfflineStoreStatus: SageMakerOfflineStoreStatus | None = None
