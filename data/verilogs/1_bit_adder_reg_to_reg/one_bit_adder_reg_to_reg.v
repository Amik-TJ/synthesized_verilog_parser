module one_bit_adder_reg_to_reg (
    input clk,
    input rst,  // Active-high synchronous reset
    input A_in,
    input B_in,
    output reg sum_out,
    output reg carry_out
);

reg A_reg, B_reg;

always @(posedge clk or posedge rst) begin
    if (rst) begin
        A_reg <= 1'b0;
        B_reg <= 1'b0;
    end else begin
        A_reg <= A_in;
        B_reg <= B_in;
    end
end

wire [1:0] result;
assign result = A_reg + B_reg;

always @(posedge clk or posedge rst) begin
    if (rst) begin
        sum_out <= 1'b0;
        carry_out <= 1'b0;
    end else begin
        sum_out <= result[0];
        carry_out <= result[1];
    end
end

endmodule
