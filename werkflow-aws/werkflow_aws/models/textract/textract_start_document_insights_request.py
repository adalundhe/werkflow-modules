from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_blueprint_item import TextractBlueprintItem
from .textract_encryption_configuration import TextractEncryptionConfiguration
from .textract_input_configuration import TextractInputConfiguration
from .textract_notification_configuration import TextractNotificationConfiguration
from .textract_output_configuration import TextractOutputConfiguration


class TextractStartDocumentInsightsRequest(BaseModel):
    InputConfiguration: TextractInputConfiguration
    OutputConfiguration: TextractOutputConfiguration
    ProjectArn: StrictStr | None = None
    Blueprints: list[TextractBlueprintItem] | None = None
    EncryptionConfiguration: TextractEncryptionConfiguration | None = None
    NotificationConfiguration: TextractNotificationConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
