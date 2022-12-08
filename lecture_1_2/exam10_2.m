close all;
clear;

m_1 = 276; % kg
m_2 = 271; % kg
% springs
L01 = 102/1000; 
k1 = 260000;

L02 = 112/1000; 
k2 = 240000;

L03 = 120/1000; 
k3 = 220000;

% dampers
b1 = 5000;
b2 = 5000;
b3 = 4000;

% lengths
h0 = 1330/1000;
h1 = 472/1000;
h2 = 432/1000;

% initial values
x_1 = 75/1000;
xDot_1 = 0;

x_2 = 712/1000;
xDot_2 = 0;

t = 0;
tEnd = 5; % s
tDelta = 1e-5;


datapoints_size = ceil(tEnd/tDelta);
tPlot = zeros(datapoints_size, 1);
x_1Plot = zeros(datapoints_size, 1);
xDot_1Plot = zeros(datapoints_size, 1);
xDotDot_1Plot = zeros(datapoints_size, 1);
x_2Plot = zeros(datapoints_size, 1);
xDot_2Plot = zeros(datapoints_size, 1);
xDotDot_2Plot = zeros(datapoints_size, 1);

i = 1;
while t < tEnd
    % forces
    Fk_1 = k1 * x_1;
    Fb_1 = b1 * xDot_1;
    
    Fk_2 = k2 * (x_2 - (h1+x_1));
    Fb_2 = b2 * (xDot_2 - xDot_1);

    Fk_3 = k3 * (h0 - (x_2+h2));
    Fb_3 = b3 * (-xDot_2);
    
    % acceleration
    xDotDot_1 = (Fk_2+Fb_2-(Fk_1+Fb_1))/m_1;
    xDotDot_2 = (Fk_3+Fb_3-(Fk_2+Fb_2))/m_2;
  

    % integrals
    xDot_1 = xDot_1 + xDotDot_1*tDelta;
    x_1 = x_1 + xDot_1*tDelta;
    xDot_2 = xDot_2 + xDotDot_2*tDelta;
    x_2 = x_2 + xDot_2*tDelta;

    
    % save values
    tPlot(i) = t;
    x_1Plot(i) = x_1 * 1000; % m to mm
    xDot_1Plot(i) = xDot_1 * 1000;
    x_2Plot(i) = x_2 * 1000; % m to mm


    i = i + 1;
    t = t + tDelta;
end

plot(tPlot, xDot_1Plot)
title(sprintf('max(abs(xDot(t)))=%f', max(abs(xDot_1Plot))));






