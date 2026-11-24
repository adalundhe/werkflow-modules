from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .macie_classification_result_status import MacieClassificationResultStatus
from .macie_custom_data_identifiers import MacieCustomDataIdentifiers
from .macie_sensitive_data_item import MacieSensitiveDataItem


class MacieClassificationResult(BaseModel):
    additionalOccurrences: StrictBool | None = None
    customDataIdentifiers: MacieCustomDataIdentifiers | None = None
    mimeType: StrictStr | None = None
    sensitiveData: list[MacieSensitiveDataItem] | None = None
    sizeClassified: StrictInt | None = None
    status: MacieClassificationResultStatus | None = None
