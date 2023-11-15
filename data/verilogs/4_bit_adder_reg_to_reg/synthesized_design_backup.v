module four_bit_adder_reg_to_reg(clk, rst, A_in, B_in, sum_out,
carry_out);
  input clk, rst;
  input [3:0] A_in, B_in;
  output [3:0] sum_out;
  output carry_out;
  wire clk, rst;
  wire [3:0] A_in, B_in;
  wire [3:0] sum_out;
  wire carry_out;
  wire [3:0] A_reg;
  wire [3:0] B_reg;
  wire n_0, n_1, n_2, n_3, n_4, n_5, n_6, n_7;
  wire n_8, n_9, n_10, n_11, n_12;
  DFFRHQX1 \sum_out_reg[3] (.RN (n_12), .CK (clk), .D (n_11), .Q (sum_out[3]));
  DFFRHQX1 carry_out_reg(.RN (n_12), .CK (clk), .D (n_10), .Q (carry_out));
  ADDFX2 g202(.A (A_reg[3]), .B (B_reg[3]), .CI (n_8), .S (n_11), .CO
       (n_10));
  DFFRHQX1 \sum_out_reg[2] (.RN (n_12), .CK (clk), .D (n_9), .Q(sum_out[2]));
  ADDFX2 g204(.A (A_reg[2]), .B (B_reg[2]), .CI (n_6), .S (n_9), .CO(n_8));
  SDFFRHQX1 \sum_out_reg[1] (.RN (n_12), .CK (clk), .D (n_5), .SI(n_0), .SE (n_4), .Q (sum_out[1]));
  DFFRHQX1 \sum_out_reg[0] (.RN (n_12), .CK (clk), .D (n_7), .Q(sum_out[0]));
  INVXL g210(.A (n_1), .Y (n_7));
  OAI21XL g206(.A0 (n_5), .A1 (n_3), .B0 (n_2), .Y (n_6));
  NAND2BXL g209(.AN (n_3), .B (n_2), .Y (n_4));
  OAI21XL g211(.A0 (A_reg[0]), .A1 (B_reg[0]), .B0 (n_5), .Y (n_1));
  INVXL g208(.A (n_5), .Y (n_0));
  NAND2XL g212(.A (B_reg[1]), .B (A_reg[1]), .Y (n_2));
  NOR2XL g213(.A (A_reg[1]), .B (B_reg[1]), .Y (n_3));
  NAND2XL g214(.A (B_reg[0]), .B (A_reg[0]), .Y (n_5));
  DFFRHQX1 \A_reg_reg[2] (.RN (n_12), .CK (clk), .D (A_in[2]), .Q
       (A_reg[2]));
  DFFRHQX1 \B_reg_reg[3] (.RN (n_12), .CK (clk), .D (B_in[3]), .Q
       (B_reg[3]));
  DFFRHQX1 \A_reg_reg[3] (.RN (n_12), .CK (clk), .D (A_in[3]), .Q
       (A_reg[3]));
  DFFRHQX1 \B_reg_reg[0] (.RN (n_12), .CK (clk), .D (B_in[0]), .Q
       (B_reg[0]));
  DFFRHQX1 \B_reg_reg[2] (.RN (n_12), .CK (clk), .D (B_in[2]), .Q
       (B_reg[2]));
  DFFRHQX1 \A_reg_reg[1] (.RN (n_12), .CK (clk), .D (A_in[1]), .Q
       (A_reg[1]));
  DFFRHQX1 \B_reg_reg[1] (.RN (n_12), .CK (clk), .D (B_in[1]), .Q
       (B_reg[1]));
  DFFRHQX1 \A_reg_reg[0] (.RN (n_12), .CK (clk), .D (A_in[0]), .Q
       (A_reg[0]));
  INVXL g223(.A (rst), .Y (n_12));
endmodule