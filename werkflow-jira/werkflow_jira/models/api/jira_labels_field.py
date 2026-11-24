from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_label_properties_input_jackson1 import JiraLabelPropertiesInputJackson1
from .jira_labels_input import JiraLabelsInput


class JiraLabelsField(BaseModel):
    bulkEditMultiSelectFieldOption: StrictStr | None = None
    fieldId: StrictStr | None = None
    labelProperties: list[JiraLabelPropertiesInputJackson1] | None = None
    labels: list[JiraLabelsInput] | None = None
