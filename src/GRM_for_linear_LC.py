# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# (GRM_for_linear_LC)=
# # Effects of dispersion on the elution of a rectangular pulse 

# %% [markdown]
# The following example is a reproduction of part of the research results published in "Analytical solutions and moment analysis of general rate model for linear liquid chromatography" (Shamsul Qamar, Javeria Nawaz Abbasi, Shumaila Javeed, Andreas Seidel-Morgenstern, Chemical Engineering Science 2014;107:192-205. doi:10.1016/j.ces.2013.12.019.). [**url**: here](https://doi.org/10.1016/j.ces.2013.12.019) <br> Their study of the General Rate Model for linear liquid chromatography was later used as a model problem by Leweke et al. for determining convergence benchmarks in CADET (_Chromatography Analysis and Design Toolkit (CADET)_, Samuel Leweke, Eric von Lieres, Computers & Chemical Engineering 2018;113:274-294. doi:10.1016/j.compchemeng.2018.02.025.)  [**url**: here](https://doi.org/10.1016/j.compchemeng.2018.02.025)
# <br>
#

# %% [markdown]
# In the example, a tracer is introduced into the column as a rectangular pulse. The binding behavior follows the Linear binding model. The unit operation model for this process is the General Rate Model.
# All numerical values are taken from Table 2 (Leweke et al.)
# The `flow_rate` can be calculated as the product of the interstitial cross section area and the interstitial velocity u. 

# %%
import numpy as np

from CADETProcess.processModel import ComponentSystem
from CADETProcess.processModel import Linear
from CADETProcess.processModel import Inlet, GeneralRateModel, Outlet
from CADETProcess.processModel import FlowSheet
from CADETProcess.processModel import Process

# Component System
component_system = ComponentSystem()
component_system.add_component('A')

# Binding Model
binding_model = Linear(component_system, name='Linear')
binding_model.is_kinetic = False
binding_model.adsorption_rate = [2.5]  # k_a [m_MP³ / (m_SP³ * s)]
binding_model.desorption_rate = [1.0]  # k_d [1 / s]


# Unit Operations
column = GeneralRateModel(component_system, name='column')
column.binding_model = binding_model
column.length = 0.017  # L [m]
column.cross_section_area = 1e-3 # [m²]
column.bed_porosity = 0.4  # ε_c [-]
column.particle_radius = 4.0e-5  # r_p [m]
column.particle_porosity = 0.333  # ε_p [-] 
column.axial_dispersion = 3.33e-9  # D_c [m² / s]
column.film_diffusion = column.n_comp * [1.67e-6]  # k_f [m / s]
column.pore_diffusion = column.n_comp * [3.003e-6]  # D_p [m² / s]
column.surface_diffusion = column.n_bound_states * [0.0]  #D_s [m² / s]
column.c = [0.0]  # [mM] 
column.q = [0.0]  # [mM]  

inlet = Inlet(component_system, name='inlet')
inlet.flow_rate = column.cross_section_area_interstitial * (0.5 * (1e-2 / 60))  # m² * [m / s] 

outlet = Outlet(component_system, name='outlet')


# Flow Sheet
flow_sheet = FlowSheet(component_system)

flow_sheet.add_unit(inlet)
flow_sheet.add_unit(column)
flow_sheet.add_unit(outlet, product_outlet=True)

flow_sheet.add_connection(inlet, column)
flow_sheet.add_connection(column, outlet)


# %%
# Process
process = Process(flow_sheet, 'pulse')
process.cycle_time = 100 * 60  # [s]
pulse_duration = 20.0 * 60  # [s]

c_pulse = np.array([1.0])  #injection conc = 1.0 [mol / m³]
c_initial = np.array([0.0])
  
process.add_event('pulse_start', 'flow_sheet.inlet.c', c_pulse)
process.add_event('pulse_stop', 'flow_sheet.inlet.c',  c_initial, pulse_duration)


# %%
print(__name__)
if __name__ == '__main__':
    from CADETProcess.simulator import Cadet
    process_simulator = Cadet()

    simulation_results = process_simulator.simulate(process)
    simulation_results.solution.column.outlet.plot()

# %% [markdown]
# The Peclet number `Pe` is a value discribing the ratio of convection to dispersion for particle flow in a column. It is given by the product of the column length and the interstiatial velocity devided by the dispersion. The `peclet_number` of the column used by Leweke et al. and shown in the plot above is around 425.4. 

# %%
peclet_number = (column.length * (0.5 * (1e-2 / 60))) / column.axial_dispersion
peclet_number

# %% [markdown]
# The effects of different Peclet numbers on the elution curve can be examined by varying the dispersion rates within the column. The results show an approaching of the elution curve to a rectangular output as the `dispersion_value` is reduced and the Peclet number increases. The greater influence of convection/advective transport (directed flow of particles with the mobile phase (eluent)) in high Peclet numbers results in a sharper rectangular peak at the outlet as the velocities of the particles within the mobile phase differ less. The elution approaches the behavior of an ideal plug flow. Smaller Peclet numbers result in a more defined, slim peak and a more gradiual elution with larger retention times as the differences between particle velocities in the mobile phase increase. 
#

# %%
print(__name__)
if __name__ == '__main__':
    import CADETProcess
    from CADETProcess.simulator import Cadet
    process_simulator = Cadet()

    dispersion_value = [1.4166666666666667e-06,  # Pe = 1 
                        2.8333333333333336e-07,  # Pe = 5
                        1.4166666666666668e-07,  # Pe = 10
                        5.666666666666667e-08,  # Pe = 25
                        2.8333333333333336e-08,  # Pe = 50
                        1.4166666666666668e-08,  # Pe = 100
                        3.33e-9]  # Pe = 425.4
    for i in dispersion_value:
        column.axial_dispersion = i  
        simulation_results = process_simulator.simulate(process)
        simulation_results.solution.column.outlet.plot()
        #CADETProcess.plotting.Layout.check_required_parameters()
        # layout = {"title": str(i)}
        #simulation_results.solution.column.outlet.plot.plotting.Layout.check_required_parameters()
