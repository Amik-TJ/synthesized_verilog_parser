import sys
import os
import re
import json


# Dynamically determine the path
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)



def read_parsed_lib_from_json(parsed_lib_json_path):
    with open(parsed_lib_json_path, 'r') as file:
        return json.load(file)



def read_gate_names_from_txt(unique_gate_names_file_path):
    with open(unique_gate_names_file_path, 'r') as file:
        gate_names = [line.strip() for line in file.readlines()]
    return gate_names



    

def extract_input_outputs(line):
    '''
    sample input
    line = ['RN(n_2)', 'CK(clk)', 'D(n_1)', 'Q(sum_out)']
    '''
    # Initialize an empty dictionary to store the key-value pairs
    key_value_pairs = {}

    # Iterate through the list of strings
    for item in line:

        parts = item.split('(')
        
        # The first part is the key, the second part is the value
        key = parts[0]
        value = parts[1].replace(')', '')
        
    
        key_value_pairs[key] = value

    return key_value_pairs


def map_pins_to_input_output(parsed_technology_library, gate_type, key_value_input_output):

    _output, _input = [], []
    for key in key_value_input_output.keys():
        direction = parsed_technology_library[gate_type]['pins'][key]['direction']
        if(direction == 'input'):
            _input.append(key_value_input_output[key])
        else:
            _output.append(key_value_input_output[key])

    return _output, _input

def sanitize(x):
    return x.strip(',;\n ()')


