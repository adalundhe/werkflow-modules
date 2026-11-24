from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_classification_status import SecurityHubClassificationStatus
from .security_hub_custom_data_identifiers_result import SecurityHubCustomDataIdentifiersResult
from .security_hub_sensitive_data_result import SecurityHubSensitiveDataResult


class SecurityHubClassificationResult(BaseModel):
    MimeType: StrictStr | None = None
    SizeClassified: StrictInt | None = None
    AdditionalOccurrences: StrictBool | None = None
    Status: SecurityHubClassificationStatus | None = None
    SensitiveData: list[SecurityHubSensitiveDataResult] | None = None
    CustomDataIdentifiers: SecurityHubCustomDataIdentifiersResult | None = None
