import ansys.fluent.core as pyfluent
import os

def create_part_inject(solver_session, injection_name, injection_start_time, injection_stop_time, injection_surface, table_name, column_with_diameters, column_with_number_fractions, injection_type="surface"):
    models = solver_session.settings.setup.models
    injection = models.discrete_phase.injections
    injection.create(injection_name)
    particle_injection = injection[injection_name]
    particle_injection.injection_type.option = injection_type
    particle_injection.initial_values.times(start_time = injection_start_time, stop_time = injection_stop_time)
    particle_injection.initial_values.location.injection_surfaces = injection_surface
    particle_injection.initial_values.velocity.use_face_normal_direction = True
    particle_injection.initial_values.particle_size.option = "tabulated"
    particle_injection.initial_values.particle_size.tabulated_size.table_name = table_name
    particle_injection.initial_values.particle_size.tabulated_size.column_with_diameters = column_with_diameters
    particle_injection.initial_values.particle_size.tabulated_size.column_with_number_fractions = column_with_number_fractions

def change_settings_tabulated(solver_session, injection_name, injection_start_time, injection_stop_time, table_name, column_with_diameters, column_with_number_fractions):
    part_inject = solver_session.settings.setup.models.discrete_phase.injections[injection_name]
    part_inject.initial_values.times(start_time=injection_start_time, stop_time=injection_stop_time)
    part_inject.initial_values.particle_size.option = "tabulated"
    part_inject.initial_values.particle_size.tabulated_size.table_name = ""
    part_inject.initial_values.particle_size.tabulated_size.table_name = table_name
    part_inject.initial_values.particle_size.tabulated_size.column_with_diameters = column_with_diameters
    part_inject.initial_values.particle_size.tabulated_size.column_with_number_fractions = column_with_number_fractions

def create_deposited_part(solver_session, injection_name, injection_type):
    models = solver_session.settings.setup.models
    injection = models.discrete_phase.injections
    injection.create(injection_name)
    particle_injection = injection[injection_name]
    particle_injection.injection_type.option = injection_type

def change_journal_file_and_run(solver_session, working_directory, original_file, new_file, start_time, end_time, injection_name, diameter):
    # reading file
    f = open(working_directory + "\\" + original_file)
    g = f.read()
    f.close()

    # replace new times
    new_text_time = str(start_time) + " " + str(end_time)
    g = g.replace("9 10", new_text_time)

    #replace new name
    g = g.replace("part-inject", injection_name)

    #replace new diameter
    g = g.replace("0.0001", str(diameter))
    f = open(working_directory + "\\" + new_file, "w")
    f.write(g)
    f.close()
    part_inject_journal = working_directory + "\\" + new_file
    solver_session.settings.file.read_journal(file_name_list=[part_inject_journal])