# Real-Time Chat Application 🚀

A real-time chat application built using Flask and Flask-SocketIO. Users can send and receive messages instantly in a shared chat room.

## Features
- Real-time messaging using WebSocket technology.
- Simple and responsive chat interface.
- Supports multiple users in the same chat room.

## How to Run

### Prerequisites
- Python 3.6 or higher
- Flask
- Flask-SocketIO

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RealTimeChatApp.git
   cd RealTimeChatApp
   python -m venv venv
   venv\Scripts\activate
   source venv/bin/activate
   pip install -r requirements.txt
   flask run
   RealTimeChatApp/
├── app.py
├── LICENSE
├── README.md
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── venv/
