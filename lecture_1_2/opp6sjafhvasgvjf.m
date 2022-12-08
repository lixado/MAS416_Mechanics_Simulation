clear;

% masses
m_1 = 273; % kg
m_2 = 209; % kg
m_3 = 56; % kg
% springs
k_1 = 57000; % N/m
L0_1 = 119/1000; % mm to m
k_2 = 59000; % N/m
L0_2 = 114/1000; % mm to m
% dempers
b_1 = 2000; % Ns/m^1.5
b_2 = 2000; % Ns/m
% others
theta = 60*(pi/180); % degrees to rad
h_1 = 482/1000; % mm to m
g = 9.81;

t = 0;
tEnd = 5;
tDelta = 1e-4;

% state variables
x_1 = 141/1000; % mm to m
x_1Dot = 0; % m/s
x_1DotDot = 0;
x_2 = 802/1000; % mm to m
x_2Dot = 0; % m/s
x_2DotDot = 0;

datapoints_size = ceil(tEnd/tDelta);
tPlot = zeros(datapoints_size, 1);
xPlot = zeros(datapoints_size, 1);
xDotPlot = zeros(datapoints_size, 1);
xDotDotPlot = zeros(datapoints_size, 1);


i = 1;
while t < tEnd
    % forces in m_2
    F_g3 = m_3*g;
    F_g2 = m_2*g*sin(theta);
    k2_delta = (x_2 - (x_1+h_1)) - L0_2;
    F_k2 = k2_delta*k_2;
    b2_delta = x_2Dot - x_1Dot;
    F_b2 = b2_delta*b_2;
    % forces in m_1
    F_g1 = m_1*g*sin(theta);
    F_k1 = 0;
    F_b1 = 0;
    if x_1 < L0_1
        k1_delta = L0_1 - x_1;
        F_k1 = k1_delta*k_1;
        b1_delta = -x_1Dot;
        F_b1 = sqrt(b1_delta)*b1_delta*b_1;
    end
    

    x_1DotDot = (F_k1+F_b1+F_k2+F_b2-F_g1)/(m_1);
    x_1Dot = x_1Dot + x_1DotDot*tDelta;
    x_1 = x_1 + x_1Dot*tDelta;

    x_2DotDot = (F_g3  -(F_k2+F_b2+F_g2))/(m_2+m_3);
    x_2Dot = x_2Dot + x_2DotDot*tDelta;
    x_2 = x_2 + x_2Dot*tDelta;

    tPlot(i) = t;
    xPlot(i) = x_1*1000; % transform back to mm
    xDotPlot(i) = x_1Dot*1000; % transform back to mm
    xDotDotPlot(i) = x_1DotDot*1000; % transform back to mm


    t = t + tDelta;
    i = i + 1;
end

plot(tPlot, xDotPlot)
title(sprintf('max(abs(xDot(t)))=%f', max(abs(xDotPlot))));
figure;

plot(tPlot, xPlot)
title(sprintf('max(x(t))=%f', max(xPlot)));

% 826,8773 (med marginen: 16,5376)

% This is Mechanical System number 15 . m1 = 273 kg . m2 = 209 kg . m3 = 56 kg , k1 = 57000 N/m , Undeformed length of k1, L01 = 119 mm , Nonlinear damper b1 = 2000 Ns/m^1.5 , k2 = 59000 N/m , Undeformed length of k2, L02 = 114 mm , Linear damper b2 = 2000 Ns/m , theta = 60 Degrees , h1 = 482 mm , x1 (initial value) = 141 mm , x1_Dot (initial value) = 0 mm/s , x2 (initial value) = 802 mm , x2_Dot (initial value) = 0 mm/s , simulation time = 5.0 Seconds . What is the maximum absolute value of the velocity [mm/s] of body m1 ?
