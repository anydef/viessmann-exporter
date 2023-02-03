import os

from dataclasses import dataclass

from PyViCare.PyViCare import PyViCare

client_id = os.getenv("VIESSMANN_API_KEY")
email = os.getenv("VIESSMANN_EMAIL")
password = os.getenv("VIESSMANN_PASSWORD")


def client():
    vicare = PyViCare()
    vicare.initWithCredentials(email, password, client_id, "/tmp/token.save")
    return vicare


@dataclass
class ViCareExports:
    online_status: str
    configured_water_temp: float
    storage_water_temp: float
    outside_temp: float
    boiler_temp: float
    burner_active: bool
    active_program: str


def fetch_metrics() -> ViCareExports:
    device = vicare.devices[0]

    t = device.asAutoDetectDevice()
    burner = t.burners[0]  # select burner
    circuit = t.circuits[0]  # select heating circuit

    online_status = "Online" if device.isOnline() else "Offline"
    configured_water_temp = t.getDomesticHotWaterConfiguredTemperature()
    storage_water_temp = t.getDomesticHotWaterStorageTemperature()
    outside_temp = t.getOutsideTemperature()
    boiler_temp = t.getBoilerTemperature()
    burner_active = burner.getActive()
    active_program = circuit.getActiveProgram()
    return ViCareExports(online_status, configured_water_temp, storage_water_temp, outside_temp, boiler_temp,
                         burner_active, active_program)


vicare = client()
