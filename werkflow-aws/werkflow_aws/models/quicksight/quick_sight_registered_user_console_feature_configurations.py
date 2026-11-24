from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_amazon_q_in_quick_sight_console_configurations import QuickSightAmazonQInQuickSightConsoleConfigurations
from .quick_sight_dashboard_customization_summary_configurations import QuickSightDashboardCustomizationSummaryConfigurations
from .quick_sight_recent_snapshots_configurations import QuickSightRecentSnapshotsConfigurations
from .quick_sight_schedules_configurations import QuickSightSchedulesConfigurations
from .quick_sight_shared_view_configurations import QuickSightSharedViewConfigurations
from .quick_sight_state_persistence_configurations import QuickSightStatePersistenceConfigurations
from .quick_sight_threshold_alerts_configurations import QuickSightThresholdAlertsConfigurations


class QuickSightRegisteredUserConsoleFeatureConfigurations(BaseModel):
    StatePersistence: QuickSightStatePersistenceConfigurations | None = None
    SharedView: QuickSightSharedViewConfigurations | None = None
    AmazonQInQuickSight: QuickSightAmazonQInQuickSightConsoleConfigurations | None = None
    Schedules: QuickSightSchedulesConfigurations | None = None
    RecentSnapshots: QuickSightRecentSnapshotsConfigurations | None = None
    ThresholdAlerts: QuickSightThresholdAlertsConfigurations | None = None
    DashboardCustomizationSummary: QuickSightDashboardCustomizationSummaryConfigurations | None = None
