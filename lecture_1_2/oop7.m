m_1 = 2000; % kg
m_2 = 400; % kg
L = 500/1000; % mm to m
k = 100*1000; % kN/m to N/m
b = 1500; % N*s/m
h = 800/1000; % mm to m
h0 = 3100/1000; % mm to m
g = -9.81; % m/s**2

t = 0;
tEnd = 5; % s
tDelta = 1e-5;
x_1 = 500/1000; % mm to m
xDot_1 = 0;
xDotDot_1 = 0;
x_2 = 1800/1000; % mm to m
xDot_2 = 0;
xDotDot_2 = 0;

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
    Fg_1 = g * m_1;
    Fk_1 = k * x_1;
    Fb_1 = b * xDot_1;
    Fk_2 = k * (x_2 - (h+x_1));
    Fb_2 = b * (xDot_2 - xDot_1);

    Fk_3 = k * (h0 - (x_2+h));
    Fb_3 = b * (-xDot_2);
    Fg_2 = g * m_2;
    
    % acceleration
    xDotDot_1 = (Fk_2+Fb_2-(Fg_1+Fk_1+Fb_1))/m_1;
    xDotDot_2 = (Fk_3+Fb_3-(Fg_2+Fk_2+Fb_2))/m_2;
  

    % integrals
    xDot_1 = xDot_1 + xDotDot_1*tDelta;
    x_1 = x_1 + xDot_1*tDelta;
    xDot_2 = xDot_2 + xDotDot_2*tDelta;
    x_2 = x_2 + xDot_2*tDelta;

    
    % save values
    tPlot(i) = t;
    x_1Plot(i) = x_1 * 1000; % m to mm
    x_2Plot(i) = x_2 * 1000; % m to mm


    i = i + 1;
    t = t + tDelta;
end

plot(tPlot, x_1Plot);
hold on
plot(tPlot, x_2Plot);
hold off






