# QC_JSON_Schema
A JSON Schema for Quantum Chemistry

The purpose of this schema is to provide API like access to pre-existing quantum
chemistry packages to enable more complex workflows.  The core of this is to
avoid parsing ASCII-based output files and place output variables, vectors,
matrices in a consistent format that can be easily parsed.

Please see the [website](http://molssi-qc-schema.readthedocs.io/en/latest/index.html#) for the current specification.


# !!! I started to edit this, but didn't find it suitable for my purposes. No longer edited. !!!


# My edits
I'm editing this to fit my own purposes, which currently is the automation of orca calculations.

## TODO:

* Possibility to define dependencies
  * Using results of previous calculations as an input

* How to integrate this in workflows?
    * Should the workflow be defined at all in the json?
      * Currently the following is defined in the schema

      ```
      [     State 1     ]------->[     State 2         ]
              ^             ^             ^
        input molecule    driver   output properties
                          method
                         keywords
      ```
    * It would be cleaner that there would be two schemas:
      1. State
      2. Transformation


* The drivers option is limited
  * Old
    * enum, so one of the following has to be chosen
      * energy, gradient, hessian, property
    * Not practical

  * energy, molecular_property, geometry_optimization
