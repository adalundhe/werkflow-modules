from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTManagedJobTemplateSummary(BaseModel):
    templateArn: StrictStr | None = None
    templateName: StrictStr | None = None
    description: StrictStr | None = None
    environments: list[StrictStr] | None = None
    templateVersion: StrictStr | None = None
