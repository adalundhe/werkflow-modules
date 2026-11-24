from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_bar_chart_visual import QuickSightBarChartVisual
from .quick_sight_box_plot_visual import QuickSightBoxPlotVisual
from .quick_sight_combo_chart_visual import QuickSightComboChartVisual
from .quick_sight_custom_content_visual import QuickSightCustomContentVisual
from .quick_sight_empty_visual import QuickSightEmptyVisual
from .quick_sight_filled_map_visual import QuickSightFilledMapVisual
from .quick_sight_funnel_chart_visual import QuickSightFunnelChartVisual
from .quick_sight_gauge_chart_visual import QuickSightGaugeChartVisual
from .quick_sight_geospatial_map_visual import QuickSightGeospatialMapVisual
from .quick_sight_heat_map_visual import QuickSightHeatMapVisual
from .quick_sight_histogram_visual import QuickSightHistogramVisual
from .quick_sight_insight_visual import QuickSightInsightVisual
from .quick_sight_kpi_visual import QuickSightKPIVisual
from .quick_sight_layer_map_visual import QuickSightLayerMapVisual
from .quick_sight_line_chart_visual import QuickSightLineChartVisual
from .quick_sight_pie_chart_visual import QuickSightPieChartVisual
from .quick_sight_pivot_table_visual import QuickSightPivotTableVisual
from .quick_sight_plugin_visual import QuickSightPluginVisual
from .quick_sight_radar_chart_visual import QuickSightRadarChartVisual
from .quick_sight_sankey_diagram_visual import QuickSightSankeyDiagramVisual
from .quick_sight_scatter_plot_visual import QuickSightScatterPlotVisual
from .quick_sight_table_visual import QuickSightTableVisual
from .quick_sight_tree_map_visual import QuickSightTreeMapVisual
from .quick_sight_waterfall_visual import QuickSightWaterfallVisual
from .quick_sight_word_cloud_visual import QuickSightWordCloudVisual


class QuickSightVisual(BaseModel):
    TableVisual: QuickSightTableVisual | None = None
    PivotTableVisual: QuickSightPivotTableVisual | None = None
    BarChartVisual: QuickSightBarChartVisual | None = None
    KPIVisual: QuickSightKPIVisual | None = None
    PieChartVisual: QuickSightPieChartVisual | None = None
    GaugeChartVisual: QuickSightGaugeChartVisual | None = None
    LineChartVisual: QuickSightLineChartVisual | None = None
    HeatMapVisual: QuickSightHeatMapVisual | None = None
    TreeMapVisual: QuickSightTreeMapVisual | None = None
    GeospatialMapVisual: QuickSightGeospatialMapVisual | None = None
    FilledMapVisual: QuickSightFilledMapVisual | None = None
    LayerMapVisual: QuickSightLayerMapVisual | None = None
    FunnelChartVisual: QuickSightFunnelChartVisual | None = None
    ScatterPlotVisual: QuickSightScatterPlotVisual | None = None
    ComboChartVisual: QuickSightComboChartVisual | None = None
    BoxPlotVisual: QuickSightBoxPlotVisual | None = None
    WaterfallVisual: QuickSightWaterfallVisual | None = None
    HistogramVisual: QuickSightHistogramVisual | None = None
    WordCloudVisual: QuickSightWordCloudVisual | None = None
    InsightVisual: QuickSightInsightVisual | None = None
    SankeyDiagramVisual: QuickSightSankeyDiagramVisual | None = None
    CustomContentVisual: QuickSightCustomContentVisual | None = None
    EmptyVisual: QuickSightEmptyVisual | None = None
    RadarChartVisual: QuickSightRadarChartVisual | None = None
    PluginVisual: QuickSightPluginVisual | None = None
