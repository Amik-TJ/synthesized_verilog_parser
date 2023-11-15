module one_bit_adder_reg_to_reg(
  clk, 
  rst, 
  A_in, 
  B_in, 
  sum_out, 
  carry_out,
  sum_out_3);

  input clk, rst, A_in, B_in;
  output sum_out, carry_out;
  wire clk, rst, A_in, B_in;
  wire sum_out, carry_out;
  wire A_reg, B_reg, n_0, n_1, n_2;
  DFFRHQX1 sum_out_reg(.RN (n_2), .CK (clk), .D (n_1), .Q (sum_out));
  DFFRHQX1 carry_out_reg(.RN (n_2), .CK (clk), .D (n_0), .Q (carry_out));

  ADDHXL g33(.A (A_reg), .B (B_reg), .S (n_1), .CO (n_0));

  DFFRHQX1 B_reg_reg(.RN (n_2), .CK (clk), .D (B_in), .Q (B_reg));
  DFFRHQX1 A_reg_reg(.RN (n_2), .CK (clk), .D (A_in), .Q (A_reg));
  
  INVXL g36(.A (rst), .Y (n_2));
endmodule