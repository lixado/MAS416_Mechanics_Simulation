m_1 = 211; % kg
m_2 = 295; % kg
k = 390000; % N/m
L0 = 114/1000; % 112 mm to m
b = 7000; % N*s/m
theta = 39*(pi/180); % degrees to rad
g = 9.81;

t = 0;
tEnd = 5;
tDelta = 1e-5;
x = 91/1000; % mm to m
xDot = 0; % m/s
xDotDot = 0;

datapoints_size = ceil(tEnd/tDelta);
tPlot = zeros(datapoints_size, 1);
xPlot = zeros(datapoints_size, 1);
xDotPlot = zeros(datapoints_size, 1);
xDotDotPlot = zeros(datapoints_size, 1);


i = 1;
while t < tEnd
    F_mg_2 = m_2*g;
    F_g = m_1*g*sin(theta);
    F_k = k * (L0-x);
    F_b = b * (-xDot);

    xDotDot = (F_k+F_b+F_mg_2-F_g)/(m_1+m_2);

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


% 465,6032 (med marginen: 9,3121)