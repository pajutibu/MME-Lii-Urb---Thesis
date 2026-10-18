import ansys.fluent.core as pyfluent
import ansys.fluent.core.parametric as para
import ansys.fluent.visualization as visu
import os

def assign_named_expressions(solver_session, peak_velocity, peak_velo_exp_name, breathing_frequency, breathing_freq_exp_name, breathing_exp_name):
    expressions = solver_session.settings.setup.named_expressions

    # peak Velocity expression
    expressions.create(peak_velo_exp_name)
    peak_velocity_expression = expressions[peak_velo_exp_name]
    peak_velocity_expression.definition = str(peak_velocity) + " [m/s]"
    peak_velocity_expression.input_parameter = True

    # breathing frequency expression
    expressions.create(breathing_freq_exp_name)
    breathing_frequency_expression = expressions[breathing_freq_exp_name]
    breathing_frequency_expression.definition = str(breathing_frequency) + " [Hz]"
    breathing_frequency_expression.input_parameter = True

    #sinusoidal breathing expression
    expressions.create(breathing_exp_name)
    inhalation_expression = expressions[breathing_exp_name]
    inhalation_expression.definition = str(peak_velo_exp_name + "*sin(" + breathing_freq_exp_name + "*2*PI*t)")
