
import pickle
import cv2
import numpy as np
np.set_printoptions(suppress=True)


with open("intention_application/src/handeyecalibration/aruco", "rb") as fp:   # Unpickling
    aruco = pickle.load(fp)
    
with open("intention_application/src/handeyecalibration/poses", "rb") as fp:   # Unpickling
    poses = pickle.load(fp)

moveit2tf=np.load("intention_application/src/handeyecalibration/moveit2tf.npy")

def calibrate_eye_hand(R_gripper2base, t_gripper2base, R_target2cam, t_target2cam, eye_to_hand=True):

    if eye_to_hand:
        # change coordinates from gripper2base to base2gripper
        R_base2gripper, t_base2gripper = [], []

        for R, t in zip(R_gripper2base, t_gripper2base):
            R_b2g = R.T
            t_b2g = -R_b2g @ t
            R_base2gripper.append(R_b2g)
            t_base2gripper.append(t_b2g)
        
        # change parameters values
        R_gripper2base = R_base2gripper
        t_gripper2base = t_base2gripper
    calibration_method = [
        cv2.CALIB_HAND_EYE_TSAI,
        cv2.CALIB_HAND_EYE_PARK,
        cv2.CALIB_HAND_EYE_HORAUD,
        cv2.CALIB_HAND_EYE_ANDREFF,
        cv2.CALIB_HAND_EYE_DANIILIDIS
    ]
    # calibrate
    R, t = cv2.calibrateHandEye(
        R_gripper2base=R_gripper2base,
        t_gripper2base=t_gripper2base,
        R_target2cam=R_target2cam,
        t_target2cam=t_target2cam,
          method=calibration_method[0]  )

    return R, t


def seperator(list,ttt):
    R=[]
    T=[]

    for i in range(len(list)):

        pose=list[i]
        if ttt== True:
            pose=np.linalg.inv(pose)
        #pose=np.matmul(moveit2tf,pose)    
            print(pose)

        I = np.eye(4)

        r=pose[:3, :3]
        t=pose[:3, 3]
        if not (np.all(np.equal(pose, I))):
            R.append(r)
            T.append(t)

            print("")
            print(pose)

            print("")

            print(r)
            print("")

            print(t)
    return R,T



R_target2cam,t_target2cam=seperator(aruco,False)
R_gripper2base,t_gripper2base=seperator(poses,True)




R, t=calibrate_eye_hand(R_gripper2base,t_gripper2base,R_target2cam,t_target2cam,eye_to_hand=True)


print(R,t)
print(np.linalg.norm(t))

np.save("intention_application/src/handeyecalibration/rotation.npy",R)
np.save("intention_application/src/handeyecalibration/translation.npy",t)


