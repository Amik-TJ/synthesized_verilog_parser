# Cadence Genus(TM) Synthesis Solution, Version 20.10-p001_1, built Dec 11 2020 16:29:55

# Date: Tue Aug 29 21:54:14 2023
# Host: thinker (x86_64 w/Linux 4.18.0-477.21.1.el8_8.x86_64) (16cores*24cpus*1physical cpu*12th Gen Intel(R) Core(TM) i9-12900F 30720KB)
# OS:   CentOS Linux release 7.9.2009 (Core)

read_lib ../design_files/slow.lib
read_hdl four_bit_adder_reg_to_reg.v
elaborate four_bit_adder_reg_to_reg
synthesize -to_mapped
write -mapped > synthesized_design.v
