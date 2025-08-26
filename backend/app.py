from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app, resources={r"/submit_feedback": {"origins": "http://localhost:3000"}})

# مسیر فایل CSV
CSV_FILE = 'بازخورد_۱۴۰۴.csv'

# ایجاد فایل CSV در صورت عدم وجود
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=[
        'زمان ثبت', 'نوع بازخورد‌دهنده', 'نوع پروژه', 'وظیفه/فرآیند',
        'امتیاز رضایت', 'دسته‌بندی مشکل', 'توضیح مشکل', 'شناسه پروژه/وظیفه'
    ])
    df.to_csv(CSV_FILE, index=False, encoding='utf-8')

@app.route('/')
def home():
    return 'سرور بازخورد آرتینو فعال است. از /submit_feedback استفاده کنید.'

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    df = pd.read_csv(CSV_FILE, encoding='utf-8')
    new_entry = {
        'زمان ثبت': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
        'نوع بازخورد‌دهنده': data['feedback_type'],
        'نوع پروژه': data.get('project_type', ''),
        'وظیفه/فرآیند': data.get('task_process', ''),
        'امتیاز رضایت': data['satisfaction_rating'],
        'دسته‌بندی مشکل': data['issue_category'],
        'توضیح مشکل': data['issue_description'],
        'شناسه پروژه/وظیفه': data.get('project_task_id', '')
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False, encoding='utf-8')
    return jsonify({'message': 'بازخورد با موفقیت ثبت شد'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)