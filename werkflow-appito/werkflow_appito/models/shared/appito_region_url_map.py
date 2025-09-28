from .appito_region import AppitoRegion, AppitoRegionName


class AppitoRegionUrlMap:
    
    def __init__(self):
        self._region_url_map: dict[AppitoRegion, str] = {
            AppitoRegion.EU: "https://frontdoor-eu.apptio.com",
            AppitoRegion.AU: "https://frontdoor-au.apptio.com",
            AppitoRegion.DEFAULT: "https://frontdoor.apptio.com",
            AppitoRegion.US: "https://frontdoor.apptio.com",
        }

    def get(self, name: AppitoRegionName):
        return self._region_url_map.get(
            AppitoRegion[name], 
            self._region_url_map[AppitoRegion.DEFAULT],
        )