###-------------------------------###
#   HT Helper V0.8 - Logrythmic24   #
###-------------------------------###

#This tool is used to create commands for Hatenatool by Pbsds
#Kinda pointless but its meant to be a simple skill test project 
#Hatenatools link: 


#cool art!!
print("""
██╗  ██╗████████╗    ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
██║  ██║╚══██╔══╝    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
███████║   ██║       ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
██╔══██║   ██║       ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║   ██║       ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                     
HT Helper by Logrythmic24 
Version: 0.8A

This tool is to help create commands for Hatenatools by Pbsds
HT HELPER WILL NOT PROCESS FILES 


                                                                    
                                                                     """)


#set each mode to false to begin
htPPM = False
htUGO = False
htNTFT = False

#Get inputs from user
pyVer = "python"
fileType = input("Resource File Type: ")

#strip the "." if it was added by the user - This is just to keep the below supported file type list smaller
fileType = fileType.lstrip(".")

#Decide what switches should be displayed and set htScript based on file type - Prepare for IF Statment nightmare! 
#-----------PPM---------------------------------------------------
if fileType.lower() in ["ppm", "flipnote"]:
    print("Flipnote PPM File")
    print("")
    print("-t: Extracts the thumbnail to the file <Output>")
    print("-f: Extracts the frame(s) to <Output>")
    print("-s: Dumps the sound files to the folder <Output>")
    print("-S: Same as mode -s, but will also dump the raw sound data files")
    print("-e: Exports the flipnote to an MKV with minimal transcoding")
    print("-E: Same as -e, but will encode the video as lossless H.265")
    print("-m: Prints out the metadata. Can also write it to <output> which also") #This was before I learned about the """ trick
    print(" supports unicode charactes.")
    print("""
                 
          """)
    htScript = "PPM.py"
    htFlag = input("Mode: ")
    if "-" not in htFlag:
        htFlag = "-" + htFlag #make sure that the - is in front of the mode
    else:
        pass
    htPPM = True
#---------------UGO-----------------------------------------------
elif fileType.lower() in ["ugo", "ugoxml"]:
    print("""UGOMenu File
          
    Convert UGO files to UGOXML or the other way around.
    When converting UGO to UGOXML any embeded files will go to a folder named 
    "UGOXML-[Filename] Embeded"
          
    Please include file extentions in your name in/outputs!
    
          
          """)
    htScript = "UGO.py"
    htUGO = True
#---------------NTFT----------------------------------------------
elif fileType.lower() in ["ntft", "ntft"]:
    print("NTFT Image File")
    print("")
    htScript = "NTFT.py"
    htNTFT = True
#------------Unknown----------------------------------------------
else:
    print("Unsupported File Type")
    exit(1)

#checking for the Frame flag, If present prompt the user for the input
if htPPM == True:
    if htFlag.lower() in ["-f"]:
        print("""Frame extraction:
        Set the amount of frames you want to extract, you can leave the field
        blank to extract all frames
          
            
          """)
        htFrameFlag = True
        while True:
            htFrame = input("Frames to extract: ")
            if not htFrame:
                htFrame = 0  # If the input is blank, set htFrame to 0
                break
            elif htFrame.isdigit():
                htFrame = int(htFrame)
                break
            else:
                print("Invalid input. Please enter a number.")
                #htFrame = input("Frames to extract: ")
    else:
        htFrameFlag = False


#check for export flag, prompt for export option if present 
if htPPM == True:
    if htFlag.lower() in ["-e"]:
        print("""Export:
        --speed N: force a specific flipnote speed (N = flipnote speed 1 to 8)
        --scale N: upscale the frames N times
              
        Replace N with a number!
        
                       
              """)
        htExportFlag = True
        htExportOption = input("Option Mode: ")
    else:
        htExportFlag = False

#Prompt for NTFT size
if htNTFT == True:
    #if fileType.lower() in ["ntft"]: -Dont think I need this anymore, commenting out just in case 
        htNtftmode = True
        print("""NTFT Image converstion:
        convert a NTFT to PNG or the other way around.
		if the Output isn't specified it will be set to the Input with an another extension
	
		The NTFT file contain only the colordata, so it's up to the user to find or
		store the resolution of the image to convert a NTFT file to a image.
		32x32 is the normal resolution for button icons in UGO files.
        
        Please include file extentions in your name in/outputs! 
        
        
              """)
        htNtftW = input("NTFT Width: ")
        htNtftH = input("NTFT Height: ")
    #else:
        #htNtftmode = False -These go with "if filetype"

#Now ask for inputs and outputs
htPath = input("PATH To File: ")
htOutput = input("Output File: ")

#Pick the script
#[Moved to above]

#Make the magic happen - Probs a better way of doing this...
if htUGO == True:
    print(pyVer + " " + htScript + " " + htPath + " " + htOutput)
elif htNTFT == True:
    print(pyVer + " " + htScript + " " + htPath + " " + htOutput + " " + htNtftW + " " + htNtftH)
elif htFrameFlag and htFrame > 0:
    htFrame = str(htFrame) #making it a string because Python wont cancat it if htFrame is an int :/
    print(pyVer + " " + htScript + " " + htFlag + " " + htPath + " " + htOutput + " " + htFrame)
elif htExportFlag == True:
    print(pyVer + " " + htScript + " " + htFlag + " " + htPath + " " + htOutput + " " + htExportOption)
else:
    print(pyVer + " " + htScript + " " + htFlag + " " + htPath + " " + htOutput)
    
    
#Output logging - maybe for the future?
#Commands.txt