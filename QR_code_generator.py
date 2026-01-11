# set up  a virtual environment
#  open terminal and type
#  python3 -m venv venv -->>> it's for install python environment 
# crete a file with name.gitignore
# in this file type ->>> venv/

# go back to terminala nd activate it to type this
# ------>>>>>>  source ven/bin/activate

# after complete your task you can deactivate by typing 
# ------>>>>>    deactivate

# now install QR code package
# ------>>>>> pip install qrcode





# now let's use our file

import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print(f"QR code saved as {filename}")
