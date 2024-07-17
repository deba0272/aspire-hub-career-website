from flask import Flask, render_template,jsonify
from datetime import datetime
app = Flask(__name__)

JOBS_2=[
  {
    'id':1,
    'title':'MS Dynamics 365 Business Central Senior Consultant',
    'location':'Bangalore, India',
    'salary':'Rs. 40,00,000',
   
  },
  {
    'id':2,
    'title':'People Consulting_WFM_Senior',
    'location':'Delhi, India',
    'salary':'Rs. 25,00,000',
  },
  {
    'id':3,
    'title':'Business Tax Advisory Senior (m/f)',
    'location':'Kolkata, India',
    'salary':'Rs. 19,00,000',

  },
  {
  'id':4,
  'title':'EY - Consultor-a Senior en Supply Chain',
  'location':'Pune, India',
  'salary':'Rs. 13,00,000',
 
},
{
    'id':5,
    'title':'Experienced VAT Analyst',
    'location':'Hyderabad, India',
    'salary':'Rs. 17,00,000',
},
{
    'id':6,
    'title':'EY - Cyber Security Junior Consultant',
    'location':'Chennai, India',
    'salary':'Rs. 20,00,000',

},
  {
  'id':7,
  'title':'Senior Actuarial Graduate',
  'location':'Chennai, India',
  'salary':'Rs. 10,00,000',
  },
  {
  'id':8,
  'title':'Developer Frontend Senior Nativo iOS',
  'location':'Chennai, India',
  'salary':'Rs. 25,00,000',
  },
  {
    'id':9,
    'title':'Senior Software Developer, People Advisory Services - Tax',
    'location':'Chennai, India',
    'salary':'Rs. 30,00,000',
  },
  {
    'id':10,
    'title':'SOC L3 Engineer',
    'location':'Chennai, India',
    'salary':'Rs. 12,00,000',
  },
  {
  'id':11,
  'title':'EY - Cyber Security Junior Consultant',
  'location':'Chennai, India',
  'salary':'Rs. 20,00,000',
  },
  {
    'id':12,
    'title':'Semi Senior Fullstack Developer',
    'location':'Chennai, India',
    'salary':'Rs. 35,00,000',
  }
]

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bangalore, India',
    'salary':'Rs. 10,00,000',

  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs. 15,00,000',
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Kolkata',
    'salary':'Rs. 12,00,000',

  },
  {
  'id':4,
  'title':'Backend Engineer',
  'location':'Pune, India',
  'salary':'Rs. 12,00,000',

},
  {
    'id':5,
    'title':'Full Stack Engineer',
    'location':'Hyderabad, India',
    'salary':'Rs. 10,00,000',
  },
  {
    'id':6,
    'title':'Firmware Engineer',
    'location':'Chennai, India',
    'salary':'Rs. 9,00,000',
  },
  {
    'id':7,
    'title':'QA Engineer',
    'location':'Chennai, India',
    'salary':'Rs. 8,00,000',
  },
  {
    'id':8,
    'title':'Junior Tax Consultant',
    'location':'Chennai, India',
    'salary':'Rs. 7,00,000',
  },
  {
    'id':9,
    'title':'Digital Engineering Staff',
    'location':'Chennai, India',
    'salary':'Rs. 6,00,000',
  },
  {
    'id':10,
    'title':'Associate Analyst-IASS-QTT',
    'location':'Chennai, India',
    'salary':'Rs. 13,00,000',
  },
  {
    'id':11,
    'title':'Admin ACR',
    'location':'Chennai, India',
    'salary':'Rs. 12,00,000',
  },
  {
    'id':12,
    'title':'Junior HR Executive',
    'location':'Chennai, India',
    'salary':'Rs. 15,00,000',
  }
]

@app.route("/")
def helllo():
  return render_template('home.html')
  
@app.route('/careers')
def careers():
  return render_template('career.html', jobs=JOBS)

@app.route('/careers1')
def careers1():
  return render_template('career1.html', jobs=JOBS_2)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
