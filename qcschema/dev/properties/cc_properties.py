"""
Coupled cluster properties. Current version written with the DLPNO-CCSD(T) method of ORCA 4 in mind.
"""

cc_properties = {}

cc_properties["ccsd_correlation_energy"] = {
    "type" : "number"
    "description" : "CCSD correlation energy"
}

cc_properties["triples_correction"] = {
    "type" : "number",
    "description" : "Triples correction from perturbation theory, the (T)"
}


cc_properties["ccsd_t_correlation_energy"] = {
    "type" : "number"
    "description" : "CCSD(T) correlation energy"
}

cc_properties["cc_total_energy"] = {
    "type" : "number"
    "description" : "The total energy (SCF + CC"
}

# Diagnostics
cc_properties["t1_diagnostic"] = {
    "type" : "number",
    "description" : "T1 diagnostic for static electron correlation"
}
