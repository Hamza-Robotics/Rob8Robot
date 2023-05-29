'''

from TF
frame_id: "base"
    child_frame_id: "tool0_controller"
    transform: 
      translation: 
        x: -0.47208351969002543
        y: -0.5231516471120154
        z: 0.38867053632656856
      rotation: 
        x: 0.42607546281101827
        y: -0.9014509157637207
        z: -0.021605042038429497
        w: 0.07334281571935719
0.4467232379875198--0.47208351969002543
0.5212845413454835--0.5231516471120154
From Moveit
    position: 
    x: 0.4467232379875198
    y: 0.5212845413454835
    z: 0.6491182727381901
  orientation: 
    x: 0.9046876658998029
    y: 0.41902205572424694
    z: 0.07343985460570611
    w: 0.023818726684806283


'''
import numpy as np
from tf.transformations import quaternion_matrix

from tf.transformations import quaternion_matrix, quaternion_from_matrix

rotation1 = np.array([0.42607546281101827, -0.9014509157637207, -0.021605042038429497, 0.07334281571935719])
rotation2 = np.array([0.9046876658998029, 0.41902205572424694, 0.07343985460570611, 0.023818726684806283])

R1=quaternion_matrix(rotation1)
R1[0][3]= 0.4467232379875198
R1[1][3]= 0.5212845413454835
R1[2][3]= 0.6491182727381901

R2=quaternion_matrix(rotation2)
R2[0][3]=-0.47208351969002543
R2[1][3]= -0.5231516471120154
R2[2][3]=0.38867053632656856

B2T=R1
B2M=R2
# Calculate the rotation matrix between the two transformations



Transform = np.matmul(R2, np.linalg.inv(R1))
matrix = R1


print(np.matmul(np.linalg.inv(Transform),B2M))


np.save("intention_application/src/handeyecalibration/moveit2tf.npy",np.linalg.inv(Transform))
np.save("intention_application/src/handeyecalibration/tf2moveit.npy",(Transform))
