module arbiter ( // makes a decision based on unpacked values and returns a signal
    input logic [31:0] lastprice,
    input logic [31:0] vol24h,
    output bit decision
);

always_comb begin
    if (lastprice < 32'd5000) // if last ETHUSD price was less than 5000
        decision = 1; // map this to making an led green
    else
        decision = 0;
    end
endmodule