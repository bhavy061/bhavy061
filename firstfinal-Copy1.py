#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import tkinter as tk
from geopy.distance import geodesic
import pywhatkit as pwt
import cv2 
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector
import speech_recognition as sr
import pyttsx3


# Create a colorful and interactive button class
class StyledButton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.config(
            relief=tk.FLAT,
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            padx=10,
            pady=5,
            font=("Helvetica", 12),
        )
def assistance():
    print("How can I help you?")
    print("1. Open Calendar")
    print("2. Open Chrome")
    print("3. Open File Explorer")
    print("4. Open Command Prompt")
    print("5. Open Control Panel")
    print("6. Open Task Manager")
    print("7. Open System Settings")
    print("8. to find distance between locations")
    print("9. to send whatsapp message  ")
    print("10.to open camera")
    print("11. make video")
    print("12. want to crop your video?")
    print("13. fingerprint detector")
    print("14.Face Detector")
    print("0. Exit")
    ch = input("Enter your choice: ").strip()
    return ch

def open_calendar():
    print("Opening calendar...")
    os.system("start outlookcal:")

def open_chrome():
    print("Opening Chrome...")
    os.system("start chrome")

def open_file_explorer():
    print("Opening File Explorer...")
    os.system("start explorer")

def open_command_prompt():
    print("Opening Command Prompt...")
    os.system("start cmd")

def open_control_panel():
    print("Opening Control Panel...")
    os.system("start control")

def open_task_manager():
    print("Opening Task Manager...")
    os.system("start taskmgr")

def open_system_settings():
    print("Opening System Settings...")
    os.system("start ms-settings:")
    
def find_distance_between_locations():
    print("Enter coordinates for Location 1:")
    lat1 = float(input("Enter latitude for Location 1: "))
    lon1 = float(input("Enter longitude for Location 1: "))

    print("Enter coordinates for Location 2:")
    lat2 = float(input("Enter latitude for Location 2: "))
    lon2 = float(input("Enter longitude for Location 2: "))

    coords1 = (lat1, lon1)
    coords2 = (lat2, lon2)

    distance = geodesic(coords1, coords2).kilometers
    print(f"The distance between the two locations is approximately {distance:.2f} kilometers.")

def open_whatsApp():
    print("opening WhatsApp for you" )
    os.system("start WhatsApp")
    pwt.sendwhatmsg_instantly("+916375997945","hello this is a message using python",20,31)
def open_camera():
    print("opening camera")
    cap = cv2.VideoCapture(0)
    status , photo = cap.read()
    status
    cv2.imwrite("photo.jpg",photo)
    cv2.imshow("photo",photo)
    cv2.waitKey()
    cv2.destroyAllWindows()
def make_video():
    print("opening your video")
    c = cv2.VideoCapture(0)
    s , p = c.read()
    s
    cv2.imshow("hii",p)
    while True:
        s , p = c.read()
        cv2.imshow("hii",p)
        if cv2.waitKey(50)==13:
            break
    cv2.destroyAllWindows()
def crop_my_video():
    print("cropping the photo")
    c = cv2.VideoCapture(0)
    s , p = c.read()
    s
    cv2.imshow("hii",p)
    while True:
        s , p = c.read()
        cv2.imshow("hii",p[100:300,200:400])
        if cv2.waitKey(50)==13:
            break
    cv2.destroyAllWindows()
def fingerprint_detector():
    print("fingerprint detector")
    model = HandDetector()
    ca = cv2.VideoCapture(0)
    st , ph = ca.read()
    hand = model.findHands(ph)
    handphoto = hand[1]
    cv2.imshow("hii",ph)
    cv2.waitKey()
    cv2.destroyAllWindows()
def Face_Detector():
    sap = cv2.VideoCapture(0)
    detector = FaceDetector()

    while True:
        success, img = sap.read()
        img, bboxs = detector.findFaces(img);
        cv2.imshow("Image", img)
        if cv2.waitKey(1)==13:
            break
    cv2.destroyAllWindows()
def assistance():
    r = sr.Recognizer()
    flag=1
    while(flag):
	
	# Exception handling to handle
	# exceptions at the runtime
        try:
		
		# use the microphone as source for input.
            with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print(" 🤖 Hii i am your robo //")
                print("What can i do for you ")

			#listens for the user's input
                audio2 = r.listen(source2)
			
			# Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print()
                print("Did you say ",MyText)
                ch=MyText
                if "notepad" in ch:
                    os.system("notepad")
                    print("Sure..")
                elif "brave" in ch:
                    os.system("Brave.lnk")
                    print("Sure..")
                elif "youtube" in ch:
                    os.system("Youtube.lnk")
                    print("Sure..")
                elif "excel" in ch:
                    os.system("Excel.lnk")
                    print("Sure..")
                elif "pc management" in ch:
                    os.system("compmgmt.msc")
                    print("Sure..")
                elif "edge" in ch:
                    os.system("start microsoft-edge:")
                    print("Sure..")
                elif "chrome" in ch:
                    os.system("start chrome")
                    print("Sure..")
                else:
                    print("i did'nt get that**//")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
		
        except sr.UnknownValueError:
            print("unknown error occurred")
        flag=flag-1

def on_button_click(choice):
    if choice == "1":
        open_calendar()
    elif choice == "2":
        open_chrome()
    elif choice == "3":
        open_file_explorer()
    elif choice == "4":
        open_command_prompt()
    elif choice == "5":
        open_control_panel()
    elif choice == "6":
        open_task_manager()
    elif choice == "7":
        open_system_settings()
    elif choice =="8":
        find_distance_between_locations()
    elif choice == "9":
        open_WhatsApp()
    elif choice == "10":
        open_camera()
    elif choice == "11":
        make_video()
    elif choice == "12":
        crop_my_video()
    elif choice == "13":
        fingerprint_detector()
    elif choice == "14":
        Face_Detector()
    elif choice == "15":
        assistance()
    elif choice == "0":
        print("Thank you for using the assistant. Goodbye!")
        root.destroy()
    else:
        print("Invalid choice. Please try again.")
        
root = tk.Tk()
root.title("Assistant")
root.config(bg="#2c3e50") 
# buttons with the StyledButton class
button_labels = ["Open Calendar", "Open Chrome", "Open File Explorer",
                 "Open Command Prompt", "Open Control Panel",
                 "Open Task Manager", "Open System Settings",
                 "Find Distance", "WhatsApp","Camera","Video","Crop my video","Fingerpoint Detector","face detector" ,"Voice assistance","Exit"]
buttons = []
for i, label in enumerate(button_labels):
    button = StyledButton(root, text=label, command=lambda idx=i: on_button_click(str(idx + 1)))
    buttons.append(button)
intro_label = tk.Label(root, text="Welcome!", fg="#2c3e50", font=("Helvetica", 14, "bold"))
intro_label.pack(pady=10)


# Pack buttons
for button in buttons:
    button.pack(fill=tk.BOTH, padx=10, pady=5)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)    
choice_var = tk.IntVar()
# the main loop
root.mainloop()


# In[ ]:





# In[ ]:




