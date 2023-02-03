from prometheus_client import Summary, Gauge

from viessmann_exporter.exporter_client import fetch_metrics


def scrape_vicare():
    print("Start scraping values")
    metrics = fetch_metrics()
    print("Scraped metrics", metrics)

    STORAGE_WATER_TEMP_GAUGE.set(metrics.storage_water_temp)
    CONFIGURED_WATER_TEMP_GAUGE.set(metrics.configured_water_temp)
    OUTSIDE_TEMP_GAUGE.set(metrics.outside_temp)
    BOILER_TEMP_GAUGE.set(metrics.boiler_temp)
    BURNER_ACTIVE_GAUGE.set(1 if metrics.burner_active else 0)


REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
STORAGE_WATER_TEMP_GAUGE = Gauge('storage_water_temp', 'Gauge for current water temperature in the storage vessel')
CONFIGURED_WATER_TEMP_GAUGE = Gauge('configured_water_temp', 'Configured water temperature.')
OUTSIDE_TEMP_GAUGE = Gauge('outside_temp', 'Outside temperature.')
BOILER_TEMP_GAUGE = Gauge('boiler_temp', 'Temperature in water boiler.')
BURNER_ACTIVE_GAUGE = Gauge('burner_active', 'Is burner burning.')
