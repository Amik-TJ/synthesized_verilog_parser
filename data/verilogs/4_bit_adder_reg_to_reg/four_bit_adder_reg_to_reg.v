module four_bit_adder_reg_to_reg (
    input clk,
    input rst,  // Active-high synchronous reset
    input [3:0] A_in,
    input [3:0] B_in,
    output reg [3:0] sum_out,
    output reg carry_out
);

reg [3:0] A_reg, B_reg;

always @(posedge clk or posedge rst) begin
    if (rst) begin
        A_reg <= 4'b0000;
        B_reg <= 4'b0000;
    end else begin
        A_reg <= A_in;
        B_reg <= B_in;
    end
end

wire [4:0] result;
assign result = A_reg + B_reg;

always @(posedge clk or posedge rst) begin
    if (rst) begin
        sum_out <= 4'b0000;
        carry_out <= 1'b0;
    end else begin
        sum_out <= result[3:0];
        carry_out <= result[4];
    end
end

endmodule
