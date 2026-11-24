from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ssm_compliance_execution_summary import SSMComplianceExecutionSummary
from .ssm_compliance_item_entry import SSMComplianceItemEntry


class SSMPutComplianceItemsRequest(BaseModel):
    ResourceId: StrictStr
    ResourceType: StrictStr
    ComplianceType: StrictStr
    ExecutionSummary: SSMComplianceExecutionSummary
    Items: list[SSMComplianceItemEntry]
    ItemContentHash: StrictStr | None = None
    UploadType: Literal['COMPLETE', 'PARTIAL'] | None = None
