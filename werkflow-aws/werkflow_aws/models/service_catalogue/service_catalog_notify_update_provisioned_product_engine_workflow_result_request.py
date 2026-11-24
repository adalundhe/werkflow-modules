from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .service_catalog_record_output import ServiceCatalogRecordOutput


class ServiceCatalogNotifyUpdateProvisionedProductEngineWorkflowResultRequest(BaseModel):
    WorkflowToken: StrictStr
    RecordId: StrictStr
    Status: Literal['SUCCEEDED', 'FAILED']
    IdempotencyToken: StrictStr
    FailureReason: StrictStr | None = None
    Outputs: list[ServiceCatalogRecordOutput] | None = None
