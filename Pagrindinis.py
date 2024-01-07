import streamlit as st
import os
import io
from natsort import natsorted
from PIL import Image
import base64

st.image("logo2.png")


def display_nuotraukos():
    # Path to the folder containing images
    image_folder = "folder1"

    # List all files in the folder and sort them naturally
    image_files = natsorted(os.listdir(image_folder))

    # Display each image in the folder
    for image_file in image_files:
        # Construct the full path to the image file
        image_path = os.path.join(image_folder, image_file)

        # Open the image using PIL
        img = Image.open(image_path)

        # Calculate the desired width as 50% of the current width
        desired_width = int(img.width * 0.5)

        # Resize the image
        img_resized = img.resize((desired_width, int(img.height * (desired_width / img.width))))

        # Display the resized image
        st.image(img_resized, use_column_width=True)


def display_vaizdo_irasai():
    st.title("Smagaus žiūrėjimo!")

    # Display the video player
    videos = [
        "https://www.youtube.com/watch?v=Tn-KRogA23g",
        "https://www.youtube.com/watch?v=Jt7c8B0bJUE",
        "https://www.youtube.com/watch?v=qoDU7cW7PH4",
        "https://www.youtube.com/watch?v=k2kp3einuKI",
        "https://www.youtube.com/watch?v=_qgFKvRGt_o",
        "https://www.youtube.com/watch?v=jLYcNT3NoBU",
        "https://www.youtube.com/watch?v=rT6dSMf9PuE",
        "https://www.youtube.com/watch?v=QEH55D8sOs8",
        "https://www.youtube.com/watch?v=pq6Zvqp6X7o",
        "https://www.youtube.com/watch?v=74wtkfG9ssw",
    ]

    for video_url in videos:
        st.video(video_url)

def display_contact_form():
    st.header("Parašyk man žinutę!")

    contact_form = """
    <form action="https://formsubmit.co/nolessas@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Vardas*" required>
        <input type="text" name="phone" placeholder="Telefono numeris*" required>
        <input type="email" name="email" placeholder="El. paštas*" required>
        <input type="text" name="event_date" placeholder="Šventės data YYYY-MM-DD*" required>
        <textarea name="message" placeholder="Jūsų pranešimas*" required></textarea>
        <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px;">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)




# Suskirstome eilutes ir stulpelius
row1_col1, row1_col2, row1_col3 = st.columns(3)
row2_col1, row2_col2, row2_col3 = st.columns(3)

# Pirmoji eilutė
with row1_col1:
    st.markdown("[🎨Instagram](https://www.instagram.com/egidijauss/)")
with row1_col2:
    st.markdown("[💖Youtube](https://www.youtube.com/channel/UC3_-vsk8JO05rVE_dQWjJFQ)")
with row1_col3:
    st.markdown("[🧢Facebook](https://www.facebook.com/EgiFoto)")

# Antroji eilutė
with row2_col1:
    st.button("Nuotraukos", key="nuotraukos_button", help="Explore photos")
with row2_col2:
    st.button("Vaizdo įrašai", key="vaizdo_irasai_button", help="Watch videos")
with row2_col3:
    st.button("Parašyk man žinutę!", key="contact_form_button", help="Write me a message")



