from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .compute_optimizer_ecs_service_recommendation_filter import ComputeOptimizerECSServiceRecommendationFilter
from .compute_optimizer_s3_destination_config import ComputeOptimizerS3DestinationConfig


class ComputeOptimizerExportECSServiceRecommendationsRequest(BaseModel):
    s3DestinationConfig: ComputeOptimizerS3DestinationConfig
    accountIds: list[StrictStr] | None = None
    filters: list[ComputeOptimizerECSServiceRecommendationFilter] | None = None
    fieldsToExport: list[Literal['AccountId', 'ServiceArn', 'LookbackPeriodInDays', 'LastRefreshTimestamp', 'LaunchType', 'CurrentPerformanceRisk', 'CurrentServiceConfigurationMemory', 'CurrentServiceConfigurationCpu', 'CurrentServiceConfigurationTaskDefinitionArn', 'CurrentServiceConfigurationAutoScalingConfiguration', 'CurrentServiceContainerConfigurations', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsMemoryMaximum', 'Finding', 'FindingReasonCodes', 'RecommendationOptionsMemory', 'RecommendationOptionsCpu', 'RecommendationOptionsSavingsOpportunityPercentage', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsContainerRecommendations', 'RecommendationOptionsProjectedUtilizationMetricsCpuMaximum', 'RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum', 'Tags', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'EffectiveRecommendationPreferencesLookBackPeriod']] | None = None
    fileFormat: Literal['Csv'] | None = None
    includeMemberAccounts: StrictBool | None = None
