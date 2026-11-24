from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .compute_optimizer_ebs_filter import ComputeOptimizerEBSFilter
from .compute_optimizer_s3_destination_config import ComputeOptimizerS3DestinationConfig


class ComputeOptimizerExportEBSVolumeRecommendationsRequest(BaseModel):
    s3DestinationConfig: ComputeOptimizerS3DestinationConfig
    accountIds: list[StrictStr] | None = None
    filters: list[ComputeOptimizerEBSFilter] | None = None
    fieldsToExport: list[StrictStr] | None = None
    fileFormat: Literal['Csv'] | None = None
    includeMemberAccounts: StrictBool | None = None
