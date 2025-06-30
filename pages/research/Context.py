import streamlit as st

st.context.cookies

st.context.headers

st.context.headers["host"]

st.context.headers.get_all("pragma")


ip = st.context.ip_address
if ip is None:
    st.write("No IP address. This is expected in local development.")
elif ip.contains(":"):
    st.write("You have an IPv6 address.")
elif ip.contains("."):
    st.write("You have an IPv4 address.")
else:
    st.error("This should not happen.")



if st.context.is_embedded:
    st.write("You are running the app in an embedded context.")


if st.context.locale == "fr-FR":
    st.write("Bonjour!")
else:
    st.write("Hello!")


from datetime import datetime, timezone, timedelta
import pytz

tz = st.context.timezone
tz_obj = pytz.timezone(tz)

now = datetime.now(timezone.utc)

f"The user's timezone is {tz}."
f"The UTC time is {now}."
f"The user's local time is {now.astimezone(tz_obj)}"



tzoff = st.context.timezone_offset
tz_obj_delta = timezone(-timedelta(minutes=tzoff))

now = datetime.now(timezone.utc)

f"The user's timezone is {tz}."
f"The UTC time is {now}."
f"The user's local time is {now.astimezone(tz_obj_delta)}"

if st.context.url.startswith("http://localhost"):
    st.write("You are running the app locally.")

st.page_link("pages/home/home_style.py", label="Home", icon="🏠")


pg = st.navigation([st.Page("pages/home/home_style.py")])
pg.run()