`timescale 1ns/1ps

module watchdog_tb;

reg clk;
reg reset;
reg heartbeat;
wire system_reset;

watchdog uut (
    .clk(clk),
    .reset(reset),
    .heartbeat(heartbeat),
    .system_reset(system_reset)
);

// Clock generation
initial begin
    clk = 0;
    forever #5 clk = ~clk; // 100 MHz clock
end

// Test scenario
initial begin
    $dumpfile("watchdog_tb.vcd");
    $dumpvars(0, watchdog_tb);

    reset = 1; heartbeat = 0; #20;
    reset = 0;

    repeat (5) begin
        heartbeat = 1; #10;
        heartbeat = 0; #999990;
    end

    heartbeat = 0; #20000000;

    $finish;
end

endmodule

