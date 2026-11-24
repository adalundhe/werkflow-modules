from __future__ import annotations
from pydantic import BaseModel
from .jira_cascading_select_field import JiraCascadingSelectField
from .jira_color_field import JiraColorField
from .jira_date_field import JiraDateField
from .jira_date_time_field import JiraDateTimeField
from .jira_duration_field import JiraDurationField
from .jira_issue_type_field import JiraIssueTypeField
from .jira_labels_field import JiraLabelsField
from .jira_multi_select_component_field import JiraMultiSelectComponentField
from .jira_multiple_group_picker_field import JiraMultipleGroupPickerField
from .jira_multiple_select_field import JiraMultipleSelectField
from .jira_multiple_select_user_picker_field import JiraMultipleSelectUserPickerField
from .jira_multiple_version_picker_field import JiraMultipleVersionPickerField
from .jira_number_field import JiraNumberField
from .jira_priority_field import JiraPriorityField
from .jira_rich_text_field import JiraRichTextField
from .jira_single_group_picker_field import JiraSingleGroupPickerField
from .jira_single_line_text_field import JiraSingleLineTextField
from .jira_single_select_field import JiraSingleSelectField
from .jira_single_select_user_picker_field import JiraSingleSelectUserPickerField
from .jira_single_version_picker_field import JiraSingleVersionPickerField
from .jira_status_input import JiraStatusInput
from .jira_time_tracking_field import JiraTimeTrackingField
from .jira_url_field import JiraUrlField


class JiraIssueFields(BaseModel):
    cascadingSelectFields: list[JiraCascadingSelectField] | None = None
    clearableNumberFields: list[JiraNumberField] | None = None
    colorFields: list[JiraColorField] | None = None
    datePickerFields: list[JiraDateField] | None = None
    dateTimePickerFields: list[JiraDateTimeField] | None = None
    issueType: JiraIssueTypeField | None = None
    labelsFields: list[JiraLabelsField] | None = None
    multipleGroupPickerFields: list[JiraMultipleGroupPickerField] | None = None
    multipleSelectClearableUserPickerFields: list[JiraMultipleSelectUserPickerField] | None = None
    multipleSelectFields: list[JiraMultipleSelectField] | None = None
    multipleVersionPickerFields: list[JiraMultipleVersionPickerField] | None = None
    multiselectComponents: JiraMultiSelectComponentField | None = None
    originalEstimateField: JiraDurationField | None = None
    priority: JiraPriorityField | None = None
    richTextFields: list[JiraRichTextField] | None = None
    singleGroupPickerFields: list[JiraSingleGroupPickerField] | None = None
    singleLineTextFields: list[JiraSingleLineTextField] | None = None
    singleSelectClearableUserPickerFields: list[JiraSingleSelectUserPickerField] | None = None
    singleSelectFields: list[JiraSingleSelectField] | None = None
    singleVersionPickerFields: list[JiraSingleVersionPickerField] | None = None
    status: JiraStatusInput | None = None
    timeTrackingField: JiraTimeTrackingField | None = None
    urlFields: list[JiraUrlField] | None = None
