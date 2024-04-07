# Bipdeal Rig Skeleton Generator Version Class 1.0 
# By Quincy Muzik
# App that lets an artist create a custom bipedal rig skeleton via GUI 

import maya.cmds as cmds 

class RigSkeltonGeneratorClass:
    
    # Constructor/GUI Creation
    def __init__(self):
        
        # Variable/Flags for Window 
        self.window = "QM_Window"
        self.title = "Rig Skeleton Generator (Bipedal)"
        self.size = (300,200)
        
        # Closes window if already open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)
        
        # Creates a new window 
        self.win = cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn = True)
        
        # Title for the window
        cmds.text(self.title)
        cmds.separator(height = 20)
        
        # Allows user to enter name of rig skeleton 
        self.rigName = cmds.textFieldGrp(label = "Character Name: ")
        
        # Allows user to choose number of fingers for skeleton (Future Update)
        # cmds.separator(height = 10,style = 'none')
        # self.numOfFingers = cmds.radioButtonGrp( label='Number of Fingers:', labelArray3=['3', '4', '5'], numberOfRadioButtons=3,data1=3,data2=4,data=5)
        
        # Button that will generate skeleton
        cmds.separator(height = 20,style = 'none')
        self.rigCreationButton = cmds.button(label = "Generate Skeleton",recomputeSize = False,command=self.createSkeleton)
        
        # Display the window
        cmds.showWindow(self.win)
    
    # Creates the Rig Skeleton when the button is pressed 
    def createSkeleton(self,*args):
        
        # Resets the Scene 
        cmds.select(all = True)
        cmds.delete()
        
        # Input from UI that is used
        name = cmds.textFieldGrp(self.rigName,query=True,text=True)
        
        # Create Locator to House the Skeleton/Components
        cmds.spaceLocator(name = name,position = (0,-33.5,2))
        
        # Create the Root aka Hips of Skeleton 
        cmds.joint(name="root",p=(0,1,-1.5))

        # Create the Left Leg of Skeleton 
        cmds.joint(name="leftLegHip",p=(3,0,0))
        cmds.joint(name="leftLegUp",p=(6.5,0,0))
        cmds.joint(name="leftLegUpRoll",p=(6.5,-8,1))
        cmds.joint(name="leftLeg",p=(6.5,-16,2))
        cmds.joint(name="leftLegRoll",p=(6.5,-24,1))

        # Create the Left Foot of Skeleton 
        cmds.joint(name="leftFoot",p=(6.5,-30,0))
        cmds.joint(name="leftFootToeBase",p=(6.5,-33,3.75))
        cmds.joint(name="leftFootToeEnd",p=(6.5,-33.5,9.5))

        # Create the Right Leg of Skeleton
        cmds.select("root")
        cmds.joint(name="rightLegHip",p=(-3,0,0))
        cmds.joint(name="rightLegUp",p=(-6.5,0,0))
        cmds.joint(name="rightLegUpRoll",p=(-6.5,-8,1))
        cmds.joint(name="rightLeg",p=(-6.5,-16,2))
        cmds.joint(name="rightLegRoll",p=(-6.5,-24,1))

        # Create the Right Foot of Skeleton 
        cmds.joint(name="rightFoot",p=(-6.5,-30,0))
        cmds.joint(name="rightFootToeBase",p=(-6.5,-33,3.75))
        cmds.joint(name="rightFootToeEnd",p=(-6.5,-33.5,9.5))

        # Create the Spine of the skeleton 
        cmds.select("root")
        cmds.joint(name="spinePlaceHolder",p=(0,5,0))
        cmds.joint(name="spine",p=(0,10,0))
        cmds.joint(name="spine1",p=(0,15,0))
        cmds.joint(name="spine2",p=(0,20,0))

        # Create the Head/Neck of Skeleton
        cmds.joint(name="neck",p=(0,27,0))
        cmds.joint(name="head",p=(0,32,0.8))
        cmds.joint(name="headTop",p=(0,39,1.8))

        # Create the Left Arm of Skeleton 
        cmds.select("spine2")
        cmds.joint(name="leftShoulderPlaceHolder",p=(1.6,24,0))
        cmds.joint(name="leftShoulder",p=(2,26,0))
        cmds.joint(name="leftArmPlaceHolder",p=(6,25.25,0))
        cmds.joint(name="leftArm",p=(8,24.75,0))
        cmds.joint(name="leftArmRoll",p=(13,24.75,0))
        cmds.joint(name="leftArmForearm",p=(18,24.75,0))
        cmds.joint(name="leftArmForearmRoll",p=(23,24.75,0))

        # Create the Left Hand
        cmds.joint(name="leftHand",p=(28,24.75,0))

        # Create the Left Hand Fingers of Skeleton 
        # Create the Left Hand Thumb 
        cmds.joint(name="leftHandThumb1",p=(30.5,24.75,-2))
        cmds.joint(name="leftHandThumb2",p=(31.75,24.75,-2.5))
        cmds.joint(name="leftHandThumb3",p=(33,24.75,-2.75))
        cmds.joint(name="leftHandThumb4",p=(34.25,24.75,-2.85))
        
        
        # Create the Left Hand Pointer Finger
        cmds.select("leftHand")
        cmds.joint(name="leftHandPointer1",p=(32,24.75,-0.90))
        cmds.joint(name="leftHandPointer2",p=(34.5,24.75,-0.90))
        cmds.joint(name="leftHandPointer3",p=(36.5,24.75,-0.90))
        cmds.joint(name="leftHandPointer4",p=(38,24.75,-0.90))
        
        
        # Create the Left Hand Middle Finger
        cmds.select("leftHand")
        cmds.joint(name="leftHandMiddle1",p=(32.5,24.75,0.2))
        cmds.joint(name="leftHandMiddle2",p=(35,24.75,0.2))
        cmds.joint(name="leftHandMiddle3",p=(37,24.75,0.2))
        cmds.joint(name="leftHandMiddle4",p=(38.5,24.75,0.2))

        # Create the Left Hand Ring Finger
        cmds.select("leftHand")
        cmds.joint(name="leftHandRing1",p=(32,24.75,1.35))
        cmds.joint(name="leftHandRing2",p=(34.5,24.75,1.35))
        cmds.joint(name="leftHandRing3",p=(36.5,24.75,1.35))
        cmds.joint(name="leftHandRing4",p=(38,24.75,1.35))

        # Create the Left Hand Pinky Finger
        cmds.select("leftHand")
        cmds.joint(name="leftHandPinky1",p=(31.5,24.75,2.5))
        cmds.joint(name="leftHandPinky2",p=(33.4,24.75,2.5))
        cmds.joint(name="leftHandPinky3",p=(35.2,24.75,2.5))
        cmds.joint(name="leftHandPinky4",p=(36.7,24.75,2.5))

        # Rotate the Hand 180 Degrees 
        cmds.select("leftHand")
        cmds.rotate(180)

        # Create the Right Arm of Skeleton
        cmds.select("spine2")
        cmds.joint(name="rightShoulderPlaceHolder",p=(-1.6,24,0))
        cmds.joint(name="rightShoulder",p=(-2,26,0))
        cmds.joint(name="rightArmPlaceHolder",p=(-6,25.25,0))
        cmds.joint(name="rightArm",p=(-8,24.75,0))
        cmds.joint(name="rightArmRoll",p=(-13,24.75,0))
        cmds.joint(name="rightArmForearm",p=(-18,24.75,0))
        cmds.joint(name="rightArmForearmRoll",p=(-23,24.75,0))

        # Create the Right Hand
        cmds.joint(name="rightHand",p=(-28,24.75,0))

        # Create the Right Hand Fingers of Skeleton 
        # Create the Right Hand Thumb 
        cmds.joint(name="rightHandThumb1",p=(-30.5,24.75,2))
        cmds.joint(name="rightHandThumb2",p=(-31.75,24.75,2.5))
        cmds.joint(name="rightHandThumb3",p=(-33,24.75,2.75))
        cmds.joint(name="rightHandThumb4",p=(-34.25,24.75,2.85))

        # Create the Right Hand Pointer Finger
        cmds.select("rightHand")
        cmds.joint(name="rightHandPointer1",p=(-32,24.75,0.90))
        cmds.joint(name="rightHandPointer2",p=(-34.5,24.75,0.90))
        cmds.joint(name="rightHandPointer3",p=(-36.5,24.75,0.90))
        cmds.joint(name="rightHandPointer4",p=(-38,24.75,0.90))

        # Create the Right Hand Middle Finger
        cmds.select("rightHand")
        cmds.joint(name="rightHandMiddle1",p=(-32.5,24.75,-0.2))
        cmds.joint(name="rightHandMiddle2",p=(-35,24.75,-0.2))
        cmds.joint(name="rightHandMiddle3",p=(-37,24.75,-0.2))
        cmds.joint(name="rightHandMiddle4",p=(-38.5,24.75,-0.2))

        # Create the Right Hand Ring Finger
        cmds.select("rightHand")
        cmds.joint(name="rightHandRing1",p=(-32,24.75,-1.35))
        cmds.joint(name="rightHandRing2",p=(-34.5,24.75,-1.35))
        cmds.joint(name="rightHandRing3",p=(-36.5,24.75,-1.35))
        cmds.joint(name="rightHandRing4",p=(-38,24.75,-1.35))

        # Create the Right Hand Pinky Finger
        cmds.select("rightHand")
        cmds.joint(name="rightHandPinky1",p=(-31.5,24.75,-2.5))
        cmds.joint(name="rightHandPinky2",p=(-33.4,24.75,-2.5))
        cmds.joint(name="rightHandPinky3",p=(-35.2,24.75,-2.5))
        cmds.joint(name="rightHandPinky4",p=(-36.7,24.75,-2.5))
        
        # Exits the Tool the skeleton has been created
        cmds.deleteUI(self.window, window=True)

# Main method    
RigSkeltonGeneratorClass()

# TODO 
    # GET FEEDBACK FROM ZOE AND JESSE:
    # Implement Figner Selection (Future Update)
    # Add Constraints, IKs, and NURB Controls  
    # Insert Mesh for Skinning (FEEDBACK First) 