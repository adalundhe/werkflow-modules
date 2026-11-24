from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_forecast_computation import QuickSightForecastComputation
from .quick_sight_growth_rate_computation import QuickSightGrowthRateComputation
from .quick_sight_maximum_minimum_computation import QuickSightMaximumMinimumComputation
from .quick_sight_metric_comparison_computation import QuickSightMetricComparisonComputation
from .quick_sight_period_over_period_computation import QuickSightPeriodOverPeriodComputation
from .quick_sight_period_to_date_computation import QuickSightPeriodToDateComputation
from .quick_sight_top_bottom_movers_computation import QuickSightTopBottomMoversComputation
from .quick_sight_top_bottom_ranked_computation import QuickSightTopBottomRankedComputation
from .quick_sight_total_aggregation_computation import QuickSightTotalAggregationComputation
from .quick_sight_unique_values_computation import QuickSightUniqueValuesComputation


class QuickSightComputation(BaseModel):
    TopBottomRanked: QuickSightTopBottomRankedComputation | None = None
    TopBottomMovers: QuickSightTopBottomMoversComputation | None = None
    TotalAggregation: QuickSightTotalAggregationComputation | None = None
    MaximumMinimum: QuickSightMaximumMinimumComputation | None = None
    MetricComparison: QuickSightMetricComparisonComputation | None = None
    PeriodOverPeriod: QuickSightPeriodOverPeriodComputation | None = None
    PeriodToDate: QuickSightPeriodToDateComputation | None = None
    GrowthRate: QuickSightGrowthRateComputation | None = None
    UniqueValues: QuickSightUniqueValuesComputation | None = None
    Forecast: QuickSightForecastComputation | None = None
