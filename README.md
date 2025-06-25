Overview  
The Event Registration Portal* is a web application built using *Flask* that allows users to:  
✔ Browse upcoming events*  
✔ Register for events* by submitting their details  
✔ View registered participants* for each event  

The application uses *CSV* for storing event data and *Excel* for tracking registrations, making it simple yet functional for small to medium-sized events.  

---

 Features  
✅ Responsive UI* – Built with *Bootstrap 5* for a clean and mobile-friendly design.  
✅ Event Management* – Add, modify, or remove events via events.csv.  
✅ Registration System* – Users can sign up for events with their name and contact info.  
✅ Participant Tracking* – Admins can view all registered participants per event.  
✅ Data Persistence* – Registrations are stored in data.xlsx for future reference.  

---

 Tech Stack  
| Category       | Technology |  
|---------------|------------|  
| *Backend*   | Flask (Python) |  
| *Frontend*  | HTML, Bootstrap 5 |  
| *Data Handling* | Pandas (CSV & Excel) |  
| *Server*    | Flask Development Server |  

---

 Project Structure  
plaintext
event-registration-portal/  
│  
├── app.py                # Main Flask application  
├── events.csv            # Contains event details (Event ID, Event Name)  
├── data.xlsx             # Stores participant registrations (auto-generated)  
├── static/  
│   └── event.jpeg        # Default event thumbnail  
├── templates/  
│   ├── home.html         # Displays all events  
│   ├── register.html     # Registration form  
│   └── participants.html # Shows event participants  
└── README.md             # Documentation  
  

---

Installation & Setup 

Prerequisites
- Python 3.6+  
- pip (Python package manager)  
Step 1: Clone the Repository*  
bash
git clone https://github.com/yourusername/event-registration-portal.git  
cd event-registration-portal  
  

Step 2: Set Up a Virtual Environment (Recommended) 
bash
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows  
  
Step 3: Install Dependencies*  
bash
pip install flask pandas openpyxl  
  

Step 4: Prepare Event Data*  
1. Edit events.csv to add/modify events in the format:  
   csv
   Event ID,Event Name  
   1,Tech Conference 2024  
   2,Coding Workshop  
   3,Networking Meetup  
     

2. (Optional) Replace static/event.jpeg with custom event images.  

Step 5: Run the Application*  
bash
python app.py  
  

Step 6: Access the Portal*  
Open your browser and navigate to:  
🔗 *http://localhost:5000*  

How to Use  

1. Viewing Events  
- The *homepage* (/) lists all available events in card format.  
- Each card displays:  
  - Event Name  
  - Event ID  
  - *Register* button (to sign up)  
  - *Participants* button (to view registered users)  

2. Registering for an Event  
1. Click *"Register"* on an event card.  
2. Fill in:  
   - *Name* (Participant's full name)  
   - *Contact* (Email/Phone)  
3. Click *"Submit"* to confirm registration.  

Data is saved in data.xlsx.**  

3. Checking Participants  
- Click *"Participants"on any event card.  
- A list of registered users (name + contact) will appear.  
- If no one has registered, it shows: "No participants yet."  

---

Customization 
1. Adding More Event Fields*  
- Edit events.csv to include additional columns (e.g., Date, Location).  
- Update home.html to display the new fields.  

2. Changing the Event Image*  
- Replace static/event.jpeg with a new image.  
- Modify the <img> tag in home.html if needed.  

3. Modifying Registration Fields*  
- Edit the form in register.html (e.g., add "Email" or "Company").  
- Update app.py to handle the new fields.  

---

 Data Storage

| File | Purpose | Format |  
|------|---------|--------|  
| events.csv | Stores event details | CSV |  
| data.xlsx | Stores participant registrations | Excel |  

Example data.xlsx Structure:  
| Event ID | Event Name | Participant | Contact |  
|----------|------------|-------------|---------|  
| 1 | Tech Conference | John Doe | john@example.com |  

---


 Future Improvements  
- [ ] *User Authentication* (Login for admins/participants)  
- [ ] *Email Notifications* (Confirmations & reminders)  
- [ ] *Event Categories & Search* (Filtering by date/type)  
- [ ] *Admin Dashboard* (Manage events & export data)  

---
 License 
This project is licensed under the *MIT License*.
