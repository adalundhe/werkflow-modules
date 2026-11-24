from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_ui_template_info import SageMakerUiTemplateInfo


class SageMakerDescribeHumanTaskUiResponse(BaseModel):
    HumanTaskUiArn: StrictStr | None = None
    HumanTaskUiName: StrictStr | None = None
    HumanTaskUiStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    UiTemplate: SageMakerUiTemplateInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
