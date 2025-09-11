module receiver ( // receives UART signals and packs it into a register
    input logic clk,
    input logic reset,
    input logic uart_rx,
    output logic [63:0] bitstream,
    output logic frame_valid
);

parameter   IDLE = 2'b00, START = 2'b01, READ = 2'b10, STOP = 2'b11; // establishes states for receiver FSM
logic [1:0] state;
logic [2:0] bit_count;

/**
 counter logic for baud rate, 50 MHz/115200 baud = 434 FPGA clocks
 essentially creates one tick every 434 FPGA clocks to properly read incoming UART
 **/
logic tick;
logic [15:0] counter;

always_ff @(posedge clk) begin
    if (reset) begin
        tick <= 0;
        counter <= 0;
    end else if (counter == 434 - 1) begin
        counter <= 0;
        tick <= 1;
    end else begin
        counter <= counter + 1;
        tick <= 0;
    end

always_ff @(posedge clk) begin
    if (reset) begin
        state <= IDLE;
    end else begin
        state <= next_state;
    end

    always_comb begin
        next_state = state;

        case(state)
            IDLE:
                if (tick && uart_rx == 0) begin
                    next_state <= START;
                    bit_count <= 0;
            START:

            READ:

            STOP:
        endcase
end

