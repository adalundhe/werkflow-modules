from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_feature_definition import SageMakerFeatureDefinition
from .sage_maker_offline_store_config import SageMakerOfflineStoreConfig
from .sage_maker_online_store_config import SageMakerOnlineStoreConfig
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_throughput_config import SageMakerThroughputConfig


class SageMakerCreateFeatureGroupRequest(BaseModel):
    FeatureGroupName: StrictStr
    RecordIdentifierFeatureName: StrictStr
    EventTimeFeatureName: StrictStr
    FeatureDefinitions: list[SageMakerFeatureDefinition]
    OnlineStoreConfig: SageMakerOnlineStoreConfig | None = None
    OfflineStoreConfig: SageMakerOfflineStoreConfig | None = None
    ThroughputConfig: SageMakerThroughputConfig | None = None
    RoleArn: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
