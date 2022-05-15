clc
clear
close all
pkg load io
[a,~,~]=xlsread('HotCell_10th_value_analysis.xlsx');
thickness = a(:,2);
Ir192_activity = 1;4000;4000;
Ho166_activity = 1;300 ;4000/280;
Na24_activity = 1%6.296E+07 /3.7e10;0.25;1/70.264;

Ir192  = a(:,3)*Ir192_activity;
Ho166  = a(:,5)*Ho166_activity;
Na24   = a(:,7)*Na24_activity;

Ir192_ln = log(Ir192);
Ho166_ln  = log(Ho166);
Na24_ln  = log(Na24);

tt = linspace(0,20,40)';
ir192 = exp(spline(thickness,Ir192_ln,tt));
ho166 = exp(spline(thickness,Ho166_ln,tt));
na24 = exp(spline(thickness,Na24_ln,tt));

ir192_rev = spline(Ir192_ln,thickness);
ho166_rev = spline(Ho166_ln,thickness);
na24_rev = spline(Na24_ln,thickness);

figure(1)
%ax(1) = subplot (211);

hold on
plot(tt,ir192,"b-.",tt,ho166,'r-.',tt,na24,'m-.');
Min=min(min([,Ir192,Ho166,Na24]))/10;

%errorbar(thickness,Ir192,Ir192.*a(:,4),'b.');
%errorbar(thickness,Ho166,Ho166.*a(:,6),'r.');

%semilogy(thickness,[Ir192,Ho166],'o')
xlabel('Lead Thickness (cm)')
ylabel('Dose Rate (Sv/hr)')
title( 'Estimated Dose Rate of the Simplified HotCell with 1 Ci Source Activity' )
quiver(interp1(ir192,tt,Ir192(1)/10),Ir192(1)/10,0,-(Ir192(1)/10-Min),'b-->')
quiver(interp1(ho166,tt,ho166(1)/10),ho166(1)/10,0,-(ho166(1)/10-Min),'r-->')
quiver(interp1(na24,tt,na24(1)/10),na24(1)/10,0,-(na24(1)/10-Min),'m-->')

text(interp1(ir192,tt,Ir192(1)/10)+0.02,1E-6, sprintf('TVL-^{192}Ir\n %4.2f cm',interp1(ir192,tt,ir192(1)/10)),"rotation",90,"color", "blue")
text(interp1(ho166,tt,ho166(1)/10)+0.0,1E-8, sprintf('TVL-^{166}Ho\n %4.2f cm',interp1(ho166,tt,ho166(1)/10)),"rotation",90,"color", "red")
text(interp1(na24,tt,na24(1)/10)+0.0,1E-10, sprintf('TVL-^{24}Na\n %4.2f cm',interp1(na24,tt,na24(1)/10)),"rotation",90,"color", "magenta")

set(gca,'YScale','log')
ylim([Min,10*max(max([,Ir192,Ho166,Na24]))])
hold off
% ax = gca;
% %ax.YGrid = 'on';
% ax.YMinorGrid = 'on';
legend({sprintf('^{192}Ir',Ir192_activity),...
sprintf('^{166}Ho',Ho166_activity),...
sprintf('^{24}Na',Na24_activity)})
grid on

%light ();
print ("-r1600", "dose_rate_vs_thinkness.png");

figure(2)
%ax(2) = subplot (212);


semilogy(tt,ir192/max(ir192),'b-.',tt,ho166/max(ho166),'r-.',...
tt,na24/max(na24),'m-.');hold on

xlim([0,7])
ylim([1e-1,1])
%semilogy(thickness,[Ir192,Ho166],'o')
xlabel('Lead Thickness (cm)')
ylabel('Normalized Response')
%yt=set(gca, 'YTick', 0.1:.1:1)

xticklabel=["10%";"100%"];
%set(gca,'xticklabel',xticklabel);
set(gca,'YTickLabel',xticklabel)
title('Normalized Response')
title('Relative Response of Simplified HotCell with Shield Thinkness' )
grid minor
legend({'^{192}Ir','^{166}Ho','^{24}Na'})

hold off
%light ();
print ("-r1600", "TVL_Estimation.png");

