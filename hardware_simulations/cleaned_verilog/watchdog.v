module watchdog(
    input clk,
    input reset,
    input heartbeat,
    output reg system_reset
);

reg [23:0] counter;

always @(posedge clk or posedge reset) begin
    if (reset) begin
        counter <= 0;
        system_reset <= 0;
    end else if (heartbeat) begin
        counter <= 0;
        system_reset <= 0;
    end else begin
        counter <= counter + 1;
        if (counter >= 24'd10000000)
            system_reset <= 1;
    end
end

endmodule

