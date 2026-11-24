from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_ad_hoc_filtering_option import QuickSightAdHocFilteringOption
from .quick_sight_dashboard_visual_publish_options import QuickSightDashboardVisualPublishOptions
from .quick_sight_data_point_drill_up_down_option import QuickSightDataPointDrillUpDownOption
from .quick_sight_data_point_menu_label_option import QuickSightDataPointMenuLabelOption
from .quick_sight_data_point_tooltip_option import QuickSightDataPointTooltipOption
from .quick_sight_data_qa_enabled_option import QuickSightDataQAEnabledOption
from .quick_sight_data_stories_sharing_option import QuickSightDataStoriesSharingOption
from .quick_sight_executive_summary_option import QuickSightExecutiveSummaryOption
from .quick_sight_export_to_csv_option import QuickSightExportToCSVOption
from .quick_sight_export_with_hidden_fields_option import QuickSightExportWithHiddenFieldsOption
from .quick_sight_quick_suite_actions_option import QuickSightQuickSuiteActionsOption
from .quick_sight_sheet_controls_option import QuickSightSheetControlsOption
from .quick_sight_sheet_layout_element_maximization_option import QuickSightSheetLayoutElementMaximizationOption
from .quick_sight_visual_axis_sort_option import QuickSightVisualAxisSortOption
from .quick_sight_visual_menu_option import QuickSightVisualMenuOption


class QuickSightDashboardPublishOptions(BaseModel):
    AdHocFilteringOption: QuickSightAdHocFilteringOption | None = None
    ExportToCSVOption: QuickSightExportToCSVOption | None = None
    SheetControlsOption: QuickSightSheetControlsOption | None = None
    VisualPublishOptions: QuickSightDashboardVisualPublishOptions | None = None
    SheetLayoutElementMaximizationOption: QuickSightSheetLayoutElementMaximizationOption | None = None
    VisualMenuOption: QuickSightVisualMenuOption | None = None
    VisualAxisSortOption: QuickSightVisualAxisSortOption | None = None
    ExportWithHiddenFieldsOption: QuickSightExportWithHiddenFieldsOption | None = None
    DataPointDrillUpDownOption: QuickSightDataPointDrillUpDownOption | None = None
    DataPointMenuLabelOption: QuickSightDataPointMenuLabelOption | None = None
    DataPointTooltipOption: QuickSightDataPointTooltipOption | None = None
    DataQAEnabledOption: QuickSightDataQAEnabledOption | None = None
    QuickSuiteActionsOption: QuickSightQuickSuiteActionsOption | None = None
    ExecutiveSummaryOption: QuickSightExecutiveSummaryOption | None = None
    DataStoriesSharingOption: QuickSightDataStoriesSharingOption | None = None
