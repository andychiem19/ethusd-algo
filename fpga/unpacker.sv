module unpacker ( // unpacks received register into its consituent parts
    input logic [63:0] bitstream,
    output logic [31:0] lastprice,
    output logic [31:0] vol24h
);

    assign lastprice = bitstream[63:32];
    assign vol24h = bitstream[31:0];

endmodule