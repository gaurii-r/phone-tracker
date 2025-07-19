import tkinter
import tkintermapview
import phonenumbers
import opencage

from key import key

from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from opencage.geocoder import OpenCageGeocode

root = Tk()
root.geometry("500x500")

label1 = Label(root, text="Phone Number Tracker")
label1.pack()

def getResult():
    num = number.get("1.0", END).strip()
    try:
        num1 = phonenumbers.parse(num)
    except:
        messagebox.showerror("Error", "Number box is empty or the input is not numeric !!")
        return

    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")

    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)

    if not results:
        messagebox.showerror("Error", "Location not found for this number")
        return

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    components = results[0]['components']

    city = components.get('city', '')
    town = components.get('town', '')
    village = components.get('village', '')
    state = components.get('state', '')
    county = components.get('county', '')
    suburb = components.get('suburb', '')
    postcode = components.get('postcode', '')
    road = components.get('road', '')

    full_location = ", ".join(filter(None, [suburb, city or town or village, county, state]))

    my_label = LabelFrame(root)
    my_label.pack(pady=20)

    map_widget = tkintermapview.TkinterMapView(my_label, width=450, height=450, corner_radius=0)
    map_widget.set_position(lat, lng)
    map_widget.set_marker(lat, lng, text=full_location or "Phone Location")
    map_widget.set_zoom(10)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack()

    result.delete("1.0", END)  # Clear previous results
    result.insert(END, "The region of this number is: " + full_location)
    result.insert(END, "\nThe SIM Card of this number is: " + service_provider)
    result.insert(END, "\nLatitude is: " + str(lat))
    result.insert(END, "\nLongitude is: " + str(lng))
    result.insert(END, "\nStreet Address is: " + (road or "N/A"))
    result.insert(END, "\nCity Address is: " + (city or town or village or "N/A"))
    result.insert(END, "\nPostal Code is: " + (postcode or "N/A"))

number = Text(root, height=1)
number.pack()

style = Style()
style.configure("TButton", font=('calibri', 20 , 'bold'), borderwidth=4)
style.map(
    "TButton",
    foreground=[('active', '!disabled', 'green')],
    background=[('active', 'black')]
)

button = Button(root, text="Search", command=getResult)
button.pack(pady=20)

result = Text(root, height=7)
result.pack()

root.mainloop()
