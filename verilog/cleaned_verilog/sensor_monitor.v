module sensor_monitor(
    input [7:0] moisture_level,
    input [7:0] temp_IR,
    output reg moisture_alert,
    output reg temp_alert
);

always @(*) begin
    moisture_alert = (moisture_level < 8'd20);
    temp_alert     = (temp_IR > 8'd75);
end

endmodule

