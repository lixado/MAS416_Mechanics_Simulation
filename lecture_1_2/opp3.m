close all;
clear;

L = 0.7; % m
m = 24; % kg
g = 9.81; % m/s**2

t = 0; % s
phi = 45*(pi/180); % 45 degrees to rad
phiDot = 2; % rad/s
phiDotDot = 0; % rad/s**2
tEnd = 8; % s
tDelta = 1e-5;

datapoints_size = ceil(tEnd/tDelta);
tPlot = zeros(datapoints_size, 1);
phiPlot = zeros(datapoints_size, 1);
phiDotPlot = zeros(datapoints_size, 1);
phiDotDotPlot = zeros(datapoints_size, 1);

i = 1;
while t < tEnd
    phiDotDot = - (g/L) * sin(phi);

    % add to arrays
    tPlot(i) = t;
    phiPlot(i) = phi * (180/pi); % in degrees
    phiDotPlot(i) = phiDot * (180/pi);
    phiDotDotPlot(i) = phiDotDot * (180/pi);

    % integrations
    phiDot = phiDot + phiDotDot*tDelta;
    phi = phi + phiDot*tDelta;
 
    
    t = t + tDelta;
    i = i + 1; % update counter to use arrays
end

figure;
plot(tPlot, phiPlot);
grid;