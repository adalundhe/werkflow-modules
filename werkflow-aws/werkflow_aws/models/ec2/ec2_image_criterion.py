from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_creation_date_condition import EC2CreationDateCondition
from .ec2_deprecation_time_condition import EC2DeprecationTimeCondition
from .ec2_image_watermark_filter_response import EC2ImageWatermarkFilterResponse
from .ec2_scan_result_condition import EC2ScanResultCondition


class EC2ImageCriterion(BaseModel):
    ImageProviders: list[StrictStr] | None = None
    MarketplaceProductCodes: list[StrictStr] | None = None
    ImageNames: list[StrictStr] | None = None
    DeprecationTimeCondition: EC2DeprecationTimeCondition | None = None
    CreationDateCondition: EC2CreationDateCondition | None = None
    ImageWatermarks: list[EC2ImageWatermarkFilterResponse] | None = None
    ScanResultCondition: EC2ScanResultCondition | None = None
