# Rig Skeleton Generator Version Class 1.0 
# By Quincy Muzik
# App that lets an artist create a custom bipedal rig skeleton via GUI 

import maya.cmds as cmds 

class RigSkeltonGeneratorClass:
    
    # Constructor/GUI Creation
    def __init__(self):
        
        self.window = "QM_Window"
        self.title = "Rig Skeleton Generator (Bipedal)"
        self.size = (400,200)
        
        # Closes window if already open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)

        # Createes a new window 
        self.win = cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn = True)
        
        # Title for the window
        cmds.text(self.title)
        cmds.separator(height = 20)
        
        # Allows user to enter name of rig skeleton 
        self.rigName = cmds.textFieldGrp(label = "Character Name: ")
        
        # Button that will generate skeleton
        cmds.separator(height = 20,style = 'none')
        self.rigCreationButton = cmds.button(label = "Create Rig",command=self.createSkeleton)
        
        # Display the window
        cmds.showWindow(self.win)
    
    # Creates the Rig Skeleton when the button is pressed 
    def createSkeleton(self,*args):
    
        # Input from UI that is used
        name = cmds.textFieldGrp(self.rigName,query=True,text=True)
        
        # Create Locator/Reference to House the Skeleton/Components
        reference = cmds.spaceLocator(name = name,position = (0,-33.5,2))
        
        # Create the Root aka Hips of Skeleton 
        pelvis = cmds.joint(name="pelvis",p=(0,1,-1.5))

        # Create the Left Leg of Skeleton 
        leftLegHip = cmds.joint(name="leftLegHip",p=(3,0,0))
        leftLegUp = cmds.joint(name="leftLegUp",p=(6.5,0,0))
        leftLegUpRoll = cmds.joint(name="leftLegUpRoll",p=(6.5,-8,1))
        leftLeg = cmds.joint(name="leftLeg",p=(6.5,-16,2))
        leftLegRoll = cmds.joint(name="leftLegRoll",p=(6.5,-24,1))

        # Create the Left Foot of Skeleton 
        leftFoot = cmds.joint(name="leftFoot",p=(6.5,-30,0))
        leftFootToeBase = cmds.joint(name="leftFootToeBase",p=(6.5,-33,3.75))
        leftFootToeEnd = cmds.joint(name="leftFootToeEnd",p=(6.5,-33.5,9.5))

        # Create the Right Leg of Skeleton
        cmds.select("pelvis")
        rightLegHip = cmds.joint(name="rightLegHip",p=(-3,0,0))
        rightLegUp = cmds.joint(name="rightLegUp",p=(-6.5,0,0))
        rightLegUpRoll = cmds.joint(name="rightLegUpRoll",p=(-6.5,-8,1))
        rightLeg = cmds.joint(name="rightLeg",p=(-6.5,-16,2))
        rightLegRoll = cmds.joint(name="rightLegRoll",p=(-6.5,-24,1))

        # Create the Right Foot of Skeleton 
        rightFoot = cmds.joint(name="rightFoot",p=(-6.5,-30,0))
        rightFootToeBase = cmds.joint(name="rightFootToeBase",p=(-6.5,-33,3.75))
        rightFootToeEnd = cmds.joint(name="rightFootToeEnd",p=(-6.5,-33.5,9.5))

        # Create the Spine of the skeleton 
        cmds.select("pelvis")
        spinePlaceHolder = cmds.joint(name="spinePlaceHolder",p=(0,5,0))
        spine = cmds.joint(name="spine",p=(0,10,0))
        spine1 = cmds.joint(name="spine1",p=(0,15,0))
        spine2 = cmds.joint(name="spine2",p=(0,20,0))

        # Create the Head/Neck of Skeleton
        neck = cmds.joint(name="neck",p=(0,27,0))
        head = cmds.joint(name="head",p=(0,32,0.8))
        headTop = cmds.joint(name="headTop",p=(0,39,1.8))

        # Create the Left Arm of Skeleton 
        cmds.select("spine2")
        leftShoulderPlaceHolder = cmds.joint(name="leftShoulderPlaceHolder",p=(1.6,24,0))
        leftShoulder = cmds.joint(name="leftShoulder",p=(2,26,0))
        leftArmPlaceHolder = cmds.joint(name="leftArmPlaceHolder",p=(6,25.25,0))
        leftArm = cmds.joint(name="leftArm",p=(8,24.75,0))
        leftArmRoll = cmds.joint(name="leftArmRoll",p=(13,24.75,0))
        leftArmForearm = cmds.joint(name="leftArmForearm",p=(18,24.75,0))
        leftArmForearmRoll = cmds.joint(name="leftArmForearmRoll",p=(23,24.75,0))

        # Create the Left Hand
        leftHand = cmds.joint(name="leftHand",p=(28,24.75,0))

        # Create the Left Hand Fingers of Skeleton 
        # Create the Left Hand Thumb 
        leftHandThumb1 = cmds.joint(name="leftHandThumb1",p=(30.5,24.75,-2))
        leftHandThumb2 = cmds.joint(name="leftHandThumb2",p=(31.75,24.75,-2.5))
        leftHandThumb3 = cmds.joint(name="leftHandThumb3",p=(33,24.75,-2.75))
        leftHandThumb4 = cmds.joint(name="leftHandThumb4",p=(34.25,24.75,-2.85))
        
        
        # Create the Left Hand Pointer Finger
        cmds.select("leftHand")
        leftHandPointer1 = cmds.joint(name="leftHandPointer1",p=(32,24.75,-0.90))
        leftHandPointer2 = cmds.joint(name="leftHandPointer2",p=(34.5,24.75,-0.90))
        leftHandPointer3 = cmds.joint(name="leftHandPointer3",p=(36.5,24.75,-0.90))
        leftHandPointer4 = cmds.joint(name="leftHandPointer4",p=(38,24.75,-0.90))
        
        
        # Create the Left Hand Middle Finger
        cmds.select("leftHand")
        leftHandMiddle1 = cmds.joint(name="leftHandMiddle1",p=(32.5,24.75,0.2))
        leftHandMiddle2 = cmds.joint(name="leftHandMiddle2",p=(35,24.75,0.2))
        leftHandMiddle3 = cmds.joint(name="leftHandMiddle3",p=(37,24.75,0.2))
        leftHandMiddle4 = cmds.joint(name="leftHandMiddle4",p=(38.5,24.75,0.2))

        # Create the Left Hand Ring Finger
        cmds.select("leftHand")
        leftHandRing1 = cmds.joint(name="leftHandRing1",p=(32,24.75,1.35))
        leftHandRing2 = cmds.joint(name="leftHandRing2",p=(34.5,24.75,1.35))
        leftHandRing3 = cmds.joint(name="leftHandRing3",p=(36.5,24.75,1.35))
        leftHandRing4 = cmds.joint(name="leftHandRing4",p=(38,24.75,1.35))

        # Create the Left Hand Pinky Finger
        cmds.select("leftHand")
        leftHandPinky1 = cmds.joint(name="leftHandPinky1",p=(31.5,24.75,2.5))
        leftHandPinky2 = cmds.joint(name="leftHandPinky2",p=(33.4,24.75,2.5))
        leftHandPinky3 = cmds.joint(name="leftHandPinky3",p=(35.2,24.75,2.5))
        leftHandPinky4 = cmds.joint(name="leftHandPinky4",p=(36.7,24.75,2.5))

        # Rotate the Hand 180 Degrees 
        cmds.select("leftHand")
        cmds.rotate(180)

        # Create the Right Arm of Skeleton
        cmds.select("spine2")
        rightShoulderPlaceHolder = cmds.joint(name="rightShoulderPlaceHolder",p=(-1.6,24,0))
        rightShoulder = cmds.joint(name="rightShoulder",p=(-2,26,0))
        rightArmPlaceHolder = cmds.joint(name="rightArmPlaceHolder",p=(-6,25.25,0))
        rightArm = cmds.joint(name="rightArm",p=(-8,24.75,0))
        rightArmRoll = cmds.joint(name="rightArmRoll",p=(-13,24.75,0))
        rightArmForearm = cmds.joint(name="rightArmForearm",p=(-18,24.75,0))
        rightArmForearmRoll = cmds.joint(name="rightArmForearmRoll",p=(-23,24.75,0))

        # Create the Right Hand
        rightHand = cmds.joint(name="rightHand",p=(-28,24.75,0))

        # Create the Right Hand Fingers of Skeleton 
        # Create the Right Hand Thumb 
        rightHandThumb1 = cmds.joint(name="rightHandThumb1",p=(-30.5,24.75,2))
        rightHandThumb2 = cmds.joint(name="rightHandThumb2",p=(-31.75,24.75,2.5))
        rightHandThumb3 = cmds.joint(name="rightHandThumb3",p=(-33,24.75,2.75))
        rightHandThumb4 = cmds.joint(name="rightHandThumb4",p=(-34.25,24.75,2.85))

        # Create the Right Hand Pointer Finger
        cmds.select("rightHand")
        rightHandPointer1 = cmds.joint(name="rightHandPointer1",p=(-32,24.75,0.90))
        rightHandPointer2 = cmds.joint(name="rightHandPointer2",p=(-34.5,24.75,0.90))
        rightHandPointer3 = cmds.joint(name="rightHandPointer3",p=(-36.5,24.75,0.90))
        rightHandPointer4 = cmds.joint(name="rightHandPointer4",p=(-38,24.75,0.90))

        # Create the Right Hand Middle Finger
        cmds.select("rightHand")
        rightHandMiddle1 = cmds.joint(name="rightHandMiddle1",p=(-32.5,24.75,-0.2))
        rightHandMiddle2 = cmds.joint(name="rightHandMiddle2",p=(-35,24.75,-0.2))
        rightHandMiddle3 = cmds.joint(name="rightHandMiddle3",p=(-37,24.75,-0.2))
        rightHandMiddle4 = cmds.joint(name="rightHandMiddle4",p=(-38.5,24.75,-0.2))

        # Create the Right Hand Ring Finger
        cmds.select("rightHand")
        rightHandRing1 = cmds.joint(name="rightHandRing1",p=(-32,24.75,-1.35))
        rightHandRing2 = cmds.joint(name="rightHandRing2",p=(-34.5,24.75,-1.35))
        rightHandRing3 = cmds.joint(name="rightHandRing3",p=(-36.5,24.75,-1.35))
        rightHandRing4 = cmds.joint(name="rightHandRing4",p=(-38,24.75,-1.35))

        # Create the Right Hand Pinky Finger
        cmds.select("rightHand")
        rightHandPinky1 = cmds.joint(name="rightHandPinky1",p=(-31.5,24.75,-2.5))
        rightHandPinky2 = cmds.joint(name="rightHandPinky2",p=(-33.4,24.75,-2.5))
        rightHandPinky3 = cmds.joint(name="rightHandPinky3",p=(-35.2,24.75,-2.5))
        rightHandPinky4 = cmds.joint(name="rightHandPinky4",p=(-36.7,24.75,-2.5))
        
        # Exits the Tool the skeleton has been created
        cmds.deleteUI(self.window, window=True)
        
RigSkeltonGeneratorClass()