def verilog_parser(synthesized_verilog_path, parsed_lib_json_path, verbose=0):


    
    parsed_technology_library = read_parsed_lib_from_json(parsed_lib_json_path)
    available_gates = list(parsed_technology_library.keys())

    input_nodes = []                # all input ports are taken as nodes to visualize better
    output_nodes = []               # all output ports are taken as nodes to visualize better
    gates = []                      # nodes
    wires = []                      # [edges][(tail, head)] here the first index is the name of the wire;
    _input, _outputs = [], []
                                    # tail and head are the nodes to which the edge is connected to

    gate_type_and_name_mapping = {}


    if not os.path.exists(synthesized_verilog_path):
        raise FileNotFoundError(f"The file '{synthesized_verilog_path}' does not exist!")

    with open(synthesized_verilog_path, 'r') as v_file:
        file_content = v_file.read().replace('\n', '')  # Remove all newline characters
        if not file_content:
            raise ValueError(f"The file '{synthesized_verilog_path}' is empty!")



    # Split the content by semicolon and then strip to get each line as a separate string
    file_content_split_lines = [line.strip() for line in file_content.split(';') if line.strip()]




    # Further process each line to remove extra spaces around parentheses and between parameters
    formatted_lines = []
    for line in file_content_split_lines:
        # Remove spaces before and after parentheses
        line = line.replace(' (', '(').replace(' )', ')').replace('( ', '(').replace(') ', ')')
        # Use regex to replace spaces between parameters
        line = re.sub(r'(?<=\.)\s+', ' ', line)         # spaces after dot
        line = re.sub(r'\s+\(', '(', line)              # spaces before opening parenthesis
        line = re.sub(r'\)\s+', ')', line)              # spaces after closing parenthesis
        formatted_lines.append(line)




    for line in formatted_lines:
        # remove all leading spaces
        line = line.lstrip()

        # find all the input ports
        # find all the input ports
        if line.startswith('input'):
            # Remove the 'input' keyword
            line = line.lstrip('input').strip()
            
            # Check for bit width specifications, e.g., [3:0]
            match = re.search(r'\[(\d+):(\d+)\]', line)
            if match:
                upper_bound = int(match.group(1))
                lower_bound = int(match.group(2))
                line = re.sub(r'\[\d+:\d+\]', '', line)
                base_ports = [port.strip(',;\n ') for port in line.split(',')]
                ports = []
                for base_port in base_ports:
                    for i in range(lower_bound, upper_bound + 1):
                        ports.append(f"{base_port}[{i}]")
            else:
                ports = [port.strip(',;\n ') for port in line.split(',')]
            
            input_nodes.extend(ports)



        # find all the output ports
        elif line.startswith('output'):
            # Remove the 'output' keyword
            line = line.lstrip('output').strip()
            
            # Extract bit width specifications, e.g., [3:0]
            bit_match = re.search(r'\[(\d+):(\d+)\]', line)
            if bit_match:
                start_bit, end_bit = map(int, bit_match.groups())
                base_name = re.sub(r'\[\d+:\d+\]', '', line).strip(',;\n ')
                ports = [f'{base_name}[{i}]' for i in range(end_bit, start_bit + 1)]
            else:
                ports = [port.strip(',;\n ') for port in line.split(',')]
            
            output_nodes.extend(ports)



        elif (any(g in line for g in available_gates)):
            gate_type = line.split(' ')[0]
            # remove gate type (gate instantiation) from line. The first word
            stri = ''
            line = (line.split(sep=' ', maxsplit=1)[1:])
            line = stri.join(line)
            line = line.replace("\\", "")                                               # removing '/' from the line
            


            
            # extract gate name from line, append to gates and remove from line
            index = line.find("(")                                              # line contains: i.e -> A_reg_reg[0](.RN(n_12), .CK(clk), .D(n_11), .Q(sum_out[3]))
            # Split the line into two parts. First part should contain the gate name
            gate = line[:index].strip()                                         # line contains: i.e -> A_reg_reg[0]
            # Split the line into two parts. Second part should contain the interconnections
            line = line[index:].strip()                                         # line contains: i.e -> (.RN(n_12), .CK(clk), .D(n_11), .Q(sum_out[3]))
            gates.append(gate)
            gate_type_and_name_mapping[gate] = gate_type


            # input, output processing
            
            line = line[1:-1]         
                                                     # Removing the first bracket and last bracket. i.e: .A0(n_5), .A1(n_3), .B0(n_2), .Y(n_6)
            line = line.replace(".", "")            # Removing dot(.) from the line. i.e: A0(n_5), A1(n_3), B0(n_2), Y(n_6)
            line = line.replace(" ", "") 
                                            
            line = line.split(',')  
            
            key_value_pairs = extract_input_outputs(line)

            _outputs, _input = map_pins_to_input_output(parsed_technology_library, gate_type, key_value_pairs)

            
            #_output, _input = (line[-1], line[:-1]) if len(line) > 1 else (line[0], [])     # Last item is output. Except that everyting is input

            
            for _output in _outputs:
                if(_output in output_nodes):
                    wires.append([_output, gate, [_output]])
                else:
                    flag = 0
                    for i in wires:
                        if(i[0] == _output):
                            i[1] = gate
                            flag = 1
                            break
                    
                    if(flag == 0):
                        wires.append([_output, gate, []])
            
                # print('-------------------------------')
                # print('-------------------------------')
                # print(f'gate         : {gate}')
                # print(f'_input       : {_input}')
                # print(f'_output      : {_output}')
                # print(f'output_nodes : {output_nodes}')
                # print(f'wires        : {wires[-1]}')
                # print('-------------------------------')
                # print()

                         
            
            for i in _input:
                # print(f'wires -> {wires}')
                # print()
                if (i in input_nodes):
                    flag = 0
                    for j in wires:
                        if (j[0] == i):
                            j[2].append(gate)
                            flag = 1
                            break
                    if (flag == 0):
                        wires.append([i, i, [gate]])
                else:
                    flag = 0
                    for j in wires:
                        # print('**************************************')
                        # print(f'i ---------{i}')
                        # print(f'j ---------{j}')
                        # print(f'j[0]-------{j[0]}')
                        # print()
                        if (j[0] == i):   
                            j[2].append(gate)
                            flag = 1
                            break
                    if (flag == 0):
                        # print(f'line -> {line}')
                        # print('+++++++++++++++++++++++++')
                        # print(f'j[0] -> {j[0]}')
                        # print(f'i    -> {i}')
                        # print(f'gate -> {gate}')
                        # print([i, ' ', [gate]])
                        # print('=========================')
                        # print()
                        wires.append([i, ' ', [gate]])



    if (verbose):

        size = os.get_terminal_size()

        [print('_', end='') for i in range(int((size.columns - 5) / 2))]
        print("NODES", end='')
        [print('_', end='') for i in range(int((size.columns - 5) / 2))]
        print("\n\nINPUT: ", end='')
        print(input_nodes)

        print("\nOUTPUT: ", end='')
        print(output_nodes)

        print("\nAVAILABLE_GATES: ", end='')
        gates.sort()
        print(gates)
        print("")

        [print('_', end='') for i in range(int((size.columns - 5) / 2))]
        print("EDGES", end='')
        [print('_', end='') for i in range(int((size.columns - 5) / 2))]

        print("\n\nWIRES: ")
        print("{:<15}{:<15}{}".format("Wire_Groups", "Tail", "Head"))

        

        for i in wires:
            print(("{:<15}|{:^15}|{}").format(i[0],i[1],str(i[2])[1:-1]))
        
        
        [print('_', end='') for i in range(int((size.columns - 5) / 2))]
        print()
        

    
    return input_nodes, output_nodes, gates, wires, gate_type_and_name_mapping
