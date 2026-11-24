from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_ebs_card_info import EC2EbsCardInfo
from .ec2_ebs_optimized_info import EC2EbsOptimizedInfo


class EC2EbsInfo(BaseModel):
    EbsOptimizedSupport: StrictStr | None = None
    EncryptionSupport: StrictStr | None = None
    EbsOptimizedInfo: EC2EbsOptimizedInfo | None = None
    NvmeSupport: StrictStr | None = None
    MaximumEbsAttachments: StrictInt | None = None
    AttachmentLimitType: StrictStr | None = None
    MaximumEbsCards: StrictInt | None = None
    EbsCards: list[EC2EbsCardInfo] | None = None
