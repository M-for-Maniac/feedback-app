import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import arabic_reshaper
from bidi.algorithm import get_display
import os

# تنظیم فونت برای نمایش صحیح فارسی
font_path = 'Vazir-Regular.ttf'  # فرض بر این است که فونت در پوشه جاری است
if not os.path.exists(font_path):
    print("لطفاً فونت Vazir-Regular.ttf را در پوشه پروژه قرار دهید یا از فونت Arial استفاده کنید")
    plt.rcParams['font.family'] = 'Arial'
else:
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()

# خواندن داده‌ها
CSV_FILE = 'بازخورد_۱۴۰۴.csv'
df = pd.read_csv(CSV_FILE, encoding='utf-8')

# تابع برای اصلاح متن فارسی
def reshape_text(text):
    return get_display(arabic_reshaper.reshape(text))

# ۱. آمار خلاصه
print("آمار خلاصه:")
print("تعداد کل بازخوردها:", len(df))
print("\nمیانگین امتیاز رضایت:")
print(df.groupby('نوع بازخورد‌دهنده')['امتیاز رضایت'].mean().round(2))
print("\nتوزیع نوع بازخورد‌دهنده:")
print(df['نوع بازخورد‌دهنده'].value_counts())

# ۲. تحلیل دسته‌بندی مشکلات
issue_counts = df['دسته‌بندی مشکل'].value_counts()
print("\nتکرار دسته‌بندی مشکلات:")
print(issue_counts)

# ۳. تحلیل نوع پروژه (مشتریان)
customer_df = df[df['نوع بازخورد‌دهنده'] == 'مشتری']
print("\nت توزیع نوع پروژه (مشتریان):")
print(customer_df['نوع پروژه'].value_counts())

# ۴. تحلیل وظیفه/فرآیند (کارمندان)
staff_df = df[df['نوع بازخورد‌دهنده'] == 'کارمند']
print("\nتوزیع وظیفه/فرآیند (کارمندان):")
print(staff_df['وظیفه/فرآیند'].value_counts())

# ۵. نمودارها
plt.rcParams['axes.unicode_minus'] = False

# نمودار دسته‌بندی مشکلات
plt.figure(figsize=(10, 6))
issue_labels = [reshape_text(label) for label in issue_counts.index]
issue_counts.plot(kind='bar')
plt.title(reshape_text('تکرار دسته‌بندی مشکلات'), fontsize=14)
plt.xlabel(reshape_text('دسته‌بندی مشکل'))
plt.ylabel(reshape_text('تعداد'))
plt.xticks(range(len(issue_labels)), issue_labels, rotation=45)
plt.tight_layout()
plt.savefig('تحلیل_دسته‌بندی_مشکلات.png')
plt.close()

# نمودار توزیع امتیاز رضایت
plt.figure(figsize=(10, 6))
satisfaction_counts = df['امتیاز رضایت'].value_counts().sort_index()
satisfaction_labels = [reshape_text(f"{i} ({['', 'بسیار ناراضی', 'ناراضی', 'متوسط', 'راضی', 'بسیار راضی'][i]})") for i in satisfaction_counts.index]
satisfaction_counts.plot(kind='bar')
plt.title(reshape_text('توزیع امتیاز رضایت'), fontsize=14)
plt.xlabel(reshape_text('امتیاز رضایت'))
plt.ylabel(reshape_text('تعداد'))
plt.xticks(range(len(satisfaction_labels)), satisfaction_labels, rotation=0)
plt.tight_layout()
plt.savefig('تحلیل_امتیاز_رضایت.png')
plt.close()

# ۶. گزارش خلاصه در فایل متنی
with open('گزارش_تحلیل_بازخورد.txt', 'w', encoding='utf-8') as f:
    f.write("گزارش تحلیل بازخورد آرتینو ۱۴۰۴\n")
    f.write("=" * 50 + "\n")
    f.write(f"تعداد کل بازخوردها: {len(df)}\n")
    f.write("\nمیانگین امتیاز رضایت:\n")
    f.write(str(df.groupby('نوع بازخورد‌دهنده')['امتیاز رضایت'].mean().round(2)))
    f.write("\n\nتکرار دسته‌بندی مشکلات:\n")
    f.write(str(issue_counts))
    f.write("\n\nتوصیه‌ها:\n")
    top_issue = issue_counts.index[0]
    f.write(f"- تمرکز بر رفع مشکل '{top_issue}' که بیشترین تکرار را دارد.\n")
    if customer_df['امتیاز رضایت'].mean() < 3:
        f.write("- بررسی پروژه‌های مشتریان برای بهبود رضایت.\n")
    if staff_df['امتیاز رضایت'].mean() < 3:
        f.write("- بهبود هماهنگی تیم و فرآیندها برای کارکنان.\n")

print("\nتحلیل کامل شد. نتایج در 'گزارش_تحلیل_بازخورد.txt' و نمودارها ذخیره شدند.")