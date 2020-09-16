% Plot three 3-d Gaussians
% Edit the values with the ones obtained in the files f1.txt and f2.txt
 figure;
 h1 = plot_gaussian_ellipsoid([ 0.1632, 0.1887, 0.1250], [0.0444,-0.0063,-0.0446; -0.0063, 0.0396,-0.0236; -0.0446,-0.0236, 0.09]');
 h2 = plot_gaussian_ellipsoid([0.3567,-0.0519 ,0.1554], [0.0074, 0.0005,-0.0011; 0.0005, 0.0362,-0.015; -0.0011,-0.015 , 0.0135]');
 h3 = plot_gaussian_ellipsoid([0.2271,0.3144, 0.0258], [ 0.0252,-0.0007,-0.0285; -0.0007, 0.0025,-0.0015;-0.0285,-0.0015, 0.0466]');

 set(h1,'facealpha',0.6);
 view(129,36); set(gca,'proj','perspective'); grid on; 
 grid on; axis equal; axis tight;
 xlabel("X")
 ylabel("Y")
 zlabel("Z")
 hold on;
 
 % Assuming you have imported the reconstructed trajectories in MATLAB as t1,t2 and t3
 plot3(t1(:,1), t1(:,2), t1(:,3), 'linewidth',3);
 hold on;
 plot3(t2(:,1), t2(:,2), t2(:,3),'linewidth',3);
 hold on;
 plot3(t3(:,1), t3(:,2), t3(:,3),'linewidth',3);
