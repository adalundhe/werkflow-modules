from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_feature_definition import SageMakerFeatureDefinition
from .sage_maker_online_store_config_update import SageMakerOnlineStoreConfigUpdate
from .sage_maker_throughput_config_update import SageMakerThroughputConfigUpdate


class SageMakerUpdateFeatureGroupRequest(BaseModel):
    FeatureGroupName: StrictStr
    FeatureAdditions: list[SageMakerFeatureDefinition] | None = None
    OnlineStoreConfig: SageMakerOnlineStoreConfigUpdate | None = None
    ThroughputConfig: SageMakerThroughputConfigUpdate | None = None
