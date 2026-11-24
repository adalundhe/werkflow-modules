import re
from typing import Annotated, List, Literal

from pydantic import BaseModel, Field, StrictInt, StrictStr


class Expose(BaseModel):
    layer_type: Literal['expose'] = 'expose'
    ports: Annotated[List[StrictInt | StrictStr], Field(min_length=1)]

    def to_string(self) -> str:
        exposed_ports = ' '.join(str(port) for port in self.ports)
        return f'EXPOSE {exposed_ports}'

    @classmethod
    def parse(cls, line: str) -> 'Expose':
        stripped = re.sub(r'^EXPOSE\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()
        ports: List[StrictInt | StrictStr] = []

        for token in stripped.split():
            if re.fullmatch(r'[0-9]+', token):
                ports.append(int(token))
            elif '/' in token and re.search(r'[0-9]+', token):
                ports.append(token)
            elif port := re.search(r'[0-9]+', token):
                ports.append(int(port.group(0)))

        if len(ports) < 1:
            ports.append(stripped)

        return cls(ports=ports)
