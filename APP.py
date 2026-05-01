from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Task 1: University Admission Knowledge Base
# Humne words ko categories mein divide kiya hai (Concept of Bag of Words)
responses = {
    "requirements": "For BSCS, you need at least 60% in Intermediate (Pre-Engineering/ICS).",
    "deadline": "The last date to apply is August 25, 2026.",
    "fee": "The fee for the first semester is 120,000 PKR, including admission charges.",
    "programs": "We offer BS Computer Science, Software Engineering, and AI programs.",
    "location": "The university campus is located on Main Raiwind Road, Lahore.",
    "greeting": "Salam! I am your University Assistant. How can I help you today?"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form['msg'].lower()
    
    # Simple NLP Logic: Keyword matching based on manual Task 1
    reply = "I'm sorry, I only have info about admission requirements, fees, and deadlines."
    
    if "hi" in user_query or "hello" in user_query or "salam" in user_query:
        reply = responses["greeting"]
    elif "requirement" in user_query or "marks" in user_query or "criteria" in user_query:
        reply = responses["requirements"]
    elif "deadline" in user_query or "last date" in user_query or "closing" in user_query:
        reply = responses["deadline"]
    elif "fee" in user_query or "charges" in user_query or "cost" in user_query:
        reply = responses["fee"]
    elif "program" in user_query or "courses" in user_query:
        reply = responses["programs"]
    elif "where" in user_query or "location" in user_query or "address" in user_query:
        reply = responses["location"]
            
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5001)