import datetime
from pydantic import BaseModel


class TimePeriod(BaseModel):
    Start: datetime.datetime | datetime.date
    End: datetime.datetime | datetime.date
    
    def dump(self, time_format: str | None = None):
        if time_format is None:
            time_format = '%Y-%m-%d'


        start = self.Start.strftime(time_format)
        end = self.End.strftime(time_format)

        return {
            'Start': start,
            'End': end
        }