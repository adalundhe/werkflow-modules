from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .compute_optimizer_license_recommendation_filter import ComputeOptimizerLicenseRecommendationFilter
from .compute_optimizer_s3_destination_config import ComputeOptimizerS3DestinationConfig


class ComputeOptimizerExportLicenseRecommendationsRequest(BaseModel):
    s3DestinationConfig: ComputeOptimizerS3DestinationConfig
    accountIds: list[StrictStr] | None = None
    filters: list[ComputeOptimizerLicenseRecommendationFilter] | None = None
    fieldsToExport: list[Literal['AccountId', 'ResourceArn', 'LookbackPeriodInDays', 'LastRefreshTimestamp', 'Finding', 'FindingReasonCodes', 'CurrentLicenseConfigurationNumberOfCores', 'CurrentLicenseConfigurationInstanceType', 'CurrentLicenseConfigurationOperatingSystem', 'CurrentLicenseConfigurationLicenseName', 'CurrentLicenseConfigurationLicenseEdition', 'CurrentLicenseConfigurationLicenseModel', 'CurrentLicenseConfigurationLicenseVersion', 'CurrentLicenseConfigurationMetricsSource', 'RecommendationOptionsOperatingSystem', 'RecommendationOptionsLicenseEdition', 'RecommendationOptionsLicenseModel', 'RecommendationOptionsSavingsOpportunityPercentage', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'Tags']] | None = None
    fileFormat: Literal['Csv'] | None = None
    includeMemberAccounts: StrictBool | None = None
