import re
from typing import Dict


def get_next_page(headers: Dict[bytes, bytes]) -> bytes | None:
    links = headers.get(b'link')
    urls = links.split(b',')

    try:


        next_page = next(
            filter(
                lambda url: b'rel="next"' in url,
                urls
            )
        )
        
        url, _ = next_page.split(b';')

        return re.sub(
            r'[<>]',
            '',
            url.decode()
        ).strip()
    
    except Exception:
        return None