fprintf('Ir192 --> 10th value layer is %4.2f mm \n',interp1(ir192,tt,Ir192(1)/10))
fprintf('Ho166 --> 10th value layer is %4.2f mm \n',interp1(ho166,tt,ho166(1)/10))
fprintf('Na24  --> 10th value layer is %4.2f mm \n',interp1(na24,tt,na24(1)/10))

figure(3)

semilogy(tt,ho166./ir192,'r--');hold on
grid on
fprintf("****************************************************\n")
fprintf('Ho166:Ir192 ratio %4.2g times \n',Ho166(end)/Ir192(end))
fprintf(' Na24:Ir192 ratio %4.2g times \n',Na24(end)/Ir192(end))
fprintf(' Na24:Ho166 ratio %4.2g times \n',Na24(end)/Ho166(end))

figure(4)

Ir192_activity = 4000;4000;
Ho166_activity = 22 ;4000/280;
Na24_activity_Ho166 = 0.00256  %6.296E+07 /3.7e10;0.25;1/70.264;
Na24_activity_Ir192 = 0.38

Ir192_Target = Ir192_activity*ir192+Na24_activity_Ir192*na24;
Ho166_Target = Ho166_activity*ho166+Na24_activity_Ho166*na24;
hold on
plot(tt,Ir192_activity*ir192+Na24_activity_Ir192*na24,"b-.",...
     tt,Ho166_activity*ho166+Na24_activity_Ho166*na24,'r-.');
##Min=min(min([,Ir192,Ho166,Na24]))/10;
##Min=min(min([,Ir192,Ho166,Na24]))/10;

%errorbar(thickness,Ir192,Ir192.*a(:,4),'b.');
%errorbar(thickness,Ho166,Ho166.*a(:,6),'r.');

%semilogy(thickness,[Ir192,Ho166],'o')
xlabel('Lead Thickness (cm)')
ylabel('Dose Rate (Sv/hr)')
title( {'Estimated Dose Rate when handling','the Irradiated Tragets (Including the ^{24}Na)'} )
%%quiver(interp1(ir192,tt,Ir192(1)/10),Ir192(1)/10,0,-(Ir192(1)/10-Min),'b-->')
%%quiver(interp1(ho166,tt,ho166(1)/10),ho166(1)/10,0,-(ho166(1)/10-Min),'r-->')
%%quiver(interp1(na24,tt,na24(1)/10),na24(1)/10,0,-(na24(1)/10-Min),'m-->')
%%
%%text(interp1(ir192,tt,Ir192(1)/10)+0.02,1E-6, sprintf('TVL-Ir^{192}\n %4.2f mm',interp1(ir192,tt,ir192(1)/10)),"rotation",90,"color", "blue")
%%text(interp1(ho166,tt,ho166(1)/10)+0.0,1E-8, sprintf('TVL-Ho^{166}\n %4.2f mm',interp1(ho166,tt,ho166(1)/10)),"rotation",90,"color", "red")
%%text(interp1(na24,tt,na24(1)/10)+0.0,1E-10, sprintf('TVL-Na^{24}\n %4.2f mm',interp1(na24,tt,na24(1)/10)),"rotation",90,"color", "magenta")
grid minor

set(gca,'YScale','log')
%% ylim([Min,10*max(max([,Ir192,Ho166,Na24]))])
legend({sprintf("Ir^{192} (%5.1f Ci) + Na^{24} (%.2g Ci)",Ir192_activity,Na24_activity_Ir192),...
sprintf("Ho^{166} (%5.1f Ci) + Na^{24} (%.2g Ci)",Ho166_activity,Na24_activity_Ho166)})

hold off
print ("-r1600", "DoseRate_vs_Tragets_Activities.png");

figure(5)
Ho166_proposed_activites=1:1000;
plot(Ho166_proposed_activites,Ho166_proposed_activites*ho166(end)*1e6+Na24_activity_Ho166*na24(end)*1e6)
hold on
plot(Ho166_proposed_activites,ones(1,length(Ho166_proposed_activites)),"k--")
quiver(260,1,0,-1+1e-6,'r-->')

grid minor
xlabel("^{166}Ho Activity (Ci)")
ylabel("Dose Rate µSv/hr")
hold off
title("^{166}Ho Activity vs Dose Rate")
set(gca,'YScale','log')
set(gca,'XScale','log')
xlim([1,1000])
legend({"Dose Rate from ^{166}Ho","Design Target"})
ylim([1e-2,10])
