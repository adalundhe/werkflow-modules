from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_creation_date_condition_request import EC2CreationDateConditionRequest
from .ec2_deprecation_time_condition_request import EC2DeprecationTimeConditionRequest
from .ec2_image_watermark_filter_request import EC2ImageWatermarkFilterRequest
from .ec2_scan_result_condition_request import EC2ScanResultConditionRequest


class EC2ImageCriterionRequest(BaseModel):
    ImageProviders: list[StrictStr] | None = None
    MarketplaceProductCodes: list[StrictStr] | None = None
    ImageNames: list[StrictStr] | None = None
    DeprecationTimeCondition: EC2DeprecationTimeConditionRequest | None = None
    CreationDateCondition: EC2CreationDateConditionRequest | None = None
    ImageWatermarks: list[EC2ImageWatermarkFilterRequest] | None = None
    ScanResultCondition: EC2ScanResultConditionRequest | None = None
