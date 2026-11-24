from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_feature_definition import SageMakerFeatureDefinition
from .sage_maker_last_update_status import SageMakerLastUpdateStatus
from .sage_maker_offline_store_config import SageMakerOfflineStoreConfig
from .sage_maker_offline_store_status import SageMakerOfflineStoreStatus
from .sage_maker_online_store_config import SageMakerOnlineStoreConfig
from .sage_maker_throughput_config_description import SageMakerThroughputConfigDescription


class SageMakerDescribeFeatureGroupResponse(BaseModel):
    FeatureGroupArn: StrictStr | None = None
    FeatureGroupName: StrictStr | None = None
    RecordIdentifierFeatureName: StrictStr | None = None
    EventTimeFeatureName: StrictStr | None = None
    FeatureDefinitions: list[SageMakerFeatureDefinition] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    OnlineStoreConfig: SageMakerOnlineStoreConfig | None = None
    OfflineStoreConfig: SageMakerOfflineStoreConfig | None = None
    ThroughputConfig: SageMakerThroughputConfigDescription | None = None
    RoleArn: StrictStr | None = None
    FeatureGroupStatus: StrictStr | None = None
    OfflineStoreStatus: SageMakerOfflineStoreStatus | None = None
    LastUpdateStatus: SageMakerLastUpdateStatus | None = None
    FailureReason: StrictStr | None = None
    Description: StrictStr | None = None
    NextToken: StrictStr | None = None
    OnlineStoreTotalSizeBytes: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
