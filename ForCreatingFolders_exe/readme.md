### You need to unify names for your folders since we will use these directory names to create an automated output generator. This .exe file will help you to quickly create the folders for new cases.

Do this instruction before using the .exe file for the first time. 
1. 1. Please open your command in Windows by pressing Windows button + R.
2. Type in "pip install pyinstaller". If you have low interent you should define timeout to give it more time by typing "pip install pyinstaller --timeout=10000"
3. Type in "pip install pyinstaller os"

After your first use and in the future, download, copy, and paste the exe file (you can find it in this directory in the folder named dist), wherever your desired directory is. In the future, for creating a folder for new cases:
1. Run the .exe file, and it will get the name and id of the patient and create the folder for this patient with three subfolders:

1.1. 3D Slicer: For saving the 3D slicer file.
1.2. Image Data: For saving original dicom images of patient
1.3. Template output: For saving the outputs, which consisted of three subfolders of "3D Navigation_4pic", "3D w MRI_6pic", and "Segmented MRI_12pic"
       
