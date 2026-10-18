import ansys.fluent.core as pyfluent
import os

def find_peak_velo(solver_session, working_directory, peak_flow_rate, calc_area, area_file_name, unit):
    write_file_path = working_directory + "\\" + area_file_name
    solver_session.settings.results.report.surface_integrals.area(surface_names = [calc_area], write_to_file = True, file_name = write_file_path)
    f = open(area_file_name)
    text = f.read()
    f.close()
    os.remove(write_file_path)
    index = text.find(".")
    inlet_surface_area = float(text[index-1:(len(text))])
    unit=str((unit).lower())
    if unit=="l/min":
        peak_inhalation_rate = peak_flow_rate*0.001/60
    flow_rate_unit = "m^3/s"
    peak_inhalation_velocity = peak_inhalation_rate/inlet_surface_area
    return peak_inhalation_velocity