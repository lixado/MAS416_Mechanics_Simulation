clc;
close all;
tic;

m1 = 256; % kg

k1 = 220000; % N/m
L01 = 0.115; % m
b1 = 22000; % (N s)/(m sqrt(m))

k2 = 23000; % N/m
L02 = 0.108; % m
b2 = 2000; % (N s)/m

h0 = 0.661; % m
h1 = 0.376; % m 

g = 9.81; % m/s^2

Time = 0;
EndTime = 1.0;
Timestep = 0.0001;
i = 1;
timePlot = zeros(EndTime/Timestep, 1);
xPlot = zeros(EndTime/Timestep, 1);
xDerivativePlot = zeros(EndTime/Timestep, 1);

x = 0.219;
xDerivative = 0;
xDerivativeAbsMax = 0;
while Time < EndTime
    delta1 = x-L01;
    delta1Derivative = xDerivative;
    delta2 = h0-h1-x-L02;
    delta2Derivative = -xDerivative;
    

    Fs1=0;
    Fd1=0;
    if delta1<=0
      Fs1 = k1*delta1;
      Fd1 = b1*sqrt(-delta1)*delta1Derivative;
    end
    Fs2 = k2*delta2;
    Fd2 = b2*delta2Derivative;
    xDoubleDerivative = (Fs2+Fd2-Fs1-Fd1-m1*g)/(m1);
    xDerivative = xDerivative + xDoubleDerivative*Timestep;
    x = x + xDerivative*Timestep;
    
    timePlot(i) = Time;
    xPlot(i) = x*1000;
    xDerivativePlot(i)=xDerivative*1000;
    if abs(xDerivative)>abs(xDerivativeAbsMax)
        xDerivativeAbsMax = abs(xDerivative);
    end    
    i = i + 1;
    Time = Time + Timestep;
end
plot(timePlot,xPlot,'LineWidth',2);
plot(timePlot,xDerivativePlot,'LineWidth',2);