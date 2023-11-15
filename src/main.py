import sys
import os
import argparse
from grapher.grapher import grapher
from verilog_parser_engine.verilog_parser import verilog_parser
from verilog_parser_engine.sta_label_parser import sta_label_parser

# Dynamically get the root directory of your project
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


verilog_dict = {
    1 : {
        'name' : '1_bit_adder_reg_to_reg',
        'synthesized_verilog_path'      : 'data/verilogs/1_bit_adder_reg_to_reg/synthesized_design.v',
        'tempus_sta_log_file_directory' : 'data/verilogs/1_bit_adder_reg_to_reg/tempus.log',
        'parsed_lib_json_path' : 'data/outputs/tsmc_180_slow_parsed_library_file.json',
    },
    2 : {
        'name' : 'test_verilog',
        'synthesized_verilog_path'      : 'data/verilogs/test_verilog/synthesized_design.v',
        'tempus_sta_log_file_directory' : 'data/verilogs/test_verilog/tempus.log',
        'parsed_lib_json_path' : 'data/outputs/tsmc_180_slow_parsed_library_file.json',
    },

}


active = 1


def main():

    # Path Initialization
    synthesized_verilog_path = os.path.join(project_root, verilog_dict[active]['synthesized_verilog_path'])
    tempus_sta_log_file_directory = os.path.join(project_root,  verilog_dict[active]['tempus_sta_log_file_directory'])
    parsed_lib_json_path = os.path.join(project_root, verilog_dict[active]['parsed_lib_json_path'])
    verbose = 1


    # Node Edge Extration from synthesized design
    in_n, out_n, nodes, edges = verilog_parser(synthesized_verilog_path = synthesized_verilog_path, parsed_lib_json_path = parsed_lib_json_path, verbose=verbose)
    

    # Graph Generation
    grapher(in_n, out_n, nodes, edges, verbose=verbose)
    sta_label_parser(tempus_sta_log_file_directory)

if __name__ == "__main__":
    main()
