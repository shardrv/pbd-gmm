% Plot three 3-d Gaussians
 figure;
 h1 = plot_gaussian_ellipsoid([ 0.1632, 0.1887, 0.1250], [0.0444,-0.0063,-0.0446; -0.0063, 0.0396,-0.0236; -0.0446,-0.0236, 0.09]');
 h2 = plot_gaussian_ellipsoid([0.3567,-0.0519 ,0.1554], [0.0074, 0.0005,-0.0011; 0.0005, 0.0362,-0.015; -0.0011,-0.015 , 0.0135]');
 h3 = plot_gaussian_ellipsoid([0.2271,0.3144, 0.0258], [ 0.0252,-0.0007,-0.0285; -0.0007, 0.0025,-0.0015;-0.0285,-0.0015, 0.0466]');

 %h1 = plot_gaussian_ellipsoid([7.88e-01 -2.51e-01 -6.08e-02], [1.84e-04  1.43e-04  8.80e-05; 1.43e-04  2.28e-04  3.15e-04; 8.80e-05  3.15e-04  8.66e-04]);
 %h2 = plot_gaussian_ellipsoid([4.37e-01 -1.37e-01  1.61e-01], [7.82e-03  9.17e-03  2.66e-03; 9.17e-03  1.35e-01  1.87e-02; 2.66e-03  1.87e-02  1.02e-02]);
 %h3 = plot_gaussian_ellipsoid([7.56e-01 -2.08e-01  6.55e-02], [1.40e-02  4.60e-03  4.89e-04; 4.60e-03  2.38e-02  6.79e-03; 4.89e-04  6.79e-03  6.95e-03]);
 set(h1,'facealpha',0.6);
 view(129,36); set(gca,'proj','perspective'); grid on; 
 grid on; axis equal; axis tight;
 xlabel("X")
 ylabel("Y")
 zlabel("Z")
 hold on;
 
 plot3(t1(:,1), t1(:,2), t1(:,3), 'linewidth',3);
 hold on;
 plot3(t2(:,1), t2(:,2), t2(:,3),'linewidth',3);
 hold on;
 plot3(t3(:,1), t3(:,2), t3(:,3),'linewidth',3);