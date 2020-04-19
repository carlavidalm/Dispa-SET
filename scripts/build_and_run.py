# -*- coding: utf-8 -*-
"""
Minimalist example file showing how to access the Dispa-SET api to read a configuration file, 
create a simulation environment folder and run the simulation in GAMS

@author: Sylvain Quoilin
"""

# Add the root folder of Dispa-SET to the path so that the library can be loaded:
import sys,os
sys.path.append(os.path.abspath('..'))

# Import Dispa-SET
import dispaset as ds

# Load the configuration file
config = ds.load_config('../ConfigFiles/ConfigBE_heat.yml')
config['HydroScheduling']='Regional'
config['StopDate'] = (2015, 10, 7, 23, 59, 0)

# Build the simulation environment:
SimData = ds.build_simulation(config)

# Solve using GAMS:
r = ds.solve_GAMS(config['SimulationDirectory'], config['GAMS_folder'])

inputs,results = ds.get_sim_results(path=config['SimulationDirectory'],cache=False)
