from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .macie_classification_details import MacieClassificationDetails
from .macie_policy_details import MaciePolicyDetails
from .macie_resources_affected import MacieResourcesAffected
from .macie_severity import MacieSeverity


class MacieFinding(BaseModel):
    accountId: StrictStr | None = None
    archived: StrictBool | None = None
    category: StrictStr | None = None
    classificationDetails: MacieClassificationDetails | None = None
    count: StrictInt | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    partition: StrictStr | None = None
    policyDetails: MaciePolicyDetails | None = None
    region: StrictStr | None = None
    resourcesAffected: MacieResourcesAffected | None = None
    sample: StrictBool | None = None
    schemaVersion: StrictStr | None = None
    severity: MacieSeverity | None = None
    title: StrictStr | None = None
    type: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
