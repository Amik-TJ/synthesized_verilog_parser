# Creating a clock with a reduced period to tighten constraints
create_clock -period 1 [get_ports clk]

# Setting a reduced input delay for the given ports
set_input_delay -clock [get_clocks clk] 1 [get_ports {A_in[*] B_in[*]}]

# Setting a reduced output delay for the given ports
set_output_delay -clock [get_clocks clk] 1 [get_ports {sum_out[*] carry_out}]

# Defining a false path for the reset signal to ignore its timing checks
set_false_path -from [get_ports rst]
