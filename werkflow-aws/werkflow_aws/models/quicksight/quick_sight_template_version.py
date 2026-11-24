from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_data_set_configuration import QuickSightDataSetConfiguration
from .quick_sight_sheet import QuickSightSheet
from .quick_sight_template_error import QuickSightTemplateError
from .quick_sight_topic_configuration import QuickSightTopicConfiguration


class QuickSightTemplateVersion(BaseModel):
    CreatedTime: datetime.datetime | StrictStr | None = None
    Errors: list[QuickSightTemplateError] | None = None
    VersionNumber: StrictInt | None = None
    Status: StrictStr | None = None
    DataSetConfigurations: list[QuickSightDataSetConfiguration] | None = None
    TopicConfigurations: list[QuickSightTopicConfiguration] | None = None
    Description: StrictStr | None = None
    SourceEntityArn: StrictStr | None = None
    ThemeArn: StrictStr | None = None
    Sheets: list[QuickSightSheet] | None = None
