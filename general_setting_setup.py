import ansys.fluent.core as pyfluent
import os

def general_settings_transients(solver_session):
    general = solver_session.settings.setup.general
    
    # transient time
    general.solver.time = "unsteady-2nd-order-bounded"

    # gravity settings
    general.operating_conditions.gravity.enable = True
    gravity = general.operating_conditions.gravity
    gravity.components = [0.0, 0.0, -9.81]

    #viscous model
    solver_session.settings.setup.models.viscous.model = "large-eddy-simulation"

    #set units
    general.units.set_units(quantity="length", units_name="mm", scale_factor=1, offset=0)

def steady_settings(solver_session):
    general = solver_session.settings.setup.general
    general.solver.time = "steady"
    solver_session.settings.setup.models.viscous.model = "k-omega"
    general.units.set_units(quantity="length", units_name="mm", scale_factor=1, offset=0)
    