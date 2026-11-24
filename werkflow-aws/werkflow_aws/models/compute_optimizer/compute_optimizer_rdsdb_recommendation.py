from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_db_storage_configuration import ComputeOptimizerDBStorageConfiguration
from .compute_optimizer_rdsdb_instance_recommendation_option import ComputeOptimizerRDSDBInstanceRecommendationOption
from .compute_optimizer_rdsdb_storage_recommendation_option import ComputeOptimizerRDSDBStorageRecommendationOption
from .compute_optimizer_rdsdb_utilization_metric import ComputeOptimizerRDSDBUtilizationMetric
from .compute_optimizer_rds_effective_recommendation_preferences import ComputeOptimizerRDSEffectiveRecommendationPreferences
from .compute_optimizer_tag import ComputeOptimizerTag


class ComputeOptimizerRDSDBRecommendation(BaseModel):
    resourceArn: StrictStr | None = None
    accountId: StrictStr | None = None
    engine: StrictStr | None = None
    engineVersion: StrictStr | None = None
    promotionTier: StrictInt | None = None
    currentDBInstanceClass: StrictStr | None = None
    currentStorageConfiguration: ComputeOptimizerDBStorageConfiguration | None = None
    dbClusterIdentifier: StrictStr | None = None
    idle: StrictStr | None = None
    instanceFinding: StrictStr | None = None
    storageFinding: StrictStr | None = None
    instanceFindingReasonCodes: list[StrictStr] | None = None
    currentInstancePerformanceRisk: StrictStr | None = None
    currentStorageEstimatedMonthlyVolumeIOPsCostVariation: StrictStr | None = None
    storageFindingReasonCodes: list[StrictStr] | None = None
    instanceRecommendationOptions: list[ComputeOptimizerRDSDBInstanceRecommendationOption] | None = None
    storageRecommendationOptions: list[ComputeOptimizerRDSDBStorageRecommendationOption] | None = None
    utilizationMetrics: list[ComputeOptimizerRDSDBUtilizationMetric] | None = None
    effectiveRecommendationPreferences: ComputeOptimizerRDSEffectiveRecommendationPreferences | None = None
    lookbackPeriodInDays: StrictFloat | StrictInt | None = None
    lastRefreshTimestamp: datetime.datetime | StrictStr | None = None
    tags: list[ComputeOptimizerTag] | None = None
