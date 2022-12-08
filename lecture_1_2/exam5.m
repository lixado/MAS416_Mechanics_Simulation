clear;
m_1 = 348; % kg
m_2 = 67; % kg
k = 160000; % N/m
L0 = 113/1000; % 112 mm to m
b = 6000; % N*s/m
theta = 45*(pi/180); % degrees to rad
v01 = 10/1000; % mm to m
mu = 0.3;
g = 9.81;

t = 0;
tEnd = 3;
tDelta = 1e-4;
x = 174/1000; % mm to m
xDot = 0; % m/s
xDotDot = 0;

datapoints_size = ceil(tEnd/tDelta);
tPlot = zeros(datapoints_size, 1);
xPlot = zeros(datapoints_size, 1);
xDotPlot = zeros(datapoints_size, 1);
xDotDotPlot = zeros(datapoints_size, 1);


i = 1;
while t < tEnd
    mu_k = xDot*(mu/v01);
    if  xDot > v01
        mu_k = mu;
    elseif xDot < -v01
        mu_k = -mu;
    end
    F_r = (m_1)*g*cos(theta)*mu_k;

    F_k = k * (L0-x);
    F_b = b * (-xDot) * sqrt((xDot));
    if x > L0
        % then there is no bumber of spring
        F_k = 0;
        F_b = 0;
    end

    F_mg_2 = m_2*g;
    F_g = m_1*g*sin(theta);

    xDotDot = (F_mg_2+F_k+F_b - F_g -F_r)/(m_1+m_2);

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


% 561,2068 (med marginen: 12,6242)