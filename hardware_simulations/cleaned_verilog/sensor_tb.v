`timescale 1ns/1ps

module sensor_tb;

reg [7:0] moisture_level;
reg [7:0] temp_IR;
wire moisture_alert;
wire temp_alert;

sensor_monitor uut (
    .moisture_level(moisture_level),
    .temp_IR(temp_IR),
    .moisture_alert(moisture_alert),
    .temp_alert(temp_alert)
);

initial begin
    $dumpfile("sensor_tb.vcd");
    $dumpvars(0, sensor_tb);

    moisture_level = 8'd50; temp_IR = 8'd60; #10;
    moisture_level = 8'd10; temp_IR = 8'd60; #10;
    moisture_level = 8'd50; temp_IR = 8'd80; #10;
    moisture_level = 8'd10; temp_IR = 8'd80; #10;

    $finish;
end

endmodule

