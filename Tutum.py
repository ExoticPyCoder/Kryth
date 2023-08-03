import streamlit as st
import streamlit.components.v1 as com
com.html(
  """
  <html>
<head>
<style>
.important {
  background-color: cyan;
  color: black;
  border: 2px solid black;
  margin: 2px;
  padding: 2px;
  text-align: center;
}
</style>
</head>
<body>
<h1 style="font-size: 50px;" class="important">Tutum Hospitium</h1>
<h1 class="important">Welcome</h1>
<pre>
Tutum Hospitium ('Safe Shelter' in Latin) is a platform that connects donors with charities. 
Our vision is to maximize the effectiveness of donating supplies to charities using technology. 
We allow charities to post the list of supplies they need as wishlists, and enable donors to pick items from the list to donate. 
Learn more about us, and how you can get involved,by clicking below!
</pre>
</body>
</html>
"""
)
