# 🚆 Railway Network of Munich

## 📌 Overview
This project visualizes the **railway network of Munich** and allows users to define and manage block sections on an interactive map.

📌 **Key Features:**
- Converts raw railway data into **GeoJSON format** for visualization.
- Provides a **Flask web application** for interacting with the railway network.
- Enables users to **define, save, and undo** block sections on the map.
- Uses **Waitress WSGI server** for production deployment.

🔗 **Live Demo (if applicable)**: *Add link here if hosted online*  
📜 **Documentation**: Check the detailed workflow below.

---

## 📂 Project Structure
📦 Railway Network of Munich ├── convert_data.py # Converts railway data into GeoJSON format ├── app.py # Flask web app for the frontend and backend ├── run_waitress.py # Runs the Flask app using the Waitress server ├── static/ │ ├── index.html # Frontend UI with Leaflet.js for visualization │ ├── style.css # Styling for the map and buttons │ ├── script.js # Handles frontend interactions with the map ├── nodes.geojson # Converted nodes data (generated by convert_data.py) ├── edges.geojson # Converted edges data (generated by convert_data.py) ├── README.md # Project documentation

---

## 🔧 Installation & Setup
### **1️⃣ Convert Railway Data**
Before running the application, convert the raw railway network data into GeoJSON format:
```sh
python convert_data.py
```
This will generate:
nodes.geojson and edges.geojson

### **2️⃣ Run the Application**
Start the Flask web application using the Waitress server:
```sh
python run_waitress.py
```
This will host the application on:
📍 http://localhost:8080

### **3️⃣ Access the Application**
Open your browser and go to: http://localhost:8080.
Interact with the railway network and define block sections.

## 🗺️ How It Works
### Frontend (index.html)
  Uses Leaflet.js to display and interact with the railway map.
  Loads nodes.geojson and edges.geojson to visualize the network.
  Allows users to select points and define block sections.
### Backend (Flask API in app.py)
  Serves the frontend (index.html).
  Handles API requests:
    /nodes.geojson: Returns the nodes GeoJSON.
    /edges.geojson: Returns the edges GeoJSON.
    /api/block-section: Saves user-defined block sections.
    /api/save-block-sections: Downloads block sections as a GeoJSON file.
    /api/undo-block-section: Removes the last block section.

### Running in Production (Waitress)
run_waitress.py starts the Flask app with the Waitress WSGI server for stable deployment.
```sh
python run_waitress.py
```
## 🎯 Features & Functionality
✔ Define Block Sections
Click two points on the map.
Click "Define Block Section" to create a section.

✔ Download Block Sections
Click "Download Block Sections" to save as GeoJSON.

✔ Undo Last Block Section
Click "Undo Last Section" to remove the last defined block.

## 💡 Contributing
Feel free to open issues and submit pull requests. Contributions are welcome!

## ✍️ Author
👤 Pushya Shree Konasale Jayaramu
📧 pushyashree.kj.2000@gmail.com
🔗 https://www.linkedin.com/in/pushya-shree-konasale-jayaramu-6a61881a8/
