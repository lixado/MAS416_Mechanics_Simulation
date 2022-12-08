close all;
clear;

R1 = 800; % ohm
R2 = 1500; % ohm
R3 = 1500; % ohm
C1 = 9; % microFarad
C2 = 310; % microFarad
t_RU1 = 0.7; % seconds
U_s1max = 15; % volt
C_1 = 0; % volt
C_2 = 0;
t = 0;
tEnd = 3.8; % s
tDelta = 1e-5;

datapoints_size = ceil(tEnd/tDelta);
tPlot = zeros(datapoints_size, 1);
i_3Plot = zeros(datapoints_size, 1);

i = 1;
while t < tEnd
    %Supply voltage
    Us = U_s1max;
    if t < t_RU1
        Us = U_s1max*t/t_RU1;
    end

    % currents
    i1 = (Us-C_1)/R1; % first resistor current
    i2 = (C_1-C_2)/R2;
    i3 = (C_2)/R3;

    
    % acceleration

  

    % integrals

    
    % save values
    tPlot(i) = t;


    i = i + 1;
    t = t + tDelta;
end

plot(tPlot, xDot_1Plot)
title(sprintf('max(abs(xDot(t)))=%f', max(abs(xDot_1Plot))));