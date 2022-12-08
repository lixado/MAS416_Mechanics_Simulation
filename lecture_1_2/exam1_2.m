m_1 = 278; % kg
m_2 = 235; % kg
k = 6000; % N/m
L0 = 112/1000; % 112 mm to m
b = 0; % N*s/m
theta = 55*(pi/180); % degrees to rad
v = 10/1000; % mm to m
mu = 0.4; 
g = -9.81;

t = 0;
tEnd = 10;
tDelta = 1e-6;
x = 134/1000; % mm to m
xDot = 0; % m/s
xDotDot = 0;

datapoints_size = ceil(tEnd/tDelta);
tPlot = zeros(datapoints_size, 1);
xPlot = zeros(datapoints_size, 1);
xDotPlot = zeros(datapoints_size, 1);
xDotDotPlot = zeros(datapoints_size, 1);


i = 1;
while t < tEnd
    F_g = m_1*g;
    F_k = k * (x - L0);
    F_b = b * (xDot);
    F_mg_2 = m_2 * g;
    F_r = (m_1*cos(theta))*(mu*tanh(xDot/v));

    xDotDot = (F_mg_2+F_r-(F_b+F_k+F_g))/(m_1);
    

    xDot = xDot + xDotDot*tDelta;
    x = x + xDot*tDelta;

    tPlot(i) = t;
    xPlot(i) = x*1000; % transform back to mm
    xDotPlot(i) = xDot*1000; % transform back to mm
    xDotDotPlot(i) = xDotDot*1000; % transform back to mm


    t = t + tDelta;
    i = i + 1;
end

plot(tPlot, xDotPlot)
title(sprintf('max(abs(xDot(t)))=%f', max(abs(xDotPlot))));
figure;

plot(tPlot, xPlot)
title(sprintf('max(x(t))=%f', max(xPlot)));