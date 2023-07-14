import os

# Get the patient name and case number from the user
patient_name = input("Enter the patient name: ")
case_number = input("Enter the case number: ")

# Create the directory structure
directory_name = f"Case {case_number} {patient_name}"
os.makedirs(directory_name)

image_data_dir = os.path.join(directory_name, "Image Data")
os.makedirs(image_data_dir)

slicer_dir = os.path.join(directory_name, "3D Slicer")
os.makedirs(slicer_dir)

template_output_dir = os.path.join(directory_name, "Template output")
os.makedirs(template_output_dir)

nav_dir = os.path.join(template_output_dir, "3D Navigation_4pic")
os.makedirs(nav_dir)

mri_dir = os.path.join(template_output_dir, "3D w MRI_6pic")
os.makedirs(mri_dir)

seg_dir = os.path.join(template_output_dir, "Segmented MRI_12pic")
os.makedirs(seg_dir)

#in the comamnd I types
#> pyinstaller --onefile pythonScriptName.pyForCreatingFolders.py
