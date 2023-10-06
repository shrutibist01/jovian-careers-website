from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
    {
        "id": 1,
        "title": "Python Developer",
        "location": "Pune",
        "salary": "Rs. 1,00,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "New Delhi",
        "salary": "Rs. 1,20,000"
    },
    {
        "id": 3,
        "title": "Backend Engineer",
        "location": "Bangalore",
        "salary": "Rs. 1,50,000"
    },
    {
        "id": 4,
        "title": "Software Engineer",
        "location": "Mumbai",
    },
    {
        "id": 5,
        "title": "Frontend Engineer",
        "location": "Hyderabad",
        "salary": "Rs. 1,90,000"
    },
]


@app.route('/')
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
