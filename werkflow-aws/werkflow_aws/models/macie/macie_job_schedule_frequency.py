from __future__ import annotations
from pydantic import BaseModel
from .macie_daily_schedule import MacieDailySchedule
from .macie_monthly_schedule import MacieMonthlySchedule
from .macie_weekly_schedule import MacieWeeklySchedule


class MacieJobScheduleFrequency(BaseModel):
    dailySchedule: MacieDailySchedule | None = None
    monthlySchedule: MacieMonthlySchedule | None = None
    weeklySchedule: MacieWeeklySchedule | None = None
