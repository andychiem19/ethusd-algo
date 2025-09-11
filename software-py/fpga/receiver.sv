module receiver ( // receives UART signals and packs it into a register
    input logic clk,
    input logic reset,
    input logic uart_rx,
    output logic [63:0] bitstream,
    output logic frame_valid
);

parameter   IDLE = 2'b00, 

always_comb begin
