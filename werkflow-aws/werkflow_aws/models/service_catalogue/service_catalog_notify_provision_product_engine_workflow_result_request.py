from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .service_catalog_engine_workflow_resource_identifier import ServiceCatalogEngineWorkflowResourceIdentifier
from .service_catalog_record_output import ServiceCatalogRecordOutput


class ServiceCatalogNotifyProvisionProductEngineWorkflowResultRequest(BaseModel):
    WorkflowToken: StrictStr
    RecordId: StrictStr
    Status: Literal['SUCCEEDED', 'FAILED']
    IdempotencyToken: StrictStr
    FailureReason: StrictStr | None = None
    ResourceIdentifier: ServiceCatalogEngineWorkflowResourceIdentifier | None = None
    Outputs: list[ServiceCatalogRecordOutput] | None = None
