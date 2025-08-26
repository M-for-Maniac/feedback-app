import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
  const [formData, setFormData] = useState({
    feedback_type: '',
    project_type: '',
    task_process: '',
    satisfaction_rating: '',
    issue_category: '',
    issue_description: '',
    project_task_id: ''
  });
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('https://artinoco.pythonanywhere.com/submit_feedback', formData);
      setMessage('بازخورد با موفقیت ثبت شد');
      setFormData({
        feedback_type: '',
        project_type: '',
        task_process: '',
        satisfaction_rating: '',
        issue_category: '',
        issue_description: '',
        project_task_id: ''
      });
      setTimeout(() => setMessage(''), 3000);
    } catch (error) {
      setMessage('خطا در ثبت بازخورد');
      console.error('Error submitting feedback:', error);
      setTimeout(() => setMessage(''), 3000);
    }
  };

  return (
    <div className="container">
      <h1>فرم بازخورد آرتینو ۱۴۰۴</h1>
      {message && <div className={`message ${message.includes('موفقیت') ? 'success' : 'error'}`}>{message}</div>}
      <form onSubmit={handleSubmit} className="feedback-form">
        <div className="form-group">
          <label>نوع بازخورد‌دهنده:</label>
          <select name="feedback_type" value={formData.feedback_type} onChange={handleChange} required>
            <option value="">انتخاب کنید</option>
            <option value="مشتری">مشتری</option>
            <option value="کارمند">کارمند</option>
          </select>
        </div>
        {formData.feedback_type === 'مشتری' && (
          <div className="form-group">
            <label>نوع پروژه:</label>
            <select name="project_type" value={formData.project_type} onChange={handleChange}>
              <option value="">انتخاب کنید</option>
              <option value="راهنمای فرودگاه">راهنمای فرودگاه</option>
              <option value="تابلوهای فضای عمومی">تابلوهای فضای عمومی</option>
              <option value="سایر">سایر</option>
            </select>
          </div>
        )}
        {formData.feedback_type === 'کارمند' && (
          <div className="form-group">
            <label>وظیفه/فرآیند:</label>
            <select name="task_process" value={formData.task_process} onChange={handleChange}>
              <option value="">انتخاب کنید</option>
              <option value="طراحی">طراحی</option>
              <option value="تولید">تولید</option>
              <option value="نصب">نصب</option>
              <option value="خرید مواد">خرید مواد</option>
              <option value="مدیریت پروژه">مدیریت پروژه</option>
              <option value="سایر">سایر</option>
            </select>
          </div>
        )}
        <div className="form-group">
          <label>امتیاز رضایت:</label>
          <select name="satisfaction_rating" value={formData.satisfaction_rating} onChange={handleChange} required>
            <option value="">انتخاب کنید</option>
            <option value="1">۱ (بسیار ناراضی)</option>
            <option value="2">۲ (ناراضی)</option>
            <option value="3">۳ (متوسط)</option>
            <option value="4">۴ (راضی)</option>
            <option value="5">۵ (بسیار راضی)</option>
          </select>
        </div>
        <div className="form-group">
          <label>دسته‌بندی مشکل:</label>
          <select name="issue_category" value={formData.issue_category} onChange={handleChange} required>
            <option value="">انتخاب کنید</option>
            <option value="دید تابلو">دید تابلو</option>
            <option value="تأخیر در نصب/وظیفه">تأخیر در نصب/وظیفه</option>
            <option value="دقت طراحی">دقت طراحی</option>
            <option value="کیفیت مواد">کیفیت مواد</option>
            <option value="هماهنگی تیم">هماهنگی تیم</option>
            <option value="سایر">سایر</option>
          </select>
        </div>
        <div className="form-group">
          <label>توضیح مشکل:</label>
          <textarea name="issue_description" value={formData.issue_description} onChange={handleChange} required />
        </div>
        <div className="form-group">
          <label>شناسه پروژه/وظیفه (اختیاری):</label>
          <input type="text" name="project_task_id" value={formData.project_task_id} onChange={handleChange} />
        </div>
        <button type="submit">ارسال بازخورد</button>
      </form>
    </div>
  );
};

export default App;