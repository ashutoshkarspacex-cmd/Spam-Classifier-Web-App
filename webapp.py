from flask import Flask, render_template, request
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
vectorizer=pickle.load(open('vectorizer.pkl','rb'))
@app.route("/")
def home():
    return render_template("basic.html")
@app.route("/predict", methods=["POST"])
def predict():
    email = request.form["email"]
    email_vector = vectorizer.transform([email])
    prediction = model.predict(email_vector)[0]#predict() returns a list , so we do indexing to get our raw number.
    if prediction == 1:
        result = "🚨 Spam Email"
    else:
        result = "✅ Not Spam"
    return render_template(
        "basic.html",
        prediction=result,
        email=email
    )    
if __name__ == "__main__":
    app.run(debug=True)