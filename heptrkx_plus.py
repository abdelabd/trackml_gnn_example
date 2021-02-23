# Input/output configuration
input_dir: C:/Users/abdel/GitHub/interaction_network/trackml_data/raw
output_dir:  C:/Users/abdel/GitHub/interaction_network/trackml_data/processed
n_files: 1770

# Graph building configuration
selection:
    pt_min: 2 # GeV
    phi_slope_max: 0.0006 #000262 # 0.0006
    z0_max: 15000 # 100
    n_phi_sections: 1
    n_eta_sections: 1
    eta_range: [-5, 5]
    endcaps: true
    phi_reflect: false
    remove_intersecting_edges: true
