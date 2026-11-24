import re
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, StrictFloat, StrictInt

from .cmd import Cmd


def _parse_number(raw: str) -> Union[int, float]:
    return float(raw) if '.' in raw else int(raw)


class Healthcheck(BaseModel):
    layer_type: Literal['healthcheck'] = 'healthcheck'
    interval: Optional[StrictInt | StrictFloat] = None
    timeout: Optional[StrictInt | StrictFloat] = None
    start_period: Optional[StrictInt | StrictFloat] = None
    retries: Optional[StrictInt | StrictFloat] = None
    command: Cmd

    def to_string(self) -> str:
        parts: List[str] = ['HEALTHCHECK']

        if self.interval is not None:
            parts.append(f'--interval={self.interval}s')

        if self.timeout is not None:
            parts.append(f'--timeout={self.timeout}s')

        if self.start_period is not None:
            parts.append(f'--start-period={self.start_period}s')

        if self.retries is not None:
            parts.append(f'--retries={self.retries}')

        parts.append(self.command.to_string())
        return ' '.join(parts)

    @classmethod
    def parse(cls, line: str) -> 'Healthcheck':
        stripped = re.sub(
            r'^HEALTHCHECK\s+',
            '',
            line.strip(),
            count=1,
            flags=re.IGNORECASE,
        ).strip()

        options: Dict[str, Any] = {}

        if command_match := re.search(r'CMD\b.*', stripped):
            command_string = command_match.group(0)
            options['command'] = Cmd.parse(command_string)
            stripped = re.sub(re.escape(command_string), '', stripped, count=1).strip()

        for token in stripped.split():
            if interval := re.fullmatch(r'--interval=([0-9]+(?:\.[0-9]+)?)s?', token):
                options['interval'] = _parse_number(interval.group(1))
            elif timeout := re.fullmatch(r'--timeout=([0-9]+(?:\.[0-9]+)?)s?', token):
                options['timeout'] = _parse_number(timeout.group(1))
            elif start_period := re.fullmatch(
                r'--start-period=([0-9]+(?:\.[0-9]+)?)s?',
                token,
            ):
                options['start_period'] = _parse_number(start_period.group(1))
            elif retries := re.fullmatch(r'--retries=([0-9]+)', token):
                options['retries'] = int(retries.group(1))

        return cls(**options)
