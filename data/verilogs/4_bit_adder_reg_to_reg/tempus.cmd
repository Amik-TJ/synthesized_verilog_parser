#######################################################
#                                                     
#  Tempus Timing Signoff Solution Command Logging File                     
#  Created on Tue Aug 29 21:59:35 2023                
#                                                     
#######################################################

#@(#)CDS: Tempus Timing Signoff Solution v21.14-s111_1 (64bit) 07/15/2022 10:03 (Linux 3.10.0-693.el7.x86_64)
#@(#)CDS: NanoRoute 21.14-s111_1 NR220628-1629/21_14-UB (database version 18.20.582) {superthreading v2.17}
#@(#)CDS: AAE 21.14-s031 (64bit) 07/15/2022 (Linux 3.10.0-693.el7.x86_64)
#@(#)CDS: CTE 21.14-s031_1 () Jun 22 2022 10:32:17 ( )
#@(#)CDS: SYNTECH 21.14-s014_1 () May 29 2022 20:47:50 ( )
#@(#)CDS: CPE v21.14-s062

read_lib ../design_files/slow.lib
read_verilog synthesized_design.v
set_top_module four_bit_adder_reg_to_reg
read_sdc design_constraints.sdc
read_sdc design_constraints.sdc
report_timing
read_lib ../design_files/slow.lib
read_verilog synthesized_design.v
read_sdc design_constraints.sdc
report_timing
read_verilog synthesized_design.v
read_sdc design_constraints.sdc
report_timing
report_timing -npaths 10000
report_timing -max_paths 10000
report_timing -max_paths 5
